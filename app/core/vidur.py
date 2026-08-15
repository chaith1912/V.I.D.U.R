class VIDUR:
    def __init__(self):
        self.name = "V.I.D.U.R."
        self.status = "OFFLINE"

    def initialize(self):
        self.status = "STANDBY"

        print()
        print("=" * 50)
        print(f"              {self.name}")
        print("=" * 50)
        print()
        print("Initializing system...")
        print()
        print("[✓] CORE ............ READY")
        print("[✓] SYSTEM .......... READY")
        print(f"[✓] STATUS .......... {self.status}")
        print()
        print(f"{self.name} is waiting for activation.")
        print()