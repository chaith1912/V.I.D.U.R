import sys
from app.config.settings import LISTEN_DURATION, GROQ_MODEL
from app.brain.groq_brain import GroqBrain
from app.core.activation import ActivationSystem


class VIDUR:
    """Core orchestrator for V.I.D.U.R. Personal AI Assistant."""

    def __init__(self):
        self.name = "V.I.D.U.R."
        self.status = "OFFLINE"
        self.brain = None
        self.activation = None
        self.speech_listener = None

    def initialize(self, run_loop: bool = True):
        self.status = "INITIALIZING"

        print()
        print("=" * 55)
        print(f"                   {self.name}")
        print("     Voice-Interactive Digital Utility & Research")
        print("=" * 55)
        print()
        print("Initializing subsystems...")

        # Initialize AI Brain
        try:
            self.brain = GroqBrain()
            print(f"[OK] BRAIN .......... READY ({GROQ_MODEL})")
        except Exception as error:
            print(f"[!] BRAIN .......... FAILED ({error})")
            raise

        # Initialize Activation & Voice
        try:
            self.activation = ActivationSystem()
            self.speech_listener = self.activation.speech_listener
            print("[OK] VOICE .......... READY")
            print("[OK] WAKE ........... READY")
        except Exception as error:
            print(f"[!] VOICE/WAKE ...... WARNING ({error})")

        self.status = "STANDBY"
        print(f"[OK] STATUS ......... {self.status}")
        print()

        if run_loop:
            self.run()

    def run(self):
        """Main application lifecycle loop."""
        print(f"{self.name} is online and awaiting activation.")
        print("Press Ctrl+C at any time to shut down.")
        print()

        try:
            while True:
                self.status = "STANDBY"
                # Wait for wake activation (double clap + wake phrase)
                activated = self.activation.wait_for_activation()

                if not activated:
                    continue

                # Switched to active interaction loop
                self.status = "ACTIVE"
                print()
                print("=" * 55)
                print(f"       {self.name} ACTIVE — LISTENING")
                print("=" * 55)
                print("Speak your query. Say 'sleep' to return to standby, or 'exit' to shut down.")
                print()

                while self.status == "ACTIVE":
                    user_speech = self.speech_listener.listen(duration=LISTEN_DURATION)

                    if not user_speech:
                        continue

                    cleaned = user_speech.lower().strip()

                    # Handle control commands
                    if cleaned in {"sleep", "standby", "go to sleep"}:
                        print()
                        print(f"{self.name}: Returning to standby mode, sir.")
                        self.status = "STANDBY"
                        break

                    if cleaned in {"exit", "quit", "shutdown", "power off"}:
                        print()
                        print(f"{self.name}: Shutting down systems. Goodbye, sir.")
                        return

                    # Query the AI Brain
                    print()
                    print(f"{self.name}: Thinking...")

                    try:
                        response = self.brain.ask(user_speech)
                        print()
                        print(f"{self.name}: {response}")
                        print()
                    except Exception as error:
                        print()
                        print(f"{self.name}: I encountered an error: {error}")
                        print()

        except KeyboardInterrupt:
            print()
            print(f"\n{self.name}: System interrupt received. Shutting down, sir.")
            self.status = "OFFLINE"
        except Exception as error:
            print(f"\n{self.name}: Unexpected runtime error: {error}")
            self.status = "ERROR"
            raise
