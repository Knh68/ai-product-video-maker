# scripts/merge_videos.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from moviepy.editor import VideoFileClip, concatenate_videoclips
from config import OUTPUT_DIR


def get_part_videos():
    files = sorted(
        [f for f in os.listdir(OUTPUT_DIR) if f.startswith("part") and f.endswith(".mp4")],
        key=lambda x: int(x.replace("part", "").replace(".mp4", ""))
    )
    return [os.path.join(OUTPUT_DIR, f) for f in files]


def merge_videos():
    video_paths = get_part_videos()
    if not video_paths:
        print("❌ Không tìm thấy video để gộp!")
        return

    print(f"🔗 Đang gộp {len(video_paths)} video...")
    clips = [VideoFileClip(v) for v in video_paths]
    final = concatenate_videoclips(clips, method="compose")
    output_path = os.path.join(OUTPUT_DIR, "full_video.mp4")
    final.write_videofile(output_path, fps=24)
    print(f"✅ Video hoàn chỉnh: {output_path}")


if __name__ == "__main__":
    merge_videos()