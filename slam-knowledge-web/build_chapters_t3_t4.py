# -*- coding: utf-8 -*-
"""
build_chapters_t3_t4.py
Biên soạn nội dung chuẩn 6 tầng tri thức cho Track 3 và Track 4 (Chương 05 - Chương 08):
- Ch 05: Đồ Thị Tư Thế (Pose Graph Optimization) & Factor Graphs (GTSAM)
- Ch 06: Visual Odometry Hình Học: Trích Xuất Đặc Trưng & Hình Học Epipolar
- Ch 07: Trích Xuất Ngữ Nghĩa & Lọc Môi Trường Động (Dynamic Masking)
- Ch 08: Bản Đồ Ngữ Nghĩa: Điểm, Mặt Phẳng, Dual Quadrics & NeRF/3DGS
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
            <span>📚 Nguồn tài liệu: <strong>Thanh Nguyen Canh et al. (IEEE 2021) & Timothy Barfoot (2024)</strong></span>
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
# CHƯƠNG 05: Đồ Thị Tư Thế & Tối Ưu Hóa Phi Tuyến (Pose Graph SLAM)
# ==============================================================================
ch05_sidebar = [
    {"id": "sec-5-1", "title": "5.1 Bước Chuyển Từ Lọc (Filter) Sang Đồ Thị (Graph)"},
    {"id": "sec-5-2", "title": "5.2 Biểu Diễn Nhóm Lie SE(2) / SE(3) & Hàm Sai Số"},
    {"id": "sec-5-3", "title": "5.3 Tối Ưu Hóa Gauss-Newton & Levenberg-Marquardt"},
    {"id": "sec-5-4", "title": "5.4 Khung Thừa Số Factor Graphs & GTSAM / g2o"},
    {"id": "sec-5-sim", "title": "⚡ Mô Phỏng Đóng Vòng Lặp Pose Graph (Canvas)"},
    {"id": "sec-5-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Giải Hệ Chuẩn H Δx = b"},
    {"id": "sec-5-bridge", "title": "🛠️ Cầu Nối Python: Tối Ưu Hóa Factor Graph Bằng GTSAM"}
]

ch05_body = r"""
        <!-- 5.1 -->
        <h2 id="sec-5-1">5.1 Bước Chuyển Mình Lịch Sử: Từ Lọc Trạng Thái Sang Tối Ưu Hóa Đồ Thị</h2>
        <p>Trong nhiều thập kỷ, SLAM bị thống trị bởi các bộ lọc xác suất (EKF-SLAM). Tuy nhiên, EKF-SLAM mang hai điểm nghẽn trí mạng:</p>
        <ul>
          <li><strong>Độ phức tạp bậc hai:</strong> Ma trận hiệp phương sai kích thước $(3 + 2M) \times (3 + 2M)$ cập nhật tốn chi phí $O(M^2)$, sụp đổ khi bản đồ có hàng vạn mốc.</li>
          <li><strong>Tuyến tính hóa sớm (Inconsistency / Early Linearization):</strong> Tuyến tính hóa Taylor tại một điểm sai lệch sẽ vĩnh viễn làm hỏng ma trận thông tin mà không thể sửa lại được.</li>
        </ul>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 GRAPH-BASED SLAM (ĐỒ THỊ YẾU TỐ) ĐỂ LÀM GÌ?</div>
          <div class="why-matters-body">
            Graph-based SLAM (khởi xướng bởi Lu & Milios, hoàn thiện bởi Dellaert, Kaess, Grisetti) mô hình hóa toàn bộ lịch sử tư thế của robot thành các đỉnh (Nodes) trong đồ thị, và các ràng buộc đo đạc (Odometry, Laser scan matching, Loop closure) thành các cạnh (Edges / Factors). 
            <br>Nhờ <strong>cấu trúc ma trận thưa thông tin (Sparse Information Matrix)</strong>, thuật toán có thể tối ưu hóa hàng triệu node trong vài mili-giây và có thể tái tuyến tính hóa lặp lại nhiều lần, triệt tiêu hoàn toàn sai số trôi dạt khi phát hiện vòng lặp đóng (Loop Closure)!
          </div>
        </div>

        <!-- 5.2 -->
        <h2 id="sec-5-2">5.2 Biểu Diễn Nhóm Lie $\mathrm{SE}(2)$ / $\mathrm{SE}(3)$ & Hàm Sai Số Cạnh Đồ Thị</h2>
        <p>Mỗi tư thế robot tại thời điểm $i$ là một phần tử thuộc nhóm biến đổi hình học đặc biệt $\mathbf{T}_i \in \mathrm{SE}(2)$ hoặc $\mathrm{SE}(3)$. Giữa hai tư thế $i$ và $j$, cảm biến đo được phép dời tương đối $\mathbf{z}_{ij}$. Sai số liên kết được định nghĩa trên đại số Lie:</p>
        <div class="formula-hero">
          <div class="formula-title">Hàm Mục Tiêu Tối Thiểu Hóa Sai Số Toàn Cục</div>
          <div class="formula-math">
            $$\mathbf{x}^* = \arg\min_{\mathbf{x}} \sum_{\langle i, j \rangle \in \mathcal{E}} \| \mathbf{e}_{ij}(\mathbf{x}_i, \mathbf{x}_j) \|_{\mathbf{\Omega}_{ij}}^2$$
          </div>
          <div class="formula-legend">
            <strong>Trong đó:</strong>
            <br>• $\mathbf{e}_{ij} = \log\left( \mathbf{z}_{ij}^{-1} (\mathbf{T}_i^{-1} \mathbf{T}_j) \right) \in \mathfrak{se}(2)$: Vector sai số lệch giữa phép đo danh định và khoảng cách giữa 2 đỉnh đồ thị.
            <br>• $\mathbf{\Omega}_{ij} = \mathbf{\Sigma}_{ij}^{-1}$: Ma trận thông tin trọng số (nghịch đảo ma trận hiệp phương sai sai số đo).
          </div>
        </div>

        <!-- 5.3 -->
        <h2 id="sec-5-3">5.3 Tối Ưu Hóa Gauss-Newton & Levenberg-Marquardt</h2>
        <p>Tuyến tính hóa hàm sai số quanh điểm ước lượng hiện tại $\mathbf{e}_{ij}(\mathbf{x} + \Delta\mathbf{x}) \approx \mathbf{e}_{ij} + \mathbf{J}_{ij} \Delta\mathbf{x}$. Đạo hàm hàm mục tiêu dẫn tới <strong>Hệ Phương Trình Chuẩn (Normal Equations)</strong>:</p>
        $$\mathbf{H} \Delta\mathbf{x} = -\mathbf{b}$$
        $$\mathbf{H} = \sum_{\langle i, j \rangle} \mathbf{J}_{ij}^T \mathbf{\Omega}_{ij} \mathbf{J}_{ij}, \quad \mathbf{b} = \sum_{\langle i, j \rangle} \mathbf{J}_{ij}^T \mathbf{\Omega}_{ij} \mathbf{e}_{ij}$$
        <p>Thuật toán <strong>Levenberg-Marquardt</strong> bổ sung hệ số cản $\lambda$ giúp bước nhảy luôn hội tụ an toàn: $(\mathbf{H} + \lambda \mathbf{I}) \Delta\mathbf{x} = -\mathbf{b}$.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-5-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Nắn Thẳng Đồ Thị Pose Graph Khi Đóng Vòng Lặp (Loop Closure)</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-05" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <button id="sim05-relax-btn" style="padding: 0.5rem 1rem; background: #10b981; color: #fff; font-weight: bold; border: none; border-radius: 6px; cursor: pointer;">🔄 Kích Hoạt Tối Ưu Hóa Gauss-Newton (Nắn Thẳng Đồ Thị)</button>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-5-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Thiết Lập Ma Trận Thông Tin $\mathbf{H}$ & Tính Bước Nhảy $\Delta x$ Cho Đồ Thị 1D</h3>
          <p>Xét robot chuyển động trên trục $x$ với 3 tư thế $x_0, x_1, x_2$. Đỉnh xuất phát ghim chặt tại gốc $x_0 = 0$ (Anchor). Các phép đo odometry: $d_{01} = 2.0$ m, $d_{12} = 2.0$ m. Cảm biến phát hiện vòng lặp giữa $x_2$ và $x_0$: $d_{20} = -3.8$ m (lẽ ra phải là $-4.0$ m). Tất cả các cạnh đều có ma trận thông tin $\Omega = 1.0$. Tư thế ban đầu: $x_0 = 0, x_1 = 2.0, x_2 = 4.0$. Thiết lập hệ phương trình $\mathbf{H} \Delta\mathbf{x} = -\mathbf{b}$ cho hai biến tự do $\Delta x_1, \Delta x_2$ và giải nghiệm.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính toán sai số các cạnh $e = (x_j - x_i) - d_{ij}$</h5>
              <p>• Cạnh 1 ($0 \to 1$): $e_{01} = (x_1 - x_0) - 2.0 = (2.0 - 0) - 2.0 = 0.0$</p>
              <p>• Cạnh 2 ($1 \to 2$): $e_{12} = (x_2 - x_1) - 2.0 = (4.0 - 2.0) - 2.0 = 0.0$</p>
              <p>• Cạnh 3 (Loop $2 \to 0$): $e_{20} = (x_0 - x_2) - (-3.8) = (0 - 4.0) + 3.8 = -0.2$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Xác định ma trận Jacobian của các cạnh theo biến $[\Delta x_1, \Delta x_2]^T$</h5>
              <p>• $\mathbf{J}_{01} = [1, 0]$</p>
              <p>• $\mathbf{J}_{12} = [-1, 1]$</p>
              <p>• $\mathbf{J}_{20} = [0, -1]$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Lập ma trận thông tin $\mathbf{H}$ và vector $\mathbf{b}$</h5>
              <p>$$\mathbf{H} = \mathbf{J}_{01}^T \mathbf{J}_{01} + \mathbf{J}_{12}^T \mathbf{J}_{12} + \mathbf{J}_{20}^T \mathbf{J}_{20} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$$</p>
              <p>Vector $\mathbf{b} = \sum \mathbf{J}^T \Omega e = \begin{bmatrix} 0 \\ -1 \end{bmatrix} (1.0) (-0.2) = \begin{bmatrix} 0 \\ +0.2 \end{bmatrix}$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Giải hệ phương trình $\mathbf{H} \Delta\mathbf{x} = -\mathbf{b}$ & Cập nhật</h5>
              <p>Nghịch đảo ma trận $2 \times 2$: $\det(\mathbf{H}) = 4 - 1 = 3 \Rightarrow \mathbf{H}^{-1} = \frac{1}{3} \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$</p>
              <p>$$\begin{bmatrix} \Delta x_1 \\ \Delta x_2 \end{bmatrix} = -\frac{1}{3} \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 0 \\ 0.2 \end{bmatrix} = \begin{bmatrix} -0.0667 \\ -0.1333 \end{bmatrix}$$</p>
              <p>Tư thế sau nắn chỉnh: $x_1 = 1.933$ m, $x_2 = 3.867$ m. Toàn bộ sai số vòng lặp $-0.2$ m được phân bổ phân tán đều dọc theo chuỗi cạnh!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-5-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Tối Ưu Hóa Factor Graph Bằng Thư Viện GTSAM (Python)</h4>
          <p>Mã nguồn chuẩn sử dụng GTSAM giải bài toán Pose Graph với thừa số `BetweenFactor` và bộ tối ưu `LevenbergMarquardtOptimizer`:</p>
          <div class="code-card">
            <div class="code-header">
              <span>pose_graph_gtsam.py (GTSAM / Python)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import gtsam
import numpy as np

def run_pose_graph():
    graph = gtsam.NonlinearFactorGraph()
    initial_estimate = gtsam.Values()
    
    # 1. Ghim đỉnh khởi đầu x0
    prior_noise = gtsam.noiseModel.Diagonal.Sigmas(np.array([0.1, 0.1, 0.05]))
    graph.add(gtsam.PriorFactorPose2(0, gtsam.Pose2(0.0, 0.0, 0.0), prior_noise))
    initial_estimate.insert(0, gtsam.Pose2(0.0, 0.0, 0.0))
    
    # 2. Thêm các cạnh Odometry
    odom_noise = gtsam.noiseModel.Diagonal.Sigmas(np.array([0.2, 0.2, 0.1]))
    graph.add(gtsam.BetweenFactorPose2(0, 1, gtsam.Pose2(2.0, 0.0, 0.0), odom_noise))
    initial_estimate.insert(1, gtsam.Pose2(2.1, 0.05, 0.02))
    
    graph.add(gtsam.BetweenFactorPose2(1, 2, gtsam.Pose2(0.0, 2.0, np.pi/2), odom_noise))
    initial_estimate.insert(2, gtsam.Pose2(2.05, 2.1, np.pi/2 + 0.03))
    
    # 3. Thêm cạnh đóng vòng lặp Loop Closure
    loop_noise = gtsam.noiseModel.Diagonal.Sigmas(np.array([0.15, 0.15, 0.08]))
    graph.add(gtsam.BetweenFactorPose2(2, 0, gtsam.Pose2(-2.0, -2.0, -np.pi/2), loop_noise))
    
    # 4. Tối ưu hóa Levenberg-Marquardt
    params = gtsam.LevenbergMarquardtParams()
    optimizer = gtsam.LevenbergMarquardtOptimizer(graph, initial_estimate, params)
    result = optimizer.optimize()
    print("Optimization converged. Pose 2:", result.atPose2(2))

if __name__ == '__main__':
    run_pose_graph()</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 06: Visual Odometry Hình Học: Trích Xuất Đặc Trưng & Hình Học Epipolar
# ==============================================================================
ch06_sidebar = [
    {"id": "sec-6-1", "title": "6.1 Feature-Based (ORB-SLAM) vs Direct Methods (DSO)"},
    {"id": "sec-6-2", "title": "6.2 Hình Học Epipolar: Ma Trận Thiết Yếu E = [t]x R"},
    {"id": "sec-6-3", "title": "6.3 Giải PnP & Tam Giác Hóa 3D (Triangulation)"},
    {"id": "sec-6-4", "title": "6.4 Bundle Adjustment & DBoW2 Loop Closing"},
    {"id": "sec-6-sim", "title": "⚡ Mô Phỏng Tam Giác Hóa Epipolar 3D (Canvas)"},
    {"id": "sec-6-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Ma Trận Thiết Yếu E"},
    {"id": "sec-6-bridge", "title": "🛠️ Cầu Nối C++: Node Visual Odometry OpenCV & ROS 2"}
]

ch06_body = r"""
        <!-- 6.1 -->
        <h2 id="sec-6-1">6.1 Bức Tranh Toàn Cảnh: Feature-Based (ORB-SLAM) vs Direct Methods (DSO)</h2>
        <p>Thị giác máy tính trong SLAM được phân nhánh thành 2 trường phái lớn:</p>
        <table class="academic-table" style="width:100%; margin: 1.5rem 0; border-collapse: collapse;">
          <thead>
            <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
              <th style="padding: 0.75rem;">Đặc Tính Kỹ Thuật</th>
              <th style="padding: 0.75rem;">Phương Pháp Đặc Trưng (Feature-Based)</th>
              <th style="padding: 0.75rem;">Phương Pháp Trực Tiếp (Direct Methods)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Hệ thống tiêu biểu</strong></td>
              <td style="padding: 0.75rem;">ORB-SLAM2/3, PTAM</td>
              <td style="padding: 0.75rem;">DSO (Direct Sparse Odometry), LSD-SLAM, SVO</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Hàm mất mát tối ưu</strong></td>
              <td style="padding: 0.75rem;">Sai số chiếu lại hình học (Geometric reprojection error)</td>
              <td style="padding: 0.75rem;">Sai số trắc quang cường độ sáng (Photometric error)</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Độ bền vững với ngoại cảnh</strong></td>
              <td style="padding: 0.75rem;">Bất biến với thay đổi ánh sáng mạnh; thất bại ở tường trắng trơn</td>
              <td style="padding: 0.75rem;">Hoạt động tốt ở vùng ít vân bề mặt; nhạy cảm với phơi sáng tự động</td>
            </tr>
          </tbody>
        </table>

        <!-- 6.2 -->
        <h2 id="sec-6-2">6.2 Hình Học Epipolar Giữa Hai Khung Nhìn (Two-View Epipolar Geometry)</h2>
        <p>Cho hai camera quan sát cùng một điểm 3D $\mathbf{X}$ trong không gian. Tia chiếu từ tâm quang học $C_1$ qua điểm ảnh $\mathbf{x}_1$ và tia chiếu từ $C_2$ qua $\mathbf{x}_2$ cùng nằm trên một mặt phẳng gọi là <strong>Mặt phẳng Epipolar</strong>.</p>
        <div class="formula-hero">
          <div class="formula-title">Ràng Buộc Đại Số Epipolar Cơ Bản</div>
          <div class="formula-math">
            $$\mathbf{x}_2^T \mathbf{K}^{-T} \mathbf{E} \mathbf{K}^{-1} \mathbf{x}_1 = 0, \quad \text{với } \mathbf{E} = [\mathbf{t}]_\times \mathbf{R}$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách thành phần:</strong>
            <br>• $\mathbf{K}$: Ma trận thông số nội tại camera (Camera Intrinsic Matrix: tiêu cự $f_x, f_y$, tâm quang học $c_x, c_y$).
            <br>• $\mathbf{E}$: Ma trận thiết yếu (Essential Matrix) mã hóa phép quay $\mathbf{R} \in \mathrm{SO}(3)$ và tịnh tiến $\mathbf{t} \in \mathbb{R}^3$ giữa hai camera.
            <br>• $[\mathbf{t}]_\times$: Ma trận phản đối xứng (Skew-symmetric matrix) của vector $\mathbf{t}$.
          </div>
        </div>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-6-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Tia Chiếu Epipolar & Tam Giác Hóa Điểm 3D (Triangulation)</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-06" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-6-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Thiết Lập Ma Trận Essential $\mathbf{E} = [\mathbf{t}]_\times \mathbf{R}$ & Kiểm Tra Ràng Buộc Epipolar</h3>
          <p>Camera 2 dịch chuyển tịnh tiến thuần túy theo trục hoành so với Camera 1 một khoảng $t_x = 0.2$ m ($\mathbf{t} = [0.2, 0, 0]^T$), không có góc xoay ($\mathbf{R} = \mathbf{I}_{3 \times 3}$). Tọa độ chuẩn hóa của một điểm trên ảnh 1 là $\mathbf{x}_1 = [0.1, 0.2, 1.0]^T$, trên ảnh 2 là $\mathbf{x}_2 = [0.0, 0.2, 1.0]^T$ (có độ chênh lệch thị sai $d = 0.1$). Tính ma trận phản đối xứng $[\mathbf{t}]_\times$, ma trận Essential $\mathbf{E}$, và kiểm tra xem ràng buộc $\mathbf{x}_2^T \mathbf{E} \mathbf{x}_1$ có bằng $0$ không.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính ma trận phản đối xứng $[\mathbf{t}]_\times$</h5>
              <p>$$[\mathbf{t}]_\times = \begin{bmatrix} 0 & -t_z & t_y \\ t_z & 0 & -t_x \\ -t_y & t_x & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & -0.2 \\ 0 & 0.2 & 0 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính ma trận Essential $\mathbf{E} = [\mathbf{t}]_\times \mathbf{R}$</h5>
              <p>Do $\mathbf{R} = \mathbf{I}$, ta có: $$\mathbf{E} = [\mathbf{t}]_\times = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & -0.2 \\ 0 & 0.2 & 0 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Nhân ma trận với vector điểm $\mathbf{x}_1$ để tìm đường Epipolar $\mathbf{l}_2 = \mathbf{E} \mathbf{x}_1$</h5>
              <p>$$\mathbf{l}_2 = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & -0.2 \\ 0 & 0.2 & 0 \end{bmatrix} \begin{bmatrix} 0.1 \\ 0.2 \\ 1.0 \end{bmatrix} = \begin{bmatrix} 0 \\ -0.2 \times 1.0 \\ 0.2 \times 0.2 \end{bmatrix} = \begin{bmatrix} 0 \\ -0.2 \\ 0.04 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Kiểm tra điều kiện Epipolar $\mathbf{x}_2^T \mathbf{l}_2$</h5>
              <p>$$\mathbf{x}_2^T \mathbf{l}_2 = [0.0, 0.2, 1.0] \begin{bmatrix} 0 \\ -0.2 \\ 0.04 \end{bmatrix} = (0.0)(0) + (0.2)(-0.2) + (1.0)(0.04)$$</p>
              <p>$$= 0 - 0.04 + 0.04 = 0.0000$$</p>
              <p>Giá trị tích vô hướng bằng 0 tuyệt đối! Điều này chứng minh cặp điểm ảnh hoàn toàn tương thích với hình học Epipolar của hệ thống camera.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-6-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Pipeline Visual Odometry Đơn Giản Trong C++ (OpenCV & ROS 2)</h4>
          <p>Mã nguồn bắt cặp đặc trưng ORB và giải ma trận Essential ước lượng tư thế camera:</p>
          <div class="code-card">
            <div class="code-header">
              <span>visual_odometry_node.cpp (C++ / OpenCV)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>#include &lt;opencv2/opencv.hpp&gt;
#include &lt;opencv2/features2d.hpp&gt;
#include &lt;vector&gt;
#include &lt;iostream&gt;

void estimateMotion(const cv::Mat& img1, const cv::Mat& img2, const cv::Mat& K, cv::Mat& R, cv::Mat& t) {
    auto orb = cv::ORB::create(1000);
    std::vector&lt;cv::KeyPoint&gt; kp1, kp2;
    cv::Mat desc1, desc2;
    orb->detectAndCompute(img1, cv::noArray(), kp1, desc1);
    orb->detectAndCompute(img2, cv::noArray(), kp2, desc2);

    auto matcher = cv::BFMatcher::create(cv::NORM_HAMMING);
    std::vector&lt;cv::DMatch&gt; matches;
    matcher->match(desc1, desc2, matches);

    std::vector&lt;cv::Point2f&gt; pts1, pts2;
    for (auto& m : matches) {
        pts1.push_back(kp1[m.queryIdx].pt);
        pts2.push_back(kp2[m.trainIdx].pt);
    }

    // Tính ma trận Essential với RANSAC
    cv::Mat mask;
    cv::Mat E = cv::findEssentialMat(pts1, pts2, K, cv::RANSAC, 0.999, 1.0, mask);
    cv::recoverPose(E, pts1, pts2, K, R, t, mask);
    std::cout &lt;&lt; "Recovered Translation:\n" &lt;&lt; t &lt;&lt; std::endl;
}</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 07: Trích Xuất Ngữ Nghĩa & Lọc Môi Trường Động (Dynamic Masking)
# ==============================================================================
ch07_sidebar = [
    {"id": "sec-7-1", "title": "7.1 Thách Thức Môi Trường Động Trong SLAM"},
    {"id": "sec-7-2", "title": "7.2 Thị Giác Học Sâu: YOLO, Mask R-CNN & SAM"},
    {"id": "sec-7-3", "title": "7.3 Chiến Lược Lọc Mặt Nạ Động (Dynamic Masking)"},
    {"id": "sec-7-4", "title": "7.4 Tái Tạo Hậu Cảnh Tĩnh (Static Scene Inpainting)"},
    {"id": "sec-7-sim", "title": "⚡ Mô Phỏng Lọc Điểm Đặc Trưng Động (Canvas)"},
    {"id": "sec-7-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Kiểm Định Chi-Square"},
    {"id": "sec-7-bridge", "title": "🛠️ Cầu Nối ROS 2 / PyTorch: Node Lọc Mây Điểm YOLO"}
]

ch07_body = r"""
        <!-- 7.1 -->
        <h2 id="sec-7-1">7.1 Nỗi Đau Của SLAM Truyền Thống Trong Môi Trường Thực Tế</h2>
        <p>Hầu hết các hệ thống SLAM hình học (ORB-SLAM, DSO, Cartographer) đều mang một giả định ngầm: <strong>Thế giới là tĩnh (Static World Assumption)</strong>. Khi mang robot vào vận hành trong nhà hàng, sân bay, kho hàng:</p>
        <ul>
          <li>Con người đi lại, xe nâng di chuyển tạo ra hàng loạt điểm đặc trưng giả (Dynamic outliers).</li>
          <li>Khi robot bám đuôi một người đang đi bộ, thuật toán tưởng lầm là cả thế giới đang dịch chuyển, dẫn đến việc ước lượng tư thế camera bị kéo lê dạt hàng mét và bản đồ bị nhòe vỡ.</li>
        </ul>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 SLAM NGỮ NGHĨA (SEMANTIC SLAM) GIẢI QUYẾT BÀI TOÁN NHƯ THẾ NÀO?</div>
          <div class="why-matters-body">
            Theo khảo cứu toàn diện của Thanh Nguyen Canh et al. (IEEE 2021), <strong>Semantic SLAM</strong> kết hợp mạng nơ-ron học sâu (YOLO, Segment Anything Model SAM) để nhận diện ngữ nghĩa từng đối tượng. Hệ thống phân loại tiên nghiệm các lớp vật thể động (`person`, `car`, `dog`) và kích hoạt cơ chế <strong>Dynamic Masking</strong>: Triệt tiêu toàn bộ các điểm ảnh nằm trong vùng động trước khi đưa vào bộ theo dõi tư thế, giúp Visual Odometry giữ vững độ chính xác tuyệt đối ngay giữa đám đông hỗn loạn!
          </div>
        </div>

        <!-- 7.2 -->
        <h2 id="sec-7-2">7.2 Chiến Lược Kết Hợp Nhất Quán Hình Học & Mặt Nạ Ngữ Nghĩa</h2>
        <p>Nếu chỉ dựa thuần túy vào nhãn ngữ nghĩa, một chiếc xe ô tô đang đậu đỗ cố định (Static car) cũng sẽ bị loại bỏ lãng phí. Thuật toán SOTA kết hợp kiểm định chéo hai tầng:</p>
        <p>1. <strong>Tầng Ngữ nghĩa (Semantic Prior):</strong> Phát hiện các vùng bounding box / segmentation mask thuộc lớp có khả năng di chuyển.</p>
        <p>2. <strong>Tầng Hình học (Geometric Verification):</strong> Tính khoảng cách hồi quy từ điểm ảnh tới đường Epipolar $\text{dist}(p, l_{\text{epipolar}})$. Nếu khoảng cách này vượt ngưỡng thống kê Chi-Square test $\chi_{1, \alpha}^2$, điểm đó được kết luận chắc chắn là điểm động và bị xóa sổ.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-7-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Lọc Mặt Nạ Động (Dynamic Masking) Bảo Vệ Điểm Đặc Trưng</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-07" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-7-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Kiểm Định Sai Số Epipolar Bằng Phân Phối Chi-Square</h3>
          <p>Một điểm đặc trưng được theo dõi từ ảnh 1 sang ảnh 2 có tọa độ chuẩn hóa $\mathbf{x}_2 = [0.15, 0.40, 1.0]^T$. Đường dóng Epipolar tính từ ma trận Fundamental là $\mathbf{l} = [a, b, c]^T = [1.2, -0.8, -0.1]^T$. Sai số đo pixel có độ lệch chuẩn $\sigma = 1.0$ pixel. Tính khoảng cách vuông góc từ điểm $\mathbf{x}_2$ tới đường $\mathbf{l}$, chuẩn hóa sai số Mahalanobis $d_M^2$, và đối chiếu với ngưỡng $\chi_{1, 0.05}^2 = 3.841$ để quyết định xem điểm này là Tĩnh hay Động.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính tử số khoảng cách đại số $|\mathbf{x}_2^T \mathbf{l}|$</h5>
              <p>$$\text{res} = (0.15)(1.2) + (0.40)(-0.8) + (1.0)(-0.1) = 0.18 - 0.32 - 0.10 = -0.24$$</p>
              <p>Độ lớn tử số: $|-0.24| = 0.24$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính mẫu số chuẩn hóa gradient $\sqrt{a^2 + b^2}$</h5>
              <p>$$\sqrt{a^2 + b^2} = \sqrt{(1.2)^2 + (-0.8)^2} = \sqrt{1.44 + 0.64} = \sqrt{2.08} \approx 1.4422$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính khoảng cách hình học và khoảng cách Mahalanobis $d_M^2$</h5>
              <p>Khoảng cách hình học: $d = \frac{0.24}{1.4422} \approx 0.1664$</p>
              <p>Phương sai sai số $\sigma^2 = 0.005$ trong không gian chuẩn hóa:</p>
              <p>$$d_M^2 = \frac{d^2}{\sigma^2} = \frac{(0.1664)^2}{0.005} = \frac{0.02769}{0.005} \approx 5.538$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Kiểm định thống kê giả thuyết Chi-Square</h5>
              <p>So sánh: $d_M^2 = 5.538 \gt \chi_{1, 0.05}^2 = 3.841$.</p>
              <p>Kết luận: Điểm ảnh vi phạm nghiêm trọng ràng buộc Epipolar với độ tin cậy $95\%$. Hệ thống kết luận đây là <strong>Điểm Chuyển Động (Dynamic Outlier)</strong> và kích hoạt loại bỏ khỏi danh sách tracking!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-7-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Node ROS 2 Python Lọc Mặt Nạ Động Bằng YOLOv8</h4>
          <p>Mã nguồn chuẩn nhận luồng ảnh RGB, chạy suy luận YOLOv8 để tạo nhãn mặt nạ động và xuất bản ảnh tĩnh:</p>
          <div class="code-card">
            <div class="code-header">
              <span>yolo_dynamic_filter_node.py (PyTorch / ROS 2)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
import cv2

class DynamicFilterNode(Node):
    def __init__(self):
        super().__init__('yolo_dynamic_filter_node')
        self.model = YOLO('yolov8n-seg.pt') # Mạng phân vùng đối tượng
        self.bridge = CvBridge()
        self.sub_img = self.create_subscription(Image, '/camera/image_raw', self.image_cb, 1)
        self.pub_mask = self.create_publisher(Image, '/camera/static_image', 1)
        self.dynamic_classes = [0, 1, 2, 3, 5, 7] # person, bicycle, car, motorcycle, bus, truck

    def image_cb(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        results = self.model(frame, verbose=False)[0]
        
        # Tạo mặt nạ nhị phân cho các vùng động
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        if results.masks is not None:
            for cls, seg in zip(results.boxes.cls, results.masks.xy):
                if int(cls) in self.dynamic_classes:
                    cv2.fillPoly(mask, [seg.astype(np.int32)], 255)
                    
        # Xóa các vùng động trên ảnh bằng màu đen
        frame[mask == 255] = 0
        out_msg = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
        self.pub_mask.publish(out_msg)</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 08: Bản Đồ Ngữ Nghĩa: Điểm, Mặt Phẳng, Dual Quadrics & NeRF/3DGS
# ==============================================================================
ch08_sidebar = [
    {"id": "sec-8-1", "title": "8.1 Các Cấp Độ Biểu Diễn Bản Đồ Ngữ Nghĩa"},
    {"id": "sec-8-2", "title": "8.2 Biểu Diễn Vật Thể Dạng Dual Quadrics Q*"},
    {"id": "sec-8-3", "title": "8.3 Phép Chiếu Đối Ngẫu Conic 2D: C* ~ P Q* P^T"},
    {"id": "sec-8-4", "title": "8.4 Trường Bức Xạ Thần Kinh NeRF & 3D Gaussian Splatting"},
    {"id": "sec-8-sim", "title": "⚡ Mô Phỏng Chiếu Khối Dual Quadric (Canvas)"},
    {"id": "sec-8-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Chiếu Quadric Ra Conic 2D"},
    {"id": "sec-8-bridge", "title": "🛠️ Cầu Nối GTSAM: Định Nghĩa Quadric Factor Bằng Python"}
]

ch08_body = r"""
        <!-- 8.1 -->
        <h2 id="sec-8-1">8.1 Các Cấp Độ Biểu Diễn Bản Đồ Trong SLAM Hiện Đại</h2>
        <p>Bản đồ robot học đã trải qua cuộc cách mạng sâu sắc về hình thức biểu diễn:</p>
        <p>1. <strong>Đám mây điểm thưa (Sparse Point Cloud):</strong> ORB-SLAM chỉ lưu các điểm góc cạnh. Tiết kiệm bộ nhớ nhưng không thể dùng cho tính toán va chạm hay tương tác bàn tay robot.</p>
        <p>2. <strong>Bề mặt tam giác / Mặt lồi (Surfels / TSDF Mesh):</strong> ElasticFusion, Voxblox tái tạo mô hình 3D liên tục, cho phép lập kế hoạch tránh vật cản.</p>
        <p>3. <strong>Bản đồ Cấp độ Đối tượng (Object-Level SLAM):</strong> Thay vì lưu hàng triệu điểm, mỗi đồ vật trong phòng (bàn, ghế, tủ) được mô hình hóa thành một thực thể hình học khép kín duy nhất.</p>

        <!-- 8.2 -->
        <h2 id="sec-8-2">8.2 Biểu Diễn Hình Học Vật Thể Bằng Dual Quadrics $\mathbf{Q}^* \in \mathbb{R}^{4 \times 4}$</h2>
        <p>Một khối hình elip 3D (Ellipsoid) bất kỳ với tâm $\mathbf{t} = [t_x, t_y, t_z]^T$, bán trục bán kính $\mathbf{s} = [s_x, s_y, s_z]^T$, và góc xoay $\mathbf{R}$ được biểu diễn cô đọng bằng một ma trận đối ngẫu cấp 4 đối xứng:</p>
        <div class="formula-hero">
          <div class="formula-title">Định Nghĩa Ma Trận Dual Quadric $\mathbf{Q}^*$</div>
          <div class="formula-math">
            $$\mathbf{Q}^* = \mathbf{Z} \begin{bmatrix} s_x^2 & 0 & 0 & 0 \\ 0 & s_y^2 & 0 & 0 \\ 0 & 0 & s_z^2 & 0 \\ 0 & 0 & 0 & -1 \end{bmatrix} \mathbf{Z}^T, \quad \text{với } \mathbf{Z} = \begin{bmatrix} \mathbf{R} & \mathbf{t} \\ \mathbf{0}^T & 1 \end{bmatrix}$$
          </div>
          <div class="formula-legend">
            <strong>Tính chất tuyệt mỹ:</strong> Khi camera có ma trận phép chiếu $\mathbf{P} = \mathbf{K} [\mathbf{R}_{cw} \mid \mathbf{t}_{cw}] \in \mathbb{R}^{3 \times 4}$ quan sát khối elip 3D này, đường viền bao hình của elip trên ảnh 2D sẽ là một đường <strong>Conic đối ngẫu $\mathbf{C}^* \in \mathbb{R}^{3 \times 3}$</strong> thỏa mãn hệ thức ma trận đóng kín:
            $$\mathbf{C}^* \sim \mathbf{P} \mathbf{Q}^* \mathbf{P}^T$$
          </div>
        </div>

        <!-- 8.3 -->
        <h2 id="sec-8-3">8.3 Kỷ Nguyên Trường Bức Xạ Thần Kinh & 3D Gaussian Splatting (3DGS-SLAM)</h2>
        <p>Giai đoạn 2023 - 2024 mở ra thời kỳ cực thịnh của biểu diễn liên tục:</p>
        <ul>
          <li><strong>NeRF-SLAM (NICE-SLAM, iMAP):</strong> Dùng mạng nơ-ron MLP để mã hóa hàm mật độ thể tích và màu sắc $F_\theta(x, y, z, \theta, \phi) = (\sigma, r, g, b)$. Cho phép kết xuất ảnh từ góc nhìn mới sắc nét nhưng tốc độ huấn luyện chậm.</li>
          <li><strong>3D Gaussian Splatting SLAM (3DGS):</strong> Biểu diễn cảnh vật bằng hàng triệu hạt Gauss 3D có thể chiếu phối cảnh vi phân thời gian thực trên GPU (tốc độ kết xuất $\gt 100$ FPS), mở ra tiềm năng photorealistic mapping cho robot tự hành.</li>
        </ul>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-8-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Chiếu Phối Cảnh Khối Elipsoid 3D Thành Đường Bao Conic 2D</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-08" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-8-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Ma Trận Conic $\mathbf{C}^* = \mathbf{P} \mathbf{Q}^* \mathbf{P}^T$ Trên Mặt Phẳng Ảnh</h3>
          <p>Camera chuẩn có tiêu cự $f = 1.0$, tâm $(0,0)$ đặt tại gốc tọa độ hướng theo trục $z$: $\mathbf{P} = [\mathbf{I}_{3 \times 3} \mid \mathbf{0}]$. Một vật thể Dual Quadric dạng hình cầu bán kính $r = 1.0$ đặt tại tâm $\mathbf{t} = [0, 0, 5.0]^T$:
          $$\mathbf{Q}^* = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 5 \\ 0 & 0 & 5 & 24 \end{bmatrix}$$
          (với phần tử $(4,4)$ là $t_z^2 - r^2 = 25 - 1 = 24$). Tính ma trận Conic đối ngẫu 2D $\mathbf{C}^* = \mathbf{P} \mathbf{Q}^* \mathbf{P}^T$ và bán kính đường tròn chiếu trên ảnh.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Thiết lập ma trận phép chiếu camera $\mathbf{P}$</h5>
              <p>$$\mathbf{P} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}$$</p>
              <p>Phép nhân $\mathbf{P} \mathbf{Q}^*$ tương đương với việc trích xuất 3 hàng đầu tiên của $\mathbf{Q}^*$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Thực hiện phép nhân ma trận $\mathbf{P} \mathbf{Q}^*$</h5>
              <p>$$\mathbf{A} = \mathbf{P} \mathbf{Q}^* = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 5 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Nhân tiếp với $\mathbf{P}^T$ để tìm ma trận Conic 2D $\mathbf{C}^*$</h5>
              <p>$$\mathbf{C}^* = \mathbf{A} \mathbf{P}^T = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 5 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Chuyển đổi sang phương trình đường tròn Conic chuẩn</h5>
              <p>Phương trình Conic đường bao: $\mathbf{x}^T (\mathbf{C}^*)^{-1} \mathbf{x} = 0 \Rightarrow x^2 + y^2 - r_{\text{proj}}^2 = 0$.</p>
              <p>Bán kính chiếu trên ảnh: $$r_{\text{proj}} = \frac{r}{\sqrt{d_z^2 - r^2}} = \frac{1}{\sqrt{25 - 1}} = \frac{1}{\sqrt{24}} \approx 0.2041$$</p>
              <p>Đường elipsoid 3D được chiếu hoàn hảo thành đường tròn 2D bán kính $0.204$ đơn vị ảnh, khớp chính xác với bounding box của mạng nhận diện đối tượng!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-8-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Khai Báo Quadric Landmark Factor Trong GTSAM</h4>
          <p>Đoạn mã Python định nghĩa thừa số ràng buộc giữa Bounding Box 2D và Dual Quadric 3D:</p>
          <div class="code-card">
            <div class="code-header">
              <span>quadric_slam_factor.py (GTSAM / Python)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import gtsam
import numpy as np

class BoundingBoxFactor:
    def __init__(self, pose_key, quadric_key, bbox_measured, calibration):
        # bbox_measured: [xmin, ymin, xmax, ymax]
        self.pose_key = pose_key
        self.quadric_key = quadric_key
        self.bbox = bbox_measured
        self.K = calibration

    def evaluate_error(self, pose, quadric):
        # Tính toán ma trận chiếu Conic C* = P Q* P^T
        P = self.K @ pose.matrix()[:3, :]
        C_star = P @ quadric.matrix() @ P.T
        
        # Trích xuất bounding box dự đoán từ Conic
        pred_xmin = (C_star[0, 2] - np.sqrt(C_star[0, 2]**2 - C_star[0, 0] * C_star[2, 2])) / C_star[2, 2]
        pred_ymin = (C_star[1, 2] - np.sqrt(C_star[1, 2]**2 - C_star[1, 1] * C_star[2, 2])) / C_star[2, 2]
        # Sai số giữa BBox quan sát và BBox dự đoán
        return np.array([self.bbox[0] - pred_xmin, self.bbox[1] - pred_ymin])</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# Generate HTML files for Track 3 and Track 4
# ==============================================================================
print("Generating Ch 05...")
with open(os.path.join(CHAPTERS_DIR, "ch05.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("05", "Đồ Thị Tư Thế & Tối Ưu Hóa Phi Tuyến (Pose Graph SLAM)", "Pose Graph Optimization, Lie Groups & Factor Graphs", "TRACK 3: SLAM HÌNH HỌC CỔ ĐIỂN & ĐỒ THỊ", "track-3", "ch04.html", "Chương 04: Bộ Lọc Hạt MCL & FastSLAM", "ch06.html", "Chương 06: Visual Odometry & Hình Học Epipolar", ch05_sidebar, ch05_body))

print("Generating Ch 06...")
with open(os.path.join(CHAPTERS_DIR, "ch06.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("06", "Visual Odometry Hình Học: Trích Xuất Đặc Trưng & Hình Học Epipolar", "Feature-Based VO, Essential Matrix & 3D Triangulation", "TRACK 3: SLAM HÌNH HỌC CỔ ĐIỂN & ĐỒ THỊ", "track-3", "ch05.html", "Chương 05: Pose Graph SLAM & GTSAM", "ch07.html", "Chương 07: Trích Xuất Ngữ Nghĩa & Lọc Môi Trường Động", ch06_sidebar, ch06_body))

print("Generating Ch 07...")
with open(os.path.join(CHAPTERS_DIR, "ch07.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("07", "Trích Xuất Ngữ Nghĩa & Lọc Môi Trường Động (Dynamic Masking)", "Deep Semantic Extraction, YOLO/SAM & Dynamic Outlier Rejection", "TRACK 4: SLAM NGỮ NGHĨA & BIỂU DIỄN HIỆN ĐẠI", "track-4", "ch06.html", "Chương 06: Visual Odometry & Epipolar", "ch08.html", "Chương 08: Bản Đồ Ngữ Nghĩa & Dual Quadrics", ch07_sidebar, ch07_body))

print("Generating Ch 08...")
with open(os.path.join(CHAPTERS_DIR, "ch08.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("08", "Bản Đồ Ngữ Nghĩa: Điểm, Mặt Phẳng, Dual Quadrics & NeRF/3DGS", "Object-Level SLAM, Dual Quadrics & Continuous Neural Fields", "TRACK 4: SLAM NGỮ NGHĨA & BIỂU DIỄN HIỆN ĐẠI", "track-4", "ch07.html", "Chương 07: Trích Xuất Ngữ Nghĩa & Dynamic Masking", "ch09.html", "Chương 09: Liên Kết Dữ Liệu Ngữ Nghĩa", ch08_sidebar, ch08_body))

print("Successfully generated Chapters 05, 06, 07, 08 for SLAM Portal!")
