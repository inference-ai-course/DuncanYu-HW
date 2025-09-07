# Week 7: Synthetic Data Generation & Fine-tuning

This week focuses on automated synthetic dataset creation and efficient model fine-tuning using QLoRA (Quantized Low-Rank Adaptation).

## 📋 Overview

The project demonstrates a complete pipeline for:
1. **Synthetic Q&A Generation**: Creating diverse question-answer pairs from research paper abstracts
2. **Data Validation**: Ensuring dataset quality and format compliance
3. **Efficient Fine-tuning**: Using QLoRA with Unsloth for memory-efficient training
4. **Model Evaluation**: Comparing fine-tuned models against base models

## 🗂️ Project Structure

```
07-Synthetic-Data-Finetuning/
├── data/
│   ├── abstracts.csv              # Research paper abstracts dataset
│   ├── prompt_template.txt        # Template for Q&A generation
│   ├── synthetic_qa.jsonl         # Generated Q&A pairs
│   └── _last_openai_output.txt    # Latest generation output
├── scripts/
│   ├── main.py                    # Main orchestration script
│   ├── gen_openai.py             # OpenAI-based Q&A generation
│   ├── gen_hf.py                 # Hugging Face model generation
│   ├── validate_jsonl.py         # Dataset validation
│   ├── train_qlora_unsloth.py    # QLoRA fine-tuning with Unsloth
│   └── eval_compare.py           # Model evaluation and comparison
└── README.md                     # This file
```

## 🚀 Key Features

### Synthetic Data Generation
- **Multi-Model Support**: Generate Q&A pairs using OpenAI GPT models or Hugging Face models
- **Diverse Question Types**: Automatically creates varied question styles (definition, mechanism, limitations, comparisons, applications)
- **Quality Control**: Built-in validation to ensure generated data meets format requirements

### Efficient Fine-tuning
- **QLoRA Integration**: Memory-efficient fine-tuning using quantized low-rank adaptation
- **Unsloth Optimization**: Accelerated training with Unsloth's optimized implementations
- **Configurable Parameters**: Flexible training configuration through config files

### Evaluation Pipeline
- **Automated Comparison**: Compare fine-tuned models against base models
- **Performance Metrics**: Comprehensive evaluation of model improvements
- **Output Analysis**: Detailed comparison of model responses

## 🛠️ Technologies Used

- **Data Generation**: OpenAI API, Hugging Face Transformers
- **Fine-tuning**: Unsloth, QLoRA, PEFT, TRL
- **Data Processing**: Pandas, JSON validation
- **Model Training**: PyTorch, Transformers, Datasets

## 📊 Workflow

1. **Data Preparation**: Load research paper abstracts from CSV
2. **Synthetic Generation**: Use LLMs to create diverse Q&A pairs
3. **Validation**: Ensure data quality and format compliance
4. **Fine-tuning**: Train models using QLoRA with Unsloth optimization
5. **Evaluation**: Compare fine-tuned vs base model performance

## 🔧 Usage

### Generate Synthetic Data
```bash
# Using OpenAI
python scripts/main.py
# Choose option 1

# Using Hugging Face models
python scripts/main.py
# Choose option 2
```

### Validate Dataset
```bash
python scripts/main.py
# Choose option 3
```

### Fine-tune Model
```bash
python scripts/train_qlora_unsloth.py
```

### Evaluate Models
```bash
python scripts/eval_compare.py
```

## 📈 Key Outcomes

- **Automated Pipeline**: End-to-end synthetic data generation and fine-tuning
- **Memory Efficiency**: QLoRA enables fine-tuning large models on limited hardware
- **Quality Assurance**: Validation ensures high-quality training data
- **Performance Gains**: Measurable improvements in domain-specific tasks

## 🎯 Learning Objectives

- Understanding synthetic data generation techniques
- Implementing efficient fine-tuning with QLoRA
- Building automated ML pipelines
- Evaluating model performance improvements
- Working with research paper datasets

---

## Data Directory Documentation

### Overview

The data directory stores research paper abstracts, prompt templates, generated synthetic Q&A pairs, and model outputs used in the fine-tuning pipeline.

### File Descriptions

#### `abstracts.csv`
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

#### `prompt_template.txt`
- **Purpose**: Template for generating Q&A pairs from abstracts
- **Format**: Plain text with placeholder instructions
- **Content**: Structured prompt for LLM to generate diverse questions
- **Features**:
  - Encourages diverse question types
  - Ensures answers are grounded in abstracts
  - Specifies output format (JSON)
  - Includes quality guidelines

#### `synthetic_qa.jsonl`
- **Purpose**: Generated question-answer pairs for model training
- **Format**: JSON Lines format for training data
- **Content**: Synthetic Q&A pairs derived from paper abstracts
- **Fields**:
  - `text`: Formatted training text (question + answer)
  - `question`: Generated question
  - `answer`: Corresponding answer
  - `source_title`: Original paper title
  - `source_abstract`: Source abstract text

#### `_last_openai_output.txt`
- **Purpose**: Raw output from the most recent OpenAI generation run
- **Format**: Plain text log file
- **Content**: Debugging information and generation logs
- **Usage**: Troubleshooting and monitoring generation quality

#### `kast_output.txt`
- **Purpose**: Additional model output or experimental results
- **Format**: Text file with model responses
- **Content**: Alternative generation outputs or test results

### Data Processing Pipeline

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

### Data Statistics

Typical dataset characteristics:
- **Source Papers**: 100-1,000 research abstracts
- **Generated Q&A Pairs**: 500-5,000 training examples
- **Question Types**: Definition, mechanism, limitation, comparison, application
- **Average Question Length**: 10-20 words
- **Average Answer Length**: 50-150 words

### Data Usage Examples

#### Loading Source Data
```python
import pandas as pd

# Load abstracts
df = pd.read_csv('data/abstracts.csv')
print(f"Loaded {len(df)} abstracts")
```

#### Loading Training Data
```python
import json

# Load synthetic Q&A pairs
qa_pairs = []
with open('data/synthetic_qa.jsonl', 'r') as f:
    for line in f:
        qa_pairs.append(json.loads(line))

print(f"Loaded {len(qa_pairs)} Q&A pairs")
```

#### Data Validation
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

### Quality Metrics

#### Question Diversity
- **Type Distribution**: Balanced across question categories
- **Length Variation**: Range of question complexities
- **Vocabulary Richness**: Diverse terminology usage

#### Answer Quality
- **Grounding**: Answers must be derivable from abstracts
- **Completeness**: Comprehensive responses to questions
- **Accuracy**: Factually correct information

#### Dataset Balance
- **Domain Coverage**: Multiple research areas represented
- **Difficulty Levels**: Mix of simple and complex questions
- **Format Consistency**: Standardized structure across examples

### Data Maintenance

#### Adding New Abstracts
1. Update `abstracts.csv` with new papers
2. Run generation pipeline on new data
3. Merge with existing `synthetic_qa.jsonl`
4. Validate combined dataset

#### Quality Improvement
- **Prompt Refinement**: Iterate on `prompt_template.txt`
- **Filtering**: Remove low-quality generated pairs
- **Augmentation**: Generate additional examples for underrepresented categories

#### Data Versioning
- **Backup**: Keep versions of datasets
- **Tracking**: Log generation parameters and model versions
- **Reproducibility**: Maintain generation scripts and configs

### Performance Considerations

- **Generation Cost**: Monitor API usage and costs
- **Quality vs. Quantity**: Balance dataset size with quality
- **Diversity**: Ensure broad coverage of question types
- **Validation**: Regular quality checks on generated data
