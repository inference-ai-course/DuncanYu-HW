import argparse, json, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    args = ap.parse_args()

    ok, n = True, 0
    with open(args.inp, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                print(f"line {i}: empty")
                ok = False
                continue
            try:
                obj = json.loads(line)
            except Exception as e:
                print(f"Line {i}: jason parse error: {e}")
                ok = False
                continue
            txt = obj.get("text","")
            if not isinstance(txt, str) or not txt.strip():
                print(f"line {i}: missing/empty 'text' field")
                ok = False
                continue
            for tag in ["<|system|>", "<|user|>", "<|assistant|>"]:
                if tag not in txt:
                    print(f"line {i}: missing tag {tag}")
                    ok = False
            n += 1

    if ok:
        print(f"OK: {n} lines validated.")
        sys.exit(0)
    else:
        print("FAILED: see messages above.")
        sys.exit(2)

if __name__ == "__main__":
    main()
