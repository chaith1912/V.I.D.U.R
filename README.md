# V.I.D.U.R.

### Voice-Interactive Digital Utility & Research Assistant

> A modular personal AI agent designed to assist with software development, research, technical writing, and everyday productivity.

---

## 🧠 About

**V.I.D.U.R.** is a personal AI assistant inspired by futuristic assistants such as JARVIS.

The goal is to build an intelligent agent capable of understanding natural language, interacting through voice, assisting with coding and research, and eventually operating tools on the user's computer with appropriate permissions.

V.I.D.U.R. is designed around a **modular architecture**, allowing individual capabilities to be developed, tested, and integrated independently.

---

## 🎯 Vision

The long-term vision is to build V.I.D.U.R. as a **personal AI agent**, rather than simply a chatbot.

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
   Filesystem    Terminal       Git
                    │
                    ▼
                  Memory
```

---

## 🧠 Gemini AI Brain

V.I.D.U.R. currently uses the **Google Gemini API** as its primary AI provider.

Gemini is used for:

* Software development
* Code generation
* Debugging
* Algorithm assistance
* Technical explanations
* Research assistance
* Technical writing
* General conversation

The Gemini model is configured through environment variables rather than being hard-coded into the application.

---

## 🏗️ Architecture

The project follows a modular architecture:

```text
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
```

---

## 🚀 Roadmap

The planned development path is:

1. **Complete the conversation system**
2. **Add Text-to-Speech**
3. **Build a desktop interface**
4. **Implement a secure tool system**
5. **Develop the coding agent**
6. **Develop the research agent**
7. **Implement persistent memory**
8. **Add filesystem, terminal, and Git integrations**
9. **Improve task routing and agent orchestration**
10. **Add permission and safety controls for computer interaction**

---

## 🔐 Security & Permissions

As V.I.D.U.R. evolves from a conversational assistant into an agent capable of interacting with a computer, potentially sensitive operations should require explicit user permissions.

Examples include:

* Reading or modifying files
* Executing terminal commands
* Creating or deleting files
* Running software
* Making Git changes
* Accessing external services

The tool system should therefore be designed around **least-privilege access, explicit permissions, and clear user confirmation for destructive actions**.

---

## 🧪 Testing

V.I.D.U.R. includes tests for its core components:

* Voice activation
* Speech recognition
* Activation logic
* Configuration
* Gemini integration
* Conversation handling
* Model behavior

Run the test suite with:

```bash
pytest
```

---

## ⚙️ Configuration

Configuration is managed through environment variables.

Create a `.env` file in the project root and configure the required API credentials and model settings.

> **Important:** Never commit `.env` or API keys to version control.

Make sure `.env` is included in `.gitignore`.

---

## 🛠️ Installation

Clone the repository and install the required dependencies:

```bash
git clone <your-repository-url>
cd V.I.D.U.R
pip install -r requirements.txt
```

Configure your environment variables, then run:

```bash
python main.py
```

---

## 📌 Project Goals

V.I.D.U.R. aims to evolve from a voice-enabled conversational assistant into a modular AI agent capable of:

* Understanding natural language
* Conversing through voice
* Generating and debugging code
* Conducting research
* Managing files
* Working with the terminal
* Interacting with Git
* Maintaining long-term memory
* Routing tasks to specialized agents
* Operating computer tools safely with user authorization

The ultimate goal is a **personal, extensible, and permission-aware AI agent** that can assist with both digital work and everyday productivity.

# 👤 Developer

## Chaithanya R Rao

V.I.D.U.R. is being developed as a personal AI agent designed to combine modern AI capabilities with practical developer and research tools.

### 🚀 Core Areas

* 🤖 **Artificial Intelligence**
* 🎙️ **Voice Interfaces**
* 🧠 **Agentic Systems**
* 💻 **Software Engineering**
* 🔬 **Research Assistance**
* 🛠️ **Developer Tooling**

V.I.D.U.R. aims to evolve into a capable personal AI assistant that can reason, research, interact through voice, assist with software development, and automate useful tasks.
