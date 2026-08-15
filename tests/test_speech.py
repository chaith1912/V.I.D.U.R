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