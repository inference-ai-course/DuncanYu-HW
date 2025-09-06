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
