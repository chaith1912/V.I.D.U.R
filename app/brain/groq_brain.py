import time
from typing import List, Dict

from groq import Groq, RateLimitError, APIStatusError

from app.brain.base import BaseBrain
from app.brain.personality import VIDUR_SYSTEM_PROMPT
from app.config.settings import GROQ_API_KEY, GROQ_MODEL


class GroqBrain(BaseBrain):
    """Groq-powered AI brain for V.I.D.U.R."""

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL
        self.system_prompt = VIDUR_SYSTEM_PROMPT
        self.messages: List[Dict[str, str]] = []
        self.reset()

    def reset(self) -> None:
        """Reset conversation history back to initial system prompt."""
        self.messages = [
            {
                "role": "system",
                "content": self.system_prompt,
            }
        ]

    def ask(self, prompt: str) -> str:
        """Send a prompt to the Groq API and return the response."""
        self.messages.append({"role": "user", "content": prompt})

        max_retries = 3

        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=self.messages,
                    temperature=0.7,
                )

                if (
                    not response.choices
                    or not response.choices[0].message
                    or not response.choices[0].message.content
                ):
                    # Pop failed user prompt to keep history clean
                    self.messages.pop()
                    return "I received an empty response, sir."

                content = response.choices[0].message.content
                self.messages.append({"role": "assistant", "content": content})
                return content

            except RateLimitError:
                # Remove the failed user prompt so future queries aren't malformed
                self.messages.pop()
                return (
                    "Sir, the Groq rate limit has been reached for now. "
                    "Please try again shortly."
                )

            except APIStatusError as error:
                if error.status_code == 503 or "UNAVAILABLE" in str(error):
                    if attempt < max_retries - 1:
                        wait_time = 2 ** attempt
                        print(
                            f"Groq service temporarily unavailable. "
                            f"Retrying in {wait_time}s..."
                        )
                        time.sleep(wait_time)
                        continue

                    self.messages.pop()
                    return (
                        "Groq is currently experiencing high demand. "
                        "Please try again shortly, sir."
                    )

                self.messages.pop()
                raise error

            except Exception as error:
                self.messages.pop()
                raise error

        self.messages.pop()
        return "I was unable to reach Groq, sir."

