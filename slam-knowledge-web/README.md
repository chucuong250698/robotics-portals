# SLAM & Active Perception Trong Robot Học - Explorable Knowledge Portal

Cổng thông tin chưng cất tri thức chuẩn học thuật và kỹ thuật số đa tầng SOTA, được thiết kế theo tiêu chuẩn kỹ thuật **Deep Reading Distiller** từ các chuyên khảo và công trình nền tảng:
- **Mordechai Ben-Ari & Francesco Mondada** (*Springer*, 311 trang) - *Elements of Robotics*.
- **Thanh Nguyen Canh, Haolan Zhang, Xiem HoangVan, Nak Young Chong** (*IEEE Access / Sensors*, 2021, 41 trang) - *Semantic Visual Simultaneous Localization and Mapping: A Survey on State of the Art, Challenges, and Future Directions*.
- **Julio A. Placed, Jared Strader, Henry Carrillo, Nikolay Atanasov, Vadim Indelman, Luca Carlone, Jose A. Castellanos** (*IEEE Transactions on Robotics (T-RO)*, 2023, 20 trang) - *A Survey on Active Simultaneous Localization and Mapping: State of the Art and New Frontiers*.

---

## 🗺️ Ma Trận 14 Chương Qua 6 Master Tracks

| Track | Chương | Tiêu Đề Chương | Trọng Tâm Kiến Thức & Thuật Toán | Mô Phỏng Tương Tác Canvas 2D | Cầu Nối Thực Tế |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Track 1** | **Ch 01** | Động Học Robot Di Động & Tích Lũy Sai Số Đo Quãng Đường | Động học vi sai hai bánh, mô hình unicycle, tích phân Runge-Kutta, sai số hệ thống vs ngẫu nhiên, UMBmark | Trôi dạt sai số Dead Reckoning | ROS 2 Odom & TF2 |
| | **Ch 02** | Mô Hình Đo Cảm Biến Cự Ly & Bản Đồ Lưới Chiếm Chỗ | Cảm biến LiDAR/Sonar/IR, mô hình cảm biến nghịch đảo xác suất, tỷ số Log-Odds, vẽ tia Bresenham | Lập bản đồ Occupancy Grid Log-odds | ROS 2 Map Publisher |
| **Track 2** | **Ch 03** | Bộ Lọc Bayes, Extended Kalman Filter (EKF) & Phân Tích Hiệp Phương Sai | Lọc Bayes đệ quy, tuyến tính hóa Taylor, ma trận Jacobian $\mathbf{F}, \mathbf{H}$, Kalman Gain $\mathbf{K}$, Elip tin cậy | Elip tin cậy EKF co giãn khi đo mốc | ROS 2 EKF YAML |
| | **Ch 04** | Bộ Lọc Hạt (Particle Filter), MCL & Khung FastSLAM | Phân phối đa mốt, giải quyết bắt cóc robot (Kidnapped Robot), tái lấy mẫu Low-Variance, FastSLAM 1.0/2.0 | Đám hạt MCL tự hội tụ & Bắt cóc robot | Python Resampler |
| **Track 3** | **Ch 05** | Đồ Thị Tư Thế (Pose Graph Optimization) & Factor Graphs (GTSAM) | Chuyển dịch từ lọc sang đồ thị thưa, nhóm Lie $\mathrm{SE}(2)$, Gauss-Newton, Levenberg-Marquardt, Loop Closure | Nắn thẳng đồ thị khi đóng vòng lặp | GTSAM Python Solver |
| | **Ch 06** | Visual Odometry Hình Học: Trích Xuất Đặc Trưng & Hình Học Epipolar | Feature-based (ORB-SLAM) vs Direct (DSO), ma trận Essential $\mathbf{E} = [\mathbf{t}]_\times \mathbf{R}$, PnP, Triangulation 3D | Tia chiếu Epipolar & Tam giác hóa 3D | OpenCV VO C++ |
| **Track 4** | **Ch 07** | Trích Xuất Ngữ Nghĩa & Lọc Môi Trường Động (Dynamic Masking) | Vượt qua giả định thế giới tĩnh, YOLOv8/SAM phân vùng vật thể, kiểm định Chi-Square lọc outliers động | Mặt nạ động triệt tiêu điểm ảnh chuyển động | YOLOv8 ROS 2 Node |
| | **Ch 08** | Bản Đồ Ngữ Nghĩa: Điểm, Mặt Phẳng, Dual Quadrics & NeRF/3DGS | Biểu diễn vật thể dạng elip 3D Dual Quadrics $\mathbf{Q}^*$, phép chiếu đối ngẫu Conic 2D $\mathbf{C}^*$, NeRF / 3D Gaussian Splatting | Chiếu khối elipsoid 3D thành Conic 2D | GTSAM Quadric Factor |
| | **Ch 09** | Liên Kết Dữ Liệu Ngữ Nghĩa & Tối Ưu Vòng Lặp Ngữ Nghĩa | Giải quyết nhập nhằng gán cặp, Hungarian bipartite matching, khoảng cách Mahalanobis + nhãn, Semantic Loop Closing | Ghép cặp đồ thị ngữ nghĩa Hungarian | SciPy Associator |
| **Track 5** | **Ch 10** | Khung Toán Học Active SLAM & Không Gian Hành Động Ứng Viên | Tự chủ ra quyết định điều hướng (IEEE T-RO 2023), khung 3 giai đoạn, nhận diện biên giới Frontier WFD & RRT | Nhận diện Frontier & Mở rộng cây RRT | Nav2 Frontier C++ |
| | **Ch 11** | Đo Lường Thông Tin Toán Học: Entropy, Mutual Info & Tiêu Chuẩn TOED | Shannon Differential Entropy, Mutual Information, Tiêu chuẩn TOED: A-opt, D-opt, E-opt của FIM | So sánh hình học elip TOED | Python TOED Evaluator |
| | **Ch 12** | Song Đề Khám Phá vs Khai Thác & Lập Kế Hoạch Không Gian Niềm Tin (BSP) | Song đề Exploration vs Exploitation, Belief-Space Planning (POMDPs), hàm thỏa dụng Pareto, Active Loop Closing | Chuyển trạng thái Explore vs Loop Close | Nav2 BehaviorTree |
| **Track 6** | **Ch 13** | Đa Robot SLAM: Phân Tán, Hợp Nhất Bản Đồ & Active Exploration | Kiến trúc P2P phân tán, hợp nhất bản đồ (Map Merging) khi chưa biết tư thế ban đầu, SVD/Horn, đấu giá thị trường | Khâu vá bản đồ đa robot (Map Stitching) | ROS 2 Map Stitcher |
| | **Ch 14** | Kiến Trúc Triển Khai Thực Tế: ROS 2 Humble, Nav2, SLAM Toolbox & Benchmarks | Ngăn xếp công nghiệp: SLAM Toolbox vs Cartographer vs RTAB-Map, Lifelong mapping, thước đo ATE RMSE / RPE | Đánh giá ATE RMSE so với Ground Truth | slam_toolbox.yaml |

---

## 🏛️ Chuẩn Thiết Kế 6 Tầng Tri Thức (6-Layer Architecture)

1. **Bảo toàn 100% mục lục:** Hệ thống phân cấp rõ ràng, bám sát các khái niệm khoa học chuẩn mực.
2. **Ý nghĩa thực tế ("Để làm gì?"):** Mỗi chương đều có khối giải thích trực giác sinh động giúp kỹ sư hiểu rõ lý do áp dụng.
3. **Bóc tách công thức toán không lỗi:** Tách rõ ý nghĩa từng biến số, sử dụng chuẩn MathJax 3 (`\lt`, `\gt`, không bao giờ gặp lỗi xử lý toán).
4. **Ví dụ tính số 4 bước:** Bố cục dạng lưới 4 cột song song hoặc thẻ thích ứng (`minmax(320px, 1fr)`).
5. **Mô phỏng Canvas 2D 60 FPS:** 14 mô phỏng tương tác động trực quan hóa cơ chế của từng thuật toán ngay trên trình duyệt (client-side only).
6. **Cầu nối kỹ thuật sản xuất:** Các đoạn mã chuẩn ROS 2 C++/Python, GTSAM và PyTorch sẵn sàng đưa vào vận hành.

---

## 💻 Trải Nghiệm Giao Diện 2 Cột Thích Ứng

- **Cột Trái (Sidebar Sticky Tag Bar - 320px):** Mục lục chi tiết của từng chương với bộ chỉ báo vị trí, cuộn mượt (Smooth Scroll) và đồng bộ trạng thái đọc.
- **Cột Phải (Main Content Container - Fit Web):** Chứa toàn bộ nội dung học thuật, công thức toán học, biểu đồ và mô phỏng tương tác.
- **Chế độ Sáng / Tối:** Chuyển đổi linh hoạt với nút gạt Theme Switcher, tự động lưu cấu hình người dùng vào `localStorage`.

---

## 🚀 Hướng Dẫn Khởi Chạy Cục Bộ (Local Preview)

Khởi chạy web server với Python tại thư mục gốc của dự án:
```bash
cd c:\Users\chucuong\OneDrive\Reading\slam-knowledge-web
python -m http.server 8000
```
Mở trình duyệt truy cập: `http://localhost:8000`

---

## 🌐 Triển Khai Miễn Phí Lên GitHub Pages (`github.io`)

1. Khởi tạo kho mã nguồn Git và đẩy lên GitHub:
   ```bash
   git init
   git add .
   git commit -m "Deploy SLAM & Active Perception Knowledge Portal SOTA"
   git branch -M main
   git remote add origin https://github.com/<your-username>/slam-knowledge-web.git
   git push -u origin main
   ```
2. Trên giao diện GitHub repository: Vào **Settings** -> **Pages**.
3. Tại mục **Build and deployment** / **Source**: Chọn `Deploy from a branch`.
4. Branch: Chọn `main`, folder: `/ (root)`, nhấn **Save**.
5. Cổng thông tin sẽ trực tuyến tại: `https://<your-username>.github.io/slam-knowledge-web/`
