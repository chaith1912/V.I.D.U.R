import time

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

        self.chat = self.client.chats.create(
            model=self.model,
            config={
                "system_instruction": VIDUR_SYSTEM_PROMPT
            },
        )

    def ask(self, prompt: str) -> str:

        max_retries = 3

        for attempt in range(max_retries):

            try:

                response = self.chat.send_message(
                    message=prompt
                )

                if not response.text:
                    return (
                        "I received an empty response "
                        "from Gemini, sir."
                    )

                return response.text

            except Exception as error:

                error_message = str(error)

                # Retry temporary server problems
                if "503" in error_message or "UNAVAILABLE" in error_message:

                    if attempt < max_retries - 1:

                        wait_time = 2 ** attempt

                        print(
                            f"Gemini is temporarily unavailable. "
                            f"Retrying in {wait_time} seconds..."
                        )

                        time.sleep(wait_time)

                        continue

                # Other errors should be reported immediately
                raise error

        return (
            "Gemini is currently unavailable. "
            "Please try again shortly, sir."
        )