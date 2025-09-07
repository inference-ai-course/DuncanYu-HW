# Week 2 – Data Collection & LLM Comparison

This week focused on data collection techniques, extraction methods, and comparing local LLM performance with cloud-based solutions.

## Tasks

### Main Homework: Data Collection & Extraction
- **Trafilatura**: Web content extraction and cleaning
- **PDF Processing**: OCR and text extraction from PDF documents
- **ASR (Automatic Speech Recognition)**: Audio transcription and processing
- **Data Cleanup**: Text preprocessing and deduplication

### Class Assignment: LLM Performance Analysis
- **Local LLM Deployment**: Set up and run LLMs locally
- **vLLM API Testing**: Test Hugging Face models via API (Llama 1B due to resource constraints)
- **Performance Comparison**: Compare local LLM results with OpenAI ChatGPT API

## Status

- [x] **Main Homework: Data Collection & Extraction**
    - [x] Trafilatura web scraping implementation
    - [x] PDF OCR processing pipeline
    - [x] ASR audio transcription system
    - [x] Data cleanup and preprocessing

- [x] **Class Assignment: LLM Comparison**
    - [x] Local LLM deployment and testing
    - [x] vLLM API integration (Llama 1B model)
    - [x] Performance comparison analysis with ChatGPT

---

## Homework: Data Collection & Extraction

This week focused on implementing various data collection and extraction methods, including OCR tools, web scraping, and multimedia processing.

### Main Task: OCR with Tesseract
- Implement Tesseract OCR for text extraction from images
- Process different image types (handwriting, typewriter, multilingual)
- Handle image preprocessing for improved OCR accuracy

### Bonus Tasks: Advanced Data Processing
- **Trafilatura**: Web content extraction and article parsing
- **PDF OCR**: Extract text from PDF documents using OCR
- **ASR (Automatic Speech Recognition)**: Audio transcription from video content
- **Data Cleanup**: Text preprocessing, deduplication, and corpus cleaning

### Implementation Status

#### Main Task: Tesseract OCR
- [x] Basic OCR implementation
- [x] Multi-language support (Chinese text processing)
- [x] Handwriting recognition testing
- [x] Image preprocessing pipeline

#### Bonus Task 1: Trafilatura Web Extraction
- [x] ArXiv paper scraping and cleaning
- [x] Content extraction and JSON formatting

#### Bonus Task 2: PDF OCR Processing
- [x] PDF to image conversion
- [x] OCR text extraction from PDF documents

#### Bonus Task 3: ASR Implementation
- [x] YouTube video download and audio extraction
- [x] Speech-to-text transcription
- [x] Batch processing of multiple videos

#### Bonus Task 4: Data Cleaning & Deduplication
- [x] Text corpus preprocessing
- [x] Duplicate removal algorithms
- [x] Statistical analysis and reporting

---

## Class Assignment: LLM Performance Analysis

This week focused on gaining hands-on experience with local and cloud-based LLMs, comparing their performance and capabilities.

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

### Implementation Status

#### Local LLM Deployment
- [x] Python-based LLM setup and testing
- [x] Local inference pipeline implementation

#### vLLM API Integration
- [x] Hugging Face model deployment via vLLM
- [x] API testing and validation
- [x] Resource constraint handling (used Llama 1B due to inference.ai limitations)

#### Performance Comparison Analysis
- [x] Comparative testing between local and cloud models
- [x] Performance metrics collection
- [x] Results documentation and analysis

### Technical Notes

Due to resource constraints on inference.ai, larger models (Llama 8B, Mistral 7B) could not be deployed. The comparison was conducted using Llama 1B as the local model alternative.
