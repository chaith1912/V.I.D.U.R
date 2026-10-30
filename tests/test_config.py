import os
import sys

# Ensure repository root is on sys.path when running script directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.config.settings import GROQ_API_KEY, GROQ_MODEL


def main():
    print("Configuration loaded successfully.")
    print(f"Groq API key configured: {bool(GROQ_API_KEY)}")
    print(f"Groq Model configured: {GROQ_MODEL}")


if __name__ == "__main__":
    main()
