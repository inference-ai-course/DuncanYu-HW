import os, sys, json, torch
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from peft import PeftModel

WEEK_DIR = Path(__file__).resolve().parent
REPO_ROOT = WEEK_DIR.parent.parent
sys.path.insert(0, str(REPO_ROOT))
import config

if getattr(config, "HF_TOKEN", ""):
    os.environ["HUGGING_FACE_HUB_TOKEN"] = config.HF_TOKEN
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = config.HF_TOKEN

PROMPTS = WEEK_DIR / "eval" / "heldout.jsonl"
BASE_MODEL = getattr(config, "HF_MODEL_NAME", "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit")
ADAPTER_DIR = WEEK_DIR / "checkpoints" / "qlora-adapter"
MERGED_DIR = WEEK_DIR / "checkpoints" / "merged"
OUT_BASE = WEEK_DIR / "eval" / "base.out.jsonl"
OUT_TUNED = WEEK_DIR / "eval" / "tuned.out.jsonl"
OUT_SBS = WEEK_DIR / "eval" / "side_by_side.tsv"

def load_prompts(p):
    items = []
    with open(p, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            pid = obj.get("id") or f"P{i}"
            prompt = obj.get("prompt") or ""
            items.append({"id": pid, "prompt": prompt})
    return items

def gen_text(model_id, adapter, prompts, out_path, max_new_tokens=200):
    tok = AutoTokenizer.from_pretrained(model_id, use_fast=True)
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
    if adapter and (adapter / "adapter_config.json").exists():
        model = PeftModel.from_pretrained(model, str(adapter))
    pipe = pipeline("text-generation", model=model, tokenizer=tok, device_map="auto")
    with open(out_path, "w", encoding="utf-8") as out:
        for item in prompts:
            text = item["prompt"]
            res = pipe(text, max_new_tokens=max_new_tokens, do_sample=False)[0]["generated_text"]
            out.write(json.dumps({"id": item["id"], "output": res}, ensure_ascii=False) + "\n")

def side_by_side(prompts, base_path, tuned_path, out_path):
    base = {}
    tuned = {}
    with open(base_path, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            base[obj["id"]] = obj["output"]
    with open(tuned_path, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            tuned[obj["id"]] = obj["output"]
    with open(out_path, "w", encoding="utf-8") as w:
        w.write("id\tprompt\tbase_output\ttuned_output\n")
        for item in prompts:
            pid = item["id"]
            w.write(f"{pid}\t{item['prompt'].replace('\t',' ')}\t{base.get(pid,'').replace('\t',' ')}\t{tuned.get(pid,'').replace('\t',' ')}\n")

def main():
    WEEK_DIR.joinpath("eval").mkdir(parents=True, exist_ok=True)
    if not PROMPTS.exists():
        with open(PROMPTS, "w", encoding="utf-8") as f:
            f.write(json.dumps({"id":"E1","prompt":"<|system|>You are a helpful research assistant.<|user|>Paper: Graph Neural Networks for Molecules\nAbstract: ...\nQ: What role do edge features play?<|assistant|>"} , ensure_ascii=False) + "\n")
            f.write(json.dumps({"id":"E2","prompt":"<|system|>You are a helpful research assistant.<|user|>Paper: Probabilistic Unfolding for Quantum Error Mitigation\nAbstract: ...\nQ: Under what condition does performance degrade?<|assistant|>"} , ensure_ascii=False) + "\n")
    prompts = load_prompts(PROMPTS)
    gen_text(BASE_MODEL, None, prompts, OUT_BASE)
    model_id = BASE_MODEL
    adapter = None
    if MERGED_DIR.exists():
        model_id = str(MERGED_DIR)
    elif ADAPTER_DIR.exists():
        adapter = ADAPTER_DIR
    gen_text(model_id, adapter, prompts, OUT_TUNED)
    side_by_side(prompts, OUT_BASE, OUT_TUNED, OUT_SBS)
    print(str(OUT_SBS))

if __name__ == "__main__":
    main()