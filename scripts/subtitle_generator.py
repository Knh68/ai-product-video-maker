import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import srt
import datetime
from config import SUBTITLE_DIR

def split_text_into_lines(text, max_chars=70):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + " " + word) <= max_chars:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

def generate_subtitles(text_path, duration, output_path):
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read()

    lines = split_text_into_lines(text)
    total_lines = len(lines)
    avg_duration = duration / total_lines
    subs = []

    for i, line in enumerate(lines):
        start = datetime.timedelta(seconds=i * avg_duration)
        end = datetime.timedelta(seconds=(i + 1) * avg_duration)
        subs.append(srt.Subtitle(index=i+1, start=start, end=end, content=line))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(srt.compose(subs))
    print(f"✅ Đã tạo phụ đề: {output_path}")