# Học Từ Đầu — Trang web học tiếng Anh (bản tĩnh)

## Giới thiệu & Công dụng

**Học Từ Đầu** là một trang web tĩnh được thiết kế nhằm giúp người mới bắt đầu học tiếng Anh tự rèn luyện toàn diện 4 kỹ năng cơ bản (Từ vựng, Nghe, Nói, Viết) một cách trực quan, dễ tiếp cận và hiệu quả.

### Công dụng & Tính năng chính:
- **Luyện từ vựng (`tu-vung.html`, `tu-vung-bai-hoc.html`):** Học từ mới qua thẻ ghi nhớ Flashcard tương tác (lật thẻ, nghe phát âm) và củng cố kiến thức bằng các bài tập điền từ trực quan theo từng chủ đề.
- **Luyện nghe (`nghe.html`, `nghe-bai-hoc.html`):** Luyện phản xạ nghe hiểu qua các đoạn hội thoại tình huống giao tiếp thực tế (như gọi món tại nhà hàng), điền từ còn thiếu vào lời thoại.
- **Luyện nói (`noi.html`, `noi-bai-hoc.html`):** Luyện tập giao tiếp tương tác bằng giọng nói sử dụng Web Speech API (`SpeechRecognition`). Hệ thống ghi nhận phát âm trực tiếp từ micro và chuyển thành văn bản để người học tự kiểm tra.
- **Luyện viết (`viet.html`, `viet-bai-hoc.html`):** Luyện tập kỹ năng viết câu, đặt câu theo ngữ cảnh và viết đoạn văn ngắn theo các gợi ý bài học.
- **Hệ thống Đăng nhập / Đăng ký mô phỏng (`login.html`, `signup.html`):** Giúp người học trải nghiệm luồng người dùng (user flow) hoàn chỉnh, dữ liệu được lưu tạm thời trên `localStorage`.

---

## Cấu trúc project

```
learn-english-web/
├── index.html                 → Trang chủ (chọn trình độ A1-C2, thanh điều hướng Đăng nhập/Đăng ký)
├── login.html                 → Trang Đăng nhập (mô phỏng, lưu bằng localStorage)
├── signup.html                → Trang Đăng ký (mô phỏng, lưu bằng localStorage)
├── pages/
│   ├── tu-vung.html            → Danh sách trình độ & chủ đề từ vựng
│   ├── tu-vung-bai-hoc.html    → Bài học từ vựng: Flashcard + bài tập điền từ (chủ đề Food)
│   ├── nghe.html                → Danh sách trình độ & chủ đề bài nghe
│   ├── nghe-bai-hoc.html        → Bài nghe: Hội thoại nhà hàng, điền từ còn thiếu
│   ├── noi.html                  → Danh sách trình độ & tình huống luyện nói
│   ├── noi-bai-hoc.html          → Bài nói: Hội thoại giao tiếp qua micro (Web Speech API)
│   ├── viet.html                 → Danh sách trình độ & chủ đề luyện viết
│   └── viet-bai-hoc.html         → Bài viết: Đặt câu và viết đoạn văn theo gợi ý
├── assets/
│   ├── css/
│   │   └── style.css          → CSS dùng chung toàn trang (theme xanh dương / trắng modern)
│   └── js/
│       ├── auth.js             → Xử lý đăng nhập / đăng ký mô phỏng
│       ├── tu-vung-bai-hoc.js  → Logic Flashcard + bài tập điền từ vựng
│       ├── nghe-bai-hoc.js     → Logic phát thanh + hội thoại nghe điền từ
│       ├── noi-bai-hoc.js      → Logic nhận diện giọng nói qua micro (Web Speech API)
│       └── viet-bai-hoc.js     → Logic xử lý bài tập luyện viết & kiểm tra
└── README.md                  → Tài liệu hướng dẫn sử dụng và cấu trúc dự án
```

---

## Hướng dẫn cài đặt & Chạy dự án

Dùng **VS Code** kết hợp extension **Live Server** (khuyến nghị):
1. Mở thư mục `learn-english-web` trong VS Code.
2. Nhấp chuột phải vào file `index.html` → Chọn **"Open with Live Server"**.
3. *Lưu ý quan trọng:* Cách chạy qua server local này là **bắt buộc** để tính năng **Micro (nhận diện giọng nói)** ở trang Luyện Nói hoạt động ổn định, do các trình duyệt hiện đại chặn quyền truy cập mic nếu mở file theo giao thức trực tiếp (`file://`).

---

## Chi tiết các tính năng & Lưu ý kỹ thuật

### 1. Phần Đăng nhập / Đăng ký (Auth)
- Đây là bản **MÔ PHỎNG (Mock Up)** — thông tin tài khoản được lưu trữ trong không gian `localStorage` của trình duyệt, chưa phải hệ thống backend thật.
- Nếu người dùng xóa dữ liệu duyệt web (Clear Storage / Cache), thông tin tài khoản demo sẽ bị xóa.
- Khi tích hợp Backend (ví dụ FastAPI): Toàn bộ logic trong `auth.js` sẽ được thay thế bằng lệnh gọi API thực tế (`/api/register`, `/api/login`), xác thực qua Token/JWT và lưu cơ sở dữ liệu.
- *Thử nghiệm:* Truy cập `login.html` khi chưa đăng ký tài khoản → Hệ thống hiển thị thông báo "Bạn chưa có tài khoản, vui lòng đăng ký".

### 2. Phần Luyện Nói (Web Speech API)
- Trang `noi-bai-hoc.html` sử dụng API chuẩn `SpeechRecognition` tích hợp sẵn trên trình duyệt (hoạt động mượt mà nhất trên **Google Chrome** hoặc **Microsoft Edge**).
- Lần đầu sử dụng, trình duyệt sẽ yêu cầu cấp quyền sử dụng Micro — vui lòng bấm **"Allow" (Cho phép)**.
- Trong trường hợp trình duyệt không hỗ trợ Web Speech API (như Safari hoặc IE cũ), trang sẽ tự động nhận biết và chuyển sang giao diện ô nhập liệu văn bản.
- *Lưu ý:* Hiện tại hệ thống ghi nhận giọng nói và hiển thị lại lời nói của bạn dưới dạng văn bản. Phần chấm điểm tự động phát âm/ngữ pháp AI sẽ được bổ sung khi phát triển Backend.

### 3. Phần Luyện Viết
- Trang `viet-bai-hoc.html` cung cấp các bài tập đặt câu theo ngữ cảnh và viết đoạn văn mẫu.
- Cho phép người học thực hành gõ câu tiếng Anh và nhận phản hồi mô phỏng gợi ý sửa lỗi.

---

## Nội dung bài học mẫu

Hiện tại dự án đã hoàn thiện đầy đủ nội dung mẫu cho **Trình độ A1 — Chủ đề "Food" (Ăn uống)** ở cả 4 kỹ năng:
- **Từ vựng:** Thẻ từ vựng món ăn, thức uống + bài tập ghép từ.
- **Nghe:** Bài nghe gọi món tại nhà hàng.
- **Nói:** Hội thoại đặt bàn và gọi món ăn.
- **Viết:** Bài tập viết câu miêu tả món ăn yêu thích và đoạn văn ngắn.

Các chủ đề khác hiển thị biểu tượng **"🔒 Sắp mở khóa"**. Để bổ sung nội dung mới, chỉ cần nhân bản (copy) cấu trúc bài học của chủ đề Food và cập nhật lại dữ liệu trong file JS tương ứng.

---

## Kế hoạch phát triển tiếp theo (Roadmap)

- [ ] **Tích hợp Backend (FastAPI / Node.js):** Thay thế dữ liệu cứng bằng Restful API, quản lý người dùng thực tế với JWT Authentication.
- [ ] **Chấm điểm bằng AI:** Kết hợp OpenAI API hoặc Speech-to-Text AI để chấm điểm phát âm, ngữ pháp và gợi ý sửa lỗi bài viết.
- [ ] **Mở khóa chủ đề:** Mở rộng dữ liệu bài học cho các trình độ A2, B1, B2, C1, C2 và các chủ đề còn lại.
- [ ] **Lưu tiến độ học tập:** Lưu trữ điểm số, lịch sử bài học và chuỗi ngày học (streak) vào Database.