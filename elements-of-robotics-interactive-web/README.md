# Elements of Robotics - Multi-Page Interactive Knowledge Portal 🤖⚡

> **Nền tảng Trưng cất Tri thức & Học tập Tương tác Đa tầng cho Robot học Tự hành**  
> Dựa trên giáo trình chuẩn học thuật quốc tế **"Elements of Robotics"** (Springer Open) của **GS. Mordechai Ben-Ari & GS. Francesco Mondada** (311 trang, 16 chương + 2 phụ lục).

---

## 🌟 ĐẶC ĐIỂM KIẾN TRÚC MỚI (MULTI-PAGE KNOWLEDGE PORTAL)

Hệ thống được thiết kế theo kiến trúc **Portal Hub & Dedicated Chapter Modules**:

1. **Trang Chủ Dashboard Tổng Quan (`index.html`):**
   - **Lộ trình Tổng quan (Curriculum Roadmap):** Hiển thị toàn cảnh 16 chương qua 7 Master Tracks.
   - **Thanh Tìm kiếm Trực tiếp (Live Search):** Gõ từ khóa (*PID, Bayes, SLAM, ToF, Odometry, Braitenberg, A\*, Inverse Kinematics...*) lọc tức thì các thẻ chương.
   - **Các Nút Lọc theo Track (Filter Pills):** Lọc theo từng nhóm chuyên đề (Cảm biến, Hành vi, Động học, Định vị, Lập bản đồ, AI & Học máy, Swarm & Cánh tay 3D).
   - **Thẻ Ma trận (Matrix Grid Cards):** Mỗi thẻ tóm tắt nội dung cốt lõi, gắn tag đại diện và liên kết trực tiếp sang trang riêng của chương đó (`chapters/chXX.html`).

2. **Các Trang Chuyên Đề Riêng Biệt (`chapters/ch01.html` đến `chapters/ch16.html` + 2 Phụ lục):**
   - **Bảo toàn 100% Mục lục Sách Giáo khoa:** Mọi phân mục con (1.1, 1.2, 1.3, 1.4, v.v.) đều được diễn giải chi tiết, không gộp tắt hay lược bỏ.
   - **Toán học & Thuật toán Chuẩn xác:** Render sắc nét bằng MathJax 3, giải thích rõ ràng từng biến số và thứ nguyên chuẩn SI.
   - **Ví dụ Tính số 4 Bước (Worked Numerical Examples):** Bài toán thực tế gán số cụ thể và diễn giải kỹ thuật.
   - **Đồ thị Động Hoạt họa & Bộ Mô phỏng Tương tác (HTML5 Canvas Simulators):** Tích hợp thanh trượt sliders điều chỉnh trực tiếp thông số vật lý thời gian thực.
   - **Điều hướng Chuyên nghiệp:** Breadcrumbs `[🏠 Lộ trình Tổng quan] / [Track] / [Chương]`, nút lật trang `[← Chương trước]` / `[Chương sau →]`, và Sidebar Mục lục riêng (ScrollSpy) của từng chương.
   - **Cầu nối Kiến trúc ROS 2:** Code mẫu, package, topic, launch file thực tế (`ros2_control`, `nav2_amcl`, `slam_toolbox`, `MoveIt 2`).

---

## 🗺️ DANH SÁCH 18 TRANG CHUYÊN ĐỀ ĐỘC LẬP

| Chương / Phụ lục | Đường Dẫn Tệp | Tiêu Đề Chương | Tính Năng Nổi Bật |
| :---: | :--- | :--- | :--- |
| **Portal Hub** | [`index.html`](index.html) | **Tổng Quan Lộ Trình Tri Thức Đào Tạo Robot Học** | 🔍 Tìm kiếm • 🏷️ Lọc 7 Tracks • 16 Thẻ Ma trận |
| **Chương 01** | [`chapters/ch01.html`](chapters/ch01.html) | Robot là gì? - Khái niệm Chuẩn & Giải phẫu Hệ thống | 🔢 Tính công suất & mô-men xoắn vượt dốc |
| **Chương 02** | [`chapters/ch02.html`](chapters/ch02.html) | Hệ thống Cảm biến Thu nhận Môi trường | ⚡ **Mô phỏng ToF Siêu âm** • 📐 SVG Tam giác đạc PSD |
| **Chương 03** | [`chapters/ch03.html`](chapters/ch03.html) | Hành vi Phản xạ & Xe Braitenberg | ⚡ **Mô phỏng Xe Braitenberg 2D** • 📐 SVG 4 Loại Xe |
| **Chương 04** | [`chapters/ch04.html`](chapters/ch04.html) | Máy trạng thái hữu hạn & Vùng trễ (FSM & Hysteresis) | ⚡ **Mô phỏng FSM Trễ Men tường** • 📐 SVG Dải trễ |
| **Chương 05** | [`chapters/ch05.html`](chapters/ch05.html) | Động học Robot Vi sai & Định vị Tích lũy Odometry | ⚡ **Mô phỏng Động học Vi sai & ICC** • 📐 2 Sơ đồ SVG |
| **Chương 06** | [`chapters/ch06.html`](chapters/ch06.html) | Điều khiển Vòng kín PID & Chống Bão hòa Tích phân | ⚡ **Mô phỏng PID Anti-Windup Clamping** • 📐 SVG Đáp ứng Bước |
| **Chương 07** | [`chapters/ch07.html`](chapters/ch07.html) | Định vị Trực tiếp & Phương pháp Hình học (Localization) | 🔢 Giải hệ Trilateration tuyến tính 3 trạm UWB |
| **Chương 08** | [`chapters/ch08.html`](chapters/ch08.html) | Định vị Xác suất & Bộ lọc Bayes (Bayes Filter) | ⚡ **Mô phỏng Bộ lọc Bayes 1D** • 📐 SVG Tiến hóa Niềm tin |
| **Chương 09** | [`chapters/ch09.html`](chapters/ch09.html) | Lập bản đồ Lưới Chiếm chỗ & Nghịch lý SLAM | 🔢 Cập nhật Log-Odds qua 3 lần quét laser |
| **Chương 10** | [`chapters/ch10.html`](chapters/ch10.html) | Không gian C-Space & Thuật toán Tìm đường A* | ⚡ **Mô phỏng A* Pathfinding Grid (Vẽ tường)** • 🔢 Duyệt tay A* |
| **Chương 11** | [`chapters/ch11.html`](chapters/ch11.html) | Môi trường Phức tạp & Điều khiển Logic Mờ (Fuzzy) | 🔢 Giải mờ Trọng tâm Centroid (p.186) |
| **Chương 12** | [`chapters/ch12.html`](chapters/ch12.html) | Xử lý Ảnh Số & Thị giác Máy tính cho Robot | 🔢 Nhân chập ma trận Sobel $3 \times 3$ |
| **Chương 13** | [`chapters/ch13.html`](chapters/ch13.html) | Mạng Nơ-ron & Học Máy Lấy Cảm Hứng Sinh Học | 🔢 Cập nhật trọng số Perceptron |
| **Chương 14** | [`chapters/ch14.html`](chapters/ch14.html) | Bộ Phân Loại Fisher LDA & Trực Giác Q-Learning | 🔢 Cập nhật phương trình Bellman |
| **Chương 15** | [`chapters/ch15.html`](chapters/ch15.html) | Robot Bầy Đàn & Thuật Toán Tụ Hội BeeClust | 🔢 Tính thời gian dừng BeeClust (p.260) |
| **Chương 16** | [`chapters/ch16.html`](chapters/ch16.html) | Cánh Tay Thao Tác 2-DOF & Động Học Không Gian 3D | ⚡ **Mô phỏng Cánh tay 2-DOF Kéo Thả IK** • 📐 SVG Động học |
| **Phụ lục A** | [`chapters/appendix-a.html`](chapters/appendix-a.html) | Nền tảng Toán học cho Kỹ thuật Robot | Lượng giác, Nhóm quay $SO(2)/SO(3)$, $SE(2)/SE(3)$, Gauss |
| **Phụ lục B** | [`chapters/appendix-b.html`](chapters/appendix-b.html) | Cầu nối Kiến trúc sang ROS 2 Humble / Jazzy | Bản đồ đối chiếu Package, Topic, Launch file |

---

## 📁 CẤU TRÚC THƯ MỤC DỰ ÁN

```text
elements-of-robotics-interactive-web/
├── index.html                                 # Trang Portal Dashboard Hub
├── README.md                                  # Hướng dẫn chi tiết & cách triển khai
├── assets/
│   ├── css/
│   │   └── style.css                          # Design System (Theme, Matrix, Breadcrumbs, Stepper)
│   ├── js/
│   │   ├── app.js                             # Logic chung (Theme, Live Search, ScrollSpy)
│   │   └── simulators.js                      # 8 bộ mô phỏng HTML5 Canvas tương tác (44.5 KB)
│   └── images/                                # 8 sơ đồ vector SVG chuẩn học thuật
│       ├── psd_triangulation.svg
│       ├── braitenberg.svg
│       ├── fsm_hysteresis.svg
│       ├── diff_drive.svg
│       ├── odometry_drift.svg
│       ├── pid_response.svg
│       ├── bayes_evolution.svg
│       └── robot_arm.svg
├── chapters/                                  # 18 Trang chuyên đề độc lập
│   ├── ch01.html -> ch16.html
│   ├── appendix-a.html
│   └── appendix-b.html
└── materials/
    ├── Elements_of_Robotics_Distillation.md   # Bản ghi chép tri thức Markdown
    ├── Elements_of_Robots_Freebook.pdf        # Sách giáo trình gốc Springer Open (311 trang)
    └── Elements_of_Robotics_Distillation_legacy.html
```

---

## 🚀 HƯỚNG DẪN CHẠY & TRIỂN KHAI LÊN GITHUB PAGES (`github.io`)

### 1. Trải nghiệm Cục bộ
Nhấp đúp chuột vào tệp `index.html` để mở trực tiếp trong trình duyệt (Chrome, Edge, Firefox, Safari).

### 2. Triển khai Lên GitHub Pages (1 Bước Đơn Giản)
1. Đẩy toàn bộ thư mục lên repository GitHub của bạn:
   ```bash
   git init
   git add .
   git commit -m "feat: complete multi-page interactive portal for Elements of Robotics"
   git branch -M main
   git remote add origin https://github.com/<username>/<repo-name>.git
   git push -u origin main
   ```
2. Mở Repository trên GitHub $\to$ **Settings** $\to$ **Pages**.
3. Tại **Build and deployment**, chọn Branch **`main`** và thư mục **`/(root)`** $\to$ Bấm **Save**.
4. Trang web sẽ trực tuyến ngay tại:
   `https://<username>.github.io/<repo-name>/`

---
*Dự án được xây dựng và chuẩn hóa bởi Hệ thống Antigravity AI, tuân thủ nghiêm ngặt chuẩn mực học thuật quốc tế.*
