from app.brain.gemini_brain import GeminiBrain


def main():

    print()
    print("=" * 60)
    print("              V.I.D.U.R. ONLINE")
    print("=" * 60)
    print()
    print("Type 'exit' to shut down V.I.D.U.R.")
    print()

    brain = GeminiBrain()

    while True:

        try:
            user_input = input("YOU: ").strip()

        except (KeyboardInterrupt, EOFError):
            print()
            print("V.I.D.U.R.: Shutting down, sir.")
            break

        if not user_input:
            continue

        if user_input.lower() in {
            "exit",
            "quit",
            "shutdown",
        }:
            print()
            print("V.I.D.U.R.: Until next time, sir.")
            break

        print()
        print("V.I.D.U.R.: Thinking...")

        try:

            response = brain.ask(user_input)

            print()
            print(f"V.I.D.U.R.: {response}")
            print()

        except Exception as error:

            print()
            print(
                f"V.I.D.U.R.: I encountered an error: {error}"
            )
            print()


if __name__ == "__main__":
    main()