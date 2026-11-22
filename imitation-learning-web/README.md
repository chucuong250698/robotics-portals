# Học Bắt Chước Trong Robot Học (Imitation Learning & Interactive IL) - Explorable Knowledge Portal

Cổng thông tin chưng cất tri thức chuẩn học thuật và kỹ thuật số đa tầng SOTA, được thiết kế theo tiêu chuẩn kỹ thuật **Deep Reading Distiller** từ các chuyên khảo và công trình nền tảng:
- **Carlos Celemin, Jens Kober et al.** (*Foundations and Trends in Robotics*, 2022) - *Interactive Imitation Learning in Robotics*.
- **Boyuan Zheng et al.** (*University of Technology Sydney*, 2021) - *Imitation Learning: A Survey of Learning Methods*.
- **Maryam Zare et al.** (*IEEE*, 2023) - *A Survey of Imitation Learning: Algorithms and Applications*.

---

## 🗺️ Ma Trận 14 Chương Qua 6 Master Tracks

| Track | Chương | Tiêu Đề Chương | Trọng Tâm Kiến Thức & Thuật Toán | Mô Phỏng Tương Tác Canvas 2D | Cầu Nối Thực Tế |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Track 1** | **Ch 01** | Giới Thiệu Học Bắt Chước & Khung Quyết Định Toán Học | MDPs $\langle \mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma \rangle$, Hiệu quả mẫu IL vs RL, Dữ liệu $\mathcal{D}_E$, 3 Trường phái BC/IRL/IIL | So sánh 3 trường phái BC vs IRL vs IIL | HDF5 Dataset |
| | **Ch 02** | Nhân Bản Hành Vi (BC) & Lệch Phân Phối Covariate Shift | Supervised Learning, Chứng minh sai số $O(T^2 \epsilon)$, Hiện tượng Causal Confusion | Mô phỏng dạt quỹ đạo Covariate Shift | PyTorch BC |
| **Track 2** | **Ch 03** | Phản Hồi Đánh Giá (Evaluative) & RLHF Trong Robot | Phản hồi nhị phân TAMER, Phân phối Dirichlet COACH, Tín dụng người $H$ | Mô phỏng Huấn luyện Khen/Chê TAMER | Python TAMER |
| | **Ch 04** | Phản Hồi Hiệu Chỉnh & Họ Thuật Toán DAgger / SafeDAgger | DAgger gộp dữ liệu chặn sai số $O(T\epsilon)$, SafeDAgger chuyển quyền an toàn, HG-DAgger | Mô phỏng Gộp Mẫu DAgger & Phân loại Can thiệp | ROS 2 DAgger |
| **Track 3** | **Ch 05** | Động Tác Nguyên Mẫu Động Lực Học (DMPs) & ProMPs | Hệ chính tắc pha $s$, Hệ biến đổi bậc 2 ổn định Lyapunov, Hàm lực phi tuyến RBF, ProMPs | Co dãn không gian $g$ & thời gian $\tau$ | ROS 2 DMP Node |
| | **Ch 06** | Diffusion Policy & Action Chunking Transformers (ACT) | Phân phối hành vi đa mốt (Multimodal), DDPM khử nhiễu ngược, ACT C-VAE, Temporal Ensembling | Quá trình khử nhiễu Denoising DDPM | PyTorch U-Net 1D |
| **Track 4** | **Ch 07** | Học Tăng Cường Nghịch Đảo (Inverse RL) & Maximum Entropy | Khôi phục phần thưởng ẩn $R^*(s,a)$, Max-Margin, MaxEnt IRL (Ziebart 2008), Feature Matching | Bản đồ nhiệt phần thưởng Gridworld | Python SVF Solver |
| | **Ch 08** | Học Bắt Chước Đối Nghịch GAIL & Khớp Phân Phối Chiếm Dụng | Định lý Ho-Ermon (2016), Phân phối chiếm dụng $d_\pi(s,a)$, Discriminator $D_\psi$, AIRL | Hội tụ phân phối chiếm dụng $d_\pi \to d_E$ | PyTorch GAIL + PPO |
| **Track 5** | **Ch 09** | Học Bắt Chước Chỉ Từ Quan Sát (Imitation from Observation - IfO) | Bắt chước từ video không nhãn hành động, Thuật toán BCO, Mô hình động lực học nghịch $f_\phi^{-1}$ | Suy luận hành động từ cặp quan sát | PyTorch BCO |
| | **Ch 10** | Học Từ Chuyên Gia Lỗi & Ngoại Suy Phần Thưởng (T-REX & D-REX) | Dữ liệu lỗi (Suboptimal), Mô hình xếp hạng Bradley-Terry, Ngoại suy siêu phàm Super-Human | Đường ngoại suy vượt trần con người | Ranking Loss GPU |
| | **Ch 11** | Bất Đồng Hình Thái & Chuyển Đổi Sim-to-Real | The Correspondence Problem, Domain Randomization vượt Reality Gap, Open X-Embodiment | Ánh xạ bàn tay người sang tay kẹp | ROS 2 Retargeting |
| **Track 6** | **Ch 12** | Giao Diện HRI, Dạy Học Động Học & Tự Chủ Chia Sẻ (Shared Autonomy) | Kinesthetic Teaching, Leader-Follower teleoperation, Bộ điều khiển $\alpha$-Blending, Barrier Functions | Tự chủ chia sẻ vượt hành lang an toàn | C++ Gravity Comp |
| | **Ch 13** | Thước Đo Đánh Giá & Các Bộ Benchmark Tiêu Chuẩn Trong Robot Học | Đánh giá ngoài Task Success Rate, Dynamic Time Warping (DTW), Tích phân độ giật Jerk Metric | Căn chỉnh quỹ đạo DTW & Chỉ số Jerk | Python DTW Evaluator |
| | **Ch 14** | Kiến Trúc Triển Khai Thực Tế: HuggingFace LeRobot, ALOHA & ROS 2 | Vòng lặp điều khiển thời gian thực 50 Hz (20 ms), Chuẩn dữ liệu Zarr/Parquet, Cầu nối ROS 2 | Giám sát độ trễ 50 Hz thời gian thực | ROS 2 LeRobot Node |

---

## 🏛️ Chuẩn Thiết Kế 6 Tầng Tri Thức (6-Layer Architecture)

1. **Bảo toàn 100% mục lục:** Hệ thống phân cấp rõ ràng, bám sát các khái niệm khoa học chuẩn mực.
2. **Ý nghĩa thực tế ("Để làm gì?"):** Mỗi chương đều có khối giải thích trực giác sinh động giúp kỹ sư hiểu rõ lý do áp dụng.
3. **Bóc tách công thức toán không lỗi:** Tách rõ ý nghĩa từng biến số, sử dụng chuẩn MathJax 3 (`\lt`, `\gt`, không bao giờ gặp lỗi xử lý toán).
4. **Ví dụ tính số 4 bước:** Bố cục dạng lưới 4 cột song song hoặc thẻ thích ứng (`minmax(320px, 1fr)`).
5. **Mô phỏng Canvas 2D 60 FPS:** 14 mô phỏng tương tác động trực quan hóa cơ chế của từng thuật toán ngay trên trình duyệt (client-side only).
6. **Cầu nối kỹ thuật sản xuất:** Các đoạn mã chuẩn ROS 2 C++/Python, PyTorch và Hugging Face LeRobot sẵn sàng đưa vào vận hành.

---

## 💻 Trải Nghiệm Giao Diện 2 Cột Thích Ứng

- **Cột Trái (Sidebar Sticky Tag Bar - 320px):** Mục lục chi tiết của từng chương với bộ chỉ báo vị trí, cuộn mượt (Smooth Scroll) và đồng bộ trạng thái đọc.
- **Cột Phải (Main Content Container - Fit Web):** Chứa toàn bộ nội dung học thuật, công thức toán học, biểu đồ và mô phỏng tương tác.
- **Chế độ Sáng / Tối:** Chuyển đổi linh hoạt với nút gạt Theme Switcher, tự động lưu cấu hình người dùng vào `localStorage`.

---

## 🚀 Hướng Dẫn Khởi Chạy Cục Bộ (Local Preview)

Khởi chạy web server với Python tại thư mục gốc của dự án:
```bash
cd c:\Users\chucuong\OneDrive\Reading\imitation-learning-web
python -m http.server 8000
```
Mở trình duyệt truy cập: `http://localhost:8000`

---

## 🌐 Triển Khai Miễn Phí Lên GitHub Pages (`github.io`)

1. Khởi tạo kho mã nguồn Git và đẩy lên GitHub:
   ```bash
   git init
   git add .
   git commit -m "Deploy Imitation Learning Knowledge Portal SOTA"
   git branch -M main
   git remote add origin https://github.com/<your-username>/imitation-learning-web.git
   git push -u origin main
   ```
2. Trên giao diện GitHub repository: Vào **Settings** -> **Pages**.
3. Tại mục **Build and deployment** / **Source**: Chọn `Deploy from a branch`.
4. Branch: Chọn `main`, folder: `/ (root)`, nhấn **Save**.
5. Cổng thông tin sẽ trực tuyến tại: `https://<your-username>.github.io/imitation-learning-web/`
