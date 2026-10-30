import sys
import os

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Ensure UTF-8 stdout on Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from app.core.vidur import VIDUR


def main():
    try:
        vidur = VIDUR()
        vidur.initialize(run_loop=True)
    except KeyboardInterrupt:
        print("\nShutdown complete.")
    except Exception as error:
        print(f"\n[FATAL] Startup failed: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
