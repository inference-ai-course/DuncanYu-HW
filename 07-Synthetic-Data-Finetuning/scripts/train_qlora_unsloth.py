import os, sys
from pathlib import Path
from datasets import load_dataset
from transformers import TrainingArguments
from trl import SFTTrainer
from unsloth import FastLanguageModel

WEEK_DIR = Path(__file__).resolve().parent
REPO_ROOT = WEEK_DIR.parent.parent
sys.path.insert(0, str(REPO_ROOT))
import config

if getattr(config, "HF_TOKEN", ""):
    os.environ["HUGGING_FACE_HUB_TOKEN"] = config.HF_TOKEN
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = config.HF_TOKEN

DATA_FILE = WEEK_DIR / "data" / "synthetic_qa.jsonl"
OUT_ADAPTER = WEEK_DIR / "checkpoints" / "qlora-adapter"
OUT_MERGED = WEEK_DIR / "checkpoints" / "merged"

BASE_MODEL = getattr(config, "HF_MODEL_NAME", "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit")
MAX_SEQ_LEN = int(getattr(config, "MAX_SEQ_LEN", 2048))
BATCH_SIZE = int(getattr(config, "BATCH_SIZE", 2))
GRAD_ACCUM = int(getattr(config, "GRAD_ACCUM", 8))
LR = float(getattr(config, "LR", 2e-4))
EPOCHS = float(getattr(config, "EPOCHS", 1))
WARMUP_RATIO = float(getattr(config, "WARMUP_RATIO", 0.05))
SAVE_STEPS = int(getattr(config, "SAVE_STEPS", 0))
MERGE_WEIGHTS = bool(getattr(config, "MERGE_WEIGHTS", False))

def main():
    if not DATA_FILE.exists():
        raise SystemExit("missing dataset")
    OUT_ADAPTER.mkdir(parents=True, exist_ok=True)
    model, tokenizer = FastLanguageModel.from_pretrained(model_name=BASE_MODEL, max_seq_length=MAX_SEQ_LEN, load_in_4bit=True)
    model = FastLanguageModel.get_peft_model(model, r=16, lora_alpha=16, lora_dropout=0.0, bias="none", target_modules=["q_proj","k_proj","v_proj","o_proj","gate_proj","up_proj","down_proj"], use_gradient_checkpointing="unsloth", random_state=1337)
    ds = load_dataset("json", data_files=str(DATA_FILE), split="train")
    args = TrainingArguments(output_dir=str(OUT_ADAPTER), per_device_train_batch_size=BATCH_SIZE, gradient_accumulation_steps=GRAD_ACCUM, learning_rate=LR, num_train_epochs=EPOCHS, warmup_ratio=WARMUP_RATIO, logging_steps=10, save_steps=SAVE_STEPS if SAVE_STEPS>0 else None, optim="paged_adamw_32bit", fp16=True, bf16=False, lr_scheduler_type="cosine", report_to="none")
    trainer = SFTTrainer(model=model, tokenizer=tokenizer, train_dataset=ds, dataset_text_field="text", max_seq_length=MAX_SEQ_LEN, packing=True, args=args)
    trainer.train()
    trainer.model.save_pretrained(str(OUT_ADAPTER))
    tokenizer.save_pretrained(str(OUT_ADAPTER))
    if MERGE_WEIGHTS:
        merged = FastLanguageModel.merge_and_unload(trainer.model)
        OUT_MERGED.mkdir(parents=True, exist_ok=True)
        merged.save_pretrained(str(OUT_MERGED), safe_serialization=True)
        tokenizer.save_pretrained(str(OUT_MERGED))

if __name__ == "__main__":
    main()
