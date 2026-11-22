# -*- coding: utf-8 -*-
"""
build_index.py
Tạo trang Portal Hub index.html cho SLAM & Active Perception Knowledge Portal:
- 14 Chương Toàn Diện qua 6 Master Tracks
- Live Search & Filter Pills
- Thống kê tiến trình học thuật
"""

import os

BASE_DIR = r"c:\Users\chucuong\OneDrive\Reading\slam-knowledge-web"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

chapters_data = [
    {
        "num": "01",
        "title": "Chương 01: Động Học Robot Di Động & Tích Lũy Sai Số Đo Quãng Đường",
        "subtitle": "Động học vi sai hai bánh, mô hình unicycle, tích phân Runge-Kutta, phân tích sai số hệ thống vs ngẫu nhiên và thử nghiệm UMBmark.",
        "track_slug": "track-1",
        "track_badge": "TRACK 1: NỀN TẢNG ĐỘNG HỌC",
        "tags": ["Kinematics", "Dead Reckoning", "Unicycle", "Odometry Drift", "UMBmark", "Canvas 2D", "ROS 2 Odom"]
    },
    {
        "num": "02",
        "title": "Chương 02: Mô Hình Đo Cảm Biến Cự Ly & Bản Đồ Lưới Chiếm Chỗ",
        "subtitle": "Đặc tính cảm biến LiDAR/Sonar/IR, mô hình cảm biến nghịch đảo xác suất, biểu diễn tỷ số Log-Odds và thuật toán vẽ tia Bresenham.",
        "track_slug": "track-1",
        "track_badge": "TRACK 1: NỀN TẢNG ĐỘNG HỌC",
        "tags": ["LiDAR", "Inverse Sensor Model", "Occupancy Grid", "Log-Odds", "Bresenham", "Canvas 2D", "ROS 2 Map"]
    },
    {
        "num": "03",
        "title": "Chương 03: Bộ Lọc Bayes, Extended Kalman Filter (EKF) & Phân Tích Hiệp Phương Sai",
        "subtitle": "Tuyến tính hóa Taylor chuỗi phi tuyến, hai pha Dự báo - Hiệu chỉnh, ma trận hiệp phương sai P_t, Kalman Gain K và elip tin cậy.",
        "track_slug": "track-2",
        "track_badge": "TRACK 2: ƯỚC LƯỢNG & ĐỊNH VỊ",
        "tags": ["Bayes Filter", "EKF", "Kalman Gain", "Covariance Ellipse", "Taylor Linearization", "Canvas 2D", "ROS 2 EKF"]
    },
    {
        "num": "04",
        "title": "Chương 04: Bộ Lọc Hạt (Particle Filter), MCL & Khung FastSLAM",
        "subtitle": "Giải quyết bài toán phân phối đa mốt & bắt cóc robot (Kidnapped Robot), tái lấy mẫu Low-Variance và phân rã Rao-Blackwellized FastSLAM.",
        "track_slug": "track-2",
        "track_badge": "TRACK 2: ƯỚC LƯỢNG & ĐỊNH VỊ",
        "tags": ["Particle Filter", "MCL", "Kidnapped Robot", "Importance Sampling", "FastSLAM", "Canvas 2D", "Python Resampler"]
    },
    {
        "num": "05",
        "title": "Chương 05: Đồ Thị Tư Thế (Pose Graph Optimization) & Factor Graphs (GTSAM)",
        "subtitle": "Bước chuyển từ lọc sang tối ưu hóa đồ thị thưa, nhóm Lie SE(2)/SE(3), Levenberg-Marquardt trên đa tạp và nắn thẳng Loop Closure.",
        "track_slug": "track-3",
        "track_badge": "TRACK 3: SLAM HÌNH HỌC & ĐỒ THỊ",
        "tags": ["Pose Graph", "Factor Graph", "Lie Group SE(2)", "Loop Closure", "GTSAM", "Levenberg-Marquardt", "Canvas 2D"]
    },
    {
        "num": "06",
        "title": "Chương 06: Visual Odometry Hình Học: Trích Xuất Đặc Trưng & Hình Học Epipolar",
        "subtitle": "Feature-based (ORB-SLAM) vs Direct (DSO), ma trận thiết yếu E = [t]x R, giải tư thế PnP, tam giác hóa 3D và Bundle Adjustment.",
        "track_slug": "track-3",
        "track_badge": "TRACK 3: SLAM HÌNH HỌC & ĐỒ THỊ",
        "tags": ["Visual Odometry", "ORB-SLAM", "Epipolar Geometry", "Essential Matrix", "Triangulation", "Canvas 2D", "OpenCV VO"]
    },
    {
        "num": "07",
        "title": "Chương 07: Trích Xuất Ngữ Nghĩa & Lọc Môi Trường Động (Dynamic Masking)",
        "subtitle": "Vượt qua giả định thế giới tĩnh, thị giác học sâu YOLOv8/SAM phân vùng vật thể, kết hợp kiểm định Chi-Square lọc sạch outliers động.",
        "track_slug": "track-4",
        "track_badge": "TRACK 4: SLAM NGỮ NGHĨA SOTA",
        "tags": ["Semantic SLAM", "Dynamic Masking", "YOLOv8", "SAM", "Chi-Square Test", "Epipolar Constraint", "Canvas 2D"]
    },
    {
        "num": "08",
        "title": "Chương 08: Bản Đồ Ngữ Nghĩa: Điểm, Mặt Phẳng, Dual Quadrics & NeRF/3DGS",
        "subtitle": "Tiến trình biểu diễn bản đồ cấp độ vật thể Dual Quadrics Q* (Ellipsoids), phép chiếu đối ngẫu Conic C* và NeRF / 3D Gaussian Splatting.",
        "track_slug": "track-4",
        "track_badge": "TRACK 4: SLAM NGỮ NGHĨA SOTA",
        "tags": ["Dual Quadrics", "Object-Level SLAM", "Conic Projection", "NeRF-SLAM", "3D Gaussian Splatting", "Canvas 2D", "GTSAM"]
    },
    {
        "num": "09",
        "title": "Chương 09: Liên Kết Dữ Liệu Ngữ Nghĩa & Tối Ưu Vòng Lặp Ngữ Nghĩa",
        "subtitle": "Giải quyết nhập nhằng liên kết dữ liệu, thuật toán Hungarian Bipartite Matching kết hợp khoảng cách Mahalanobis và nhãn ngữ nghĩa.",
        "track_slug": "track-4",
        "track_badge": "TRACK 4: SLAM NGỮ NGHĨA SOTA",
        "tags": ["Data Association", "Hungarian Algorithm", "Mahalanobis", "Semantic Loop Closing", "Perceptual Aliasing", "Canvas 2D"]
    },
    {
        "num": "10",
        "title": "Chương 10: Khung Toán Học Active SLAM & Không Gian Hành Động Ứng Viên",
        "subtitle": "Tự chủ ra quyết định điều hướng tối thiểu hóa độ bất định (IEEE T-RO 2023), khung 3 giai đoạn, nhận diện biên giới Frontier và RRT.",
        "track_slug": "track-5",
        "track_badge": "TRACK 5: ACTIVE SLAM & RA QUYẾT ĐỊNH",
        "tags": ["Active SLAM", "Autonomous Exploration", "Frontier Detection", "RRT", "Candidate Generation", "Canvas 2D", "Nav2 C++"]
    },
    {
        "num": "11",
        "title": "Chương 11: Đo Lường Thông Tin Toán Học: Entropy, Mutual Info & Tiêu Chuẩn TOED",
        "subtitle": "Shannon Differential Entropy, Mutual Information, và Lý thuyết thiết kế thực nghiệm tối ưu TOED: A-optimality, D-optimality, E-optimality.",
        "track_slug": "track-5",
        "track_badge": "TRACK 5: ACTIVE SLAM & RA QUYẾT ĐỊNH",
        "tags": ["Information Theory", "Shannon Entropy", "Mutual Information", "TOED", "A-opt", "D-opt", "E-opt", "Canvas 2D"]
    },
    {
        "num": "12",
        "title": "Chương 12: Song Đề Khám Phá vs Khai Thác & Lập Kế Hoạch Không Gian Niềm Tin (BSP)",
        "subtitle": "Song đề Exploration vs Exploitation, Belief-Space Planning (POMDPs), hàm thỏa dụng Pareto đa mục tiêu và kích hoạt Active Loop Closing.",
        "track_slug": "track-5",
        "track_badge": "TRACK 5: ACTIVE SLAM & RA QUYẾT ĐỊNH",
        "tags": ["Belief-Space Planning", "POMDP", "Exploration vs Exploitation", "Active Loop Closure", "Pareto Utility", "Canvas 2D"]
    },
    {
        "num": "13",
        "title": "Chương 13: Đa Robot SLAM: Phân Tán, Hợp Nhất Bản Đồ & Active Exploration",
        "subtitle": "Kiến trúc P2P phân tán, hợp nhất bản đồ (Map Merging) khi chưa biết tư thế tương đối ban đầu, thuật toán Horn SVD và đấu giá thị trường.",
        "track_slug": "track-6",
        "track_badge": "TRACK 6: ĐA ROBOT & THỰC TẾ",
        "tags": ["Multi-Robot SLAM", "Map Stitching", "Decentralized", "Inter-Robot Loop Closure", "Rigid Transform SVD", "Canvas 2D"]
    },
    {
        "num": "14",
        "title": "Chương 14: Kiến Trúc Triển Khai Thực Tế: ROS 2 Humble, Nav2, SLAM Toolbox & Benchmarks",
        "subtitle": "So sánh ngăn xếp SLAM Toolbox vs Cartographer vs RTAB-Map, Lifelong mapping, chỉ số ATE RMSE / RPE và tệp cấu hình YAML nhà xưởng.",
        "track_slug": "track-6",
        "track_badge": "TRACK 6: ĐA ROBOT & THỰC TẾ",
        "tags": ["SLAM Toolbox", "Nav2 Humble", "Lifelong Mapping", "ATE RMSE", "RPE", "Tuning Guide", "YAML Params", "Canvas 2D"]
    }
]

cards_html = ""
for ch in chapters_data:
    tags_html = "".join([f'<span class="card-tag">{t}</span>' for t in ch["tags"]])
    cards_html += f"""
          <!-- Card Ch {ch['num']} -->
          <a href="chapters/ch{ch['num']}.html" class="matrix-card" data-track="{ch['track_slug']}">
            <div class="matrix-card-header">
              <span class="card-track-badge">{ch['track_badge']}</span>
              <span class="card-ch-num">CHƯƠNG {ch['num']}</span>
            </div>
            <h3 class="card-title">{ch['title']}</h3>
            <p class="card-desc">{ch['subtitle']}</p>
            <div class="card-tags">
              {tags_html}
            </div>
          </a>"""

index_content = f"""<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SLAM & Active Perception Trong Robot Học - Explorable Knowledge Portal</title>
  <meta name="description" content="Chương trình chưng cất tri thức chuẩn học thuật đa tầng: Khảo sát hệ thống 14 chương chuyên khảo SLAM, Semantic SLAM & Active SLAM qua 6 Master Tracks.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }}
    }};
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
  <div id="reading-progress"></div>
  
  <!-- Global Header -->
  <header class="site-header">
    <div class="header-left">
      <div class="brand-logo">
        <span class="logo-icon">🗺️</span>
        <div class="brand-text">
          <span class="brand-title">SLAM & Active Perception Trong Robot Học</span>
          <span class="brand-subtitle">EXPLORABLE KNOWLEDGE PLATFORM • SOTA PEDAGOGICAL PORTAL</span>
        </div>
      </div>
    </div>
    <div class="header-right">
      <div class="book-badge">
        <span class="badge-icon">📖</span> Nguồn: Elements of Robotics (Springer), Semantic Visual SLAM (IEEE 2021) & Active SLAM (IEEE T-RO 2023)
      </div>
      <button id="theme-btn" class="theme-toggle-btn" aria-label="Toggle Theme">
        <span id="theme-icon">☀️</span>
        <span id="theme-text">Chế độ sáng</span>
      </button>
    </div>
  </header>

  <!-- Portal Hub Matrix Roadmap -->
  <div class="app-layout single-col">
    <main class="main-content" style="max-width: 1240px; margin: 0 auto; width: 100%; padding: 1.5rem 1rem 4rem;">
      <section class="curriculum-roadmap" id="curriculum-roadmap">
        <div class="roadmap-header">
          <div class="card-track-badge" style="margin-bottom: 0.5rem; display: inline-block;">LỘ TRÌNH TRI THỨC TOÀN DIỆN CHUẨN 6 TẦNG</div>
          <h2>MA TRẬN CHƯƠNG TRÌNH KHẢO SÁT SLAM & ACTIVE PERCEPTION</h2>
          <p>Hệ thống tri thức chuyên sâu 14 chương từ nền tảng động học Dead Reckoning, Lập bản đồ Occupancy Grid, Lọc Bayes EKF/Particle Filter, Đồ thị Pose Graph/GTSAM, SLAM Ngữ nghĩa YOLO/SAM/Dual Quadrics/NeRF, đến Active SLAM thông tin TOED và Triển khai thực tế ROS 2 Humble/Nav2.</p>
          
          <div class="roadmap-stats">
            <span class="stat-badge"><span class="stat-num">14</span> Chương Toàn Diện</span>
            <span class="stat-badge"><span class="stat-num">6</span> Master Tracks</span>
            <span class="stat-badge"><span class="stat-num">14</span> Mô Phỏng Canvas 2D 60 FPS</span>
            <span class="stat-badge"><span class="stat-num">14</span> Ví Dụ Tính Số 4 Bước</span>
            <span class="stat-badge"><span class="stat-num">100%</span> Zero-Error MathJax & ROS 2 Bridge</span>
          </div>
        </div>

        <!-- Live Search & Filter Controls -->
        <div class="search-filter-wrapper">
          <div class="search-input-box">
            <span class="search-icon">🔍</span>
            <input type="text" id="matrix-search-input" placeholder="Tìm kiếm khái niệm, thuật toán, công thức (EKF, FastSLAM, GTSAM, ORB-SLAM, YOLO, Quadrics, Active SLAM, TOED, Nav2)...">
          </div>
          
          <div class="filter-pills">
            <button class="filter-pill active" data-filter="all">Tất cả (14 Chương)</button>
            <button class="filter-pill" data-filter="track-1">Track 1: Nền Tảng Động Học & Cảm Biến (Ch 1-2)</button>
            <button class="filter-pill" data-filter="track-2">Track 2: Ước Lượng Trạng Thái & Định Vị (Ch 3-4)</button>
            <button class="filter-pill" data-filter="track-3">Track 3: SLAM Hình Học Cổ Điển & Đồ Thị (Ch 5-6)</button>
            <button class="filter-pill" data-filter="track-4">Track 4: SLAM Ngữ Nghĩa & Biểu Diễn Hiện Đại (Ch 7-9)</button>
            <button class="filter-pill" data-filter="track-5">Track 5: Active SLAM & Ra Quyết Định (Ch 10-12)</button>
            <button class="filter-pill" data-filter="track-6">Track 6: Đa Robot & Triển Khai Sản Xuất (Ch 13-14)</button>
          </div>
        </div>

        <!-- Curriculum Matrix Grid Cards -->
        <div class="curriculum-matrix-grid" id="matrix-grid">
{cards_html}
        </div>
      </section>

      <footer class="site-footer" style="margin-top: 3rem; text-align: center; border-top: 1px solid var(--border-color); padding-top: 2rem;">
        <p>Hệ Thống Tri Thức SLAM & Active Perception • SOTA Pedagogical Portal</p>
        <p class="footer-meta">Biên dịch & Chưng cất theo chuẩn Deep Reading Distiller • Sẵn sàng chạy offline 100% & Xuất bản GitHub Pages</p>
      </footer>
    </main>
  </div>

  <script src="assets/js/app.js"></script>
</body>
</html>"""

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Successfully generated Portal Hub index.html with all 14 chapters across 6 Master Tracks for SLAM Portal!")
