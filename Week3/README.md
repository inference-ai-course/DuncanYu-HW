# Week 3 – Voice Research Agent

**🔗 External Repository**: This week's project was implemented in a separate repository: [voice-research-agent](https://github.com/Duncanyu/voice-research-agent)

This week focused on building an end-to-end voice-enabled research assistant with speech-to-text, natural language processing, and text-to-speech capabilities.

## Tasks

### Core Requirements
- **FastAPI Backend**: File upload handling and API endpoints
- **Speech Recognition**: OpenAI Whisper for audio transcription
- **Language Model**: Hugging Face Llama integration via vLLM
- **Text-to-Speech**: Coqui TTS for voice synthesis

### Advanced Features (Optional)
- **Live Audio Processing**: Real-time recording with Sounddevice and WebRTC VAD
- **Enhanced LLM Integration**: OpenAI API fallback for improved conversational memory
- **Web Interface**: Browser-based interaction and file upload system

## Status

- [x] **Core Voice Research Agent**
    - [x] FastAPI backend with file upload support
    - [x] OpenAI Whisper speech recognition integration
    - [x] Hugging Face Llama model deployment
    - [x] Coqui TTS voice synthesis

- [x] **Advanced Features**
    - [x] Live audio recording with Sounddevice
    - [x] WebRTC VAD for voice activity detection
    - [x] OpenAI API integration (used due to Llama memory limitations)
    - [x] Web-based user interface

## Technical Notes

Due to challenges with Llama's conversational memory capabilities, OpenAI ChatGPT API was integrated as a fallback solution to ensure proper context retention across conversations.
