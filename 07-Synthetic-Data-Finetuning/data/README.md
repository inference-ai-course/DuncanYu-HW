# Data Directory

This directory contains the datasets and files used for synthetic data generation and model fine-tuning.

## 📋 Overview

The data directory stores research paper abstracts, prompt templates, generated synthetic Q&A pairs, and model outputs used in the fine-tuning pipeline.

## 🗂️ File Structure

```
data/
├── abstracts.csv              # Research paper abstracts dataset
├── prompt_template.txt        # Template for Q&A generation
├── synthetic_qa.jsonl         # Generated Q&A pairs for training
├── _last_openai_output.txt    # Latest OpenAI generation output
├── kast_output.txt           # Additional model output
└── README.md                 # This file
```

## 📄 File Descriptions

### `abstracts.csv`
- **Purpose**: Source dataset of research paper abstracts
- **Format**: CSV file with paper metadata and abstracts
- **Content**: Academic papers from various domains (AI, ML, etc.)
- **Fields**:
  - `title`: Paper title
  - `abstract`: Paper abstract text
  - `authors`: Paper authors
  - `venue`: Publication venue
  - `year`: Publication year
  - `url`: Paper URL (if available)

### `prompt_template.txt`
- **Purpose**: Template for generating Q&A pairs from abstracts
- **Format**: Plain text with placeholder instructions
- **Content**: Structured prompt for LLM to generate diverse questions
- **Features**:
  - Encourages diverse question types
  - Ensures answers are grounded in abstracts
  - Specifies output format (JSON)
  - Includes quality guidelines

### `synthetic_qa.jsonl`
- **Purpose**: Generated question-answer pairs for model training
- **Format**: JSON Lines format for training data
- **Content**: Synthetic Q&A pairs derived from paper abstracts
- **Fields**:
  - `text`: Formatted training text (question + answer)
  - `question`: Generated question
  - `answer`: Corresponding answer
  - `source_title`: Original paper title
  - `source_abstract`: Source abstract text

### `_last_openai_output.txt`
- **Purpose**: Raw output from the most recent OpenAI generation run
- **Format**: Plain text log file
- **Content**: Debugging information and generation logs
- **Usage**: Troubleshooting and monitoring generation quality

### `kast_output.txt`
- **Purpose**: Additional model output or experimental results
- **Format**: Text file with model responses
- **Content**: Alternative generation outputs or test results

## 🔄 Data Processing Pipeline

1. **Source Data** → `abstracts.csv`
   - Collect research paper abstracts
   - Clean and format metadata
   - Ensure quality and diversity

2. **Prompt Engineering** → `prompt_template.txt`
   - Design effective prompts for Q&A generation
   - Specify output format and quality criteria
   - Test and refine prompt effectiveness

3. **Synthetic Generation** → `synthetic_qa.jsonl`
   - Use LLMs to generate Q&A pairs
   - Apply prompt template to each abstract
   - Format for training compatibility

4. **Quality Control** → Validation and filtering
   - Validate JSON format
   - Check answer grounding
   - Filter low-quality pairs

## 📊 Data Statistics

Typical dataset characteristics:
- **Source Papers**: 100-1,000 research abstracts
- **Generated Q&A Pairs**: 500-5,000 training examples
- **Question Types**: Definition, mechanism, limitation, comparison, application
- **Average Question Length**: 10-20 words
- **Average Answer Length**: 50-150 words

## 🔧 Usage

### Loading Source Data
```python
import pandas as pd

# Load abstracts
df = pd.read_csv('data/abstracts.csv')
print(f"Loaded {len(df)} abstracts")
```

### Loading Training Data
```python
import json

# Load synthetic Q&A pairs
qa_pairs = []
with open('data/synthetic_qa.jsonl', 'r') as f:
    for line in f:
        qa_pairs.append(json.loads(line))

print(f"Loaded {len(qa_pairs)} Q&A pairs")
```

### Data Validation
```python
# Validate JSONL format
def validate_jsonl(filepath):
    valid_count = 0
    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            try:
                data = json.loads(line)
                if 'text' in data:
                    valid_count += 1
            except json.JSONDecodeError:
                print(f"Invalid JSON at line {i+1}")
    return valid_count
```

## 🎯 Quality Metrics

### Question Diversity
- **Type Distribution**: Balanced across question categories
- **Length Variation**: Range of question complexities
- **Vocabulary Richness**: Diverse terminology usage

### Answer Quality
- **Grounding**: Answers must be derivable from abstracts
- **Completeness**: Comprehensive responses to questions
- **Accuracy**: Factually correct information

### Dataset Balance
- **Domain Coverage**: Multiple research areas represented
- **Difficulty Levels**: Mix of simple and complex questions
- **Format Consistency**: Standardized structure across examples

## 🛠️ Maintenance

### Adding New Abstracts
1. Update `abstracts.csv` with new papers
2. Run generation pipeline on new data
3. Merge with existing `synthetic_qa.jsonl`
4. Validate combined dataset

### Quality Improvement
- **Prompt Refinement**: Iterate on `prompt_template.txt`
- **Filtering**: Remove low-quality generated pairs
- **Augmentation**: Generate additional examples for underrepresented categories

### Data Versioning
- **Backup**: Keep versions of datasets
- **Tracking**: Log generation parameters and model versions
- **Reproducibility**: Maintain generation scripts and configs

## 📈 Performance Considerations

- **Generation Cost**: Monitor API usage and costs
- **Quality vs. Quantity**: Balance dataset size with quality
- **Diversity**: Ensure broad coverage of question types
- **Validation**: Regular quality checks on generated data
