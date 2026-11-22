# -*- coding: utf-8 -*-
"""
build_index.py
Tạo trang Portal Hub Dashboard hoàn chỉnh (index.html) cho Hệ Thống Động Lực Học & Modeling Robot
"""

import os

BASE_DIR = r"c:\Users\chucuong\OneDrive\Reading\robot-dynamics-modeling-web"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

chapters_meta = [
    {
        "ch": "01",
        "track_id": "track-1",
        "track_name": "TRACK 1: CƠ SỞ & ĐỘNG HỌC",
        "title": "Biểu Diễn Hệ Thống Hợp Nhất & State-Space",
        "desc": "Quy chuẩn hóa biến nỗ lực (Effort) & biến dòng (Flow), sơ đồ Bond Graph Paynter cơ - điện - thủy lực, không gian trạng thái phi tuyến, tuyến tính hóa Taylor và tính thụ động.",
        "tags": ["Effort & Flow", "Bond Graph", "State Space", "Linearization", "Passivity"],
        "sim": "⚡ Mô phỏng Ghép Nối Cơ - Điện",
        "worked": "Ví dụ số: Tuyến tính hóa"
    },
    {
        "ch": "02",
        "track_id": "track-1",
        "track_name": "TRACK 1: CƠ SỞ & ĐỘNG HỌC",
        "title": "Động Học Vật Rắn 3D & Biến Đổi Tọa Độ Robot",
        "desc": "Ma trận quay SO(3), các bộ góc Euler, hiện tượng khóa khớp Gimbal Lock, đại số Quaternions không kỳ dị, vận tốc góc S(ω), bảng DH và Jacobian hình học / giải tích.",
        "tags": ["SO(3)", "Gimbal Lock", "Quaternions", "Kinematic DEs", "Jacobians"],
        "sim": "⚡ Mô phỏng 3D Quaternions",
        "worked": "Ví dụ số: Euler sang Quaternion"
    },
    {
        "ch": "03",
        "track_id": "track-2",
        "track_name": "TRACK 2: CHẤP HÀNH & MA SÁT",
        "title": "Động Lực Học Động Cơ & Khớp Đàn Hồi",
        "desc": "Ghép nối điện - cơ động cơ DC & BLDC FOC, hộp số giảm tốc Harmonic Drive, định luật phản xạ quán tính 1/N², mô hình khớp đàn hồi Spong và bộ chấp hành áp điện.",
        "tags": ["DC / BLDC", "Harmonic Drive", "Inertia Reflected", "Spong Model", "Flexible Joint"],
        "sim": "⚡ Mô phỏng Khớp Đàn Hồi Spong",
        "worked": "Ví dụ số: Phản xạ quán tính"
    },
    {
        "ch": "04",
        "track_id": "track-2",
        "track_name": "TRACK 2: CHẤP HÀNH & MA SÁT",
        "title": "Ma Sát Động LuGre & Hệ Truyền Động Thủy Lực",
        "desc": "Hiện tượng ma sát tĩnh, hiệu ứng Stribeck dốc âm, mô hình vi gai tiếp xúc Dahl & LuGre, tính thụ động và động lực học xi-lanh/van servo thủy lực công suất lớn.",
        "tags": ["Stiction", "Stribeck", "LuGre Model", "Passivity", "Hydraulics"],
        "sim": "⚡ Mô phỏng Dính - Trượt Stick-Slip",
        "worked": "Ví dụ số: Dự báo ma sát LuGre"
    },
    {
        "ch": "05",
        "track_id": "track-3",
        "track_name": "TRACK 3: CƠ HỌC GIẢI TÍCH",
        "title": "Động Lực Học Newton-Euler & Thuật Toán RNEA O(n)",
        "desc": "Động lượng & mô-men động lượng 3D, tensor quán tính Steiner, phương trình Newton-Euler và thuật toán đệ quy RNEA O(n) hai bước tiến - lùi thời gian thực.",
        "tags": ["Newton-Euler", "Inertia Tensor", "RNEA O(n)", "Furuta Pendulum", "Inverse Dynamics"],
        "sim": "⚡ Mô phỏng Con lắc Furuta",
        "worked": "Ví dụ số: RNEA Forward Pass"
    },
    {
        "ch": "06",
        "track_id": "track-3",
        "track_name": "TRACK 3: CƠ HỌC GIẢI TÍCH",
        "title": "Cơ Học Lagrange & Động Lực Học Robot Cánh Tay",
        "desc": "Nguyên lý công ảo D'Alembert, phương trình Euler-Lagrange, ma trận quán tính đối xứng M(q), đẳng thức phản đối xứng vàng Ṁ - 2C = 0 và ma trận hồi quy Y(q,q̇,q̈)θ.",
        "tags": ["Euler-Lagrange", "Manipulator Equation", "Ṁ - 2C = 0", "Skew-Symmetry", "Regressor Y"],
        "sim": "⚡ Mô phỏng Robot 2R & Ṁ-2C=0",
        "worked": "Ví dụ số: Tính ma trận M & C"
    },
    {
        "ch": "07",
        "track_id": "track-3",
        "track_name": "TRACK 3: CƠ HỌC GIẢI TÍCH",
        "title": "Động Lực Học Hệ Ràng Buộc & Phương Pháp Kane",
        "desc": "Phân loại ràng buộc Holonomic vs Nonholonomic, nhân tử Lagrange, hệ phương trình LDAEs, phương pháp Kane lực quán tính suy rộng và robot di động bánh xe vi sai.",
        "tags": ["Nonholonomic", "Lagrange Multipliers", "LDAEs", "Kane's Method", "WMR Dynamics"],
        "sim": "⚡ Mô phỏng WMR Nonholonomic",
        "worked": "Ví dụ số: Khử nhân tử Lagrange"
    },
    {
        "ch": "08",
        "track_id": "track-3",
        "track_name": "TRACK 3: CƠ HỌC GIẢI TÍCH",
        "title": "Cơ Học Hamilton & Hệ Port-Hamiltonian Trong Robot",
        "desc": "Biến đổi Legendre, biến động lượng p, phương trình chính tắc Hamilton, cấu trúc Port-Hamiltonian PCHS luân chuyển năng lượng và điều khiển thụ động IDA-PBC.",
        "tags": ["Hamiltonian", "PCHS", "Energy Conservation", "IDA-PBC", "Telemanipulation"],
        "sim": "⚡ Mô phỏng Suy Giảm Năng Lượng PBC",
        "worked": "Ví dụ số: Thiết kế luật IDA-PBC"
    },
    {
        "ch": "09",
        "track_id": "track-4",
        "track_name": "TRACK 4: DAO ĐỘNG & DẦM MỀM",
        "title": "Dao Động Cơ Học, Dầm Đàn Hồi & Phân Tích FEM",
        "desc": "Phân tích Modal bài toán trị riêng, phương trình đạo hàm riêng PDE dầm mềm Euler-Bernoulli, phương pháp Galerkin hàm dạng và phần tử hữu hạn FEM cho cánh tay nhẹ.",
        "tags": ["Modal Analysis", "Euler-Bernoulli", "Galerkin Method", "FEM", "Flexible Manipulator"],
        "sim": "⚡ Mô phỏng 3 Mode Dao Động Dầm",
        "worked": "Ví dụ số: Tần số tự nhiên Galerkin"
    },
    {
        "ch": "10",
        "track_id": "track-5",
        "track_name": "TRACK 5: GIẢI TÍCH SỐ & MÔ PHỎNG",
        "title": "Thuật Toán Tích Phân Số ODEs Cho Động Lực Học",
        "desc": "Bài toán giá trị ban đầu IVP, các phương pháp Euler hiện/ẩn, Runge-Kutta bậc 4 RK4, bảng Butcher, RK45 thích nghi bước Dormand-Prince và miền ổn định tuyệt đối.",
        "tags": ["IVP", "Euler Methods", "Classical RK4", "Butcher Tableau", "RK45 Adaptive"],
        "sim": "⚡ Mô phỏng Euler vs Midpoint vs RK4",
        "worked": "Ví dụ số: Tích phân thủ công RK4"
    },
    {
        "ch": "11",
        "track_id": "track-5",
        "track_name": "TRACK 5: GIẢI TÍCH SỐ & MÔ PHỎNG",
        "title": "Hệ Cứng, Tích Phân Symplectic & Phương Pháp Đa Bước",
        "desc": "Bản chất hệ vi phân cứng Stiff trong va chạm cơ học, ổn định A-stability & L-stability, tích phân Symplectic Verlet bảo toàn năng lượng, đa bước Adams và BDF.",
        "tags": ["Stiff Systems", "A-Stability", "Symplectic Verlet", "Multistep Adams", "BDF Methods"],
        "sim": "⚡ Mô phỏng Symplectic Verlet vs RK4",
        "worked": "Ví dụ số: Thuật toán BDF-2"
    },
    {
        "ch": "12",
        "track_id": "track-5",
        "track_name": "TRACK 5: GIẢI TÍCH SỐ & MÔ PHỎNG",
        "title": "Giải Hệ Phương Trình DAEs & Động Lực Học Va Chạm",
        "desc": "Chỉ số vi phân Index-3, kỹ thuật ổn định hóa dập tắt sai số ràng buộc Baumgarte, điều kiện ban đầu tương thích, phân rã ma trận LU có chọn trục và tiếp xúc LCP.",
        "tags": ["DAE Index-3", "Baumgarte Stabilization", "LU Decomposition", "Pivoting", "LCP Contact"],
        "sim": "⚡ Mô phỏng Ổn Định Hóa Baumgarte",
        "worked": "Ví dụ số: Phân rã LU ma trận M"
    },
    {
        "ch": "13",
        "track_id": "track-6",
        "track_name": "TRACK 6: ỔN ĐỊNH & TRIỂN KHAI",
        "title": "Phân Tích Ổn Định Lyapunov & Điều Khiển Mô-Men Tính Toán",
        "desc": "Tính ổn định tiệm cận & ổn định mũ Lyapunov, nguyên lý bất biến LaSalle, bộ điều khiển PD có bù trọng lực và kỹ thuật điều khiển mô-men tính toán CTC tuyến tính hóa phản hồi.",
        "tags": ["Lyapunov Stability", "LaSalle Invariance", "PD + Gravity", "Computed Torque", "Inverse Dynamics"],
        "sim": "⚡ Mô phỏng Bám Quỹ Đạo CTC",
        "worked": "Ví dụ số: Thiết kế Kp, Kd cho CTC"
    },
    {
        "ch": "14",
        "track_id": "track-6",
        "track_name": "TRACK 6: ỔN ĐỊNH & TRIỂN KHAI",
        "title": "Kiến Trúc Thực Tế: URDF, Pinocchio, ros2_control & Gazebo",
        "desc": "Ánh xạ quán tính URDF, thư viện tính toán không gian Pinocchio AVX2, vòng lặp điều khiển thời gian thực 1000 Hz PREEMPT_RT, cầu nối mô phỏng Gazebo Sim và HIL.",
        "tags": ["URDF / XACRO", "Pinocchio C++", "ros2_control 1000Hz", "Gazebo Sim", "Real-Time Jitter"],
        "sim": "⚡ Giám Sát Jitter Vòng Lặp 1000Hz",
        "worked": "Ví dụ số: Ngân sách thời gian thực"
    }
]

# Build cards HTML
cards_html = ""
for item in chapters_meta:
    tags_html = "".join([f'<span class="card-tag">{t}</span>' for t in item["tags"]])
    cards_html += f"""
          <!-- Card Ch {item['ch']} -->
          <a href="chapters/ch{item['ch']}.html" class="matrix-card" data-track="{item['track_id']}">
            <div class="matrix-card-header">
              <span class="card-track-badge">{item['track_name']}</span>
              <span class="card-ch-num">CHƯƠNG {item['ch']}</span>
            </div>
            <h3 class="card-title">Chương {item['ch']}: {item['title']}</h3>
            <p class="card-desc">{item['desc']}</p>
            <div class="card-tags">
              {tags_html}
            </div>
            <div class="matrix-card-footer">
              <span class="card-feat-badge">{item['sim']}</span>
              <span class="card-cta">Khám phá chi tiết →</span>
            </div>
          </a>"""

index_html = f"""<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Động Lực Học & Modeling Robot - Portal Hub Khảo Sát & Trưng Cất Tri Thức</title>
  <meta name="description" content="Chương trình chưng cất tri thức chuẩn học thuật đa tầng: Khảo sát hệ thống 14 chương chuyên khảo Động Lực Học & Modeling Robot qua 6 Master Tracks.">
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
        <span class="logo-icon">🤖</span>
        <div class="brand-text">
          <span class="brand-title">Động Lực Học & Modeling Robot</span>
          <span class="brand-subtitle">EXPLORABLE KNOWLEDGE PLATFORM</span>
        </div>
      </div>
    </div>
    <div class="header-right">
      <div class="book-badge">
        <span class="badge-icon">📖</span> Tác giả: Brian Fabien, Olav Egeland, J. Tommy Gravdahl • Springer & Marine Cybernetics
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
          <div class="card-track-badge" style="margin-bottom: 0.5rem; display: inline-block;">LỘ TRÌNH TRI THỨC TOÀN DIỆN</div>
          <h2>TỔNG QUAN HỆ THỐNG ĐỘNG LỰC HỌC & MODELING ROBOT</h2>
          <p>Khảo sát hệ thống 14 chương chuyên sâu từ các tác phẩm kinh điển của Brian Fabien, Olav Egeland & Jan Tommy Gravdahl qua 6 Master Tracks từ cơ học giải tích, động học 3D, Newton-Euler RNEA, Euler-Lagrange đến giải tích số stiff/symplectic và triển khai ROS 2. Nhấp vào bất kỳ chương nào để truy cập nội dung diễn giải chi tiết, công thức toán và mô phỏng tương tác.</p>
          
          <div class="roadmap-stats">
            <span class="stat-badge"><span class="stat-num">14</span> Chương toàn diện</span>
            <span class="stat-badge"><span class="stat-num">6</span> Master Tracks</span>
            <span class="stat-badge"><span class="stat-num">14</span> Mô phỏng trực tiếp</span>
            <span class="stat-badge"><span class="stat-num">14</span> Sơ đồ Vector SVG</span>
            <span class="stat-badge"><span class="stat-num">14</span> Ví dụ tính số 4 bước</span>
            <span class="stat-badge"><span class="stat-num">100%</span> Client-Side GitHub Pages</span>
          </div>
        </div>

        <!-- Live Search & Filter Controls -->
        <div class="search-filter-wrapper">
          <div class="search-input-box">
            <span class="search-icon">🔍</span>
            <input type="text" id="matrix-search-input" placeholder="Tìm kiếm khái niệm, công thức hoặc chương (vd: RNEA, Lagrange, LuGre, Runge-Kutta, DAE, Lyapunov, Port-Hamiltonian, Pinocchio...)">
          </div>
          
          <div class="filter-pills">
            <button class="filter-pill active" data-filter="all">Tất cả (14 Chương)</button>
            <button class="filter-pill" data-filter="track-1">Track 1: Cơ Sở & Động Học (Ch. 1-2)</button>
            <button class="filter-pill" data-filter="track-2">Track 2: Chấp Hành & Ma Sát (Ch. 3-4)</button>
            <button class="filter-pill" data-filter="track-3">Track 3: Cơ Học Giải Tích (Ch. 5-8)</button>
            <button class="filter-pill" data-filter="track-4">Track 4: Dao Động & Dầm Mềm (Ch. 9)</button>
            <button class="filter-pill" data-filter="track-5">Track 5: Giải Tích Số & Mô Phỏng (Ch. 10-12)</button>
            <button class="filter-pill" data-filter="track-6">Track 6: Ổn Định & Triển Khai (Ch. 13-14)</button>
          </div>
        </div>

        <!-- Curriculum Matrix Grid Cards -->
        <div class="curriculum-matrix-grid" id="matrix-grid">
{cards_html}
        </div>
      </section>

      <footer class="site-footer">
        <p>Động Lực Học & Modeling Robot • Hệ Thống Chưng Cất Tri Thức Học Thuật</p>
        <p class="footer-meta">Biên soạn tự động theo chuẩn Deep Reading Distiller • Sẵn sàng chạy offline & GitHub Pages</p>
      </footer>
    </main>
  </div>

  <script src="assets/js/app.js"></script>
</body>
</html>"""

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(index_html)
print("Successfully generated Portal Hub index.html with all 14 cards and 6 tracks!")
