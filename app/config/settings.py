import os

from dotenv import load_dotenv


load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

# Optional audio configurations
_device_env = os.getenv("AUDIO_DEVICE")
AUDIO_DEVICE = int(_device_env) if _device_env and _device_env.strip().isdigit() else 3

_duration_env = os.getenv("LISTEN_DURATION")
LISTEN_DURATION = int(_duration_env) if _duration_env and _duration_env.strip().isdigit() else 7


if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is not configured. "
        "Add it to the .env file."
    )


if not GROQ_MODEL:
    raise RuntimeError(
        "GROQ_MODEL is not configured. "
        "Add it to the .env file."
    )
