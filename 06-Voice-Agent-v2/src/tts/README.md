# TTS (Text-to-Speech) Module

This module handles all text-to-speech functionality for the Voice Research Agent v2.

## 📋 Overview

The TTS module provides high-quality speech synthesis using Coqui TTS, enabling the voice agent to respond with natural-sounding speech output.

## 🗂️ Module Structure

```
tts/
├── speak.py         # Main TTS functionality
└── README.md        # This file
```

## 🚀 Key Components

### Speech Synthesizer (`speak.py`)
- **Coqui TTS Integration**: Uses state-of-the-art neural TTS models
- **Voice Cloning**: Support for custom voice models
- **Real-time Synthesis**: Low-latency text-to-speech conversion
- **Cross-platform Audio**: Compatible audio playback across operating systems

## 🛠️ Technologies Used

- **Coqui TTS**: Advanced neural text-to-speech synthesis
- **PyAudio/Sounddevice**: Audio playback functionality
- **NumPy**: Audio data processing
- **Torch**: Neural network inference

## 🔧 Usage

### Basic Text-to-Speech
```python
from tts.speak import TextToSpeech

tts = TextToSpeech()
tts.speak("Hello, this is your voice research agent!")
```

### Advanced Configuration
```python
from tts.speak import TextToSpeech

# Initialize with custom settings
tts = TextToSpeech(
    model_name="tts_models/en/ljspeech/tacotron2-DDC",
    vocoder_name="vocoder_models/en/ljspeech/hifigan_v2"
)

# Synthesize and save to file
tts.synthesize_to_file("Welcome to the voice agent!", "output.wav")

# Real-time speech
tts.speak("This will be spoken immediately!")
```

## ⚙️ Configuration

Key parameters that can be configured:
- **Model Selection**: Choose from various pre-trained TTS models
- **Voice Settings**: Adjust speed, pitch, and volume
- **Output Format**: Configure audio sample rate and format
- **Language Support**: Multi-language TTS capabilities

## 🎯 Features

- **Natural Speech**: High-quality, human-like voice synthesis
- **Fast Inference**: Optimized for real-time applications
- **Multiple Voices**: Support for different speaker voices
- **Customizable**: Adjustable speech parameters
- **File Export**: Save synthesized speech to audio files
- **Streaming**: Real-time audio streaming capabilities

## 🔊 Supported Models

The module supports various Coqui TTS models:
- **Tacotron2**: High-quality attention-based TTS
- **FastSpeech2**: Fast and controllable speech synthesis
- **VITS**: End-to-end neural TTS with vocoder
- **YourTTS**: Multi-speaker, multi-lingual TTS

## 🎵 Audio Quality

- **Sample Rate**: Configurable (typically 22kHz or 44.1kHz)
- **Bit Depth**: 16-bit or 32-bit audio output
- **Format Support**: WAV, MP3, and other common formats
- **Real-time Factor**: Optimized for sub-real-time synthesis
