import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import openai
from config import OPENAI_API_KEY, TTS_MODEL, TTS_VOICE, TTS_SPEED

def generate_tts(text_path, output_path):
    openai.api_key = OPENAI_API_KEY
    with open(text_path, "r", encoding="utf-8") as f:
        input_text = f.read()

    speech_file_path = os.path.abspath(output_path)
    response = openai.audio.speech.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        speed=TTS_SPEED,
        input=input_text
    )
    response.stream_to_file(speech_file_path)
    print(f"✅ Đã tạo audio: {speech_file_path}")
