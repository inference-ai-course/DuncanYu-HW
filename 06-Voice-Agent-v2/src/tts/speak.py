from TTS.api import TTS
import tempfile
import os

tts = None
tts_model_name = None

def generate_tts(text, model, speaker):
    global tts, tts_model_name
    if tts is None or tts_model_name != model:
        tts = TTS(model)
        tts_model_name = model
    temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    path = temp_file.name
    temp_file.close()
    tts.tts_to_file(text=text, file_path=path, speaker=speaker)
    return path
