# -*- coding: utf-8 -*-
"""
build_chapters_t5_t6.py
Biên soạn nội dung chuẩn 6 tầng tri thức cho Track 5 và Track 6 (Chương 09 - Chương 14):
- Ch 09: Liên Kết Dữ Liệu Ngữ Nghĩa & Tối Ưu Vòng Lặp Ngữ Nghĩa
- Ch 10: Khung Toán Học Active SLAM & Không Gian Hành Động Ứng Viên
- Ch 11: Đo Lường Thông Tin Toán Học: Entropy, Mutual Info & Tiêu Chuẩn TOED
- Ch 12: Song Đề Khám Phá vs Khai Thác & Lập Kế Hoạch Không Gian Niềm Tin (BSP)
- Ch 13: Đa Robot SLAM: Phân Tán, Hợp Nhất Bản Đồ & Active Exploration
- Ch 14: Kiến Trúc Triển Khai Thực Tế: ROS 2 Humble, Nav2, SLAM Toolbox & Benchmarks
"""

import os

BASE_DIR = r"c:\Users\chucuong\OneDrive\Reading\slam-knowledge-web"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

def make_chapter_html(ch_num_str, title, subtitle, track_name, track_slug, prev_url, prev_title, next_url, next_title, sidebar_items, body_content):
    sidebar_html = ""
    for item in sidebar_items:
        sidebar_html += f"""
        <div class="nav-item">
          <a href="#{item['id']}">
            <span class="nav-text">{item['title']}</span>
          </a>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chương {ch_num_str}: {title} - SLAM & Active Perception Portal</title>
  <meta name="description" content="{subtitle}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
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

  <!-- Global Header with Breadcrumbs -->
  <header class="site-header">
    <div class="header-left">
      <nav class="breadcrumb-nav">
        <a href="../index.html" class="breadcrumb-item">🏠 Lộ trình Tổng quan</a>
        <span class="breadcrumb-sep">/</span>
        <span class="breadcrumb-item">{track_name}</span>
        <span class="breadcrumb-sep">/</span>
        <span class="breadcrumb-item current">Chương {ch_num_str}</span>
      </nav>
    </div>
    <div class="header-right">
      <a href="../index.html" class="book-badge" style="text-decoration: none; color: inherit;">
        <span class="badge-icon">🗺️</span> Bảng Ma Trận
      </a>
      <button id="theme-btn" class="theme-toggle-btn" aria-label="Toggle Theme">
        <span id="theme-icon">☀️</span>
        <span id="theme-text">Chế độ sáng</span>
      </button>
    </div>
  </header>

  <div class="app-layout">
    <!-- Chapter Specific Sticky Tag Bar Sidebar (320px) -->
    <aside class="sidebar-container" id="sidebar">
      <div class="sidebar-header">
        <span class="sidebar-title">MỤC LỤC CHƯƠNG {ch_num_str}</span>
        <span class="sidebar-badge">{len(sidebar_items)} MỤC</span>
      </div>

      <nav class="sidebar-nav" id="sidebar-nav">
        {sidebar_html}
      </nav>

      <div class="sidebar-footer">
        <a href="../index.html" class="sidebar-back-btn">
          <span>←</span> Về Trang Tổng Quan
        </a>
      </div>
    </aside>

    <!-- Main Content Container (Fit Web) -->
    <main class="main-content" id="main-content">
      <article class="chapter-article">
        <div class="article-header">
          <div class="chapter-meta-pill">{track_name} • CHƯƠNG {ch_num_str}</div>
          <h1 class="chapter-title">{title}</h1>
          <p class="chapter-subtitle">{subtitle}</p>
          <div class="article-source-bar">
            <span>📚 Nguồn tài liệu: <strong>Julio A. Placed et al. (IEEE T-RO 2023) & Thanh Nguyen Canh et al. (2021)</strong></span>
          </div>
        </div>

        {body_content}

        <!-- Pagination Footer -->
        <div class="chapter-nav-cards">
          <a href="{prev_url}" class="ch-nav-card prev">
            <span class="nav-direction">← CHƯƠNG TRƯỚC</span>
            <span class="nav-ch-title">{prev_title}</span>
          </a>
          <a href="{next_url}" class="ch-nav-card next">
            <span class="nav-direction">CHƯƠNG TIẾP THEO →</span>
            <span class="nav-ch-title">{next_title}</span>
          </a>
        </div>
      </article>

      <footer class="site-footer">
        <p>Hệ Thống Tri Thức SLAM & Active Perception • SOTA Pedagogical Portal</p>
        <p class="footer-meta">Biên soạn tự động theo chuẩn Deep Reading Distiller • Sẵn sàng chạy offline 100% & GitHub Pages</p>
      </footer>
    </main>
  </div>

  <script src="../assets/js/app.js"></script>
  <script src="../assets/js/simulators.js"></script>
</body>
</html>"""
    return html

# ==============================================================================
# CHƯƠNG 09: Liên Kết Dữ Liệu Ngữ Nghĩa & Tối Ưu Vòng Lặp Ngữ Nghĩa
# ==============================================================================
ch09_sidebar = [
    {"id": "sec-9-1", "title": "9.1 Thách Thức Nhập Nhằng Liên Kết Dữ Liệu Ngữ Nghĩa"},
    {"id": "sec-9-2", "title": "9.2 Thuật Toán Gán Cặp Hungarian (Munkres)"},
    {"id": "sec-9-3", "title": "9.3 Vòng Lặp Ngữ Nghĩa & Giải Quyết Perceptual Aliasing"},
    {"id": "sec-9-4", "title": "9.4 Semantically-Informed Pose Graph Optimization"},
    {"id": "sec-9-sim", "title": "⚡ Mô Phỏng Ghép Nối Đồ Thị Ngữ Nghĩa (Canvas)"},
    {"id": "sec-9-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Ma Trận Chi Phí Mahalanobis"},
    {"id": "sec-9-bridge", "title": "🛠️ Cầu Nối Python: Hungarian Data Association Scipy"}
]

ch09_body = r"""
        <!-- 9.1 -->
        <h2 id="sec-9-1">9.1 Thách Thức Nhập Nhằng Liên Kết Dữ Liệu Ngữ Nghĩa (Data Association Ambiguity)</h2>
        <p>Khi robot tiến vào một căn phòng có hàng chục đồ vật cùng loại (ví dụ: 8 chiếc ghế giống hệt nhau quanh bàn họp), mạng học sâu phát hiện ra 8 bounding box đều có nhãn `chair`. Thuật toán SLAM phải đối mặt với bài toán nan giải: <em>"Chiếc ghế quan sát được ở khung hình hiện tại tương ứng với landmark chiếc ghế số mấy trong bản đồ?"</em></p>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 LIÊN KẾT DỮ LIỆU ĐÚNG ĐỂ LÀM GÌ?</div>
          <div class="why-matters-body">
            Liên kết dữ liệu (Data Association) là tử huyệt của SLAM. Nếu gán nhầm landmark chiếc ghế A sang chiếc ghế B, bộ tối ưu hóa Pose Graph sẽ bị ép phải bẻ cong quỹ đạo để hai điểm khác nhau trùng khít lên nhau, dẫn đến hiện tượng bản đồ bị xoắn vặn và phá hủy hoàn toàn. Thuật toán **Hungarian Bipartite Matching** kết hợp khoảng cách hình học Mahalanobis với nhãn ngữ nghĩa đảm bảo tỷ lệ gán cặp tối ưu toàn cục.
          </div>
        </div>

        <!-- 9.2 -->
        <h2 id="sec-9-2">9.2 Thuật Toán Hungarian (Munkres) Kết Hợp Khoảng Cách Mahalanobis</h2>
        <p>Ma trận chi phí gán cặp $\mathbf{C} \in \mathbb{R}^{M \times N}$ giữa $M$ detection quan sát $z_i$ và $N$ landmark bản đồ $L_j$ được tính toán kết hợp cả hình học lẫn phân phối xác suất lớp:</p>
        <div class="formula-hero">
          <div class="formula-title">Hàm Chi Phí Gán Cặp Ngữ Nghĩa Hỗn Hợp</div>
          <div class="formula-math">
            $$C_{ij} = (z_i - \hat{z}_j)^T (\mathbf{H}_j \mathbf{P} \mathbf{H}_j^T + \mathbf{R}_i)^{-1} (z_i - \hat{z}_j) - \beta \log P(\text{class}_i = \text{class}_j)$$
          </div>
          <div class="formula-legend">
            <strong>Trong đó:</strong>
            <br>• Số hạng thứ nhất là khoảng cách Mahalanobis bình phương chuẩn hóa theo hiệp phương sai đổi mới $\mathbf{S} = \mathbf{H} \mathbf{P} \mathbf{H}^T + \mathbf{R}$.
            <br>• Số hạng thứ hai là phần thưởng tương thích nhãn lớp ngữ nghĩa (nếu cùng loại `chair` thì chi phí giảm mạnh; nếu khác loại thì bị gán chi phí cực lớn $+\infty$).
          </div>
        </div>

        <!-- 9.3 -->
        <h2 id="sec-9-3">9.3 Đóng Vòng Lặp Ngữ Nghĩa (Semantic Loop Closure) & Giải Quyết Perceptual Aliasing</h2>
        <p>Trong các tòa nhà lớn, hai căn phòng ở tầng 2 và tầng 3 có thể có cùng kích thước, cùng sơn màu trắng và lát cùng loại gạch. Các phương pháp DBoW2 truyền thống dựa trên từ điển thị giác bề ngoài (Appearance) thường bị lừa dẫn đến đóng vòng lặp sai (Perceptual Aliasing). <strong>Semantic Loop Closure</strong> sử dụng cấu trúc không gian của các cụm đồ vật (Semantic Subgraph: ví dụ phòng có 1 bàn ăn ở giữa, 4 ghế xung quanh và 1 tivi góc phải) tạo nên một "dấu vân tay ngữ nghĩa" độc nhất vô nhị, loại trừ hoàn toàn các kết nối vòng lặp giả tạo!</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-9-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Liên Kết Dữ Liệu Bipartite Matching Bằng Thuật Toán Hungarian</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-09" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-9-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Lập Ma Trận Chi Phí Mahalanobis & Giải Gán Cặp Hungarian 2x2</h3>
          <p>Có 2 quan sát $z_1, z_2$ và 2 landmark bản đồ $L_1, L_2$. Khoảng cách hình học Euclid đo được: $d(z_1, L_1) = 1.0$, $d(z_1, L_2) = 4.0$, $d(z_2, L_1) = 3.0$, $d(z_2, L_2) = 1.5$. Nhãn ngữ nghĩa: $z_1$ là `Chair`, $z_2$ là `Table`; $L_1$ là `Chair`, $L_2$ là `Table`. Giả định phương sai $\sigma^2 = 1.0$, nếu lệch nhãn phạt thêm $+10.0$. Thiết lập ma trận chi phí $\mathbf{C}$ và giải cặp gán tối ưu theo thuật toán Hungarian.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính toán chi phí cho từng cặp phần tử $(i, j)$</h5>
              <p>• Cặp $(z_1, L_1)$: Cùng nhãn `Chair` $\Rightarrow C_{11} = (1.0)^2 + 0 = 1.0$</p>
              <p>• Cặp $(z_1, L_2)$: Khác nhãn (`Chair` vs `Table`) $\Rightarrow C_{12} = (4.0)^2 + 10.0 = 16.0 + 10.0 = 26.0$</p>
              <p>• Cặp $(z_2, L_1)$: Khác nhãn (`Table` vs `Chair`) $\Rightarrow C_{21} = (3.0)^2 + 10.0 = 9.0 + 10.0 = 19.0$</p>
              <p>• Cặp $(z_2, L_2)$: Cùng nhãn `Table` $\Rightarrow C_{22} = (1.5)^2 + 0 = 2.25$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Lập ma trận chi phí tổng hợp $\mathbf{C}$</h5>
              <p>$$\mathbf{C} = \begin{bmatrix} 1.0 & 26.0 \\ 19.0 & 2.25 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: So sánh hai phương án hoán vị gán cặp</h5>
              <p>• Phương án A ($z_1 \to L_1, z_2 \to L_2$): $\text{Cost}_A = C_{11} + C_{22} = 1.0 + 2.25 = 3.25$</p>
              <p>• Phương án B ($z_1 \to L_2, z_2 \to L_1$): $\text{Cost}_B = C_{12} + C_{21} = 26.0 + 19.0 = 45.0$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Kết luận cặp ghép tối ưu toàn cục</h5>
              <p>Do $\text{Cost}_A = 3.25 \ll \text{Cost}_B = 45.0$, thuật toán Hungarian chọn cặp ghép tối ưu: $z_1 \leftrightarrow L_1$ và $z_2 \leftrightarrow L_2$. Nhờ số hạng ngữ nghĩa, thuật toán triệt tiêu $100\%$ nguy cơ gán nhầm giữa bàn và ghế!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-9-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Module Hungarian Data Association Với SciPy (Python)</h4>
          <p>Mã nguồn thực thi giải bài toán gán cặp bipartite matching tối ưu:</p>
          <div class="code-card">
            <div class="code-header">
              <span>hungarian_associator.py (Python / SciPy)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import numpy as np
from scipy.optimize import linear_sum_assignment

def associate_detections_to_landmarks(dets, lms, dist_threshold=3.0):
    # dets: danh sách quan sát [N, 3] (x, y, class_id)
    # lms: danh sách landmark [M, 3] (x, y, class_id)
    N, M = len(dets), len(lms)
    cost_matrix = np.full((N, M), 1e6) # Khởi tạo vô cùng
    
    for i in range(N):
        for j in range(M):
            # Nếu trùng nhãn ngữ nghĩa
            if dets[i][2] == lms[j][2]:
                dist = np.hypot(dets[i][0] - lms[j][0], dets[i][1] - lms[j][1])
                if dist \lt dist_threshold:
                    cost_matrix[i, j] = dist**2
                    
    # Giải bài toán Hungarian
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    matches = []
    for r, c in zip(row_ind, col_ind):
        if cost_matrix[r, c] \lt 1e5:
            matches.append((r, c))
    return matches</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 10: Khung Toán Học Active SLAM & Không Gian Hành Động Ứng Viên
# ==============================================================================
ch10_sidebar = [
    {"id": "sec-10-1", "title": "10.1 Định Nghĩa Bài Toán Active SLAM (A-SLAM)"},
    {"id": "sec-10-2", "title": "10.2 Khung Phân Rã 3 Giai Đoạn Chuẩn"},
    {"id": "sec-10-3", "title": "10.3 Nhận Diện Điểm Đích: Frontier-Based Exploration"},
    {"id": "sec-10-4", "title": "10.4 Sinh Quỹ Đạo Bằng Cây Mở Rộng RRT & NBV"},
    {"id": "sec-10-sim", "title": "⚡ Mô Phỏng Nhận Diện Biên Giới Frontier & RRT (Canvas)"},
    {"id": "sec-10-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Thuật Toán Wavefront WFD"},
    {"id": "sec-10-bridge", "title": "🛠️ Cầu Nối ROS 2: Node Frontier Exploration C++ Nav2"}
]

ch10_body = r"""
        <!-- 10.1 -->
        <h2 id="sec-10-1">10.1 Định Nghĩa Bài Toán Active SLAM (A-SLAM)</h2>
        <p>Hầu hết các hệ thống SLAM cổ điển là hệ thống <strong>thụ động (Passive SLAM)</strong>: Robot nhận quỹ đạo do con người điều khiển từ xa hoặc do bộ lập kế hoạch đường đi định sẵn, nhiệm vụ của SLAM chỉ là quan sát và xây bản đồ theo sau.</p>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 ACTIVE SLAM LÀ GÌ VÀ TẠI SAO CẦN THIẾT?</div>
          <div class="why-matters-body">
            Theo khảo cứu toàn diện của Julio A. Placed, Luca Carlone et al. (IEEE T-RO 2023), <strong>Active SLAM (A-SLAM)</strong> trao quyền tự chủ tuyệt đối cho robot: Robot tự mình tính toán, ra quyết định chọn hành động di chuyển tiếp theo sao cho:
            <br>1. <strong>Tối đa hóa thông tin thu được để mở rộng bản đồ</strong> (khám phá khu vực chưa biết).
            <br>2. <strong>Tối thiểu hóa độ bất định hiệp phương sai</strong> của cả quỹ đạo di chuyển lẫn bản đồ.
            <br>Nhờ Active SLAM, một robot cứu hộ thả vào tòa nhà sập có thể tự động thám hiểm và quét sạch bản đồ toàn khu vực mà không cần một người điều khiển nào!
          </div>
        </div>

        <!-- 10.2 -->
        <h2 id="sec-10-2">10.2 Khung Phân Rã 3 Giai Đoạn Chuẩn Trong Active SLAM</h2>
        <p>Để giải quyết bài toán tối ưu hóa phức tạp trong thời gian thực, hệ thống A-SLAM phân rã thành 3 giai đoạn nối tiếp:</p>
        <p>• <strong>Giai đoạn 1 (Candidate Identification):</strong> Sinh tập hợp các điểm đến tiềm năng $\mathcal{A}_{\text{cand}}$ từ bản đồ hiện tại (biên giới, tư thế quan sát Next-Best-View).</p>
        <p>• <strong>Giai đoạn 2 (Utility Computation):</strong> Đánh giá hàm thỏa dụng thông tin $\mathcal{U}(a)$ cho từng ứng viên dựa trên lý thuyết thông tin và thiết kế thực nghiệm tối ưu (TOED).</p>
        <p>• <strong>Giai đoạn 3 (Action Selection & Execution):</strong> Chọn hành động $a^* = \arg\max \mathcal{U}(a)$, lập đường đi tránh va chạm và gửi lệnh điều khiển xuống động cơ.</p>

        <!-- 10.3 -->
        <h2 id="sec-10-3">10.3 Kỹ Thuật Nhận Diện Biên Giới Khám Phá (Frontier-Based Exploration)</h2>
        <p>Brian Yamauchi (1997) đưa ra nguyên lý kinh điển: <em>"Biên giới (Frontier) là ranh giới phân tách giữa các ô đã biết là trống (Free) và các ô chưa từng được quét tới (Unknown)".</em> Khi robot di chuyển tới biên giới, nó đảm bảo chắc chắn sẽ mở rộng thêm các khoảng không gian mới chưa từng biết.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-10-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Nhận Diện Biên Giới (Frontier) & Cây Khám Phá RRT</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-10" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-10-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Thuật Toán Wavefront Frontier Detection (WFD) Phân Nhóm Biên Giới Trên Lưới</h3>
          <p>Cho ma trận bản đồ $4 \times 4$ với các mã: `0` (Free Space), `-1` (Unknown), `100` (Wall). 
          <br>Hàng 1: `[ 0,  0, -1, -1]`
          <br>Hàng 2: `[ 0,  0, -1, -1]`
          <br>Hàng 3: `[ 0, 100, -1, -1]`
          <br>Hàng 4: `[100, 100, -1, -1]`
          Áp dụng định nghĩa: Một ô là Frontier khi và chỉ khi nó là ô `0` (Free) và có ít nhất một ô láng giềng 4 hướng là ô `-1` (Unknown). Xác định tất cả các ô Frontier và tính tọa độ tâm cụm (Centroid).</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Quét các ô Free (giá trị 0)</h5>
              <p>Danh sách các ô giá trị 0: $(1,1), (1,2), (2,1), (2,2), (3,1)$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Kiểm tra láng giềng 4 hướng (Trên, Dưới, Trái, Phải)</h5>
              <p>• Ô $(1,1)$: Phải là $(1,2)$ (0), Dưới là $(2,1)$ (0) $\Rightarrow$ Không có láng giềng `-1`.</p>
              <p>• Ô $(1,2)$: Phải là $(1,3)$ (`-1`!) $\Rightarrow$ <strong>Là Frontier $F_1$</strong>.</p>
              <p>• Ô $(2,1)$: Phải là $(2,2)$ (0), Dưới là $(3,1)$ (0) $\Rightarrow$ Không có láng giềng `-1`.</p>
              <p>• Ô $(2,2)$: Phải là $(2,3)$ (`-1`!) $\Rightarrow$ <strong>Là Frontier $F_2$</strong>.</p>
              <p>• Ô $(3,1)$: Phải là $(3,2)$ (`100` Wall), Dưới là $(4,1)$ (`100` Wall) $\Rightarrow$ Không có láng giềng `-1`.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Gom nhóm các ô Frontier liền kề</h5>
              <p>Cụm biên giới gồm 2 ô kề nhau: $F = \{(1, 2), (2, 2)\}$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Tính tọa độ đích đến tâm cụm (Goal Centroid)</h5>
              <p>$$x_{\text{goal}} = \frac{1 + 2}{2} = 1.5, \quad y_{\text{goal}} = \frac{2 + 2}{2} = 2.0$$</p>
              <p>Tọa độ đích $(1.5, 2.0)$ được đưa vào danh sách ứng viên điều hướng của Active SLAM!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-10-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Node Tìm Biên Giới Frontier Bằng C++ Cho Nav2</h4>
          <p>Mã nguồn C++ quét bản đồ `OccupancyGrid` và xuất bản danh sách các điểm mục tiêu thám hiểm:</p>
          <div class="code-card">
            <div class="code-header">
              <span>frontier_detector_node.cpp (ROS 2 / C++)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>#include &lt;rclcpp/rclcpp.hpp&gt;
#include &lt;nav_msgs/msg/occupancy_grid.hpp&gt;
#include &lt;geometry_msgs/msg/point.hpp&gt;
#include &lt;vector&gt;

class FrontierDetector : public rclcpp::Node {
public:
  FrontierDetector() : Node("frontier_detector") {
    map_sub_ = this->create_subscription&lt;nav_msgs::msg::OccupancyGrid&gt;(
      "/map", 1, std::bind(&FrontierDetector::mapCallback, this, std::placeholders::_1));
  }

private:
  void mapCallback(const nav_msgs::msg::OccupancyGrid::SharedPtr msg) {
    int w = msg->info.width;
    int h = msg->info.height;
    std::vector&lt;geometry_msgs::msg::Point&gt; frontiers;

    for (int y = 1; y \lt h - 1; ++y) {
      for (int x = 1; x \lt w - 1; ++x) {
        int idx = y * w + x;
        if (msg->data[idx] == 0) { // Ô Free
          // Kiểm tra xem có láng giềng nào là Unknown (-1) không
          if (msg->data[idx + 1] == -1 || msg->data[idx - 1] == -1 ||
              msg->data[idx + w] == -1 || msg->data[idx - w] == -1) {
            geometry_msgs::msg::Point pt;
            pt.x = msg->info.origin.position.x + x * msg->info.resolution;
            pt.y = msg->info.origin.position.y + y * msg->info.resolution;
            frontiers.push_back(pt);
          }
        }
      }
    }
    RCLCPP_INFO(this->get_logger(), "Detected %zu frontier points.", frontiers.size());
  }
  rclcpp::Subscription&lt;nav_msgs::msg::OccupancyGrid&gt;::SharedPtr map_sub_;
};</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 11: Đo Lường Thông Tin Toán Học: Entropy, Mutual Info & Tiêu Chuẩn TOED
# ==============================================================================
ch11_sidebar = [
    {"id": "sec-11-1", "title": "11.1 Định Lượng Độ Bất Định Bằng Shannon Entropy"},
    {"id": "sec-11-2", "title": "11.2 Độ Lợi Thông Tin Tương Hỗ (Mutual Information)"},
    {"id": "sec-11-3", "title": "11.3 Tiêu Chuẩn TOED: A-opt, D-opt & E-opt"},
    {"id": "sec-11-4", "title": "11.4 Phân Tích Hình Học Siêu Elip Tin Cậy"},
    {"id": "sec-11-sim", "title": "⚡ Mô Phỏng So Sánh Tiêu Chuẩn TOED (Canvas)"},
    {"id": "sec-11-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Xếp Hạng Quỹ Đạo Bằng TOED"},
    {"id": "sec-11-bridge", "title": "🛠️ Cầu Nối Python: Script Tính Toán Information Utility"}
]

ch11_body = r"""
        <!-- 11.1 -->
        <h2 id="sec-11-1">11.1 Định Lượng Độ Bất Định Toán Học Bằng Shannon Entropy</h2>
        <p>Để so sánh xem hai hành động tiềm năng hành động nào "tốt hơn", robot cần một hàm toán học định lượng chính xác độ bất định của trạng thái niềm tin (Belief state). Đối với vector trạng thái ngẫu nhiên $X \sim \mathcal{N}(\mu, \mathbf{\Sigma}) \in \mathbb{R}^n$, <strong>Shannon Differential Entropy</strong> được tính gọn gàng qua định thức ma trận hiệp phương sai:</p>
        <div class="formula-hero">
          <div class="formula-title">Entropy Của Phân Phối Chuẩn Đa Chiều</div>
          <div class="formula-math">
            $$H(X) = \frac{1}{2} \ln \left( (2\pi e)^n \det(\mathbf{\Sigma}) \right) = \frac{n}{2}(1 + \ln 2\pi) + \frac{1}{2} \ln \det(\mathbf{\Sigma})$$
          </div>
          <div class="formula-legend">
            <strong>Bản chất:</strong> Entropy tỷ lệ thuận với logarit của định thức $\det(\mathbf{\Sigma})$ (thể tích của siêu elip tin cậy bất định). Giảm $\det(\mathbf{\Sigma})$ đồng nghĩa với việc thu hẹp độ không chắc chắn của vị trí robot!
          </div>
        </div>

        <!-- 11.2 -->
        <h2 id="sec-11-2">11.2 Độ Lợi Thông Tin Tương Hỗ (Mutual Information)</h2>
        <p>Lượng thông tin dự kiến thu nhận được từ phép đo tương lai $Z$ được đo bằng độ sụt giảm Entropy:</p>
        $$I(X; Z) = H(X) - H(X \mid Z) = \frac{1}{2} \ln \frac{\det(\mathbf{\Sigma}_X)}{\det(\mathbf{\Sigma}_{X \mid Z})}$$

        <!-- 11.3 -->
        <h2 id="sec-11-3">11.3 Lý Thuyết Thiết Kế Thực Nghiệm Tối Ưu (TOED: Theory of Optimal Experimental Design)</h2>
        <p>Theo khảo cứu IEEE T-RO (2023), việc chỉ nhìn vào thể tích đôi khi gây đánh lừa: một hình elip rất dài và hẹp (sai số hướng ngang cực lớn nhưng hướng dọc cực nhỏ) vẫn có thể có thể tích nhỏ. Lý thuyết TOED áp dụng trên ma trận thông tin Fisher $\mathbf{\Lambda} = \mathbf{\Sigma}^{-1}$ đưa ra 3 tiêu chuẩn vàng:</p>
        <ul>
          <li><strong>D-optimality (Định thức):</strong> $\min \det(\mathbf{\Sigma}) = \max \det(\mathbf{\Lambda})$. Cực tiểu hóa thể tích elip sai số toàn cục.</li>
          <li><strong>A-optimality (Vết Trace):</strong> $\min \mathrm{tr}(\mathbf{\Sigma}) = \min \sum \lambda_i(\mathbf{\Sigma})$. Cực tiểu hóa trung bình phương sai theo các trục tọa độ.</li>
          <li><strong>E-optimality (Giá trị riêng lớn nhất):</strong> $\min \lambda_{\max}(\mathbf{\Sigma}) = \max \lambda_{\min}(\mathbf{\Lambda})$. Cực tiểu hóa bán trục dài nhất của elip (giảm sai số theo hướng xấu nhất).</li>
        </ul>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-11-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: So Sánh Hình Học Siêu Elip Theo Tiêu Chuẩn TOED</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-11" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-11-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Toán A-opt, D-opt, E-opt Của Ma Trận Hiệp Phương Sai 2x2</h3>
          <p>Có 2 quỹ đạo ứng viên dẫn tới 2 ma trận hiệp phương sai tư thế dự đoán:
          $$\mathbf{\Sigma}_1 = \begin{bmatrix} 4.0 & 0.0 \\ 0.0 & 1.0 \end{bmatrix}, \quad \mathbf{\Sigma}_2 = \begin{bmatrix} 2.5 & 0.0 \\ 0.0 & 2.0 \end{bmatrix}$$
          Tính chỉ số D-opt ($\det$), A-opt ($\mathrm{tr}$), và E-opt ($\lambda_{\max}$) cho cả hai ứng viên và đưa ra nhận xét so sánh chuyên sâu.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính tiêu chuẩn D-optimality (Thể tích elip)</h5>
              <p>• Ứng viên 1: $\det(\mathbf{\Sigma}_1) = 4.0 \times 1.0 - 0 = 4.0$</p>
              <p>• Ứng viên 2: $\det(\mathbf{\Sigma}_2) = 2.5 \times 2.0 - 0 = 5.0$</p>
              <p>Nhận xét D-opt: Ứng viên 1 tốt hơn ($4.0 \lt 5.0$).</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính tiêu chuẩn A-optimality (Trung bình phương sai)</h5>
              <p>• Ứng viên 1: $\mathrm{tr}(\mathbf{\Sigma}_1) = 4.0 + 1.0 = 5.0$</p>
              <p>• Ứng viên 2: $\mathrm{tr}(\mathbf{\Sigma}_2) = 2.5 + 2.0 = 4.5$</p>
              <p>Nhận xét A-opt: Ứng viên 2 tốt hơn ($4.5 \lt 5.0$).</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính tiêu chuẩn E-optimality (Trục sai số xấu nhất)</h5>
              <p>• Ứng viên 1: $\lambda_{\max}(\mathbf{\Sigma}_1) = 4.0$ (bán trục dài $a = \sqrt{4} = 2.0$ m)</p>
              <p>• Ứng viên 2: $\lambda_{\max}(\mathbf{\Sigma}_2) = 2.5$ (bán trục dài $a = \sqrt{2.5} \approx 1.58$ m)</p>
              <p>Nhận xét E-opt: Ứng viên 2 vượt trội hoàn toàn ($2.5 \ll 4.0$).</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Quyết định lựa chọn trong Active SLAM</h5>
              <p>Mặc dù Ứng viên 1 có thể tích elip nhỏ hơn (D-opt thắng), nhưng sai số trục $x$ của nó lên tới $4.0\text{ m}^2$ (nguy cơ va chạm thành bên rất cao). Do đó, tiêu chuẩn E-opt và A-opt chọn <strong>Ứng viên 2</strong> vì sự đẳng hướng (Isotropic), an toàn cơ học hơn nhiều cho xe tự hành!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-11-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Module Tính Thỏa Dụng Thông Tin TOED Bằng Python</h4>
          <p>Mã nguồn tính toán các chỉ số D-opt, A-opt, E-opt từ ma trận thông tin đồ thị:</p>
          <div class="code-card">
            <div class="code-header">
              <span>toed_utility_evaluator.py (Python / NumPy)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import numpy as np

class TOEDUtilityEvaluator:
    @staticmethod
    def evaluate(cov_matrix):
        # cov_matrix: ma trận hiệp phương sai [n, n]
        eigvals = np.linalg.eigvalsh(cov_matrix)
        
        d_opt = np.log(np.linalg.det(cov_matrix) + 1e-12) # log-det
        a_opt = np.trace(cov_matrix)                      # trace
        e_opt = np.max(eigvals)                           # max eigenvalue
        
        return {
            "D_opt_log_det": float(d_opt),
            "A_opt_trace": float(a_opt),
            "E_opt_max_eig": float(e_opt)
        }</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 12: Song Đề Khám Phá vs Khai Thác & Lập Kế Hoạch Không Gian Niềm Tin (BSP)
# ==============================================================================
ch12_sidebar = [
    {"id": "sec-12-1", "title": "12.1 Song Đề Cốt Lõi: Exploration vs Exploitation"},
    {"id": "sec-12-2", "title": "12.2 Lập Kế Hoạch Trong Không Gian Niềm Tin (BSP)"},
    {"id": "sec-12-3", "title": "12.3 Thiết Kế Hàm Thỏa Dụng Đa Mục Tiêu Pareto"},
    {"id": "sec-12-4", "title": "12.4 Cơ Chế Tự Động Kích Hoạt Active Loop Closure"},
    {"id": "sec-12-sim", "title": "⚡ Mô Phỏng Bộ Chuyển Đổi Explore vs Loop Close (Canvas)"},
    {"id": "sec-12-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Hàm Thỏa Dụng Đa Mục Tiêu"},
    {"id": "sec-12-bridge", "title": "🛠️ Cầu Nối ROS 2: Cây Hành Vi BehaviorTree Nav2"}
]

ch12_body = r"""
        <!-- 12.1 -->
        <h2 id="sec-12-1">12.1 Song Đề Sinh Tử Của Active SLAM: Exploration vs Exploitation</h2>
        <p>Mâu thuẫn lớn nhất trong điều khiển robot thám hiểm tự hành:</p>
        <ul>
          <li><strong>Khám phá (Exploration):</strong> Thúc đẩy robot liên tục lao vào các vùng chưa biết để tăng độ phủ bản đồ. Tuy nhiên, càng đi xa, sai số Dead Reckoning càng tích lũy, các tia laser đo được bị gán sai vị trí khiến bản đồ mới bị méo mó.</li>
          <li><strong>Khai thác / Đóng vòng lặp (Exploitation / Loop Closure):</strong> Điều khiển robot quay ngược trở lại các vùng đã lập bản đồ trước đó để tái nhận diện mốc quen thuộc. Vòng lặp đóng lại triệt tiêu toàn bộ hiệp phương sai sai số, nhưng lại làm tốn pin và không mở rộng thêm mét vuông bản đồ nào.</li>
        </ul>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 GIẢI PHÁP LẬP KẾ HOẠCH TRONG KHÔNG GIAN NIỀM TIN (BSP)</div>
          <div class="why-matters-body">
            Belief-Space Planning (BSP) không chỉ lập kế hoạch trong không gian tọa độ vật lý thông thường $(x, y)$, mà lập kế hoạch trực tiếp trên <strong>Không gian Niềm tin (Belief Space)</strong> bao gồm cả phân phối xác suất và ma trận hiệp phương sai $\mathcal{B} = (\mathbf{x}, \mathbf{\Sigma})$. Hệ thống dự đoán trước độ bất định sẽ tăng lên bao nhiêu nếu đi hướng A, và sẽ giảm được bao nhiêu nếu quay lại đóng vòng lặp ở hướng B, từ đó đưa ra quyết định chuyển đổi trạng thái tối ưu toán học!
          </div>
        </div>

        <!-- 12.2 -->
        <h2 id="sec-12-2">12.2 Thiết Kế Hàm Thỏa Dụng Đa Mục Tiêu</h2>
        <p>Hàm chi phí tổng hợp cho mỗi quỹ đạo ứng viên $\tau$:</p>
        <div class="formula-hero">
          <div class="formula-title">Hàm Thỏa Dụng Cân Bằng Năng Lượng & Độ Bất Định</div>
          <div class="formula-math">
            $$J(\tau) = \alpha \cdot \text{Cost}_{\text{distance}}(\tau) - \beta \cdot \text{InfoGain}_{\text{map}}(\tau) - \gamma \cdot \Delta H_{\text{pose}}(\tau)$$
          </div>
          <div class="formula-legend">
            <strong>Trọng số điều tiết:</strong>
            <br>• $\alpha$: Phạt quãng đường di chuyển (tiết kiệm thời gian và pin).
            <br>• $\beta$: Thưởng số lượng ô lưới Unknown dự kiến sẽ được quét sạch.
            <br>• $\gamma$: Thưởng mức độ giảm Entropy của tư thế (khi quỹ đạo chứa khả năng đóng vòng lặp).
          </div>
        </div>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-12-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Bộ Chuyển Đổi Trạng Thái Khám Phá vs Active Loop Closing</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-12" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-12-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: So Sánh Hàm Thỏa Dụng Đa Mục Tiêu Cho 2 Quỹ Đạo Ứng Viên</h3>
          <p>Hệ thống có các hệ số trọng số: $\alpha = 0.5$ (chi phí/mét), $\beta = 0.1$ (điểm/ô mới), $\gamma = 2.0$ (điểm/đơn vị entropy giảm).
          <br>• <strong>Ứng viên 1 (Đi tới biên giới xa):</strong> Quãng đường $d = 8.0$ m, khám phá được $120$ ô mới, làm tăng Entropy thêm $\Delta H = +1.5$ (không có loop closure).
          <br>• <strong>Ứng viên 2 (Quay đầu đóng vòng lặp gần):</strong> Quãng đường $d = 3.0$ m, chỉ mở thêm $10$ ô mới, nhưng giảm Entropy $\Delta H = -2.2$ (giảm bất định).
          Tính điểm thỏa dụng $J_1$ và $J_2$, và xác định quyết định hành động của robot.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Thiết lập công thức tính điểm thỏa dụng $J = -\alpha d + \beta \text{Gain} - \gamma \Delta H$</h5>
              <p>Điểm càng cao thì hành động càng được ưu tiên lựa chọn.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính điểm cho Ứng viên 1 (Mở rộng biên giới)</h5>
              <p>• Chi phí di chuyển: $-0.5 \times 8.0 = -4.0$</p>
              <p>• Lợi ích bản đồ: $+0.1 \times 120 = +12.0$</p>
              <p>• Phạt tăng bất định: $-2.0 \times (+1.5) = -3.0$</p>
              <p>$$J_1 = -4.0 + 12.0 - 3.0 = +5.0$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính điểm cho Ứng viên 2 (Active Loop Closing)</h5>
              <p>• Chi phí di chuyển: $-0.5 \times 3.0 = -1.5$</p>
              <p>• Lợi ích bản đồ: $+0.1 \times 10 = +1.0$</p>
              <p>• Thưởng giảm bất định: $-2.0 \times (-2.2) = +4.4$</p>
              <p>$$J_2 = -1.5 + 1.0 + 4.4 = +3.9$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Ra quyết định điều khiển</h5>
              <p>Do $J_1 = 5.0 \gt J_2 = 3.9$, hệ thống chọn <strong>Ứng viên 1</strong> để tiếp tục mở rộng bản đồ. Tuy nhiên, nếu ở bước tiếp theo sai số tiếp tục tăng khiến $\Delta H \gt 2.5$, điểm $J_1$ sẽ tụt xuống dưới $3.0$ và quyền ưu tiên sẽ lập tức chuyển sang Ứng viên 2 để kích hoạt quay đầu đóng vòng lặp!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-12-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Cấu Trúc Cây Hành Vi Active SLAM Trong Nav2 (XML)</h4>
          <p>Mã nguồn định nghĩa Behavior Tree điều phối chuyển trạng thái giữa Khám phá và Đóng vòng lặp:</p>
          <div class="code-card">
            <div class="code-header">
              <span>active_slam_behavior_tree.xml (Nav2 / ROS 2)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>&lt;root main_tree_to_execute="MainTree"&gt;
  &lt;BehaviorTree ID="MainTree"&gt;
    &lt;RecoveryNode number_of_retries="3"&gt;
      &lt;Fallback name="ActiveSLAMStrategy"&gt;
        &lt;!-- Nếu hiệp phương sai quá cao -> Kích hoạt Loop Closure --&gt;
        &lt;Sequence name="TriggerLoopClosure"&gt;
          &lt;Condition ID="IsUncertaintyHigh" threshold="0.8"/&gt;
          &lt;Action ID="NavigateToKnownLandmark" goal="{loop_goal}"/&gt;
          &lt;Action ID="PerformScanMatching"/&gt;
        &lt;/Sequence&gt;
        
        &lt;!-- Ngược lại -> Tiếp tục khám phá biên giới --&gt;
        &lt;Sequence name="ExploreFrontier"&gt;
          &lt;Action ID="ComputeBestFrontier" goal="{frontier_goal}"/&gt;
          &lt;Action ID="NavigateToPose" goal="{frontier_goal}"/&gt;
        &lt;/Sequence&gt;
      &lt;/Fallback&gt;
      &lt;Action ID="SpinRecovery"/&gt;
    &lt;/RecoveryNode&gt;
  &lt;/BehaviorTree&gt;
&lt;/root&gt;</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 13: Đa Robot SLAM: Phân Tán, Hợp Nhất Bản Đồ & Active Exploration
# ==============================================================================
ch13_sidebar = [
    {"id": "sec-13-1", "title": "13.1 Kiến Trúc Đa Robot: Tập Trung vs Phân Tán"},
    {"id": "sec-13-2", "title": "13.2 Bài Toán Hợp Nhất Bản Đồ (Map Merging)"},
    {"id": "sec-13-3", "title": "13.3 Đóng Vòng Lặp Liên Robot (Inter-Robot Loop Closure)"},
    {"id": "sec-13-4", "title": "13.4 Phân Bổ Biên Giới Khám Phá Hợp Tác"},
    {"id": "sec-13-sim", "title": "⚡ Mô Phỏng Ghép Nối Bản Đồ Đa Robot (Canvas)"},
    {"id": "sec-13-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Thuật Toán Biến Đổi SVD / Horn"},
    {"id": "sec-13-bridge", "title": "🛠️ Cầu Nối ROS 2 C++: Node Hợp Nhất Bản Đồ Map Stitcher"}
]

ch13_body = r"""
        <!-- 13.1 -->
        <h2 id="sec-13-1">13.1 Kiến Trúc Đa Robot SLAM: Tập Trung (Centralized) vs Phân Tán (Decentralized)</h2>
        <p>Khi triển khai một đội gồm $N$ robot cùng vẽ bản đồ một khu vực rộng lớn:</p>
        <table class="academic-table" style="width:100%; margin: 1.5rem 0; border-collapse: collapse;">
          <thead>
            <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
              <th style="padding: 0.75rem;">Đặc Tính Kỹ Thuật</th>
              <th style="padding: 0.75rem;">Kiến Trúc Tập Trung (Centralized)</th>
              <th style="padding: 0.75rem;">Kiến Trúc Phân Tán (Decentralized / P2P)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Cấu trúc</strong></td>
              <td style="padding: 0.75rem;">Các robot gửi toàn bộ dữ liệu thô về một máy chủ trung tâm xử lý</td>
              <td style="padding: 0.75rem;">Mỗi robot tự chạy SLAM cục bộ, chỉ trao đổi mốc đặc trưng khi gặp nhau</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Điểm nghẽn hạ tầng</strong></td>
              <td style="padding: 0.75rem;">Nếu trạm chủ mất kết nối hoặc sập nguồn, toàn bộ hệ thống tê liệt</td>
              <td style="padding: 0.75rem;">Không có điểm lỗi đơn (No single point of failure), chịu lỗi cực cao</td>
            </tr>
            <tr>
              <td style="padding: 0.75rem;"><strong>Băng thông mạng</strong></td>
              <td style="padding: 0.75rem;">Đòi hỏi băng thông cực lớn để truyền mây điểm và ảnh RGB liên tục</td>
              <td style="padding: 0.75rem;">Băng thông siêu nhỏ (chỉ gửi vector đặc trưng và ma trận con g2o)</td>
            </tr>
          </tbody>
        </table>

        <!-- 13.2 -->
        <h2 id="sec-13-2">13.2 Hợp Nhất Bản Đồ & Đóng Vòng Lặp Liên Robot (Inter-Robot Loop Closure)</h2>
        <p>Thách thức lớn nhất của Multi-Robot SLAM là các robot thường xuất phát từ các vị trí ngẫu nhiên mà <em>không hề biết trước tư thế tương đối ban đầu</em>. Khi Robot $A$ và Robot $B$ tình cờ đi vào cùng một sảnh và quan sát chung một nhóm mốc đặc trưng, thuật toán phát hiện vòng lặp liên robot (Inter-Robot Loop Closure) kích hoạt để tìm ra phép biến đổi đồng dạng cứng $\mathbf{T}_B^A = (\mathbf{R}, \mathbf{t}) \in \mathrm{SE}(2)$:</p>
        $$\mathbf{p}_i^A = \mathbf{R} \mathbf{p}_i^B + \mathbf{t}$$
        <p>Hai đồ thị con độc lập lập tức được "khâu vá" (Stitched) thành một đồ thị Pose Graph hợp nhất toàn cầu duy nhất!</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-13-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Khâu Vá Hợp Nhất Bản Đồ Đa Robot (Map Stitching)</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-13" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-13-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tìm Phép Biến Đổi Tọa Độ $(\theta, t_x, t_y)$ Giữa Hai Đội Robot Bằng SVD</h3>
          <p>Hai robot cùng nhận diện 2 mốc chuẩn trong hệ tọa độ riêng của mình:
          <br>• Tọa độ của Robot A: $p_1^A = [1.0, 2.0]^T$, $p_2^A = [4.0, 2.0]^T$.
          <br>• Tọa độ của Robot B: $p_1^B = [2.0, -1.0]^T$, $p_2^B = [2.0, -4.0]^T$.
          Tính toán góc quay tương đối $\theta$ và vector tịnh tiến $\mathbf{t} = [t_x, t_y]^T$ để chuyển đổi bản đồ từ Robot B sang Robot A.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính trọng tâm của 2 tập điểm</h5>
              <p>• Trọng tâm A: $\bar{p}^A = \frac{[1+4, 2+2]^T}{2} = [2.5, 2.0]^T$</p>
              <p>• Trọng tâm B: $\bar{p}^B = \frac{[2+2, -1-4]^T}{2} = [2.0, -2.5]^T$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Dời về gốc tọa độ và xác định vector hướng</h5>
              <p>• Vector hướng A: $\Delta p^A = p_2^A - p_1^A = [4 - 1, 2 - 2]^T = [3.0, 0.0]^T$ (hướng góc $0^\circ$)</p>
              <p>• Vector hướng B: $\Delta p^B = p_2^B - p_1^B = [2 - 2, -4 - (-1)]^T = [0.0, -3.0]^T$ (hướng góc $-90^\circ$)</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính góc quay $\theta$</h5>
              <p>Góc quay làm cho vector $\Delta p^B$ trùng với $\Delta p^A$:</p>
              <p>$$\theta = \theta_A - \theta_B = 0^\circ - (-90^\circ) = +90^\circ \quad (\frac{\pi}{2}\text{ rad})$$</p>
              <p>Ma trận quay: $$\mathbf{R} = \begin{bmatrix} \cos(90^\circ) & -\sin(90^\circ) \\ \sin(90^\circ) & \cos(90^\circ) \end{bmatrix} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Tính vector tịnh tiến $\mathbf{t} = \bar{p}^A - \mathbf{R} \bar{p}^B$</h5>
              <p>$$\mathbf{R} \bar{p}^B = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 2.0 \\ -2.5 \end{bmatrix} = \begin{bmatrix} 2.5 \\ 2.0 \end{bmatrix}$$</p>
              <p>$$\mathbf{t} = \begin{bmatrix} 2.5 \\ 2.0 \end{bmatrix} - \begin{bmatrix} 2.5 \\ 2.0 \end{bmatrix} = \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix}$$</p>
              <p>Phép biến đổi đồng dạng cứng: Quay một góc $+90^\circ$ quanh gốc tọa độ. Bản đồ Robot B được xoay khớp hoàn hảo vào khung tham chiếu của Robot A!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-13-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Node ROS 2 Ghép Nối Bản Đồ Hai Robot (C++)</h4>
          <p>Mã nguồn nhận bản đồ từ `/robot1/map` và `/robot2/map` để hợp nhất thành `/merged_map`:</p>
          <div class="code-card">
            <div class="code-header">
              <span>map_stitcher_node.cpp (ROS 2 / C++)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>#include &lt;rclcpp/rclcpp.hpp&gt;
#include &lt;nav_msgs/msg/occupancy_grid.hpp&gt;

class MapStitcher : public rclcpp::Node {
public:
  MapStitcher() : Node("map_stitcher") {
    sub_map1_ = this->create_subscription&lt;nav_msgs::msg::OccupancyGrid&gt;(
      "/robot1/map", 1, [this](nav_msgs::msg::OccupancyGrid::SharedPtr msg){ map1_ = msg; tryMerge(); });
    sub_map2_ = this->create_subscription&lt;nav_msgs::msg::OccupancyGrid&gt;(
      "/robot2/map", 1, [this](nav_msgs::msg::OccupancyGrid::SharedPtr msg){ map2_ = msg; tryMerge(); });
    pub_merged_ = this->create_publisher&lt;nav_msgs::msg::OccupancyGrid&gt;("/merged_map", 1);
  }

private:
  void tryMerge() {
    if (!map1_ || !map2_) return;
    // Khởi tạo bản đồ hợp nhất với kích thước bao phủ cả hai
    auto merged = std::make_shared&lt;nav_msgs::msg::OccupancyGrid&gt;(*map1_);
    merged->header.stamp = this->now();
    merged->header.frame_id = "map";
    
    // Ghép dữ liệu ô lưới (Logic OR chướng ngại vật)
    for (size_t i = 0; i \lt merged->data.size() && i \lt map2_->data.size(); ++i) {
      if (map2_->data[i] \gt merged->data[i]) {
        merged->data[i] = map2_->data[i];
      }
    }
    pub_merged_->publish(*merged);
  }
  nav_msgs::msg::OccupancyGrid::SharedPtr map1_, map2_;
  rclcpp::Subscription&lt;nav_msgs::msg::OccupancyGrid&gt;::SharedPtr sub_map1_, sub_map2_;
  rclcpp::Publisher&lt;nav_msgs::msg::OccupancyGrid&gt;::SharedPtr pub_merged_;
};</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 14: Kiến Trúc Triển Khai Thực Tế: ROS 2 Humble, Nav2, SLAM Toolbox & Benchmarks
# ==============================================================================
ch14_sidebar = [
    {"id": "sec-14-1", "title": "14.1 So Sánh Ngăn Xếp SLAM Công Nghiệp"},
    {"id": "sec-14-2", "title": "14.2 Kỹ Thuật Bản Đồ Trọn Đời (Lifelong Mapping)"},
    {"id": "sec-14-3", "title": "14.3 Thước Đo Benchmark Quốc Tế: ATE RMSE & RPE"},
    {"id": "sec-14-4", "title": "14.4 Hướng Dẫn Tinh Chỉnh Tham Số SLAM Toolbox Thực Chiến"},
    {"id": "sec-14-sim", "title": "⚡ Mô Phỏng Đánh Giá Quỹ Đạo ATE / RPE (Canvas)"},
    {"id": "sec-14-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Căn Chỉnh Umeyama & ATE RMSE"},
    {"id": "sec-14-bridge", "title": "🛠️ Cầu Nối ROS 2: Cấu Hình slam_toolbox_params.yaml Chuẩn"}
]

ch14_body = r"""
        <!-- 14.1 -->
        <h2 id="sec-14-1">14.1 Bảng So Sánh Toàn Diện Các Ngăn Xếp SLAM Công Nghiệp Hàng Đầu</h2>
        <table class="academic-table" style="width:100%; margin: 1.5rem 0; border-collapse: collapse;">
          <thead>
            <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
              <th style="padding: 0.75rem;">Phần Mềm</th>
              <th style="padding: 0.75rem;">Phương Pháp Lõi</th>
              <th style="padding: 0.75rem;">Cảm Biến Yêu Cầu</th>
              <th style="padding: 0.75rem;">Ưu Điểm Nổi Bật</th>
              <th style="padding: 0.75rem;">Môi Trường Khuyên Dùng</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>SLAM Toolbox (Steve Macenski)</strong></td>
              <td style="padding: 0.75rem;">Karto Graph-based SLAM tối ưu đa luồng</td>
              <td style="padding: 0.75rem;">2D LiDAR + Odometry</td>
              <td style="padding: 0.75rem;">Hỗ trợ Lifelong Mapping cực mạnh, bản đồ rộng hàng ngàn m², chuẩn mặc định của Nav2 ROS 2</td>
              <td style="padding: 0.75rem;">Xe tự hành AMR nhà kho, nhà máy công nghiệp</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Google Cartographer</strong></td>
              <td style="padding: 0.75rem;">Submap Branch-and-Bound Scan Matching</td>
              <td style="padding: 0.75rem;">2D/3D LiDAR + IMU</td>
              <td style="padding: 0.75rem;">Độ chính xác rất cao, ghép nối submap thông minh</td>
              <td style="padding: 0.75rem;">Khảo sát trắc địa, xe tải tự hành ngoài trời</td>
            </tr>
            <tr>
              <td style="padding: 0.75rem;"><strong>RTAB-Map (Labbe et al.)</strong></td>
              <td style="padding: 0.75rem;">Memory Management Graph SLAM (STM / LTM)</td>
              <td style="padding: 0.75rem;">RGB-D / Stereo Camera + LiDAR</td>
              <td style="padding: 0.75rem;">Cơ chế quên bộ nhớ tránh tràn RAM khi chạy nhiều ngày liên tục</td>
              <td style="padding: 0.75rem;">Robot dịch vụ trong nhà, cánh tay robot di động</td>
            </tr>
          </tbody>
        </table>

        <!-- 14.2 -->
        <h2 id="sec-14-2">14.2 Thước Đo Chuẩn Học Thuật Quốc Tế: ATE RMSE & RPE</h2>
        <p>Để đánh giá bài báo khoa học hay sản phẩm thương mại có đạt chuẩn hay không, cộng đồng sử dụng 2 thước đo:</p>
        <div class="formula-hero">
          <div class="formula-title">Sai Số Quỹ Đạo Tuyệt Đối (Absolute Trajectory Error - ATE RMSE)</div>
          <div class="formula-math">
            $$\text{ATE}_{\text{RMSE}} = \sqrt{\frac{1}{N} \sum_{i=1}^N \| \text{trans}(\mathbf{Q}_i^{-1} \mathbf{S} \mathbf{P}_i) \|^2}$$
          </div>
          <div class="formula-legend">
            <strong>Ý nghĩa:</strong> Căn chỉnh toàn bộ quỹ đạo ước lượng $\mathbf{P}_{1:N}$ với quỹ đạo chân thực Ground Truth $\mathbf{Q}_{1:N}$ bằng thuật toán Umeyama $\mathbf{S} \in \mathrm{SE}(3)$, sau đó tính căn bậc hai trung bình bình phương sai số khoảng cách. Đo lường độ trôi dạt toàn cục (Global Drift).
          </div>
        </div>

        <p><strong>Sai số tư thế tương đối (Relative Pose Error - RPE):</strong> Đo lường sai số vận tốc trôi trên mỗi mét hoặc mỗi giây di chuyển (Local Drift per second/meter).</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-14-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Đánh Giá Sai Số Quỹ Đạo ATE RMSE So Với Ground Truth</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-14" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-14-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Toán ATE RMSE Giữa Quỹ Đạo Ước Lượng Và Ground Truth</h3>
          <p>Có 3 mốc vị trí 2D đo được sau khi căn chỉnh:
          <br>• Mốc 1: Ground Truth $Q_1 = [0.0, 0.0]$, Ước lượng $P_1 = [0.02, 0.01]$
          <br>• Mốc 2: Ground Truth $Q_2 = [2.0, 0.0]$, Ước lượng $P_2 = [2.05, -0.03]$
          <br>• Mốc 3: Ground Truth $Q_3 = [4.0, 1.0]$, Ước lượng $P_3 = [4.08, 0.94]$
          Tính vector sai số vị trí từng bước, bình phương khoảng cách, và tính chỉ số ATE RMSE.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính vector sai lệch vị trí $\mathbf{e}_i = P_i - Q_i$</h5>
              <p>• $\mathbf{e}_1 = [0.02 - 0, 0.01 - 0] = [0.02, 0.01]$ m</p>
              <p>• $\mathbf{e}_2 = [2.05 - 2.0, -0.03 - 0] = [0.05, -0.03]$ m</p>
              <p>• $\mathbf{e}_3 = [4.08 - 4.0, 0.94 - 1.0] = [0.08, -0.06]$ m</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính bình phương khoảng cách Euclid $\|\mathbf{e}_i\|^2 = e_{x,i}^2 + e_{y,i}^2$</h5>
              <p>• $\|\mathbf{e}_1\|^2 = (0.02)^2 + (0.01)^2 = 0.0004 + 0.0001 = 0.0005\text{ m}^2$</p>
              <p>• $\|\mathbf{e}_2\|^2 = (0.05)^2 + (-0.03)^2 = 0.0025 + 0.0009 = 0.0034\text{ m}^2$</p>
              <p>• $\|\mathbf{e}_3\|^2 = (0.08)^2 + (-0.06)^2 = 0.0064 + 0.0036 = 0.0100\text{ m}^2$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính trung bình cộng các sai số bình phương (Mean Squared Error - MSE)</h5>
              <p>$$\text{MSE} = \frac{0.0005 + 0.0034 + 0.0100}{3} = \frac{0.0139}{3} \approx 0.004633\text{ m}^2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Khai căn bậc hai để tìm ATE RMSE</h5>
              <p>$$\text{ATE}_{\text{RMSE}} = \sqrt{\text{MSE}} = \sqrt{0.004633} \approx 0.0681\text{ m} = 6.81\text{ cm}$$</p>
              <p>Sai số quỹ đạo toàn cục chỉ $6.81$ cm trên toàn bộ hành trình 4 mét, đạt chuẩn chất lượng xuất sắc theo tiêu chuẩn TUM/KITTI!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-14-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Tệp Cấu Hình Tham Số slam_toolbox_params.yaml Tối Ưu Cho AMR</h4>
          <p>Tệp cấu hình tối ưu hóa bộ nhớ cho hoạt động Lifelong Mapping trong nhà máy công nghiệp:</p>
          <div class="code-card">
            <div class="code-header">
              <span>slam_toolbox_params.yaml (ROS 2 Humble / Nav2)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>slam_toolbox:
  ros__parameters:
    # Chế độ chạy: synchronous (đảm bảo không rơi khung hình scan)
    solver_plugin: solver_plugins::CeresSolver
    ceres_linear_solver: SPARSE_NORMAL_CHOLESKY
    ceres_preconditioner: JACOBI
    
    # Khung tọa độ chuẩn ROS
    odom_frame: odom
    map_frame: map
    base_frame: base_link
    scan_topic: /scan
    mode: mapping # hoặc localization

    # Tần số xử lý & Khoảng cách cập nhật
    map_update_interval: 1.0
    minimum_travel_distance: 0.3 # Di chuyển ít nhất 30cm mới thêm node
    minimum_travel_heading: 0.2  # Hoặc quay ít nhất 0.2 rad
    
    # Tham số quét khớp tia Laser
    max_laser_range: 25.0
    resolution: 0.05 # 5cm / ô
    
    # Tham số đóng vòng lặp Loop Closure
    do_loop_closing: true
    loop_search_maximum_distance: 8.0
    loop_match_minimum_chain_size: 10
    loop_match_maximum_variance_coarse: 3.0
    loop_match_minimum_response_coarse: 0.35</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# Generate HTML files for Track 5 and Track 6
# ==============================================================================
print("Generating Ch 09...")
with open(os.path.join(CHAPTERS_DIR, "ch09.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("09", "Liên Kết Dữ Liệu Ngữ Nghĩa & Tối Ưu Vòng Lặp Ngữ Nghĩa", "Semantic Data Association, Hungarian Algorithm & Loop Closing", "TRACK 5: SLAM CHỦ ĐỘNG & RA QUYẾT ĐỊNH", "track-5", "ch08.html", "Chương 08: Bản Đồ Ngữ Nghĩa & Dual Quadrics", "ch10.html", "Chương 10: Khung Toán Học Active SLAM", ch09_sidebar, ch09_body))

print("Generating Ch 10...")
with open(os.path.join(CHAPTERS_DIR, "ch10.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("10", "Khung Toán Học Active SLAM & Không Gian Hành Động Ứng Viên", "Active SLAM 3-Stage Formulation & Frontier Exploration", "TRACK 5: SLAM CHỦ ĐỘNG & RA QUYẾT ĐỊNH", "track-5", "ch09.html", "Chương 09: Liên Kết Dữ Liệu Ngữ Nghĩa", "ch11.html", "Chương 11: Đo Lường Thông Tin Toán Học TOED", ch10_sidebar, ch10_body))

print("Generating Ch 11...")
with open(os.path.join(CHAPTERS_DIR, "ch11.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("11", "Đo Lường Thông Tin Toán Học: Entropy, Mutual Info & Tiêu Chuẩn TOED", "Shannon Entropy, Mutual Information & TOED Criteria (A/D/E-opt)", "TRACK 5: SLAM CHỦ ĐỘNG & RA QUYẾT ĐỊNH", "track-5", "ch10.html", "Chương 10: Khung Toán Học Active SLAM", "ch12.html", "Chương 12: Song Đề Khám Phá vs Khai Thác BSP", ch11_sidebar, ch11_body))

print("Generating Ch 12...")
with open(os.path.join(CHAPTERS_DIR, "ch12.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("12", "Song Đề Khám Phá vs Khai Thác & Lập Kế Hoạch Không Gian Niềm Tin (BSP)", "Exploration vs Exploitation Dilemma & Belief-Space Planning", "TRACK 5: SLAM CHỦ ĐỘNG & RA QUYẾT ĐỊNH", "track-5", "ch11.html", "Chương 11: Đo Lường Thông Tin Toán Học TOED", "ch13.html", "Chương 13: Đa Robot SLAM & Hợp Nhất Bản Đồ", ch12_sidebar, ch12_body))

print("Generating Ch 13...")
with open(os.path.join(CHAPTERS_DIR, "ch13.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("13", "Đa Robot SLAM: Phân Tán, Hợp Nhất Bản Đồ & Active Exploration", "Distributed Multi-Robot SLAM, Map Stitching & Collaborative Exploration", "TRACK 6: ĐA ROBOT & TRIỂN KHAI SẢN XUẤT", "track-6", "ch12.html", "Chương 12: Song Đề Khám Phá vs Khai Thác BSP", "ch14.html", "Chương 14: Kiến Trúc Triển Khai Thực Tế Nav2", ch13_sidebar, ch13_body))

print("Generating Ch 14...")
with open(os.path.join(CHAPTERS_DIR, "ch14.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("14", "Kiến Trúc Triển Khai Thực Tế: ROS 2 Humble, Nav2, SLAM Toolbox & Benchmarks", "Production SLAM Toolbox, Nav2 Lifelong Mapping & ATE/RPE Benchmarks", "TRACK 6: ĐA ROBOT & TRIỂN KHAI SẢN XUẤT", "track-6", "ch13.html", "Chương 13: Đa Robot SLAM & Hợp Nhất Bản Đồ", "../index.html", "Lộ trình Tổng quan", ch14_sidebar, ch14_body))

print("Successfully generated Chapters 09, 10, 11, 12, 13, 14 for SLAM Portal!")
