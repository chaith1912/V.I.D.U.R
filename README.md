# V.I.D.U.R.

### Voice-Interactive Digital Utility & Research Assistant

> A modular personal AI assistant inspired by JARVIS, designed to assist with software development, research, technical writing, and everyday productivity.

---

## 🧠 About

**V.I.D.U.R.** is a personal AI assistant built with a modular Python architecture. It features a hands-free double-clap wake detection system, speech-to-text recognition, and ultra-fast inference powered by the **Groq API** with persistent session personality.

---

## 🏗️ Architecture

```text
V.I.D.U.R/
│
├── app/
│   ├── brain/
│   │   ├── base.py              # Abstract BaseBrain interface
│   │   ├── groq_brain.py        # Groq SDK provider implementation
│   │   ├── personality.py       # VIDUR persona & behavioral system prompt
│   │   └── router.py            # Task routing interface (planned)
│   │
│   ├── config/
│   │   ├── settings.py          # Environment configuration & validation
│   │   └── __init__.py
│   │
│   ├── core/
│   │   ├── vidur.py             # Main system orchestrator & lifecycle loop
│   │   └── activation.py        # Wake pipeline (clap → speech → wake phrase)
│   │
│   ├── voice/
│   │   └── speech_listener.py   # Microphone audio capture & STT
│   │
│   └── wake/
│       └── clap_detector.py     # Continuous audio stream & double-clap detection
│
├── tests/
│   ├── test_unit.py             # Automated unit tests (mocked, no hardware needed)
│   ├── test_config.py           # Configuration loader test
│   ├── test_groq.py             # Groq API connectivity test
│   ├── test_conversation.py     # Interactive terminal conversation loop
│   ├── test_models.py           # Multi-model inference test
│   ├── test_clap.py             # Hardware test: clap detection
│   ├── test_speech.py           # Hardware test: microphone STT
│   └── test_activation.py       # Hardware test: activation pipeline
│
├── .env.example                 # Environment configuration template
├── .gitignore                   # Git exclusion rules (protects .env)
├── main.py                      # Canonical application entry point
├── requirements.txt             # Project dependencies
└── README.md
```

---

## ⚡ Execution Flow

```text
User (Microphone)
       │
       ▼
[ClapDetector] ────────────► Listens for 2 peaks within window
       │ (Double-clap detected)
       ▼
[SpeechListener] ──────────► Captures voice & transcribes via Google STT
       │ (Wake phrase: "hey", "hello", "vidur")
       ▼
[VIDUR Orchestrator] ──────► Enters ACTIVE state
       │
       ▼
[GroqBrain] ───────────────► High-speed inference with conversation history
       │ (openai/gpt-oss-120b or configured Groq model)
       ▼
Console Output (V.I.D.U.R. Response)
```

---

## 🛠️ Installation & Setup

### 1. Clone & Set Up Virtual Environment

```bash
git clone https://github.com/chaith1912/V.I.D.U.R.git
cd V.I.D.U.R
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit `.env` and provide your Groq API credentials:

```dotenv
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-120b
AUDIO_DEVICE=3
LISTEN_DURATION=7
```

> **Security Note:** Never commit your `.env` file or API keys to version control. The `.env` file is excluded in `.gitignore`.

---

## 🚀 Running V.I.D.U.R.

### Main Assistant (Voice Activation & Interaction)

```bash
python main.py
```

1. The system initializes the core orchestrator, brain, and wake subsystems.
2. Status enters **STANDBY**.
3. **Clap twice** to trigger wake detection.
4. Speak the wake phrase (e.g., *"Hello VIDUR"*).
5. V.I.D.U.R. goes **ACTIVE** and converses with you.
6. Say *"sleep"* or *"standby"* to return to sleep mode, or *"exit"* to shut down.

### Interactive Text Chat Mode (Testing without Microphone)

```bash
python tests/test_conversation.py
```

---

## 🧪 Testing

### Automated Unit Tests (No hardware or API key required)

```bash
python -m unittest discover tests
```

### Provider & Model Tests (Requires GROQ_API_KEY)

```bash
python tests/test_config.py
python tests/test_groq.py
python tests/test_models.py
```

### Hardware Tests (Requires Microphone)

```bash
python tests/test_clap.py
python tests/test_speech.py
python tests/test_activation.py
```

---

## 👤 Developer

**Chaithanya R Rao**
