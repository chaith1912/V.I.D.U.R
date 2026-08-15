from app.brain.gemini_brain import GeminiBrain


def main():

    print()
    print("=" * 55)
    print("                 V.I.D.U.R.")
    print("                AI BRAIN TEST")
    print("=" * 55)
    print()

    print("Initializing Gemini...")

    brain = GeminiBrain()

    print("✓ Gemini initialized")
    print()

    prompt = (
        "Introduce yourself to me in two sentences. "
        "Do not explain your name."
    )

    print("Sending request to Gemini...")
    print()

    response = brain.ask(prompt)

    print("V.I.D.U.R.:")
    print(response)

    print()
    print("=" * 55)


if __name__ == "__main__":
    main()