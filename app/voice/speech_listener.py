import numpy as np
import sounddevice as sd
import speech_recognition as sr


class SpeechListener:
    def __init__(
        self,
        device=3,
        sample_rate=16000,
        channels=1,
    ):
        self.device = device
        self.sample_rate = sample_rate
        self.channels = channels

        self.recognizer = sr.Recognizer()

    def listen(self, duration=5):

        print()
        print("🎤 V.I.D.U.R. is listening...")
        print("Speak now.")

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="float32",
            device=self.device,
        )

        sd.wait()

        # Convert float32 audio (-1.0 to 1.0)
        # into 16-bit PCM audio.
        audio = np.clip(audio, -1.0, 1.0)

        audio_int16 = (audio * 32767).astype(np.int16)

        raw_audio = audio_int16.tobytes()

        speech_audio = sr.AudioData(
            raw_audio,
            self.sample_rate,
            2,
        )

        try:

            text = self.recognizer.recognize_google(
                speech_audio
            )

            print()
            print(f"You said: {text}")

            return text

        except sr.UnknownValueError:

            print()
            print("V.I.D.U.R. could not understand the speech.")

            return None

        except sr.RequestError as error:

            print()
            print(f"Speech recognition error: {error}")

            return None