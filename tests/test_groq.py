import os
import sys

# Ensure repository root is on sys.path when running script directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Force UTF-8 stdout if supported to avoid CP1252 encoding issues on Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from app.brain.groq_brain import GroqBrain


def main():
    print()
    print("=" * 55)
    print("                 V.I.D.U.R.")
    print("             GROQ AI BRAIN TEST")
    print("=" * 55)
    print()

    print("Initializing Groq Brain...")

    brain = GroqBrain()

    print("[OK] Groq Brain initialized")
    print()

    prompt = (
        "Introduce yourself to me in two sentences. "
        "Do not explain your name."
    )

    print("Sending request to Groq...")
    print()

    response = brain.ask(prompt)

    print("V.I.D.U.R.:")
    print(response)

    print()
    print("=" * 55)


if __name__ == "__main__":
    main()
