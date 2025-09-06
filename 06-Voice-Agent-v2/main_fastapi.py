from fastapi import FastAPI, File, UploadFile, Body
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import tempfile
import base64
from pathlib import Path

from Week6.src.asr.transcriber import transcribe
from Week6.src.llm.openai_llm import gpt_respond
from Week6.src.llm.router import route_llm_output
from Week6.src.tts.speak import generate_tts
from Week6.config import OPENAI_MODEL, TTS_MODEL, TTS_SPEAKER

app = FastAPI()

STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def index():
    return open(str(STATIC_DIR / "index.html")).read()

@app.post("/chat/")
async def chat(audio_file: UploadFile = File(...)):
    wav_bytes = await audio_file.read()
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp.write(wav_bytes)
        audio_path = tmp.name
    transcript = transcribe(audio_path)
    response_text = gpt_respond(transcript, model=OPENAI_MODEL)
    tts_path = generate_tts(response_text, TTS_MODEL, TTS_SPEAKER)
    audio_b64 = base64.b64encode(open(tts_path, "rb").read()).decode()
    return JSONResponse({"transcript": transcript, "response": response_text, "audio": audio_b64})

@app.post("/voice_query")
async def voice_query(req=Body(...)):
    user_text = req.get("text", "")
    llm_response = gpt_respond(user_text, model=OPENAI_MODEL)
    final_text, used_tool = route_llm_output(llm_response)
    tts_path = generate_tts(final_text, TTS_MODEL, TTS_SPEAKER)
    audio_b64 = base64.b64encode(open(tts_path, "rb").read()).decode()
    return {"text": final_text, "used_tool": used_tool, "audio_b64": audio_b64}

if __name__ == "__main__":
    uvicorn.run("Week6.main_fastapi:app", host="0.0.0.0", port=8000, reload=True)