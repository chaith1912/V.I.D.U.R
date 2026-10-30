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

from app.core.activation import ActivationSystem


def main():
    activation = ActivationSystem()
    activated = activation.wait_for_activation()

    print()
    if activated:
        print("[✓] V.I.D.U.R. ACTIVATION SUCCESSFUL")
    else:
        print("[✗] V.I.D.U.R. ACTIVATION FAILED")


if __name__ == "__main__":
    main()
