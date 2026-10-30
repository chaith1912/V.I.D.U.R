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

from app.brain.groq_brain import GroqBrain


def main():
    print()
    print("=" * 60)
    print("              V.I.D.U.R. ONLINE (CONVERSATION)")
    print("=" * 60)
    print()
    print("Type 'exit' to shut down V.I.D.U.R.")
    print()

    brain = GroqBrain()

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
