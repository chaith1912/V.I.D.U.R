import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.brain.base import BaseBrain
from app.brain.personality import VIDUR_SYSTEM_PROMPT


class TestBrainInterface(unittest.TestCase):
    def test_base_brain_is_abstract(self):
        """Verify BaseBrain cannot be instantiated directly."""
        with self.assertRaises(TypeError):
            BaseBrain()

    def test_personality_content(self):
        """Verify the personality prompt contains essential VIDUR traits."""
        self.assertIn("V.I.D.U.R.", VIDUR_SYSTEM_PROMPT)
        self.assertIn("software development", VIDUR_SYSTEM_PROMPT)
        self.assertIn("sir", VIDUR_SYSTEM_PROMPT)


class TestGroqBrain(unittest.TestCase):
    @patch("app.brain.groq_brain.Groq")
    def test_groq_brain_initialization(self, mock_groq_class):
        from app.brain.groq_brain import GroqBrain

        brain = GroqBrain()
        self.assertEqual(len(brain.messages), 1)
        self.assertEqual(brain.messages[0]["role"], "system")
        self.assertEqual(brain.messages[0]["content"], VIDUR_SYSTEM_PROMPT)

    @patch("app.brain.groq_brain.Groq")
    def test_groq_brain_ask_flow(self, mock_groq_class):
        from app.brain.groq_brain import GroqBrain

        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_choice = MagicMock()
        mock_choice.message.content = "At your service, sir."
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_groq_class.return_value = mock_client

        brain = GroqBrain()
        reply = brain.ask("Hello VIDUR")

        self.assertEqual(reply, "At your service, sir.")
        # messages should now contain: system, user, assistant
        self.assertEqual(len(brain.messages), 3)
        self.assertEqual(brain.messages[1]["role"], "user")
        self.assertEqual(brain.messages[1]["content"], "Hello VIDUR")
        self.assertEqual(brain.messages[2]["role"], "assistant")
        self.assertEqual(brain.messages[2]["content"], "At your service, sir.")

    @patch("app.brain.groq_brain.Groq")
    def test_groq_brain_reset(self, mock_groq_class):
        from app.brain.groq_brain import GroqBrain

        brain = GroqBrain()
        brain.messages.append({"role": "user", "content": "Query 1"})
        self.assertEqual(len(brain.messages), 2)
        brain.reset()
        self.assertEqual(len(brain.messages), 1)
        self.assertEqual(brain.messages[0]["role"], "system")


class TestVIDUROrchestrator(unittest.TestCase):
    @patch("app.core.vidur.GroqBrain")
    @patch("app.core.vidur.ActivationSystem")
    def test_vidur_initialization_no_loop(self, mock_act_class, mock_brain_class):
        from app.core.vidur import VIDUR

        vidur = VIDUR()
        vidur.initialize(run_loop=False)
        self.assertEqual(vidur.status, "STANDBY")
        self.assertIsNotNone(vidur.brain)
        self.assertIsNotNone(vidur.activation)


if __name__ == "__main__":
    unittest.main()

