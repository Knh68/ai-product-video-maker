# Facebook Video Seller 🚀🎬

Tự động tạo video bán hàng hấp dẫn từ văn bản với giọng đọc AI, phụ đề, hình ảnh minh họa và nhạc nền.  
Ứng dụng lý tưởng cho quảng bá sản phẩm trên Facebook, YouTube, TikTok...

---

## 💡 Tính năng
- ✅ Chuyển văn bản thành giọng đọc tự nhiên (OpenAI TTS)
- ✅ Tạo phụ đề đồng bộ theo giọng đọc
- ✅ Ghép hình ảnh minh họa và nhạc nền
- ✅ Tự động chia kịch bản nếu quá dài
- ✅ Xuất video MP4 sẵn sàng đăng Facebook

---
🧙 Yêu cầu hệ thống
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
## ▶️ Cách sử dụng
Cài đặt: pip install -r requirements.txt

1. **Tạo nội dung** trong `input/full_script.txt` (kịch bản bán hàng)
2. **Thêm hình ảnh** vào `input/images/`
3. (Tùy chọn) Thêm nhạc nền `input/background.mp3`
4. Chạy:
```bash
python main.py

📄 Giấy phép sử dụng – MIT License
Bạn được phép sử dụng lại, chỉnh sửa, và tích hợp dự án này cho mục đích cá nhân hoặc thương mại, miễn là giữ nguyên thông tin bản quyền trong file LICENSE.

Dự án được chia sẻ với tinh thần cộng đồng và sáng tạo tự do.
Chúng tôi không chịu trách nhiệm nếu có lỗi hoặc thiệt hại phát sinh khi sử dụng phần mềm.
Xem chi tiết tại: LICENSE
❤️ Credits
Chia sẻ để lan tỏa ứng dụng AI vào kinh doanh hiệu quả
🤝 Dự án này được hoàn thành với sự đồng hành và hỗ trợ tuyệt vời từ ChatGPT – Trợ lý AI đáng tin cậy trong hành trình sáng tạo.
