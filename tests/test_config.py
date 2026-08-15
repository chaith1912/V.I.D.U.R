from app.config.settings import GEMINI_API_KEY


def main():
    print("Configuration loaded successfully.")
    print(f"Gemini API key configured: {bool(GEMINI_API_KEY)}")


if __name__ == "__main__":
    main()  