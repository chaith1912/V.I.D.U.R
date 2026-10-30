import time

import numpy as np
import sounddevice as sd

from app.config.settings import AUDIO_DEVICE


class ClapDetector:
    def __init__(
        self,
        device=AUDIO_DEVICE,
        sample_rate=44100,
        channels=4,
        peak_threshold=0.20,
        clap_window=1.2,
        cooldown=0.30,
    ):
        self.device = device
        self.sample_rate = sample_rate
        self.channels = channels
        self.peak_threshold = peak_threshold
        self.clap_window = clap_window
        self.cooldown = cooldown

        self.first_clap_time = None
        self.last_clap_time = 0
        self.double_clap_detected = False

    def process_audio(self, indata, frames, time_info, status):
        if status:
            print("Audio status:", status)

        # Find the loudest signal across all microphone-array channels
        peak = np.max(np.abs(indata))

        current_time = time.time()

        # Ignore quiet sounds
        if peak < self.peak_threshold:
            return

        # Prevent one physical clap from being detected multiple times
        if current_time - self.last_clap_time < self.cooldown:
            return

        self.last_clap_time = current_time

        # ----------------------------------------
        # First clap
        # ----------------------------------------
        if self.first_clap_time is None:
            self.first_clap_time = current_time
            print(f"First clap detected! Peak: {peak:.3f}")
            return

        # ----------------------------------------
        # Check for second clap
        # ----------------------------------------
        elapsed = current_time - self.first_clap_time

        if elapsed <= self.clap_window:
            print(f"Second clap detected! Peak: {peak:.3f}")
            print("[+] DOUBLE CLAP DETECTED")
            # Signal detection
            self.double_clap_detected = True
            return

        # ----------------------------------------
        # Too much time passed: treat as new first clap
        # ----------------------------------------
        self.first_clap_time = current_time
        print(f"New first clap detected! Peak: {peak:.3f}")

    def wait_for_double_clap(self):
        print()
        print("=" * 45)
        print("          V.I.D.U.R. WAKE SYSTEM")
        print("=" * 45)
        print()
        print(f"Microphone device : {self.device}")
        print(f"Channels          : {self.channels}")
        print(f"Threshold         : {self.peak_threshold}")
        print()
        print("STATUS: STANDBY")
        print()
        print("Clap twice to activate VIDUR.")
        print()

        # Reset detector state
        self.double_clap_detected = False
        self.first_clap_time = None
        self.last_clap_time = 0

        # Start continuous microphone stream
        with sd.InputStream(
            device=self.device,
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="float32",
            blocksize=1024,
            callback=self.process_audio,
        ):
            # Keep listening until the callback detects two claps
            while not self.double_clap_detected:
                sd.sleep(50)

        print()
        print("V.I.D.U.R. ACTIVATION TRIGGERED")
        return True
