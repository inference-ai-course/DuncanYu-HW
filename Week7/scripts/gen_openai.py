import os, json, argparse, re
import pandas as pd
from openai import OpenAI

def save_debug(text, path):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception:
        pass

def extract_json_list(s: str):
    if not s:
        return None
    fence = re.search(r"```(?:json)?\s*(.*?)```", s, flags=re.DOTALL | re.IGNORECASE)
    if fence:
        s = fence.group(1)
    start = s.find("[")
    end = s.rfind("]")
    if start != -1 and end != -1 and end > start:
        chunk = s[start:end+1]
        try:
            data = json.loads(chunk)
            if isinstance(data, list):
                return data
        except Exception:
            pass
    try:
        data = json.loads(s)
        if isinstance(data, list):
            return data
    except Exception:
        return None
    return None

def build_chat_block(title, abstract, q, a, i):
    system = "You are a helpful research assistant."
    user = f"paper: {title}\nabstract: {abstract}\nQ{i}: {q}"
    assistant = f"A{i}: {a}"
    return {"text": f"<|system|>{system}<|user|>{user}<|assistant|>{assistant}"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="gpt-4.1-mini")
    ap.add_argument("--per_abstract", type=int, default=5)
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    with open(args.prompt, "r", encoding="utf-8") as f:
        base_prompt = f.read().strip()

    df = pd.read_csv(args.csv)
    if df.empty:
        raise SystemExit(f"CSV at {args.csv} has no rows.")

    client = OpenAI()

    total_written = 0
    with open(args.out, "w", encoding="utf-8") as out:
        for ridx, row in df.iterrows():
            title, abstract = row["title"], row["abstract"]
            user_payload = (
                f"{base_prompt}\n\ntitle: {title}\nabstract: {abstract}\n"
                f"return ~{args.per_abstract} Qa pairs as a JSON list of objects "
                f"with keys exactly: question, answer."
            )
            resp = client.chat.completions.create(
                model=args.model,
                messages=[
                    {"role": "system", "content": "You are a helpful research assistant."},
                    {"role": "user", "content": user_payload},
                ],
                temperature=0.4,
            )
            content = (resp.choices[0].message.content or "").strip()

            dbg_path = os.path.join(os.path.dirname(args.out), "kast_output.txt")
            save_debug(content, dbg_path)

            qas = extract_json_list(content)
            if not qas:
                print(f"row {ridx}: could not parse JSON list. See {dbg_path}")
                raise SystemExit("model did not return parseable JSON")

            written_this_row = 0
            for i, qa in enumerate(qas, 1):
                q = (qa.get("question") or "").strip()
                a = (qa.get("answer") or "").strip()
                if not q or not a:
                    continue
                out.write(json.dumps(build_chat_block(title, abstract, q, a, i), ensure_ascii=False) + "\n")
                written_this_row += 1
                total_written += 1

            print(f"[info] {title[:48]}… → wrote {written_this_row} pairs")

    if total_written == 0:
        raise SystemExit("No qa pairs were written. Aborting.")
    print(f"DOne! total: {total_written} qa pairs to {args.out}")

if __name__ == "__main__":
    main()
