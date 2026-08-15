# V.I.D.U.R.

### Voice-Interactive Digital Utility & Research Assistant

> A personal AI agent designed to assist with software development, research, technical writing, and everyday productivity.

---

## 🧠 About

**V.I.D.U.R.** is a personal AI assistant inspired by futuristic assistants such as JARVIS.

The goal is to build an intelligent agent capable of understanding natural language, interacting through voice, assisting with coding and research, and eventually operating tools on the user's computer with appropriate permissions.

V.I.D.U.R. is designed around a modular architecture so that individual capabilities can be developed, tested, and integrated independently.

---

## 🎯 Vision

The long-term vision is to build V.I.D.U.R. as a personal AI agent rather than simply a chatbot.

```text
                         V.I.D.U.R.
                              │
                              ▼
                       Voice Interface
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              Speech-to-Text       Text-to-Speech
                    │                   ▲
                    ▼                   │
                 AI Brain ──────────────┘
                    │
                    ▼
                Task Router
                    │
        ┌───────────┼────────────┐
        ▼           ▼            ▼
     Research     Coding       General
       Agent       Agent        Agent
        │           │            │
        └───────────┼────────────┘
                    ▼
                  Tools
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
    Filesystem    Terminal      Git
                    │
                    ▼
                  Memory


🧠 Gemini AI Brain

V.I.D.U.R. currently uses the Google Gemini API as its primary AI provider.

Gemini is used for:

Software development
Code generation
Debugging
Algorithm assistance
Technical explanations
Research assistance
Technical writing
General conversation

The Gemini model is configurable through environment variables rather than being hard-coded into the application.

🏗️ Architecture

The project follows a modular architecture:
V.I.D.U.R/
│
├── app/
│   ├── brain/
│   │   ├── gemini_brain.py
│   │   └── personality.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── __init__.py
│   │
│   ├── voice/
│   │   └── speech_listener.py
│   │
│   └── wake/
│       └── clap_detector.py
│
├── tests/
│   ├── test_clap.py
│   ├── test_speech.py
│   ├── test_activation.py
│   ├── test_config.py
│   ├── test_gemini.py
│   ├── test_conversation.py
│   └── test_models.py
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md

📈 Development Status
    Voice Activation       ████████████████████ 100%
    Speech Recognition     ████████████████████ 100%
    Gemini Integration     ████████████████████ 100%
    Conversation System     ██████████████████░░  90%
    Text-to-Speech         ░░░░░░░░░░░░░░░░░░░░   0%
    Desktop UI             ░░░░░░░░░░░░░░░░░░░░   0%
    Tool System             ░░░░░░░░░░░░░░░░░░░░   0%
    Coding Agent            ░░░░░░░░░░░░░░░░░░░░   0%
    Research Agent          ░░░░░░░░░░░░░░░░░░░░   0%
    Memory                  ░░░░░░░░░░░░░░░░░░░░   0%