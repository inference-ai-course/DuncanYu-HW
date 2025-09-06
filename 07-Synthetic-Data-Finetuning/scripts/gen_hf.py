import os, json, argparse, torch
import pandas as pd
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

def format_prompt(sys_prompt, base_prompt, title, abstract, n):
    user_payload = f"{base_prompt}\n\nTitle: {title}\nAbstract: {abstract}\nReturn ~{n} Q&A pairs as a JSON list {{question, answer}}."
    return f"<|system|>{sys_prompt}<|user|>{user_payload}<|assistant|>"

def build_chat_block(title, abstract, q, a, i):
    system = "You are a helpful research assistant."
    user = f"0aper: {title}\nAbstract: {abstract}\nQ{i}: {q}"
    assistant = f"A{i}: {a}"
    return {"text": f"<|system|>{system}<|user|>{user}<|assistant|>{assistant}"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="meta-llama/Meta-Llama-3-8B-Instruct")
    ap.add_argument("--per_abstract", type=int, default=5)
    ap.add_argument("--max_new_tokens", type=int, default=800)
    args = ap.parse_args()

    with open(args.prompt, "r", encoding="utf-8") as f:
        base_prompt = f.read().strip()

    device = 0 if torch.cuda.is_available() else -1
    tok = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None
    )
    gen = pipeline("text-generation", model=model, tokenizer=tok, device=device)

    df = pd.read_csv(args.csv)
    sys_prompt = "You are a helpful research assistant."
    with open(args.out, "w", encoding="utf-8") as out:
        for _, row in tqdm(df.iterrows(), total=len(df)):
            title, abstract = row["title"], row["abstract"]
            prompt_text = format_prompt(sys_prompt, base_prompt, title, abstract, args.per_abstract)
            resp = gen(prompt_text, max_new_tokens=args.max_new_tokens, do_sample=True, temperature=0.6)[0]["generated_text"]
            content = resp.split("<|assistant|>")[-1].strip()

            qas = None
            try:
                qas = json.loads(content)
                if not isinstance(qas, list):
                    raise ValueError("Not a list")
            except Exception:
                qas = []
                for chunk in content.split("\n\n"):
                    if "?" in chunk and ":" in chunk:
                        lines = [x.strip() for x in chunk.split("\n") if x.strip()]
                        q, a = None, None
                        for ln in lines:
                            low = ln.lower()
                            if low.startswith("q:"): q = ln.split(":",1)[1].strip()
                            if low.startswith("a:"): a = ln.split(":",1)[1].strip()
                        if q and a:
                            qas.append({"question": q, "answer": a})

            for i, qa in enumerate(qas, 1):
                q = qa.get("question","").strip()
                a = qa.get("answer","").strip()
                if not q or not a: 
                    continue
                out.write(json.dumps(build_chat_block(title, abstract, q, a, i), ensure_ascii=False) + "\n")

    print(f"Wrote JSONL to {args.out}")

if __name__ == "__main__":
    main()
