import os
import sys

# Ensure repository root is on sys.path when running script directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Force UTF-8 stdout if supported
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from groq import Groq
from app.config.settings import GROQ_API_KEY


def main():
    client = Groq(api_key=GROQ_API_KEY)

    models_to_test = [
        "openai/gpt-oss-120b",
        "qwen/qwen3.8-27b",
    ]

    prompt = "Reply with exactly: V.I.D.U.R. ONLINE"

    for model in models_to_test:
        print()
        print("=" * 60)
        print(f"Testing: {model}")
        print("=" * 60)

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )

            print("SUCCESS")
            print(response.choices[0].message.content)

        except Exception as error:
            print("FAILED")
            print(error)


if __name__ == "__main__":
    main()
