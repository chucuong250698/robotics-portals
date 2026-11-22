# -*- coding: utf-8 -*-
"""
build_chapters_t3_t4.py
Biên soạn nội dung chuẩn 6 tầng tri thức cho Track 3 và Track 4 (Chương 05 - Chương 08):
- Ch 05: Động Tác Nguyên Mẫu Động Lực Học (DMPs) & ProMPs
- Ch 06: Diffusion Policy & Action Chunking Transformers
- Ch 07: Học Tăng Cường Nghịch Đảo (Inverse RL) & Maximum Entropy
- Ch 08: Học Bắt Chước Đối Nghịch GAIL & Khớp Phân Phối Chiếm Dụng
"""

import os

BASE_DIR = r"c:\Users\chucuong\OneDrive\Reading\imitation-learning-web"
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
  <title>Chương {ch_num_str}: {title} - Imitation Learning in Robotics</title>
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
            <span>📚 Nguồn tài liệu: <strong>Carlos Celemin et al. (FnT Robotics 2022) & Zare et al. (IEEE 2023)</strong></span>
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
        <p>Học Bắt Chước Trong Robot Học • Hệ Thống Chưng Cất Tri Thức SOTA</p>
        <p class="footer-meta">Biên soạn tự động theo chuẩn Deep Reading Distiller • Sẵn sàng chạy offline & GitHub Pages</p>
      </footer>
    </main>
  </div>

  <script src="../assets/js/app.js"></script>
  <script src="../assets/js/simulators.js"></script>
</body>
</html>"""
    return html

# ==============================================================================
# CHƯƠNG 05: Động Tác Nguyên Mẫu Động Lực Học (DMPs) & ProMPs
# ==============================================================================
ch05_sidebar = [
    {"id": "sec-5-1", "title": "5.1 Giới hạn Nội suy Điểm & Khái niệm DMPs"},
    {"id": "sec-5-2", "title": "5.2 Kiến trúc Hệ Chính Tắc & Hệ Biến Đổi Bậc 2"},
    {"id": "sec-5-3", "title": "5.3 Hàm Lực Phi Tuyến RBF & Tính Bất Biến Tỷ Lệ"},
    {"id": "sec-5-4", "title": "5.4 Mở rộng Probabilistic Movement Primitives (ProMPs)"},
    {"id": "sec-5-sim", "title": "⚡ Mô phỏng Co Giãn Quỹ Đạo DMPs (Canvas)"},
    {"id": "sec-5-worked", "title": "📐 Ví dụ Tính Số 4 Bước Cập Nhật Trọng Số w_i"},
    {"id": "sec-5-bridge", "title": "🛠️ Cầu nối ROS 2: Node Phát Sinh Quỹ Đạo DMPs"}
]

ch05_body = r"""
        <!-- 5.1 -->
        <h2 id="sec-5-1">5.1 Giới Hạn Của Nội Suy Rời Rạc & Sự Ra Đời Của DMPs</h2>
        <p>Trong các phương pháp truyền thống của robot học, quỹ đạo biểu diễn của con người thường được lưu trữ dưới dạng một chuỗi các tọa độ rời rạc $(x_t, y_t, z_t)$ kèm mốc thời gian $t$. Tuy nhiên, cách tiếp cận này bộc lộ những nhược điểm chí mạng:</p>
        <ul>
          <li><strong>Nhạy cảm với nhiễu thời gian:</strong> Nếu robot bị cản trở hoặc làm chậm, toàn bộ chuỗi điểm nội suy sẽ bị lệch pha.</li>
          <li><strong>Không có khả năng khái quát hóa không gian:</strong> Khi vị trí vật thể cần gắp dời sang tọa độ mới $(g' \neq g)$, quỹ đạo cũ hoàn toàn vô dụng và việc co dãn tuyến tính đơn giản sẽ làm biến dạng các đặc trưng vận động then chốt.</li>
          <li><strong>Không đảm bảo tính ổn định Lyapunov:</strong> Robot dễ rơi vào dao động mất ổn định ở cuối hành trình.</li>
        </ul>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 ĐỘNG TÁC NGUYÊN MẪU (DMPs) ĐỂ LÀM GÌ?</div>
          <div class="why-matters-body">
            Dynamic Movement Primitives (DMPs), được khởi xướng bởi Stefan Schaal và Auke Ijspeert, mô hình hóa chuyển động của robot như một hệ phương trình vi phân phi tuyến có điểm hút ổn định toàn cục (Globally Stable Attractor). DMPs cho phép robot:
            <br>1. <strong>Tự động co dãn theo không gian:</strong> Khi điểm đích $g$ dịch chuyển, quỹ đạo tự uốn nắn mượt mà tới đích mà không va chạm.
            <br>2. <strong>Tự động co dãn theo thời gian:</strong> Thay đổi tham số $\tau$ cho phép tăng giảm tốc độ thực hiện động tác mà vẫn giữ nguyên hình dáng cử động.
            <br>3. <strong>Bền vững với nhiễu ngoại lực:</strong> Nếu bị bàn tay người đẩy lệch, hệ thống tự động sinh lực phục hồi kéo robot quay trở lại quỹ đạo danh định.
          </div>
        </div>

        <!-- 5.2 -->
        <h2 id="sec-5-2">5.2 Kiến Trúc Hệ Thống: Hệ Chính Tắc (Canonical) & Hệ Biến Đổi (Transformation)</h2>
        <p>Kiến trúc toán học của DMPs được cấu thành từ hai hệ phương trình vi phân tương tác chặt chẽ:</p>

        <div class="formula-hero">
          <div class="formula-title">1. Hệ Chính Tắc (Canonical System)</div>
          <div class="formula-math">
            $$\tau \dot{s} = -\alpha_s s, \quad s(0) = 1$$
          </div>
          <div class="formula-legend">
            <strong>Ý nghĩa tham số:</strong>
            <br>• $s \in (0, 1]$: Biến pha thay thế cho thời gian $t$. Khi thời gian trôi qua, $s$ suy giảm đơn điệu từ $1$ về $0$ theo hàm mũ $s(t) = \exp(-\alpha_s t / \tau)$.
            <br>• $\alpha_s$: Hệ số suy giảm pha định trước.
            <br>• $\tau$: Tham số tỷ lệ thời gian (Time scaling factor). Tăng $\tau$ giúp động tác chuyển động chậm rãi hơn.
          </div>
        </div>

        <div class="formula-hero" style="margin-top: 1.5rem;">
          <div class="formula-title">2. Hệ Biến Đổi Bậc Hai (Transformation System)</div>
          <div class="formula-math">
            $$\tau^2 \ddot{y} = \alpha_y \left( \beta_y (g - y) - \tau \dot{y} \right) + f(s)$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách thành phần cơ học:</strong>
            <br>• $y, \dot{y}, \ddot{y}$: Vị trí, vận tốc và gia tốc góc khớp hoặc tọa độ không gian tác vụ.
            <br>• $g$: Điểm đích mục tiêu (Goal position).
            <br>• $\alpha_y, \beta_y$: Các hằng số lò xo - giảm chấn (thường chọn $\beta_y = \alpha_y / 4$ để hệ suy giảm tới hạn - Critically Damped, triệt tiêu hoàn toàn dao động vọt lố).
            <br>• $f(s)$: Hàm lực ép phi tuyến (Nonlinear forcing term) mã hóa hình dáng đặc trưng của quỹ đạo thị phạm.
          </div>
        </div>

        <!-- 5.3 -->
        <h2 id="sec-5-3">5.3 Biểu Diễn Hàm Lực Phi Tuyến RBF & Tính Bất Biến Tỷ Lệ Không Gian</h2>
        <p>Hàm lực ép $f(s)$ được biểu diễn bằng tổ hợp tuyến tính của $K$ hàm nhân cơ sở hướng tâm Gauss (Gaussian Radial Basis Functions - RBFs):</p>
        <div class="formula-hero">
          <div class="formula-title">Công Thức Hàm Lực Phi Tuyến $f(s)$</div>
          <div class="formula-math">
            $$f(s) = \frac{\sum_{i=1}^K \psi_i(s) w_i}{\sum_{i=1}^K \psi_i(s)} s (g - y_0)$$
          </div>
          <div class="formula-legend">
            <strong>Trong đó:</strong>
            <br>• $\psi_i(s) = \exp\left( -h_i (s - c_i)^2 \right)$: Hàm Gaussian thứ $i$ phân bố dọc theo pha suy giảm $s$, với tâm $c_i$ và độ rộng $h_i$.
            <br>• $w_i$: Trọng số học được từ quỹ đạo mẫu của chuyên gia.
            <br>• $s$: Nhân tố dập tắt lực ép khi về gần đích ($s \to 0 \Rightarrow f(s) \to 0$), đảm bảo hệ thống hồi tụ chính xác tuyệt đối về điểm đích $g$.
            <br>• $(g - y_0)$: Nhân tố tỷ lệ không gian giúp co dãn toàn bộ biên độ động tác khi khoảng cách giữa điểm xuất phát $y_0$ và đích $g$ thay đổi.
          </div>
        </div>

        <!-- 5.4 -->
        <h2 id="sec-5-4">5.4 Mở Rộng Sang Probabilistic Movement Primitives (ProMPs)</h2>
        <p>Mặc dù DMPs xuất sắc trong việc co dãn không gian - thời gian, nhưng lại là mô hình tất định (Deterministic) chỉ học từ duy nhất một quỹ đạo mẫu. Khi chuyên gia cung cấp nhiều quỹ đạo thị phạm với sự biến thiên tự nhiên, <strong>Probabilistic Movement Primitives (ProMPs)</strong> được phát triển nhằm nắm bắt phân phối xác suất của cử động:</p>
        $$y_t = \Phi_t w + \epsilon_y, \quad \epsilon_y \sim \mathcal{N}(0, \Sigma_y)$$
        $$p(w) = \mathcal{N}(\mu_w, \Sigma_w)$$
        <p>ProMPs cho phép thực hiện phép <em>Điều kiện hóa (Conditioning)</em> theo lý thuyết xác suất Bayes: khi robot bắt buộc phải đi qua một điểm chướng ngại hoặc điểm gắp tại thời điểm $t_1$, phân phối trọng số mới $p(w \mid y_{t_1})$ được cập nhật đóng kín (Closed-form) mà không làm mất đi dáng điệu tự nhiên của toàn bộ chuyển động.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-5-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Co Giãn Quỹ Đạo DMPs Khi Thay Đổi Đích $g$ & Thời Gian $\tau$</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-05" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Vị trí Đích Goal $g$: <input type="range" id="sim05-goal" min="40" max="220" step="5" value="100"> <span id="sim05-goal-val">Đích G = 100</span></label>
            <label style="font-size: 0.85rem; font-weight: 600;">Hệ số thời gian $\tau$: <input type="range" id="sim05-tau" min="0.5" max="3.0" step="0.1" value="1.0"> <span id="sim05-tau-val">Thời gian τ = 1.0x</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-5-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Học Trọng Số Lực Ép $w_i$ Bằng Hồi Quy Tuyến Tính Trọng Số (Weighted Ridge Regression)</h3>
          <p>Cho một quỹ đạo mẫu 1 bậc tự do có tọa độ xuất phát $y_0 = 0.0$ m, đích $g = 1.0$ m, thời gian thực hiện $T = 1.0$ s ($\tau = 1.0$). Tại thời điểm $t = 0.5$ s, pha $s = \exp(-3.0 \times 0.5) = 0.2231$. Vị trí, vận tốc, gia tốc đo được là $y = 0.65$ m, $\dot{y} = 1.2$ m/s, $\ddot{y} = -2.5$ m/s$^2$. Các thông số hệ biến đổi: $\alpha_y = 25.0, \beta_y = 6.25$. Có 2 hàm cơ sở tại pha này với hoạt độ $\psi_1 = 0.8$ và $\psi_2 = 0.2$. Tính giá trị lực ép mục tiêu $f_{\text{target}}$ và biểu thức hồi quy để giải trọng số $w_1, w_2$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính lực ép mục tiêu $f_{\text{target}}$ từ phương trình hệ biến đổi</h5>
              <p>Biến đổi phương trình DMP để tách riêng lực ép:</p>
              <p>$$f_{\text{target}} = \tau^2 \ddot{y} - \alpha_y (\beta_y (g - y) - \tau \dot{y})$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Thay số tính toán lực phục hồi đàn hồi</h5>
              <p>• Thành phần lò xo: $\beta_y (g - y) = 6.25 \times (1.0 - 0.65) = 6.25 \times 0.35 = 2.1875$</p>
              <p>• Thành phần cản: $\tau \dot{y} = 1.0 \times 1.2 = 1.2$</p>
              <p>• Hiệu lò xo - cản: $2.1875 - 1.2 = 0.9875$</p>
              <p>• Nhân với $\alpha_y$: $25.0 \times 0.9875 = 24.6875$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính lực ép phi tuyến $f_{\text{target}}$</h5>
              <p>$$f_{\text{target}} = (1.0)^2 \times (-2.5) - 24.6875 = -2.5 - 24.6875 = -27.1875\text{ N}$$</p>
              <p>Lực ép âm biểu thị quỹ đạo mẫu cần một lực hãm ngược lại lò xo để tạo đường cong vận động.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Thiết lập phương trình hồi quy trọng số</h5>
              <p>Ta có: $f(s) = \frac{\psi_1 w_1 + \psi_2 w_2}{\psi_1 + \psi_2} s (g - y_0) = f_{\text{target}}$</p>
              <p>$$\frac{0.8 w_1 + 0.2 w_2}{1.0} \times 0.2231 \times (1.0 - 0.0) = -27.1875$$</p>
              <p>$$0.8 w_1 + 0.2 w_2 = \frac{-27.1875}{0.2231} \approx -121.86$$</p>
              <p>Khi gom đủ các bước thời gian $t_1, \dots, t_M$, bài toán trở thành hệ phương trình chính tắc giải bằng bình phương tối thiểu có chính quy hóa (Ridge Regression): $\mathbf{w} = (\mathbf{\Psi}^T \mathbf{S}^2 \mathbf{\Psi} + \lambda \mathbf{I})^{-1} \mathbf{\Psi}^T \mathbf{S} \mathbf{f}_{\text{target}}$.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-5-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Bộ Phát Quỹ Đạo DMPs Trong ROS 2 C++ / Python</h4>
          <p>Triển khai phát xung quỹ đạo DMPs thời gian thực ở tần số 100 Hz truyền lệnh vị trí tới bộ điều khiển cánh tay robot:</p>
          <div class="code-card">
            <div class="code-header">
              <span>dmp_trajectory_node.py (ROS 2 / Python)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import numpy as np

class DMPControllerNode(Node):
    def __init__(self):
        super().__init__('dmp_trajectory_node')
        self.pub_traj = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)
        self.timer = self.create_timer(0.01, self.step_dmp) # Vòng lặp 100 Hz
        self.alpha_s = 3.0
        self.tau = 1.5 # Giãn thời gian 1.5x
        self.s = 1.0
        self.dt = 0.01
        self.y = np.array([0.0, -0.5, 0.0, 1.2, 0.0, 0.0]) # 6 khớp
        self.yd = np.zeros(6)
        self.goal = np.array([0.4, 0.2, -0.3, 1.5, 0.1, -0.2]) # Đích mới

    def step_dmp(self):
        if self.s \lt 0.001:
            return # Đã hội tụ về đích
        # Cập nhật pha
        self.s -= (self.alpha_s * self.s / self.tau) * self.dt
        # Tính toán hệ biến đổi bậc 2
        f_s = self.compute_forcing_term(self.s)
        ydd = (25.0 * (6.25 * (self.goal - self.y) - self.tau * self.yd) + f_s) / (self.tau**2)
        self.yd += ydd * self.dt
        self.y += self.yd * self.dt

        # Đóng gói bản tin ROS 2
        msg = JointTrajectory()
        pt = JointTrajectoryPoint()
        pt.positions = self.y.tolist()
        pt.velocities = self.yd.tolist()
        msg.points.append(pt)
        self.pub_traj.publish(msg)

    def compute_forcing_term(self, s):
        # Trọng số RBFs đã huấn luyện offline
        return np.sin(s * np.pi) * 20.0 * s</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 06: Diffusion Policy & Action Chunking Transformers
# ==============================================================================
ch06_sidebar = [
    {"id": "sec-6-1", "title": "6.1 Giới Hạn MLP & Phân Phối Hành Vi Đa Đỉnh"},
    {"id": "sec-6-2", "title": "6.2 Kiến Trúc Denoising Diffusion Probabilistic Models (DDPM)"},
    {"id": "sec-6-3", "title": "6.3 Action Chunking with Transformers (ACT)"},
    {"id": "sec-6-4", "title": "6.4 Kỹ Thuật Ghép Quỹ Đạo Temporal Ensembling"},
    {"id": "sec-6-sim", "title": "⚡ Mô Phỏng Diffusion Khử Nhiễu Đa Mốt (Canvas)"},
    {"id": "sec-6-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Khử Nhiễu Bước k -> k-1"},
    {"id": "sec-6-bridge", "title": "🛠️ Cầu Nối PyTorch: Huấn Luyện Diffusion Policy U-Net"}
]

ch06_body = r"""
        <!-- 6.1 -->
        <h2 id="sec-6-1">6.1 Giới Hạn Của MLP Truyền Thống & Phân Phối Hành Vi Đa Đỉnh (Multimodal Action Distributions)</h2>
        <p>Trong suốt nhiều năm, các mô hình Behavioral Cloning sử dụng mạng nơ-ron truyền thẳng (Multi-Layer Perceptrons - MLP) tối ưu hóa bằng hàm mất mát sai số toàn phương trung bình (Mean Squared Error - MSE):</p>
        $$\mathcal{L}_{MSE}(\theta) = \mathbb{E}_{(s, a) \sim \mathcal{D}_E} \left[ \| \pi_\theta(s) - a \|^2 \right]$$
        <p>Hàm mất mát này mang một giả định ngầm cực kỳ nguy hiểm: phân phối hành động có điều kiện $p(a \mid s)$ tuân theo phân phối chuẩn đơn mốt (Unimodal Gaussian). Khi đối mặt với tác vụ đa mốt (Multimodal), trong đó con người có nhiều phương án hành động đều đúng (ví dụ: vòng tránh vật cản sang bên trái HOẶC bên phải), MLP tối ưu bằng MSE sẽ cho ra kết quả trung bình cộng:</p>
        $$a_{\text{MLP}} = \frac{a_{\text{left}} + a_{\text{right}}}{2} = a_{\text{va chạm}}$$
        <p>Kết quả là robot lao thẳng vào vật cản! Đây chính là điểm tắc nghẽn lớn nhất khiến robot không thể thực hiện các thao tác khéo léo trong thế giới thực.</p>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 DIFFUSION POLICY & ACT GIẢI QUYẾT BÀI TOÁN NÀY NHƯ THẾ NÀO?</div>
          <div class="why-matters-body">
            Đột phá xuất hiện vào giai đoạn 2023 - 2024 với hai kiến trúc SOTA:
            <br>1. <strong>Diffusion Policy (Cheng Chi et al., Columbia / TRI):</strong> Thay vì dự đoán trực tiếp hành động, mạng học cách khử nhiễu dần dần một vector nhiễu ngẫu nhiên Gaussian thành quỹ đạo hành vi hợp lệ, dễ dàng biểu diễn phân phối đa mốt tùy ý mà không bị trung bình hóa.
            <br>2. <strong>Action Chunking with Transformers - ACT (Tony Zhao et al., Stanford / ALOHA):</strong> Dự đoán đồng thời một chuỗi khối hành động tương lai (Action Chunks) thay vì từng bước riêng lẻ, kết hợp bộ mã hóa biến thiên C-VAE và Temporal Ensembling để động tác đạt độ mượt mà cấp độ con người.
          </div>
        </div>

        <!-- 6.2 -->
        <h2 id="sec-6-2">6.2 Kiến Trúc Denoising Diffusion Probabilistic Models (DDPM) Cho Robot Manipulation</h2>
        <p>Diffusion Policy xây dựng quy trình sinh hành động gồm hai chiều:</p>

        <div class="formula-hero">
          <div class="formula-title">1. Quá Trình Khuếch Tán Thuận (Forward Diffusion Process)</div>
          <div class="formula-math">
            $$q(A^k \mid A^0) = \mathcal{N}\left(A^k; \sqrt{\bar{\alpha}_k} A^0, (1 - \bar{\alpha}_k) \mathbf{I}\right)$$
          </div>
          <div class="formula-legend">
            <strong>Ý nghĩa:</strong> Thêm nhiễu Gauss tăng dần vào chuỗi hành động chuyên gia $A^0$ qua $K$ bước khuếch tán. Khi $k = K$, $A^K \sim \mathcal{N}(0, \mathbf{I})$ trở thành nhiễu trắng thuần túy.
          </div>
        </div>

        <div class="formula-hero" style="margin-top: 1.5rem;">
          <div class="formula-title">2. Quá Trình Khử Nhiễu Ngược (Reverse Denoising Process) Có Điều Kiện Quan Sát $O_t$</div>
          <div class="formula-math">
            $$p_\theta(A^{k-1} \mid A^k, O_t) = \mathcal{N}\left(A^{k-1}; \mu_\theta(A^k, k, O_t), \sigma_k^2 \mathbf{I}\right)$$
          </div>
          <div class="formula-legend">
            <strong>Trong đó:</strong> Mạng nơ-ron U-Net 1D hoặc Transformer $\epsilon_\theta(A^k, k, O_t)$ học cách dự đoán vector nhiễu $\epsilon$ đã được thêm vào ở bước $k$, với điều kiện đầu vào là chuỗi quan sát thị giác $O_t$:
            $$\mathcal{L}_{\text{Diffusion}}(\theta) = \mathbb{E}_{k, A^0, \epsilon} \left[ \| \epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_k} A^0 + \sqrt{1 - \bar{\alpha}_k} \epsilon, k, O_t) \|^2 \right]$$
          </div>
        </div>

        <!-- 6.3 -->
        <h2 id="sec-6-3">6.3 Action Chunking With Transformers (ACT) & Conditional VAE</h2>
        <p>Thay vì sinh hành động từng bước thời gian $a_t = \pi(s_t)$, ACT dự đoán một khối gồm $H$ hành động liên tiếp trong tương lai:</p>
        $$A_t = [a_t, a_{t+1}, \dots, a_{t+H-1}] \in \mathbb{R}^{H \times d_a}$$
        <p>Việc nhóm hành động (Action Chunking) mang lại 3 ưu điểm vượt trội:
        <br>• Triệt tiêu sai số tích lũy Covariate Shift vì số lần robot phải quyết định giảm đi $H$ lần.
        <br>• Khắc phục hiện tượng trễ truyền thông và độ trễ suy luận của mạng nơ-ron sâu.
        <br>• Cho phép robot tự điều hòa động học nội tại giữa các bước để đảm bảo gia tốc và lực giật (Jerk) êm dịu.</p>

        <!-- 6.4 -->
        <h2 id="sec-6-4">6.4 Kỹ Thuật Ghép Quỹ Đạo Temporal Ensembling Chống Rung Giật</h2>
        <p>Tại mỗi bước thời gian $t$, robot thực hiện truy vấn mạng ACT để lấy ra một khối mới $A_t$. Như vậy, tại thời điểm hiện tại sẽ có sự trùng lặp của $H$ dự đoán khác nhau đến từ các thời điểm $t-H+1, \dots, t$. Kỹ thuật <strong>Temporal Ensembling</strong> tổng hợp hành động thực thi bằng trọng số hàm mũ:</p>
        $$a_t = \sum_{i=0}^{\min(t, H-1)} w_i A_{t-i}[i], \quad w_i = \frac{\exp(-m \cdot i)}{\sum_j \exp(-m \cdot j)}$$
        <p>Hệ số $m \gt 0$ gán trọng số cao hơn cho các dự đoán mới nhất. Kỹ thuật này giúp quỹ đạo thực thi mượt như nhung, loại bỏ hiện tượng giật cục tại các mốc phân ranh giới chunk.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-6-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Quy Trình Khử Nhiễu Denoising Sinh Hành Động Đa Mốt</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-06" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Bước khử nhiễu $k$ (Khuếch tán ngược): <input type="range" id="sim06-step" min="0" max="16" step="1" value="10"> <span id="sim06-step-val">Bước khử nhiễu: k = 10 / 16</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-6-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Một Bước Khử Nhiễu DDPM Lấy Mẫu Hành Động Khớp $a^{k-1}$ Từ $a^k$</h3>
          <p>Xét một bậc tự do tay gắp với hành động $a \in [-1.0, 1.0]$. Tại bước khử nhiễu $k = 5$, tham số lịch trình nhiễu là $\beta_5 = 0.1$, $\alpha_5 = 1 - \beta_5 = 0.9$, $\bar{\alpha}_5 = 0.65$. Hành động nhiễu hiện tại đo được là $a^5 = 0.82$. Mạng nơ-ron U-Net dự đoán thành phần nhiễu là $\epsilon_\theta(a^5, 5, O_t) = 0.35$. Vector ngẫu nhiên sinh từ phân phối chuẩn tại bước này là $z = 0.12$. Tính giá trị hành động khử nhiễu $a^4$ theo phương trình lấy mẫu DDPM.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Thiết lập công thức lấy mẫu khử nhiễu ngược DDPM</h5>
              <p>Phương trình cập nhật trạng thái hành động từ bước $k$ về $k-1$:</p>
              <p>$$a^{k-1} = \frac{1}{\sqrt{\alpha_k}} \left( a^k - \frac{\beta_k}{\sqrt{1 - \bar{\alpha}_k}} \epsilon_\theta(a^k, k, O_t) \right) + \sigma_k z$$</p>
              <p>với độ lệch chuẩn nhiễu lấy mẫu $\sigma_k = \sqrt{\beta_k} = \sqrt{0.1} \approx 0.3162$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính thành phần hiệu chỉnh dự đoán nhiễu</h5>
              <p>• Mẫu số căn bậc hai: $\sqrt{1 - \bar{\alpha}_5} = \sqrt{1 - 0.65} = \sqrt{0.35} \approx 0.5916$</p>
              <p>• Tỷ số trọng số: $\frac{\beta_5}{\sqrt{1 - \bar{\alpha}_5}} = \frac{0.1}{0.5916} \approx 0.1690$</p>
              <p>• Lượng trừ đi: $0.1690 \times \epsilon_\theta = 0.1690 \times 0.35 \approx 0.0592$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính kỳ vọng giá trị trung bình $\mu_\theta$</h5>
              <p>• Hiệu số trong ngoặc: $a^5 - 0.0592 = 0.82 - 0.0592 = 0.7608$</p>
              <p>• Nhân với nghịch đảo $\frac{1}{\sqrt{\alpha_5}} = \frac{1}{\sqrt{0.9}} \approx \frac{1}{0.9487} \approx 1.0541$</p>
              <p>• Kỳ vọng trung bình: $\mu_5 = 1.0541 \times 0.7608 \approx 0.8019$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Cộng thành phần nhiễu ngẫu nhiên Langevin & Kết luận</h5>
              <p>• Thành phần ngẫu nhiên: $\sigma_5 \times z = 0.3162 \times 0.12 \approx 0.0379$</p>
              <p>• Hành động khử nhiễu: $$a^4 = 0.8019 + 0.0379 = 0.8398$$</p>
              <p>Sau 16 bước lặp khử nhiễu liên tiếp từ $k = 16$ về $k = 0$, mẫu hành động cuối cùng $a^0$ sẽ hội tụ chính xác về một mốt hành vi tối ưu của người làm mẫu.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-6-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Vòng Lặp Suy Luận Diffusion Policy U-Net 1D (PyTorch)</h4>
          <p>Mã nguồn chuẩn triển khai mạng U-Net 1D khử nhiễu hành động đa chiều cho cánh tay thao tác robot:</p>
          <div class="code-card">
            <div class="code-header">
              <span>diffusion_policy_infer.py (PyTorch / GPU)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import torch
import torch.nn as nn

class DiffusionPolicyRunner:
    def __init__(self, model, noise_scheduler, obs_horizon=2, pred_horizon=16, action_dim=7):
        self.model = model # U-Net 1D Conditional Denoising Network
        self.scheduler = noise_scheduler
        self.pred_horizon = pred_horizon
        self.action_dim = action_dim

    @torch.no_grad()
    def predict_action_chunk(self, condition_obs):
        # condition_obs: Tensor [1, obs_horizon, obs_dim]
        # Khởi tạo chuỗi hành động ngẫu nhiên thuần Gaussian
        noisy_action = torch.randn((1, self.pred_horizon, self.action_dim), device='cuda')
        
        # Vòng lặp khử nhiễu ngược 16 bước
        for k in reversed(range(len(self.scheduler.timesteps))):
            t = torch.tensor([k], device='cuda')
            # Dự đoán vector nhiễu epsilon
            noise_pred = self.model(noisy_action, t, condition_obs)
            # Khử nhiễu bước k -> k-1
            noisy_action = self.scheduler.step(noise_pred, k, noisy_action).prev_sample
            
        # Trả về chunk hành động tối ưu [pred_horizon, action_dim]
        return noisy_action.squeeze(0).cpu().numpy()</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 07: Học Tăng Cường Nghịch Đảo (Inverse RL) & Maximum Entropy
# ==============================================================================
ch07_sidebar = [
    {"id": "sec-7-1", "title": "7.1 Bài Toán Khôi Phục Hàm Phần Thưởng Ẩn R(s,a)"},
    {"id": "sec-7-2", "title": "7.2 Thuật Toán Maximum Margin IRL (Ng & Russell)"},
    {"id": "sec-7-3", "title": "7.3 Maximum Entropy IRL (Ziebart 2008)"},
    {"id": "sec-7-4", "title": "7.4 Feature Matching & Gradient Descent"},
    {"id": "sec-7-sim", "title": "⚡ Mô Phỏng Bản Đồ Nhiệt Thưởng R(s) Gridworld (Canvas)"},
    {"id": "sec-7-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Gradient Feature Matching"},
    {"id": "sec-7-bridge", "title": "🛠️ Cầu Nối Kỹ Thuật: Triển Khai Thuật Toán MaxEnt Solver"}
]

ch07_body = r"""
        <!-- 7.1 -->
        <h2 id="sec-7-1">7.1 Đặt Vấn Đề: Tại Sao Cần Khôi Phục Hàm Phần Thưởng Ẩn?</h2>
        <p>Nhân bản hành vi (BC) chỉ đơn thuần "bắt chước mù quáng" các hành động bề mặt $a$ mà không hề thấu hiểu <em>mục đích tối hậu</em> của chuyên gia. Khi môi trường có sự thay đổi về chướng ngại vật hoặc luật động học, chính sách BC lập tức sụp đổ. <strong>Học Tăng Cường Nghịch Đảo (Inverse Reinforcement Learning - IRL)</strong> đi tìm câu trả lời cho câu hỏi cốt lõi: <em>"Động cơ hay hàm phần thưởng $R^*(s,a)$ nào đã khiến chuyên gia hành động như vậy?"</em></p>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 ƯU ĐIỂM VƯỢT TRỘI CỦA HÀM PHẦN THƯỞNG R(s,a)</div>
          <div class="why-matters-body">
            1. <strong>Bất biến với động lực học môi trường (Environment Invariance):</strong> Nếu thay đổi khối lượng robot hoặc bề mặt ma sát, chính sách cũ không dùng được, nhưng hàm phần thưởng $R(s)$ vẫn giữ nguyên chân lý. Ta chỉ việc chạy lại thuật toán RL tối ưu là robot mới lập tức thích nghi.
            <br>2. <strong>Biểu diễn cô đọng nhất của hành vi:</strong> Toàn bộ tri thức phức tạp được nén gọn trong một hàm thế vô hướng $R: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$.
            <br>3. <strong>Vấn đề nan giải (Ill-posed problem):</strong> Luôn tồn tại vô số hàm thưởng tầm thường thỏa mãn (ví dụ: $R(s,a) \equiv 0$ khiến mọi chính sách đều có giá trị bằng nhau).
          </div>
        </div>

        <!-- 7.2 -->
        <h2 id="sec-7-2">7.2 Thuật Toán Maximum Margin IRL (Abbeel & Ng 2004)</h2>
        <p>Giả định hàm phần thưởng tuyến tính theo vector đặc trưng trạng thái $\phi(s) \in \mathbb{R}^d$:</p>
        $$R_w(s) = w^T \phi(s), \quad \|w\|_2 \le 1$$
        <p>Giá trị kỳ vọng của một chính sách $\pi$ được biểu diễn qua vector đặc trưng kỳ vọng (Expected Feature Counts):</p>
        $$\mathbb{E}\left[\sum_{t=0}^\infty \gamma^t R(s_t)\right] = w^T \mu(\pi), \quad \text{với } \mu(\pi) = \mathbb{E}\left[\sum_{t=0}^\infty \gamma^t \phi(s_t) \;\middle|\; \pi\right]$$
        <p>Thuật toán <strong>Maximum Margin</strong> tìm kiếm vector trọng số $w$ sao cho chính sách chuyên gia $\pi_E$ vượt trội hơn tất cả các chính sách khác một khoảng lề an toàn tối đa (Margin):</p>
        $$\max_w \min_i w^T \left( \mu_E - \mu(\pi_i) \right), \quad \text{s.t. } \|w\|_2 \le 1$$

        <!-- 7.3 -->
        <h2 id="sec-7-3">7.3 Maximum Entropy IRL (Ziebart et al., 2008)</h2>
        <p>Thuật toán Max-Margin vẫn còn nhược điểm: giả định con người hành động hoàn hảo và có thể chọn một hàm thưởng tùy tiện ở biên. Brian Ziebart đưa ra nguyên lý mang tính bước ngoặt: <em>Trong số tất cả các phân phối quỹ đạo phù hợp với dữ liệu chuyên gia, hãy chọn phân phối có Entropy cực đại (ít thiên kiến giả định nhất).</em></p>

        <div class="formula-hero">
          <div class="formula-title">Phân Phối Xác Suất Quỹ Đạo Theo Nguyên Lý Gibbs/Boltzmann</div>
          <div class="formula-math">
            $$P(\tau \mid \theta) = \frac{1}{Z(\theta)} \exp\left( R_\theta(\tau) \right) = \frac{1}{Z(\theta)} \exp\left( \theta^T \Phi(\tau) \right)$$
          </div>
          <div class="formula-legend">
            <strong>Trong đó:</strong>
            <br>• $\Phi(\tau) = \sum_{t=0}^T \phi(s_t)$: Tổng vector đặc trưng tích lũy dọc theo quỹ đạo $\tau$.
            <br>• $Z(\theta) = \int \exp\left(\theta^T \Phi(\tau)\right) d\tau$: Hàm phân phối trạng thái (Partition function), tích phân trên toàn bộ các quỹ đạo hợp lệ có thể sinh ra trong MDP.
            <br>• Quỹ đạo có tổng phần thưởng cao hơn sẽ có xác suất xuất hiện lớn hơn theo quy luật hàm mũ, đồng thời chuyên gia vẫn có thể mắc sai sót nhỏ ngẫu nhiên (Bounded Rationality).
          </div>
        </div>

        <!-- 7.4 -->
        <h2 id="sec-7-4">7.4 Feature Matching & Thuật Toán Tối Ưu Gradient Descent</h2>
        <p>Hàm mục tiêu Log-Likelihood cực đại hóa xác suất của tập biểu diễn chuyên gia $\mathcal{D}_E$:</p>
        $$\mathcal{L}(\theta) = \sum_{\tau \in \mathcal{D}_E} \log P(\tau \mid \theta) = \sum_{\tau \in \mathcal{D}_E} \theta^T \Phi(\tau) - |\mathcal{D}_E| \log Z(\theta)$$
        <p>Đạo hàm Gradient đẹp đẽ của hàm mục tiêu theo tham số $\theta$:</p>
        $$\nabla_\theta \mathcal{L}(\theta) = \tilde{\mu}_E - \sum_{\tau} P(\tau \mid \theta) \Phi(\tau) = \tilde{\mu}_E - \sum_{s \in \mathcal{S}} D_s \phi(s)$$
        <p>với $\tilde{\mu}_E = \frac{1}{N} \sum_{i=1}^N \Phi(\tau_i)$ là đặc trưng thực nghiệm của chuyên gia, và $D_s$ là tần suất viếng thăm trạng thái (State Visitation Frequency - SVF) tính bằng quy hoạch động.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-7-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Khôi Phục Bản Đồ Nhiệt Phần Thưởng Ẩn $R(s)$ Trong Gridworld</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-07" width="700" height="320" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-7-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Cập Nhật Trọng Số Phần Thưởng $\theta$ Qua Gradient Feature Matching</h3>
          <p>Xét một bài toán robot có 2 đặc trưng quan sát: $\phi_1(s)$ (tốc độ di chuyển) và $\phi_2(s)$ (khoảng cách tới vật cản). Chuyên gia có vector đặc trưng trung bình thực nghiệm $\tilde{\mu}_E = [4.5, 0.8]^T$. Trọng số thưởng khởi tạo hiện tại là $\theta = [0.5, -1.0]^T$. Khi mô phỏng chính sách hiện tại với $\theta$, tần suất viếng thăm trạng thái sinh ra vector đặc trưng kỳ vọng là $\mathbb{E}_{\pi_\theta}[\mu] = [3.2, 1.5]^T$. Tốc độ học $\eta = 0.1$. Tính vector gradient và cập nhật vector trọng số thưởng $\theta_{\text{new}}$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính vector sai lệch đặc trưng (Feature Discrepancy)</h5>
              <p>Gradient hàm mục tiêu chính là hiệu giữa đặc trưng chuyên gia và đặc trưng chính sách:</p>
              <p>$$\nabla_\theta \mathcal{L}(\theta) = \tilde{\mu}_E - \mathbb{E}_{\pi_\theta}[\mu]$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Thay số tính toán từng thành phần gradient</h5>
              <p>• Thành phần tốc độ: $\Delta_1 = 4.5 - 3.2 = +1.3$</p>
              <p>• Thành phần vật cản: $\Delta_2 = 0.8 - 1.5 = -0.7$</p>
              <p>Vector gradient: $\nabla_\theta \mathcal{L} = [1.3, -0.7]^T$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Cập nhật trọng số thưởng theo Gradient Ascent</h5>
              <p>$$\theta_{\text{new}} = \theta_{\text{old}} + \eta \nabla_\theta \mathcal{L}(\theta)$$</p>
              <p>• $\theta_1^{\text{new}} = 0.5 + 0.1 \times (1.3) = 0.5 + 0.13 = 0.63$</p>
              <p>• $\theta_2^{\text{new}} = -1.0 + 0.1 \times (-0.7) = -1.0 - 0.07 = -1.07$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Phân tích ý nghĩa học máy của trọng số mới</h5>
              <p>• $\theta_1$ tăng từ $0.5 \to 0.63$: Robot được khuyến khích di chuyển nhanh hơn để bắt kịp phong cách chuyên gia.</p>
              <p>• $\theta_2$ giảm sâu hơn từ $-1.0 \to -1.07$: Hình phạt lại gần vật cản bị siết chặt hơn do chính sách cũ tiếp cận quá gần vật cản so với chuyên gia.</p>
              <p>Thuật toán hội tụ khi $\|\nabla_\theta \mathcal{L}\| \to 0$ (Đặc trưng khớp hoàn hảo).</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-7-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Thuật Toán Tính Tần Suất Trạng Thái (SVF) MaxEnt Trong Python</h4>
          <p>Mã nguồn lõi tính toán tần suất viếng thăm trạng thái $D_s$ bằng quy hoạch động thuận nghịch:</p>
          <div class="code-card">
            <div class="code-header">
              <span>maxent_svf_solver.py (Python)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import numpy as np

def compute_state_visitation_frequency(P_trans, policy, p0, T):
    # P_trans: [n_states, n_actions, n_states]
    # policy: [n_states, n_actions]
    # p0: phân phối xuất phát [n_states]
    n_states, n_actions, _ = P_trans.shape
    D = np.zeros((n_states, T))
    D[:, 0] = p0

    for t in range(1, T):
        for s_prime in range(n_states):
            # Tính tổng xác suất chuyển dịch từ mọi cặp (s, a) tới s_prime
            prob_flow = 0.0
            for s in range(n_states):
                for a in range(n_actions):
                    prob_flow += D[s, t-1] * policy[s, a] * P_trans[s, a, s_prime]
            D[s_prime, t] = prob_flow
            
    # Tần suất viếng thăm trạng thái tích lũy
    return np.sum(D, axis=1)</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 08: Học Bắt Chước Đối Nghịch GAIL & Khớp Phân Phối Chiếm Dụng
# ==============================================================================
ch08_sidebar = [
    {"id": "sec-8-1", "title": "8.1 Nghẽn Cổ Chai Của IRL & Phân Phối Chiếm Dụng"},
    {"id": "sec-8-2", "title": "8.2 Định Lý Ho & Ermon (NeurIPS 2016)"},
    {"id": "sec-8-3", "title": "8.3 Cấu Trúc Đối Nghịch Discriminator vs Generator"},
    {"id": "sec-8-4", "title": "8.4 Mở Rộng Sang Adversarial Inverse RL (AIRL)"},
    {"id": "sec-8-sim", "title": "⚡ Mô Phỏng Khớp Phân Phối Chiếm Dụng d_pi (Canvas)"},
    {"id": "sec-8-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Cập Nhật Discriminator"},
    {"id": "sec-8-bridge", "title": "🛠️ Cầu Nối PyTorch: Vòng Lặp Huấn Luyện GAIL + PPO"}
]

ch08_body = r"""
        <!-- 8.1 -->
        <h2 id="sec-8-1">8.1 Nghẽn Cổ Chai Của IRL Truyền Thống & Khái Niệm Phân Phối Chiếm Dụng (Occupancy Measure)</h2>
        <p>Thuật toán IRL cổ điển mang một gánh nặng tính toán khổng lồ: <em>Trong mỗi bước lặp cập nhật hàm thưởng $R_\theta$, hệ thống bắt buộc phải giải trọn vẹn một bài toán RL thuận (Reinforcement Learning) đến khi hội tụ để tìm chính sách tối ưu tương ứng.</em> Việc giải RL lồng bên trong IRL khiến việc ứng dụng trên các robot có không gian trạng thái liên tục nhiều bậc tự do trở nên bất khả thi.</p>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 PHÂN PHỐI CHIẾM DỤNG (OCCUPANCY MEASURE) LÀ GÌ?</div>
          <div class="why-matters-body">
            Định nghĩa phân phối chiếm dụng trạng thái - hành động của một chính sách $\pi$:
            $$d_\pi(s, a) = (1 - \gamma) \sum_{t=0}^\infty \gamma^t P(s_t = s, a_t = a \mid \pi)$$
            $d_\pi(s,a)$ đo lường mật độ xuất hiện của cặp trạng thái - hành động $(s, a)$ khi robot tương tác với môi trường theo chính sách $\pi$. 
            <br><strong>Định lý ánh xạ một-một:</strong> Tồn tại quan hệ tương đương song ánh giữa một chính sách $\pi$ và phân phối chiếm dụng $d_\pi$. Nói cách khác: <em>Hai chính sách là đồng nhất khi và chỉ khi phân phối chiếm dụng của chúng trùng khít nhau ($d_\pi = d_E$).</em>
          </div>
        </div>

        <!-- 8.2 -->
        <h2 id="sec-8-2">8.2 Định Lý Ho & Ermon (NeurIPS 2016): Đồng Nhất Hóa Khớp Phân Phối Với GAN</h2>
        <p>Jonathan Ho và Stefano Ermon đã chứng minh một phát kiến thiên tài: Quá trình tìm kiếm chính sách có phân phối chiếm dụng trùng với chuyên gia có thể được đồng nhất hóa toán học chính xác với bài toán huấn luyện Mạng Đối Nghịch Tạo Sinh (Generative Adversarial Networks - GAN):</p>
        <div class="formula-hero">
          <div class="formula-title">Hàm Mục Tiêu Tối Thiểu Hóa Khoảng Cách Jensen-Shannon Của GAIL</div>
          <div class="formula-math">
            $$\min_\pi \max_D \mathbb{E}_{\mathcal{D}_E} \left[ \log D(s, a) \right] + \mathbb{E}_{\pi} \left[ \log(1 - D(s, a)) \right] - \lambda H(\pi)$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách kiến trúc 2 đối thủ:</strong>
            <br>• <strong>Discriminator $D_\psi(s,a) \in (0, 1)$:</strong> Đóng vai trò giám khảo, cố gắng phân biệt xem cặp $(s,a)$ là do chuyên gia thực hiện ($D \to 1$) hay do robot tự sinh ($D \to 0$).
            <br>• <strong>Policy Generator $\pi_\theta(a|s)$:</strong> Đóng vai trò kẻ làm giả, điều khiển robot hành động sao cho đánh lừa được Discriminator ($D \to 1$).
            <br>• $H(\pi)$: Số hạng điều hòa Entropy giúp chính sách khám phá liên tục và tránh sụp đổ mốt (Mode Collapse).
          </div>
        </div>

        <!-- 8.3 -->
        <h2 id="sec-8-3">8.3 Cơ Chế Sinh Thưởng Đại Diện & Vòng Lặp Học GAIL</h2>
        <p>Không cần bất kỳ hàm thưởng thủ công nào, chính sách $\pi_\theta$ coi Discriminator như một bộ sinh phần thưởng tự động (Surrogate Reward):</p>
        $$r_t(s_t, a_t) = -\log\left(1 - D_\psi(s_t, a_t)\right) \quad \text{hoặc} \quad r_t(s_t, a_t) = \log D_\psi(s_t, a_t)$$
        <p>Khi robot hành động giống hệt chuyên gia, $D_\psi(s,a) \approx 0.99 \Rightarrow r_t \approx -\log(0.01) = 4.6$ (Thưởng rất cao). Ngược lại, nếu robot đi chệch quỹ đạo, $D_\psi(s,a) \approx 0.05 \Rightarrow r_t \approx -\log(0.95) = 0.05$ (Không có thưởng). Chính sách sau đó được cập nhật bằng các thuật toán Policy Gradient tiên tiến như PPO (Proximal Policy Optimization) hoặc TRPO.</p>

        <!-- 8.4 -->
        <h2 id="sec-8-4">8.4 Mở Rộng Sang Adversarial Inverse RL (AIRL)</h2>
        <p>GAIL giải quyết triệt để vấn đề khớp phân phối nhưng bản thân Discriminator của GAIL lại không trích xuất được một hàm phần thưởng bất biến (Nó phụ thuộc chặt chẽ vào động lực học môi trường lúc huấn luyện). <strong>AIRL (Fu et al., 2018)</strong> khắc phục điều này bằng cách phân rã cấu trúc Discriminator thành:</p>
        $$D_{\theta, \phi}(s, a, s') = \frac{\exp\left( f_{\theta, \phi}(s, a, s') \right)}{\exp\left( f_{\theta, \phi}(s, a, s') \right) + \pi(a \mid s)}$$
        $$f_{\theta, \phi}(s, a, s') = g_\theta(s, a) + \gamma h_\phi(s') - h_\phi(s)$$
        <p>Trong đó $g_\theta(s,a)$ đóng vai trò là hàm phần thưởng chân thực (Disentangled Reward) không đổi ngay cả khi mang sang một robot khác với động học mới.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-8-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Sự Hội Tụ Phân Phối Chiếm Dụng $d_\pi$ Về $d_E$ Theo Từng Epoch</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-08" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Số Epoch Huấn Luyện GAIL: <input type="range" id="sim08-disc" min="1" max="30" step="1" value="10"> <span id="sim08-d-val">Vòng huấn luyện GAIL: Epoch 10</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-8-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Cập Nhật Discriminator GAIL & Tính Điểm Thưởng Cho Chính Sách</h3>
          <p>Mạng Discriminator $D_\psi(s,a) = \sigma(z)$ với hàm kích hoạt Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$. Tại bước huấn luyện thứ $t$, chuyên gia thực hiện mẫu $(s_E, a_E)$ với giá trị logit dự đoán $z_E = 1.8$. Robot thực hiện bước $(s_\pi, a_\pi)$ với giá trị logit $z_\pi = -0.5$. Tính đầu ra xác suất $D(s_E, a_E)$, $D(s_\pi, a_\pi)$, hàm mất mát Binary Cross Entropy $\mathcal{L}_D$ và điểm thưởng $r(s_\pi, a_\pi)$ trả về cho chính sách robot.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính xác suất đầu ra của Discriminator</h5>
              <p>• Với mẫu chuyên gia: $$D(s_E, a_E) = \sigma(1.8) = \frac{1}{1 + e^{-1.8}} = \frac{1}{1 + 0.1653} \approx 0.8581$$</p>
              <p>• Với mẫu robot: $$D(s_\pi, a_\pi) = \sigma(-0.5) = \frac{1}{1 + e^{0.5}} = \frac{1}{1 + 1.6487} \approx 0.3775$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính hàm mất mát Binary Cross Entropy của Discriminator</h5>
              <p>$$\mathcal{L}_D = -\left[ \ln D(s_E, a_E) + \ln(1 - D(s_\pi, a_\pi)) \right]$$</p>
              <p>• $\ln(0.8581) \approx -0.1530$</p>
              <p>• $1 - D(s_\pi, a_\pi) = 1 - 0.3775 = 0.6225 \Rightarrow \ln(0.6225) \approx -0.4740$</p>
              <p>$$\mathcal{L}_D = -(-0.1530 - 0.4740) = 0.6270$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính điểm thưởng nội sinh trả về cho Policy Generator</h5>
              <p>Theo công thức phần thưởng GAIL chuẩn:</p>
              <p>$$r(s_\pi, a_\pi) = -\ln(1 - D(s_\pi, a_\pi))$$</p>
              <p>$$r(s_\pi, a_\pi) = -\ln(0.6225) \approx +0.4740$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Phân tích hướng tối ưu của vòng lặp</h5>
              <p>• Giá trị thưởng hiện tại là $+0.4740$. Nếu robot tiến bộ và đưa hành vi tới gần chuyên gia hơn ($D \to 0.9$), điểm thưởng sẽ tăng vọt lên $-\ln(0.1) = 2.3026$.</p>
              <p>• Discriminator nhận tín hiệu lỗi $\mathcal{L}_D = 0.6270$ và cập nhật trọng số bằng Adam Optimizer để phân loại sắc bén hơn trong lượt tiếp theo.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-8-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Module GAIL Discriminator & Tính Thưởng Với PyTorch</h4>
          <p>Mã nguồn chuẩn triển khai mạng Discriminator và tích hợp vào thuật toán tối ưu PPO:</p>
          <div class="code-card">
            <div class="code-header">
              <span>gail_discriminator.py (PyTorch)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import torch
import torch.nn as nn

class GAILDiscriminator(nn.Module):
    def __init__(self, state_dim, action_dim, hidden_dim=256):
        super(GAILDiscriminator, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim + action_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, 1),
            nn.Sigmoid()
        )
        self.optimizer = torch.optim.Adam(self.parameters(), lr=3e-4)
        self.loss_fn = nn.BCELoss()

    def get_reward(self, state, action):
        with torch.no_grad():
            x = torch.cat([state, action], dim=-1)
            d = self.net(x)
            # Hàm thưởng surrogate: -log(1 - D)
            return -torch.log(torch.clamp(1.0 - d, min=1e-5))

    def update(self, expert_states, expert_actions, policy_states, policy_actions):
        exp_x = torch.cat([expert_states, expert_actions], dim=-1)
        pol_x = torch.cat([policy_states, policy_actions], dim=-1)
        
        exp_labels = torch.ones((exp_x.shape[0], 1), device=exp_x.device)
        pol_labels = torch.zeros((pol_x.shape[0], 1), device=pol_x.device)
        
        loss = self.loss_fn(self.net(exp_x), exp_labels) + self.loss_fn(self.net(pol_x), pol_labels)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return loss.item()</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# Generate HTML files for Track 3 and Track 4
# ==============================================================================
print("Generating Ch 05...")
with open(os.path.join(CHAPTERS_DIR, "ch05.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("05", "Động Tác Nguyên Mẫu Động Lực Học (DMPs) & ProMPs", "Dynamic Movement Primitives & Probabilistic Motor Skills", "TRACK 3: BIỂU DIỄN ĐỘNG TÁC & DEEP IL", "track-3", "ch04.html", "Chương 04: Họ Thuật Toán DAgger", "ch06.html", "Chương 06: Diffusion Policy & ACT", ch05_sidebar, ch05_body))

print("Generating Ch 06...")
with open(os.path.join(CHAPTERS_DIR, "ch06.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("06", "Diffusion Policy & Action Chunking Transformers", "State-of-the-Art Generative Policies in Robot Manipulation", "TRACK 3: BIỂU DIỄN ĐỘNG TÁC & DEEP IL", "track-3", "ch05.html", "Chương 05: Động Tác Nguyên Mẫu DMPs", "ch07.html", "Chương 07: Học Tăng Cường Nghịch Đảo IRL", ch06_sidebar, ch06_body))

print("Generating Ch 07...")
with open(os.path.join(CHAPTERS_DIR, "ch07.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("07", "Học Tăng Cường Nghịch Đảo (Inverse RL) & Maximum Entropy", "Inverse Reinforcement Learning & Feature Matching", "TRACK 4: HỌC TĂNG CƯỜNG NGHỊCH ĐẢO & ĐỐI NGHỊCH", "track-4", "ch06.html", "Chương 06: Diffusion Policy & ACT", "ch08.html", "Chương 08: Học Bắt Chước Đối Nghịch GAIL", ch07_sidebar, ch07_body))

print("Generating Ch 08...")
with open(os.path.join(CHAPTERS_DIR, "ch08.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("08", "Học Bắt Chước Đối Nghịch GAIL & Khớp Phân Phối Chiếm Dụng", "Generative Adversarial Imitation Learning & Occupancy Matching", "TRACK 4: HỌC TĂNG CƯỜNG NGHỊCH ĐẢO & ĐỐI NGHỊCH", "track-4", "ch07.html", "Chương 07: Học Tăng Cường Nghịch Đảo IRL", "ch09.html", "Chương 09: Học Bắt Chước Từ Quan Sát", ch08_sidebar, ch08_body))

print("Successfully generated Chapters 05, 06, 07, 08 for Imitation Learning!")
