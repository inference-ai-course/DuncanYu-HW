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

---

## Module Documentation

### ASR (Automatic Speech Recognition) Module

This module handles all speech-to-text functionality for the Voice Research Agent v2.

#### Overview

The ASR module provides a complete pipeline for converting audio input to text using OpenAI's Whisper model, with support for real-time recording and transcription.

#### Module Structure

```
asr/
├── asr_pipeline.py      # Main ASR pipeline orchestration
├── recorder.py          # Audio recording functionality
├── transcriber.py       # Whisper-based transcription
├── test_audio.mp3      # Sample audio for testing
└── README.md           # This file
```

#### Key Components

**ASR Pipeline (`asr_pipeline.py`)**
- **Unified Interface**: Single entry point for all ASR operations
- **Error Handling**: Robust error handling for audio processing
- **Configuration**: Configurable audio parameters and model settings

**Audio Recorder (`recorder.py`)**
- **Real-time Recording**: Live audio capture from microphone
- **Format Control**: Configurable sample rate, channels, and audio format
- **Cross-platform**: Works on macOS, Windows, and Linux

**Transcriber (`transcriber.py`)**
- **Whisper Integration**: Uses OpenAI Whisper for high-quality transcription
- **Multiple Models**: Support for different Whisper model sizes
- **Language Detection**: Automatic language detection and transcription

#### Technologies Used

- **OpenAI Whisper**: State-of-the-art speech recognition
- **Sounddevice**: Cross-platform audio I/O
- **NumPy**: Audio data processing
- **Wave**: Audio file handling

#### Usage

**Basic Transcription**
```python
from asr.asr_pipeline import ASRPipeline

asr = ASRPipeline()
text = asr.transcribe_audio("path/to/audio.wav")
print(text)
```

**Real-time Recording and Transcription**
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

#### Configuration

Key parameters that can be configured:
- **Sample Rate**: Audio sampling frequency (default: 16kHz)
- **Channels**: Mono/stereo recording (default: mono)
- **Model Size**: Whisper model variant (tiny, base, small, medium, large)
- **Language**: Target language for transcription

#### Features

- **High Accuracy**: Leverages Whisper's state-of-the-art performance
- **Real-time Processing**: Low-latency audio capture and transcription
- **Robust Error Handling**: Graceful handling of audio device issues
- **Flexible Input**: Supports both file and live audio input

---

### LLM (Large Language Model) Module

This module handles all language model interactions for the Voice Research Agent v2, providing flexible support for multiple LLM providers and intelligent routing.

#### Overview

The LLM module provides a unified interface for interacting with various language models, including OpenAI GPT models and Hugging Face transformers, with intelligent prompt engineering and response routing.

#### Module Structure

```
llm/
├── openai_llm.py       # OpenAI API integration
├── hf_llm.py          # Hugging Face models integration
├── router.py          # Intelligent model routing
├── prompting.py       # Prompt engineering and templates
└── README.md          # This file
```

#### Key Components

**OpenAI Integration (`openai_llm.py`)**
- **GPT Models**: Support for GPT-3.5, GPT-4, and other OpenAI models
- **Streaming**: Real-time response streaming
- **Function Calling**: Advanced function calling capabilities
- **Error Handling**: Robust API error handling and retries

**Hugging Face Integration (`hf_llm.py`)**
- **Local Models**: Run models locally for privacy and cost efficiency
- **Model Variety**: Support for various open-source models
- **Quantization**: Memory-efficient model loading
- **Custom Models**: Support for fine-tuned models

**Model Router (`router.py`)**
- **Intelligent Routing**: Automatically select the best model for each task
- **Load Balancing**: Distribute requests across multiple models
- **Fallback Logic**: Graceful fallback to alternative models
- **Cost Optimization**: Route to cost-effective models when appropriate

**Prompt Engineering (`prompting.py`)**
- **Template System**: Reusable prompt templates
- **Context Management**: Intelligent context window management
- **Role-based Prompts**: Different prompts for different agent roles
- **Dynamic Prompting**: Adaptive prompts based on conversation context

#### Technologies Used

- **OpenAI API**: GPT models and embeddings
- **Hugging Face Transformers**: Open-source language models
- **Torch**: Neural network inference
- **Tiktoken**: Token counting and management
- **Asyncio**: Asynchronous request handling

#### Usage

**Basic LLM Interaction**
```python
from llm.openai_llm import OpenAILLM

llm = OpenAILLM(model="gpt-4")
response = llm.generate("What is machine learning?")
print(response)
```

**Using the Router**
```python
from llm.router import LLMRouter

router = LLMRouter()
response = router.route_and_generate(
    prompt="Explain quantum computing",
    task_type="explanation",
    complexity="high"
)
print(response)
```

**Prompt Templates**
```python
from llm.prompting import PromptTemplate

template = PromptTemplate("research_assistant")
prompt = template.format(
    query="What are the latest developments in AI?",
    context="User is a researcher"
)
```

**Streaming Responses**
```python
from llm.openai_llm import OpenAILLM

llm = OpenAILLM(model="gpt-4")
for chunk in llm.stream("Tell me about renewable energy"):
    print(chunk, end="", flush=True)
```

#### Configuration

Key parameters that can be configured:
- **Model Selection**: Choose specific models for different tasks
- **Temperature**: Control response creativity and randomness
- **Max Tokens**: Limit response length
- **System Prompts**: Set agent personality and behavior
- **Routing Rules**: Define model selection criteria

#### Features

**Multi-Provider Support**
- **OpenAI Models**: GPT-3.5, GPT-4, and future models
- **Hugging Face**: Llama, Mistral, CodeLlama, and custom models
- **Local Deployment**: Run models locally for privacy
- **API Flexibility**: Easy to add new providers

**Intelligent Routing**
- **Task-Based**: Route based on task complexity and type
- **Cost-Aware**: Optimize for cost vs. performance
- **Availability**: Handle model availability and rate limits
- **Performance**: Route to fastest available model

**Advanced Features**
- **Function Calling**: Tool use and API integration
- **Context Management**: Intelligent conversation memory
- **Prompt Optimization**: Automatic prompt improvement
- **Response Validation**: Ensure response quality and safety

#### Model Routing Logic

The router uses several factors to select the optimal model:

1. **Task Complexity**: Simple tasks → faster models, complex tasks → powerful models
2. **Response Time**: Real-time needs → fast models, batch processing → thorough models
3. **Cost Constraints**: Budget-conscious → efficient models, quality-focused → premium models
4. **Availability**: Handle rate limits and model availability
5. **Specialization**: Route domain-specific queries to specialized models

#### Safety and Reliability

- **Input Validation**: Sanitize and validate all inputs
- **Output Filtering**: Filter inappropriate or harmful content
- **Rate Limiting**: Respect API rate limits and quotas
- **Error Recovery**: Graceful handling of API failures
- **Monitoring**: Track usage, costs, and performance metrics

---

### Tools Module

This module provides external tool integration capabilities for the Voice Research Agent v2, enabling the agent to perform web searches, access APIs, and interact with external services.

#### Overview

The Tools module implements a flexible framework for extending the voice agent's capabilities through external tools and APIs, allowing it to perform research, gather information, and interact with various services.

#### Module Structure

```
tools/
├── tools.py         # Main tools framework and implementations
└── README.md        # This file
```

#### Key Components

**Tool Framework (`tools.py`)**
- **Tool Registry**: Dynamic tool registration and discovery
- **Execution Engine**: Safe and controlled tool execution
- **Result Processing**: Standardized tool output handling
- **Error Management**: Robust error handling for tool failures

#### Available Tools

**Web Search Tools**
- **Search Engines**: Integration with Google, Bing, DuckDuckGo
- **Academic Search**: arXiv, Google Scholar, PubMed integration
- **News Search**: Real-time news and current events
- **Image Search**: Visual content discovery

**API Integration Tools**
- **Weather APIs**: Current weather and forecasts
- **Stock Market**: Financial data and market information
- **Social Media**: Twitter, Reddit content analysis
- **Knowledge Bases**: Wikipedia, Wikidata queries

**Utility Tools**
- **URL Processing**: Web page content extraction
- **File Operations**: Document processing and analysis
- **Data Conversion**: Format conversion and transformation
- **Calculation**: Mathematical and statistical operations

#### Usage

**Basic Tool Execution**
```python
from tools.tools import ToolRegistry

registry = ToolRegistry()
result = registry.execute_tool(
    tool_name="web_search",
    query="latest AI research papers",
    max_results=5
)
print(result)
```

**Custom Tool Registration**
```python
from tools.tools import Tool, ToolRegistry

class CustomTool(Tool):
    def __init__(self):
        super().__init__(
            name="custom_tool",
            description="A custom tool for specific tasks"
        )
    
    def execute(self, **kwargs):
        # Tool implementation
        return {"result": "Custom tool output"}

registry = ToolRegistry()
registry.register_tool(CustomTool())
```

**Tool Chaining**
```python
from tools.tools import ToolChain

chain = ToolChain([
    ("web_search", {"query": "climate change research"}),
    ("summarize", {"max_length": 200}),
    ("translate", {"target_language": "es"})
])

result = chain.execute()
```

#### Tool Configuration

**Search Tools**
```python
search_config = {
    "engine": "google",
    "api_key": "your_api_key",
    "max_results": 10,
    "safe_search": True,
    "language": "en"
}
```

**API Tools**
```python
api_config = {
    "timeout": 30,
    "retries": 3,
    "rate_limit": 100,  # requests per minute
    "cache_duration": 3600  # seconds
}
```

#### Features

**Safety and Security**
- **Input Validation**: Sanitize all tool inputs
- **Output Filtering**: Filter sensitive or inappropriate content
- **Rate Limiting**: Respect API rate limits and quotas
- **Sandboxing**: Isolated execution environment for tools

**Performance Optimization**
- **Caching**: Intelligent caching of tool results
- **Parallel Execution**: Concurrent tool execution when possible
- **Lazy Loading**: Load tools only when needed
- **Result Streaming**: Stream results for long-running tools

**Extensibility**
- **Plugin Architecture**: Easy addition of new tools
- **Configuration Management**: Flexible tool configuration
- **Dependency Injection**: Modular tool dependencies
- **Event System**: Tool execution monitoring and logging

#### Tool Integration

**Adding New Tools**

1. **Inherit from Tool Base Class**:
```python
class NewTool(Tool):
    def __init__(self):
        super().__init__(
            name="new_tool",
            description="Description of the new tool",
            parameters={
                "param1": {"type": "string", "required": True},
                "param2": {"type": "int", "default": 10}
            }
        )
```

2. **Implement Execute Method**:
```python
def execute(self, **kwargs):
    # Tool logic here
    return {"status": "success", "data": result}
```

3. **Register the Tool**:
```python
registry.register_tool(NewTool())
```

#### Tool Categories

- **Information Retrieval**: Search, lookup, and data gathering tools
- **Content Processing**: Text analysis, summarization, translation
- **Communication**: Email, messaging, notification tools
- **File Operations**: Document processing, file management
- **Calculation**: Mathematical, statistical, and analytical tools
- **External APIs**: Third-party service integrations

#### Error Handling

The tools framework includes comprehensive error handling:

- **Network Errors**: Automatic retries with exponential backoff
- **API Errors**: Graceful handling of API failures and rate limits
- **Validation Errors**: Clear error messages for invalid inputs
- **Timeout Handling**: Configurable timeouts for long-running operations
- **Fallback Mechanisms**: Alternative tools when primary tools fail

#### Monitoring and Logging

- **Execution Metrics**: Track tool usage and performance
- **Error Logging**: Detailed error reporting and debugging
- **Usage Analytics**: Monitor tool popularity and effectiveness
- **Performance Profiling**: Identify bottlenecks and optimization opportunities

---

### TTS (Text-to-Speech) Module

This module handles all text-to-speech functionality for the Voice Research Agent v2.

#### Overview

The TTS module provides high-quality speech synthesis using Coqui TTS, enabling the voice agent to respond with natural-sounding speech output.

#### Module Structure

```
tts/
├── speak.py         # Main TTS functionality
└── README.md        # This file
```

#### Key Components

**Speech Synthesizer (`speak.py`)**
- **Coqui TTS Integration**: Uses state-of-the-art neural TTS models
- **Voice Cloning**: Support for custom voice models
- **Real-time Synthesis**: Low-latency text-to-speech conversion
- **Cross-platform Audio**: Compatible audio playback across operating systems

#### Technologies Used

- **Coqui TTS**: Advanced neural text-to-speech synthesis
- **PyAudio/Sounddevice**: Audio playback functionality
- **NumPy**: Audio data processing
- **Torch**: Neural network inference

#### Usage

**Basic Text-to-Speech**
```python
from tts.speak import TextToSpeech

tts = TextToSpeech()
tts.speak("Hello, this is your voice research agent!")
```

**Advanced Configuration**
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

#### Configuration

Key parameters that can be configured:
- **Model Selection**: Choose from various pre-trained TTS models
- **Voice Settings**: Adjust speed, pitch, and volume
- **Output Format**: Configure audio sample rate and format
- **Language Support**: Multi-language TTS capabilities

#### Features

- **Natural Speech**: High-quality, human-like voice synthesis
- **Fast Inference**: Optimized for real-time applications
- **Multiple Voices**: Support for different speaker voices
- **Customizable**: Adjustable speech parameters
- **File Export**: Save synthesized speech to audio files
- **Streaming**: Real-time audio streaming capabilities

#### Supported Models

The module supports various Coqui TTS models:
- **Tacotron2**: High-quality attention-based TTS
- **FastSpeech2**: Fast and controllable speech synthesis
- **VITS**: End-to-end neural TTS with vocoder
- **YourTTS**: Multi-speaker, multi-lingual TTS

#### Audio Quality

- **Sample Rate**: Configurable (typically 22kHz or 44.1kHz)
- **Bit Depth**: 16-bit or 32-bit audio output
- **Format Support**: WAV, MP3, and other common formats
- **Real-time Factor**: Optimized for sub-real-time synthesis
