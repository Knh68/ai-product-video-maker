# ai-product-video-maker 🚀🎬

> 📢 Dự án tạo video bán hàng bằng AI – hỗ trợ Facebook, TikTok, YouTube, giọng đọc và phụ đề tự động.
---

## 💡 Tính năng
- ✅ Chuyển văn bản thành giọng đọc tự nhiên (OpenAI TTS)
- ✅ Tạo phụ đề đồng bộ theo giọng đọc
- ✅ Ghép hình ảnh minh họa và nhạc nền
- ✅ Tự động chia kịch bản nếu quá dài
- ✅ Xuất video MP4 sẵn sàng đăng Facebook

---
🧙 Yêu cầu hệ thống:
Đã thử với Python 3.9.13
🖼️ ImageMagick
MoviePy cần ImageMagick để hiển thị phụ đề đẹp (chữ căn giữa, có nền mờ):

Tải tại: https://imagemagick.org/

Khi cài đặt, hãy tick chọn: ✅ "Install legacy utilities (convert)"

Cập nhật đường dẫn magick.exe trong video_maker.py nếu cần

## 📂 Cấu trúc thư mục
```
project/
├── main.py
├── config.py
├── scripts/
│ ├── tts_engine.py
│ ├── subtitle_generator.py
│ └── video_maker.py
├── input/
│ ├── full_script.txt
│ ├── images/
│ └── background.mp3
├── audio/
├── subtitles/
├── output/
└── requirements.txt
```
**Cấu hình OpenAI API Key:**
Mở file .env, dán Key vào ```sk-nhập OpenAI key của bạn``` và lưu lại
c**ác tùy chọn bổ sung**
**Giọng đọc:**
TTS_VOICE=echo mặc định giọng đọc nam, để có giọng đọc nữ, đổi thành: TTS_VOICE=nova
**Tốc độ đọc**
TTS_SPEED=1.0 mặc định, tăng tốc độ đọc ví dụ: TTS_SPEED=1.2
Sau khi điều chỉnh lưu lại.
## ▶️ Cách sử dụng
Cài đặt: pip install -r requirements.txt

1. **Tạo nội dung** trong `input/full_script.txt` (kịch bản bán hàng)
2. **Thêm hình ảnh** vào `input/images/`
3. (Tùy chọn) Thêm nhạc nền `input/background.mp3`
4. Chạy:
```bash
python main.py```
Kết quả: Video xuất ra ở thư mục output, trường hợp full_script.txt dài, có thể xuất nhiều file video mp4.
Nếu nhiều file mp4, gộp lại bằng cách chạy: python scripts/merge_videos.py
kết quả sẽ có file final_video.mp4 trong thư mục output.

**Những hạn chế**
Video sẽ lấy các hình ảnh làm nền với hiệu ứng nhẹ. 
Có thể dùng file mp3 và file phụ đề ở thư mục audio và subtitles đã đồng bộ chính xác cùng nhau và chuyển qua các ứng dụng mạnh mẽ khác như Canva, CapCut có thể tiết kiệm thời gian.

📄 **Giấy phép sử dụng – MIT License**
Bạn được phép sử dụng lại, chỉnh sửa, và tích hợp dự án này cho mục đích cá nhân hoặc thương mại, miễn là giữ nguyên thông tin bản quyền trong file LICENSE.
```
Dự án được chia sẻ với tinh thần cộng đồng và sáng tạo tự do.
Chúng tôi không chịu trách nhiệm nếu có lỗi hoặc thiệt hại phát sinh khi sử dụng phần mềm.
Xem chi tiết tại: LICENSE
❤️ Credits
Chia sẻ để lan tỏa ứng dụng AI vào kinh doanh hiệu quả
🤝 Dự án này được hoàn thành với sự đồng hành và hỗ trợ tuyệt vời từ ChatGPT – Trợ lý AI đáng tin cậy trong hành trình sáng tạo.
```
