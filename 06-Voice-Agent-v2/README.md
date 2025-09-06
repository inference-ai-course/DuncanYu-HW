# Week 6 – Voice Research Agent v2

This week focused on building an enhanced, lightweight and modular voice interaction agent that enables real-time speech-to-speech conversations. The system combines **Whisper-based ASR**, customizable **LLMs (OpenAI & Hugging Face)**, and **Coqui TTS** for flexible local or API-powered backends.

## Tasks

### Core Voice Processing Pipeline
- **Speech Recognition**: OpenAI Whisper integration for accurate audio transcription
- **Language Model Integration**: Configurable LLM backends (OpenAI API & Hugging Face models)
- **Text-to-Speech**: Coqui TTS for natural voice synthesis
- **Real-time Processing**: Live audio capture and processing pipeline

### System Architecture & Configuration
- **Modular Design**: Swappable components for ASR, LLM, and TTS
- **Cross-platform Compatibility**: Support for Mac, Linux, and Windows
- **Configuration Management**: Template-based setup for easy customization
- **API Integration**: FastAPI backend for web-based interactions

## ⚠️ Important Notes

**Hugging Face Model Limitations**: When using Hugging Face models, be aware that they may have difficulty following instructions to return responses in strict JSON format and typically maintain only a 5-turn conversation memory. For applications requiring structured outputs or longer conversation contexts, consider using OpenAI API models instead.

## Status

- [x] **Core Voice Processing Pipeline**
    - [x] OpenAI Whisper speech recognition integration
    - [x] Configurable LLM backend support (OpenAI & Hugging Face)
    - [x] Coqui TTS voice synthesis implementation
    - [x] Real-time audio capture and processing

- [x] **System Architecture & Configuration**
    - [x] Modular component design and swappable backends
    - [x] Cross-platform compatibility (Mac, Linux, Windows)
    - [x] Template-based configuration management
    - [x] FastAPI backend for web interactions

---

## Getting Started

### 1. Download or Clone

Clone the repository:  
```bash
git clone https://github.com/<your-username>/voice-research-agent.git
cd voice-research-agent
```

Or download the ZIP from GitHub and extract it into your preferred directory.

### 2. Set up a Virtual Environment

**Mac/Linux:**  
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**  
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install `espeak-ng` (for TTS)

**Mac (Homebrew):**  
```bash
brew install espeak-ng
```

**Linux (Debian/Ubuntu):**  
```bash
sudo apt-get update
sudo apt-get install espeak-ng
```

**Windows:**  
Download and install `espeak-ng` from the [official releases](https://github.com/espeak-ng/espeak-ng/releases).  
Make sure to add it to your `PATH` during installation.

### 5. Configure

Duplicate the template configuration file and rename it:  
```bash
cp config_template.py config.py
```

Then open `config.py` and edit the settings (e.g., API keys, model names, devices).

### 6. Run the Agent

```bash
python main.py
```

---

## Specifications

*(To be filled in)*

---

## Roadmap

- **Optimize** the overall pipeline for better performance and lower latency  
- **Add CLI** support to allow more advanced control and flexibility
