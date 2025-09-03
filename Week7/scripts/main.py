import os, sys, subprocess
from pathlib import Path

HERE = Path(__file__).resolve()
if (HERE.parent.name.lower() == "scripts") and (HERE.parent.parent / "data").exists():
    WEEK_DIR = HERE.parent.parent
else:
    WEEK_DIR = HERE.parent

REPO_ROOT = WEEK_DIR.parent
SCRIPTS   = WEEK_DIR / "scripts"
DATA      = WEEK_DIR / "data"
OUTFILE   = DATA / "synthetic_qa.jsonl"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

OPENAI_KEY = ""
HF_TOKEN   = ""
try:
    import config
    OPENAI_KEY = getattr(config, "OPENAI_API", "").strip()
    HF_TOKEN   = getattr(config, "HF_TOKEN", "").strip()
except Exception as e:
    print(f"couldnt import keys.py from {REPO_ROOT}: {e}\n"
          f"      no tokens")

def env_with_keys():
    env = os.environ.copy()
    if OPENAI_KEY:
        env["OPENAI_API_KEY"] = OPENAI_KEY
    if HF_TOKEN:
        env["HUGGING_FACE_HUB_TOKEN"] = HF_TOKEN
        env["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN
    return env

def run(cmd):
    print("\n$ " + " ".join(map(str, cmd)))
    res = subprocess.run(cmd, cwd=str(WEEK_DIR), env=env_with_keys())
    if res.returncode != 0:
        raise SystemExit(f"\command failed with exit code {res.returncode}. "
                         f"check up there for details.")

def run_openai():
    csv = DATA / "abstracts.csv"
    prompt = DATA / "prompt_template.txt"
    if not OPENAI_KEY:
        print("couldnt find api in config.")
        return
    if not csv.exists():
        print(f"Misissing: {csv}")
        return
    if not prompt.exists():
        print(f"Missing: {prompt}")
        return
    cmd = [
        sys.executable, str(SCRIPTS / "gen_openai.py"),
        "--csv", str(csv),
        "--prompt", str(prompt),
        "--out", str(OUTFILE),
        "--model", "gpt-4.1-mini",
        "--per_abstract", "5",
    ]
    run(cmd)

def run_hf():
    csv = DATA / "abstracts.csv"
    prompt = DATA / "prompt_template.txt"
    if not csv.exists():
        print(f"Missing: {csv}")
        return
    if not prompt.exists():
        print(f"Missing: {prompt}")
        return
    if not HF_TOKEN:
        print("no token found in config! for hf")
    cmd = [
        sys.executable, str(SCRIPTS / "gen_hf.py"),
        "--csv", str(csv),
        "--prompt", str(prompt),
        "--out", str(OUTFILE),
        "--model", "meta-llama/Meta-Llama-3-8B-Instruct",
        "--per_abstract", "5",
        "--max_new_tokens", "800",
    ]
    run(cmd)

def run_validate():
    if not OUTFILE.exists():
        print(f"cant validate: missing {OUTFILE}")
        return
    cmd = [sys.executable, str(SCRIPTS / "validate_jsonl.py"), "--in", str(OUTFILE)]
    run(cmd)

if __name__ == "__main__":
    print(f"WEEK_DIR={WEEK_DIR}")
    print(f"DATA   ={DATA}")
    print(f"SCRIPTS={SCRIPTS}")
    print(f"OPENAI={'set' if OPENAI_KEY else 'missing'}, HF={'set' if HF_TOKEN else 'missing'}\n")

    print("1 openai")
    print("2 hf")
    print("3 validate")
    choice = input("enter 1 or 2 or 3: ").strip()

    if choice == "1":
        run_openai()
    elif choice == "2":
        run_hf()
    elif choice == "3":
        run_validate()
