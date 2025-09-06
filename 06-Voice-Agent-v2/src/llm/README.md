# LLM (Large Language Model) Module

This module handles all language model interactions for the Voice Research Agent v2, providing flexible support for multiple LLM providers and intelligent routing.

## 📋 Overview

The LLM module provides a unified interface for interacting with various language models, including OpenAI GPT models and Hugging Face transformers, with intelligent prompt engineering and response routing.

## 🗂️ Module Structure

```
llm/
├── openai_llm.py       # OpenAI API integration
├── hf_llm.py          # Hugging Face models integration
├── router.py          # Intelligent model routing
├── prompting.py       # Prompt engineering and templates
└── README.md          # This file
```

## 🚀 Key Components

### OpenAI Integration (`openai_llm.py`)
- **GPT Models**: Support for GPT-3.5, GPT-4, and other OpenAI models
- **Streaming**: Real-time response streaming
- **Function Calling**: Advanced function calling capabilities
- **Error Handling**: Robust API error handling and retries

### Hugging Face Integration (`hf_llm.py`)
- **Local Models**: Run models locally for privacy and cost efficiency
- **Model Variety**: Support for various open-source models
- **Quantization**: Memory-efficient model loading
- **Custom Models**: Support for fine-tuned models

### Model Router (`router.py`)
- **Intelligent Routing**: Automatically select the best model for each task
- **Load Balancing**: Distribute requests across multiple models
- **Fallback Logic**: Graceful fallback to alternative models
- **Cost Optimization**: Route to cost-effective models when appropriate

### Prompt Engineering (`prompting.py`)
- **Template System**: Reusable prompt templates
- **Context Management**: Intelligent context window management
- **Role-based Prompts**: Different prompts for different agent roles
- **Dynamic Prompting**: Adaptive prompts based on conversation context

## 🛠️ Technologies Used

- **OpenAI API**: GPT models and embeddings
- **Hugging Face Transformers**: Open-source language models
- **Torch**: Neural network inference
- **Tiktoken**: Token counting and management
- **Asyncio**: Asynchronous request handling

## 🔧 Usage

### Basic LLM Interaction
```python
from llm.openai_llm import OpenAILLM

llm = OpenAILLM(model="gpt-4")
response = llm.generate("What is machine learning?")
print(response)
```

### Using the Router
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

### Prompt Templates
```python
from llm.prompting import PromptTemplate

template = PromptTemplate("research_assistant")
prompt = template.format(
    query="What are the latest developments in AI?",
    context="User is a researcher"
)
```

### Streaming Responses
```python
from llm.openai_llm import OpenAILLM

llm = OpenAILLM(model="gpt-4")
for chunk in llm.stream("Tell me about renewable energy"):
    print(chunk, end="", flush=True)
```

## ⚙️ Configuration

Key parameters that can be configured:
- **Model Selection**: Choose specific models for different tasks
- **Temperature**: Control response creativity and randomness
- **Max Tokens**: Limit response length
- **System Prompts**: Set agent personality and behavior
- **Routing Rules**: Define model selection criteria

## 🎯 Features

### Multi-Provider Support
- **OpenAI Models**: GPT-3.5, GPT-4, and future models
- **Hugging Face**: Llama, Mistral, CodeLlama, and custom models
- **Local Deployment**: Run models locally for privacy
- **API Flexibility**: Easy to add new providers

### Intelligent Routing
- **Task-Based**: Route based on task complexity and type
- **Cost-Aware**: Optimize for cost vs. performance
- **Availability**: Handle model availability and rate limits
- **Performance**: Route to fastest available model

### Advanced Features
- **Function Calling**: Tool use and API integration
- **Context Management**: Intelligent conversation memory
- **Prompt Optimization**: Automatic prompt improvement
- **Response Validation**: Ensure response quality and safety

## 🔄 Model Routing Logic

The router uses several factors to select the optimal model:

1. **Task Complexity**: Simple tasks → faster models, complex tasks → powerful models
2. **Response Time**: Real-time needs → fast models, batch processing → thorough models
3. **Cost Constraints**: Budget-conscious → efficient models, quality-focused → premium models
4. **Availability**: Handle rate limits and model availability
5. **Specialization**: Route domain-specific queries to specialized models

## 🛡️ Safety and Reliability

- **Input Validation**: Sanitize and validate all inputs
- **Output Filtering**: Filter inappropriate or harmful content
- **Rate Limiting**: Respect API rate limits and quotas
- **Error Recovery**: Graceful handling of API failures
- **Monitoring**: Track usage, costs, and performance metrics
