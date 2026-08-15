from google import genai

from app.config.settings import GEMINI_API_KEY


def main():

    client = genai.Client(
        api_key=GEMINI_API_KEY
    )

    models_to_test = [
        "gemini-3.7-flash",
        "deep-research-preview-04-2026",
        "deep-research-pro-preview-12-2025",
    ]

    prompt = "Reply with exactly: V.I.D.U.R. ONLINE"

    for model in models_to_test:

        print()
        print("=" * 60)
        print(f"Testing: {model}")
        print("=" * 60)

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt,
            )

            print("SUCCESS")
            print(response.text)

        except Exception as error:

            print("FAILED")
            print(error)


if __name__ == "__main__":
    main()