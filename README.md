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

## 📂 Cấu trúc thư mục

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

---

## ▶️ Cách sử dụng

1. **Tạo nội dung** trong `input/full_script.txt` (kịch bản bán hàng)
2. **Thêm hình ảnh** vào `input/images/`
3. (Tùy chọn) Thêm nhạc nền `input/background.mp3`
4. Chạy:
```bash
python main.py
❤️ Credits
Chia sẻ để lan tỏa ứng dụng AI vào kinh doanh hiệu quả
🤝 Dự án này được hoàn thành với sự đồng hành và hỗ trợ tuyệt vời từ ChatGPT – Trợ lý AI đáng tin cậy trong hành trình sáng tạo.
