# ASR (Automatic Speech Recognition) Module

This module handles all speech-to-text functionality for the Voice Research Agent v2.

## 📋 Overview

The ASR module provides a complete pipeline for converting audio input to text using OpenAI's Whisper model, with support for real-time recording and transcription.

## 🗂️ Module Structure

```
asr/
├── asr_pipeline.py      # Main ASR pipeline orchestration
├── recorder.py          # Audio recording functionality
├── transcriber.py       # Whisper-based transcription
├── test_audio.mp3      # Sample audio for testing
└── README.md           # This file
```

## 🚀 Key Components

### ASR Pipeline (`asr_pipeline.py`)
- **Unified Interface**: Single entry point for all ASR operations
- **Error Handling**: Robust error handling for audio processing
- **Configuration**: Configurable audio parameters and model settings

### Audio Recorder (`recorder.py`)
- **Real-time Recording**: Live audio capture from microphone
- **Format Control**: Configurable sample rate, channels, and audio format
- **Cross-platform**: Works on macOS, Windows, and Linux

### Transcriber (`transcriber.py`)
- **Whisper Integration**: Uses OpenAI Whisper for high-quality transcription
- **Multiple Models**: Support for different Whisper model sizes
- **Language Detection**: Automatic language detection and transcription

## 🛠️ Technologies Used

- **OpenAI Whisper**: State-of-the-art speech recognition
- **Sounddevice**: Cross-platform audio I/O
- **NumPy**: Audio data processing
- **Wave**: Audio file handling

## 🔧 Usage

### Basic Transcription
```python
from asr.asr_pipeline import ASRPipeline

asr = ASRPipeline()
text = asr.transcribe_audio("path/to/audio.wav")
print(text)
```

### Real-time Recording and Transcription
```python
from asr.recorder import AudioRecorder
from asr.transcriber import WhisperTranscriber

recorder = AudioRecorder()
transcriber = WhisperTranscriber()

# Record audio
audio_data = recorder.record(duration=5)

# Transcribe
text = transcriber.transcribe(audio_data)
print(text)
```

## ⚙️ Configuration

Key parameters that can be configured:
- **Sample Rate**: Audio sampling frequency (default: 16kHz)
- **Channels**: Mono/stereo recording (default: mono)
- **Model Size**: Whisper model variant (tiny, base, small, medium, large)
- **Language**: Target language for transcription

## 🎯 Features

- **High Accuracy**: Leverages Whisper's state-of-the-art performance
- **Real-time Processing**: Low-latency audio capture and transcription
- **Robust Error Handling**: Graceful handling of audio device issues
- **Flexible Input**: Supports both file and live audio input
