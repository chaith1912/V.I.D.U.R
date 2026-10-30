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

from app.voice.speech_listener import SpeechListener


def main():
    listener = SpeechListener()
    text = listener.listen(duration=5)

    print()
    print("=" * 45)
    if text:
        print(f"Recognized: {text}")
    else:
        print("No speech recognized.")
    print("=" * 45)


if __name__ == "__main__":
    main()
