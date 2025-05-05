import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scripts.tts_engine import generate_tts
from scripts.subtitle_generator import generate_subtitles
from scripts.video_maker import create_video
from moviepy.editor import AudioFileClip
from config import INPUT_DIR, AUDIO_DIR, SUBTITLE_DIR

def split_script_if_needed(text, max_duration=120, avg_words_per_second=2.5):
    """
    Chia văn bản thành các đoạn nhỏ, mỗi đoạn ~120s (dựa vào tốc độ nói trung bình).
    """
    words = text.split()
    words_per_part = int(max_duration * avg_words_per_second)
    parts = [words[i:i + words_per_part] for i in range(0, len(words), words_per_part)]

    for idx, part_words in enumerate(parts, start=1):
        part_text = ' '.join(part_words)
        output_path = os.path.join(INPUT_DIR, f"script_part{idx}.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(part_text)
        print(f"📄 Đã tạo file script_part{idx}.txt ({len(part_words)} từ)")

def run_pipeline(part_id):
    script_path = os.path.join(INPUT_DIR, f"script_part{part_id}.txt")
    audio_path = os.path.join(AUDIO_DIR, f"part{part_id}.mp3")
    subtitle_path = os.path.join(SUBTITLE_DIR, f"part{part_id}.srt")

    print(f"▶️ Bắt đầu xử lý part{part_id}...")

    generate_tts(script_path, audio_path)

    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    generate_subtitles(script_path, duration, subtitle_path)

    create_video(part_id)
    print(f"🎬 Hoàn tất part{part_id}\n")

if __name__ == "__main__":
    # B1: Kiểm tra full_script.txt có tồn tại không
    full_script_path = os.path.join(INPUT_DIR, "full_script.txt")
    if os.path.exists(full_script_path):
        with open(full_script_path, "r", encoding="utf-8") as f:
            full_text = f.read()
        split_script_if_needed(full_text)
    else:
        print("❗ Không tìm thấy full_script.txt")

    # B2: Chạy từng part nếu tồn tại
    for part_id in range(1, 10):  # tối đa 9 phần
        part_path = os.path.join(INPUT_DIR, f"script_part{part_id}.txt")
        if os.path.exists(part_path):
            run_pipeline(part_id)
