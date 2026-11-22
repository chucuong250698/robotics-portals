# -*- coding: utf-8 -*-
"""
build_index.py
Tạo trang Portal Hub index.html đồng bộ đầy đủ 14 chương theo 6 Master Tracks:
- Track 1: Nền Tảng & Lệch Phân Phối (Ch 01 - 02)
- Track 2: Học Tương Tác Có Con Người Tham Gia (IIL) (Ch 03 - 04)
- Track 3: Biểu Diễn Động Tác & Deep IL SOTA (Ch 05 - 06)
- Track 4: Học Tăng Cường Nghịch Đảo & Đối Nghịch (Ch 07 - 08)
- Track 5: Quan Sát, Dữ Liệu Lỗi & Chênh Lệch Miền (Ch 09 - 11)
- Track 6: Giao Diện HRI, Benchmarks & Triển Khai Thực Tế (Ch 12 - 14)
"""

import os

BASE_DIR = r"c:\Users\chucuong\OneDrive\Reading\imitation-learning-web"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

chapters_data = [
    {
        "num": "01",
        "title": "Chương 01: Giới Thiệu Học Bắt Chước & Khung Quyết Định Toán Học",
        "subtitle": "Bản chất toán học MDPs, so sánh hiệu quả mẫu IL vs RL, tập dữ liệu chuyên gia D_E và phân loại 3 trường phái BC, IRL, IIL.",
        "track_slug": "track-1",
        "track_badge": "TRACK 1: NỀN TẢNG",
        "tags": ["MDP", "D_E", "BC vs IRL vs IIL", "Hiệu quả mẫu", "Canvas 2D", "Ví dụ số 4 bước", "HDF5"]
    },
    {
        "num": "02",
        "title": "Chương 02: Nhân Bản Hành Vi (BC) & Tích Lũy Sai Số Covariate Shift",
        "subtitle": "Behavioral Cloning dưới góc nhìn Supervised Learning, chứng minh cận sai số bậc hai O(T^2 epsilon) và hiện tượng Causal Confusion.",
        "track_slug": "track-1",
        "track_badge": "TRACK 1: NỀN TẢNG",
        "tags": ["Supervised Learning", "Covariate Shift", "O(T^2)", "Causal Confusion", "Canvas 2D", "PyTorch BC"]
    },
    {
        "num": "03",
        "title": "Chương 03: Phản Hồi Đánh Giá (Evaluative) & RLHF Trong Robot",
        "subtitle": "Khung phản hồi nhị phân khen/chê TAMER, phân phối Dirichlet của COACH và tối ưu hóa phản hồi con người trong vòng lặp thời gian thực.",
        "track_slug": "track-2",
        "track_badge": "TRACK 2: HỌC TƯƠNG TÁC IIL",
        "tags": ["Evaluative Feedback", "TAMER", "COACH", "RLHF", "Human Credit", "Canvas 2D", "HRI"]
    },
    {
        "num": "04",
        "title": "Chương 04: Phản Hồi Hiệu Chỉnh & Họ Thuật Toán DAgger / SafeDAgger",
        "subtitle": "Tập hợp dữ liệu gộp DAgger chặn sai số O(T epsilon), cơ chế can thiệp an toàn SafeDAgger và giảm tải cho người làm mẫu.",
        "track_slug": "track-2",
        "track_badge": "TRACK 2: HỌC TƯƠNG TÁC IIL",
        "tags": ["Corrective Feedback", "DAgger", "SafeDAgger", "Cận O(T)", "No-regret", "Canvas 2D", "ROS 2"]
    },
    {
        "num": "05",
        "title": "Chương 05: Động Tác Nguyên Mẫu Động Lực Học (DMPs) & ProMPs",
        "subtitle": "Hệ chính tắc pha Canonical System, hệ biến đổi bậc 2 ổn định Lyapunov, hàm lực phi tuyến RBF và xác suất vận động ProMPs.",
        "track_slug": "track-3",
        "track_badge": "TRACK 3: ĐỘNG TÁC & DEEP IL",
        "tags": ["DMP", "Canonical System", "Lyapunov", "RBF", "ProMP", "Canvas 2D", "ROS 2 C++"]
    },
    {
        "num": "06",
        "title": "Chương 06: Diffusion Policy & Action Chunking Transformers (ACT)",
        "subtitle": "Phá vỡ giới hạn phân phối đa mốt bằng DDPM, kiến trúc Action Chunking Transformers (ACT) và ghép khối Temporal Ensembling.",
        "track_slug": "track-3",
        "track_badge": "TRACK 3: ĐỘNG TÁC & DEEP IL",
        "tags": ["Diffusion Policy", "DDPM", "ACT", "Temporal Ensembling", "U-Net 1D", "Canvas 2D", "PyTorch"]
    },
    {
        "num": "07",
        "title": "Chương 07: Học Tăng Cường Nghịch Đảo (Inverse RL) & Maximum Entropy",
        "subtitle": "Khôi phục hàm phần thưởng ẩn bất biến R*(s,a), thuật toán Maximum Margin, nguyên lý Maximum Entropy và Feature Matching.",
        "track_slug": "track-4",
        "track_badge": "TRACK 4: INVERSE RL & GAIL",
        "tags": ["Inverse RL", "Max-Margin", "MaxEnt IRL", "Feature Matching", "Boltzmann", "Canvas 2D", "SVF Solver"]
    },
    {
        "num": "08",
        "title": "Chương 08: Học Bắt Chước Đối Nghịch GAIL & Khớp Phân Phối Chiếm Dụng",
        "subtitle": "Đồng nhất hóa IRL với GAN, khớp phân phối chiếm dụng d_pi = d_E, bộ sinh Discriminator và mở rộng sang AIRL.",
        "track_slug": "track-4",
        "track_badge": "TRACK 4: INVERSE RL & GAIL",
        "tags": ["GAIL", "Occupancy Measure", "GAN", "Jensen-Shannon", "PPO", "AIRL", "Canvas 2D"]
    },
    {
        "num": "09",
        "title": "Chương 09: Học Bắt Chước Chỉ Từ Quan Sát (Imitation from Observation - IfO)",
        "subtitle": "Khai thác dữ liệu video không có nhãn hành động qua BCO (Behavioral Cloning from Observation) và mô hình động lực học nghịch.",
        "track_slug": "track-5",
        "track_badge": "TRACK 5: QUAN SÁT & MIỀN DỮ LIỆU",
        "tags": ["IfO", "BCO", "Inverse Dynamics", "Video Learning", "GAIfO", "Canvas 2D", "PyTorch"]
    },
    {
        "num": "10",
        "title": "Chương 10: Học Từ Chuyên Gia Lỗi & Ngoại Suy Phần Thưởng (T-REX & D-REX)",
        "subtitle": "Vượt qua trần con người bằng Trajectory Ranking, mô hình lựa chọn Bradley-Terry, và ngoại suy siêu phàm Super-Human.",
        "track_slug": "track-5",
        "track_badge": "TRACK 5: QUAN SÁT & MIỀN DỮ LIỆU",
        "tags": ["T-REX", "D-REX", "Suboptimal Demos", "Bradley-Terry", "Super-Human", "Canvas 2D", "Ranking Loss"]
    },
    {
        "num": "11",
        "title": "Chương 11: Bất Đồng Hình Thái & Chuyển Đổi Sim-to-Real",
        "subtitle": "Giải quyết Correspondence Problem giữa người và robot, Domain Randomization vượt qua Reality Gap và Open X-Embodiment.",
        "track_slug": "track-5",
        "track_badge": "TRACK 5: QUAN SÁT & MIỀN DỮ LIỆU",
        "tags": ["Correspondence Problem", "Sim-to-Real", "Domain Randomization", "Jacobian IK", "Cross-Embodiment", "Canvas 2D", "ROS 2"]
    },
    {
        "num": "12",
        "title": "Chương 12: Giao Diện HRI, Dạy Học Động Học & Tự Chủ Chia Sẻ (Shared Autonomy)",
        "subtitle": "Kinesthetic Teaching, Leader-Follower teleoperation và bộ điều khiển hòa trộn tín hiệu alpha-blending kèm Barrier Functions.",
        "track_slug": "track-6",
        "track_badge": "TRACK 6: HRI & BENCHMARK THỰC TẾ",
        "tags": ["Kinesthetic", "Leader-Follower", "Shared Autonomy", "Alpha-Blending", "CBF", "Canvas 2D", "ROS 2 C++"]
    },
    {
        "num": "13",
        "title": "Chương 13: Thước Đo Đánh Giá & Các Bộ Benchmark Tiêu Chuẩn Trong Robot Học",
        "subtitle": "Đánh giá quỹ đạo bằng Dynamic Time Warping (DTW), chỉ số an toàn cơ học tích phân độ giật Jerk Metric và bộ dữ liệu RoboMimic.",
        "track_slug": "track-6",
        "track_badge": "TRACK 6: HRI & BENCHMARK THỰC TẾ",
        "tags": ["Task Success", "DTW", "Jerk Metric", "RoboMimic", "RLBench", "Mechanical Safety", "Canvas 2D"]
    },
    {
        "num": "14",
        "title": "Chương 14: Kiến Trúc Triển Khai Thực Tế: HuggingFace LeRobot, ALOHA & ROS 2",
        "subtitle": "Vòng lặp thực thi thời gian thực 50 Hz, chuẩn dữ liệu Zarr/Parquet, nén video AV1 và kiến trúc Node ROS 2 kết nối GPU suy luận.",
        "track_slug": "track-6",
        "track_badge": "TRACK 6: HRI & BENCHMARK THỰC TẾ",
        "tags": ["LeRobot", "ALOHA", "50 Hz Loop", "Zarr", "ROS 2 Humble", "Real-Time", "Canvas 2D"]
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
  <title>Học Bắt Chước Trong Robot Học (Imitation Learning & Interactive IL) - Portal Hub Khảo Sát & Trưng Cất Tri Thức</title>
  <meta name="description" content="Chương trình chưng cất tri thức chuẩn học thuật đa tầng: Khảo sát hệ thống 14 chương chuyên khảo Học Bắt Chước Trong Robot Học (Imitation Learning & Interactive IL) qua 6 Master Tracks.">
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
          <span class="brand-title">Học Bắt Chước Trong Robot Học (Imitation Learning & Interactive IL)</span>
          <span class="brand-subtitle">EXPLORABLE KNOWLEDGE PLATFORM • SOTA PEDAGOGICAL PORTAL</span>
        </div>
      </div>
    </div>
    <div class="header-right">
      <div class="book-badge">
        <span class="badge-icon">📖</span> Nguồn: Carlos Celemin et al. (FnT Robotics 2022), Boyuan Zheng (2021) & Maryam Zare (IEEE 2023)
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
          <h2>MA TRẬN CHƯƠNG TRÌNH KHẢO SÁT HỌC BẮT CHƯỚC</h2>
          <p>Hệ thống tri thức chuyên sâu 14 chương xuyên suốt từ nền tảng toán học MDPs, Behavioral Cloning, DAgger, Dynamic Movement Primitives, Diffusion Policy, Inverse RL, GAIL đến triển khai thực tế trên HuggingFace LeRobot & ALOHA 50 Hz.</p>
          
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
            <input type="text" id="matrix-search-input" placeholder="Tìm kiếm khái niệm, thuật toán, công thức (BC, DAgger, DMPs, Diffusion, GAIL, T-REX, LeRobot)...">
          </div>
          
          <div class="filter-pills">
            <button class="filter-pill active" data-filter="all">Tất cả (14 Chương)</button>
            <button class="filter-pill" data-filter="track-1">Track 1: Nền Tảng & Lệch Phân Phối (Ch 1-2)</button>
            <button class="filter-pill" data-filter="track-2">Track 2: Học Tương Tác IIL (Ch 3-4)</button>
            <button class="filter-pill" data-filter="track-3">Track 3: Động Tác & Deep IL SOTA (Ch 5-6)</button>
            <button class="filter-pill" data-filter="track-4">Track 4: Inverse RL & GAIL (Ch 7-8)</button>
            <button class="filter-pill" data-filter="track-5">Track 5: Quan Sát & Dữ Liệu Lỗi (Ch 9-11)</button>
            <button class="filter-pill" data-filter="track-6">Track 6: HRI & Triển Khai Thực Tế (Ch 12-14)</button>
          </div>
        </div>

        <!-- Curriculum Matrix Grid Cards -->
        <div class="curriculum-matrix-grid" id="matrix-grid">
{cards_html}
        </div>
      </section>

      <footer class="site-footer" style="margin-top: 3rem; text-align: center; border-top: 1px solid var(--border-color); padding-top: 2rem;">
        <p>Học Bắt Chước Trong Robot Học • Hệ Thống Chưng Cất Tri Thức Đa Tầng</p>
        <p class="footer-meta">Biên dịch & Chưng cất theo chuẩn Deep Reading Distiller • Sẵn sàng chạy offline 100% & Xuất bản GitHub Pages</p>
      </footer>
    </main>
  </div>

  <script src="assets/js/app.js"></script>
</body>
</html>"""

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Successfully generated Portal Hub index.html with all 14 chapters across 6 Master Tracks!")
