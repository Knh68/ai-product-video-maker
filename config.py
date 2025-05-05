import os
from dotenv import load_dotenv

load_dotenv()  # Đọc biến môi trường từ .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TTS_MODEL = os.getenv("TTS_MODEL", "tts-1")
TTS_VOICE = os.getenv("TTS_VOICE", "echo")
TTS_SPEED = float(os.getenv("TTS_SPEED", 1.0))
# Thư mục xử lý
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_DIR = os.path.join(BASE_DIR, "input")
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
SUBTITLE_DIR = os.path.join(BASE_DIR, "subtitles")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Tự tạo thư mục nếu chưa có
for folder in [INPUT_DIR, AUDIO_DIR, SUBTITLE_DIR, OUTPUT_DIR]:
    os.makedirs(folder, exist_ok=True)
