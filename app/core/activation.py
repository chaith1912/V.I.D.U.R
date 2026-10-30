from app.wake.clap_detector import ClapDetector
from app.voice.speech_listener import SpeechListener


class ActivationSystem:
    def __init__(self):
        self.clap_detector = ClapDetector()
        self.speech_listener = SpeechListener()

    def wait_for_activation(self) -> bool:
        print()
        print("=" * 45)
        print("       V.I.D.U.R. ACTIVATION SYSTEM")
        print("=" * 45)
        print()
        print("STATUS: STANDBY")
        print()
        print("Clap twice to activate VIDUR.")
        print()

        # Wait for double clap
        self.clap_detector.wait_for_double_clap()

        print()
        print("[+] DOUBLE CLAP CONFIRMED")
        print()

        # Start speech recognition after the double clap
        print("[*] Preparing voice recognition...")

        text = self.speech_listener.listen(duration=5)

        if text is None:
            print()
            print("No speech detected.")
            return False

        text = text.lower().strip()
        print()
        print(f"Recognized command: {text}")

        # Check wake phrase
        if any(phrase in text for phrase in ["hey", "hello", "vidur"]):
            print()
            print("=" * 45)
            print("          V.I.D.U.R. ONLINE")
            print("=" * 45)
            print()
            return True

        print()
        print("Wake phrase not recognized.")
        return False
