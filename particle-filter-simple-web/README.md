# Particle Filter Made Simple: Knowledge Portal (#12)

Cổng thông tin tri thức học thuật tương tác chất lượng cao được chưng cất toàn diện từ chuyên khảo:
**"Particle Filter Made Simple: A Step-by-Step Beginner-friendly Guide"**
Tác giả: **Sahil Rajesh Dhayalkar** (Arizona State University, arXiv:2511.01281)

---

## 🌟 Tổng Quan Kiến Trúc & Số Liệu Chuyên Khảo

- **5 Chương Học Thuật 6 Tầng:** Bảo toàn 100% đề mục gốc, phân tích Why It Matters, công thức MathJax 3 chuẩn xác, ví dụ số học 4 bước, mô phỏng Canvas 60 FPS và cầu nối ROS 2 / C++.
- **5 Mô Phỏng Canvas 2D 60 FPS:**
  1. *Chương 01:* So sánh phân bố đơn đỉnh Kalman vs Đám mây hạt đa đỉnh trong hành lang đối xứng.
  2. *Chương 02:* Histogram xác suất chuyển động Monte Carlo & truyền trạng thái phi tuyến.
  3. *Chương 03:* Thoái hóa mẫu, tính toán $N_{eff}$ & vòng quay Systematic Resampling roulette.
  4. *Chương 04:* Bám vết trực tiếp vật thể 1D theo từng bước thời gian ($Q=1.0, R=4.0$).
  5. *Chương 05:* Định vị Robot Monte Carlo 2D với 4 cột mốc & Nút bấm "Bắt cóc Robot" (Kidnap Recovery).
- **5 Bài Tập Số Học 4 Bước:** Giải chi tiết từng phép cộng trừ nhân chia số học bằng tay.
- **2 Trục Kiến Thức (Tracks):**
  - **Track 1:** Cơ Sở Lý Thuyết & Thuật Toán SIR (Chương 01 - 03)
  - **Track 2:** Thực Hành Số Học & Lọc Đa Chiều (Chương 04 - 05)

---

## 📂 Cấu Trúc Thư Mục

```
web-content/particle-filter-simple-web/
├── index.html                   # Hub Dashboard với Live Search, Filter Pills & Stats
├── README.md                    # Tài liệu kỹ thuật
├── template_helpers.py          # Bộ sinh template trang học thuật
├── build_portal.py              # Metadata 5 chương
├── build_ch01.py .. build_ch05.py # Bộ sinh 5 trang chương chi tiết
├── build_index.py               # Bộ sinh Hub Dashboard
├── assets/
│   ├── css/
│   │   └── style.css            # Hệ thống Design System học thuật, Dark/Light mode
│   └── js/
│       ├── app.js               # Search Ctrl+K, Filter Pills, ScrollSpy, Theme Manager (pf-theme)
│       └── simulators.js        # Bộ 5 bộ mô phỏng Canvas 2D 60 FPS tương tác
└── chapters/
    ├── ch01.html                # Chương 01: Giới thiệu & Nhu cầu bộ lọc hạt
    ├── ch02.html                # Chương 02: Từ ý tưởng đến biểu diễn toán học
    ├── ch03.html                # Chương 03: Thuật toán SIR toàn diện
    ├── ch04.html                # Chương 04: Ví dụ số học 1D & Code Lab
    └── ch05.html                # Chương 05: Bộ lọc hạt trong không gian đa chiều
```

---

## 🚀 Triển Khai & Kiểm Thử

- **Local Preview:** `http://localhost:8777/particle-filter-simple-web/`
- **Master Gateway:** `http://localhost:8777/index.html`
- **Live GitHub Pages:** `https://chucuong250698.github.io/robotics-portals/particle-filter-simple-web/`
