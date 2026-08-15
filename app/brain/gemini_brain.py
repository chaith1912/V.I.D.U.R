from google import genai

from app.brain.personality import VIDUR_SYSTEM_PROMPT
from app.config.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)


class GeminiBrain:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = GEMINI_MODEL

    def ask(self, prompt: str) -> str:

        full_prompt = f"""
{VIDUR_SYSTEM_PROMPT}

USER:
{prompt}

V.I.D.U.R.:
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=full_prompt,
        )

        if not response.text:
            return "I was unable to generate a response."

        return response.text