# Week 2 – LLM Performance Analysis

This week focused on gaining hands-on experience with local and cloud-based LLMs, comparing their performance and capabilities.

## Tasks

### Local LLM Deployment
- Set up and run LLMs locally via Python
- Test model inference and response quality
- Measure performance metrics and resource usage

### vLLM API Integration
- Deploy Hugging Face models using vLLM API
- Test API endpoints and response handling
- Evaluate model performance under API constraints

### Performance Comparison Study
- Compare local LLM results with OpenAI ChatGPT API
- Analyze response quality, speed, and accuracy
- Document findings and performance trade-offs

## Status

- [x] **Local LLM Deployment**
    - [x] Python-based LLM setup and testing
    - [x] Local inference pipeline implementation

- [x] **vLLM API Integration**
    - [x] Hugging Face model deployment via vLLM
    - [x] API testing and validation
    - [x] Resource constraint handling (used Llama 1B due to inference.ai limitations)

- [x] **Performance Comparison Analysis**
    - [x] Comparative testing between local and cloud models
    - [x] Performance metrics collection
    - [x] Results documentation and analysis

## Notes

Due to resource constraints on inference.ai, larger models (Llama 8B, Mistral 7B) could not be deployed. The comparison was conducted using Llama 1B as the local model alternative.
