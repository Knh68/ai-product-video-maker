# scripts/video_maker.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import moviepy.config as mp_config
mp_config.change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})
from config import INPUT_DIR, OUTPUT_DIR
from moviepy.editor import (
    ImageClip,
    concatenate_videoclips,
    AudioFileClip,
    CompositeAudioClip,
    TextClip,
    CompositeVideoClip
)
import random
import srt
import datetime

VIDEO_SIZE = (1080, 1350)  # Tỷ lệ 4:5 – phù hợp Facebook
IMAGE_DURATION = 5
MUSIC_PATH = os.path.join("input", "background.mp3")
FONT = "Arial"
FONTSIZE = 26
COLOR = "#F0FD61"


def get_image_files(folder):
    exts = ['.jpg', '.jpeg', '.png']
    return [os.path.join(folder, f) for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in exts]


def load_subtitles(subtitle_path):
    with open(subtitle_path, "r", encoding="utf-8") as f:
        return list(srt.parse(f.read()))


def create_video(part_id):
    image_folder = os.path.join(INPUT_DIR, "images")
    audio_path = os.path.join("audio", f"part{part_id}.mp3")
    subtitle_path = os.path.join("subtitles", f"part{part_id}.srt")
    output_path = os.path.join(OUTPUT_DIR, f"part{part_id}.mp4")

    image_files = get_image_files(image_folder)
    if not image_files:
        raise ValueError("❌ Không tìm thấy hình ảnh trong thư mục!")

    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration

    num_images = int(audio_duration / IMAGE_DURATION) + 1

    if len(image_files) < num_images:
        repeat_times = (num_images // len(image_files)) + 1
        image_files *= repeat_times

    selected_images = image_files[:num_images]
    clips = []

    for img_path in selected_images:
        img_clip = ImageClip(img_path, duration=IMAGE_DURATION)
        img_clip = img_clip.resize(newsize=VIDEO_SIZE).fadein(0.5).fadeout(0.5)
        clips.append(img_clip)

    base_video = concatenate_videoclips(clips, method="compose").set_duration(audio_duration)

    # Phụ đề căn giữa từng dòng
    subtitles = load_subtitles(subtitle_path)
    subtitle_clips = []
    for sub in subtitles:
        text = TextClip(
            sub.content.upper(),
            fontsize=FONTSIZE,
            color=COLOR,
            font="Arial-Bold",
            method="caption",
            size=(VIDEO_SIZE[0] - 100, None),
            align="center"
        )

        # Khung nền mờ
        bg = (text
              .on_color(size=(text.w + 20, text.h + 10),
                        color=(0, 0, 0), col_opacity=0.4)
              .set_position(("center", VIDEO_SIZE[1] - 100))  # căn thấp hơn
              .set_start(sub.start.total_seconds())
              .set_end(sub.end.total_seconds()))

        subtitle_clips.append(bg)

    video_with_subs = CompositeVideoClip([base_video] + subtitle_clips)

    # Nhạc nền nếu có
    if os.path.exists(MUSIC_PATH):
        music = AudioFileClip(MUSIC_PATH).volumex(0.3).set_duration(audio_duration)
        final_audio = CompositeAudioClip([music, audio_clip])
    else:
        final_audio = audio_clip

    final_clip = video_with_subs.set_audio(final_audio)
    final_clip.write_videofile(output_path, fps=24)
    print(f"✅ Đã tạo video: {output_path}")
