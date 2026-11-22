# -*- coding: utf-8 -*-
"""
build_chapters_t1_t2.py
Biên soạn nội dung chuẩn 6 tầng tri thức cho Track 1 và Track 2 (Chương 01 - Chương 04):
- Ch 01: Biểu Diễn Hệ Thống Hợp Nhất & Không Gian Trạng Thái
- Ch 02: Động Học Vật Rắn 3D & Biến Đổi Tọa Độ Robot
- Ch 03: Động Lực Học Động Cơ & Khớp Đàn Hồi
- Ch 04: Ma Sát Động LuGre & Hệ Truyền Động Thủy Lực
"""

import os

BASE_DIR = r"c:\Users\chucuong\OneDrive\Reading\robot-dynamics-modeling-web"
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
  <title>Chương {ch_num_str}: {title} - Robot Dynamics & Modeling</title>
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
            <span>📚 Nguồn tài liệu: <strong>Brian Fabien (Springer 2009) & Olav Egeland (NTNU 2002)</strong></span>
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
        <p>Động Lực Học & Modeling Robot • Hệ Thống Chưng Cất Tri Thức Học Thuật</p>
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
# CHƯƠNG 01: Biểu Diễn Hệ Thống Hợp Nhất & Không Gian Trạng Thái
# ==============================================================================
ch01_sidebar = [
    {"id": "sec-1-1", "title": "1.1 Đại lượng Động học & Động lực học"},
    {"id": "sec-1-2", "title": "1.2 Phần tử Lưu trữ & Tiêu tán Năng lượng"},
    {"id": "sec-1-3", "title": "1.3 Sơ đồ Bond Graph & Paynter Đa miền"},
    {"id": "sec-1-4", "title": "1.4 Không gian Trạng thái & Điểm Cân bằng"},
    {"id": "sec-1-5", "title": "1.5 Tuyến tính hóa Taylor Quanh Điểm Vận hành"},
    {"id": "sec-1-6", "title": "1.6 Tính Thụ động & Biến sóng Năng lượng"},
    {"id": "sec-1-sim", "title": "⚡ Mô phỏng Ghép Nối Cơ - Điện (Canvas)"},
    {"id": "sec-1-worked", "title": "📐 Ví dụ Tính Số 4 Bước Tuyến Tính Hóa"},
    {"id": "sec-1-bridge", "title": "🛠️ Cầu nối ROS 2 State Estimator Node"}
]

ch01_body = r"""
        <!-- 1.1 -->
        <h2 id="sec-1-1">1.1 Khái Niệm Cơ Bản & Phân Loại Đại Lượng Hệ Thống</h2>
        <p>Trong kỹ thuật mô hình hóa hệ thống động học đa ngành (multidiscipline dynamic systems), một hệ thống vật lý bất kỳ—từ robot cánh tay, xe tự hành đến mạch công suất và cơ cấu thủy lực—đều có thể quy về sự tương tác của hai nhóm biến cơ bản: <strong>biến nỗ lực (Effort variable - $e(t)$)</strong> và <strong>biến dòng chảy (Flow variable - $f(t)$)</strong>.</p>
        
        <div class="why-matters-box">
          <div class="why-matters-header">💡 Ý NGHĨA & ỨNG DỤNG ĐỂ LÀM GÌ?</div>
          <div class="why-matters-body">
            Quy chuẩn hóa toàn bộ các miền năng lượng (Cơ học tịnh tiến, Cơ học quay, Mạch điện, Thủy lực) về cặp biến chung $(e, f)$ cho phép kỹ sư phân tích các hệ thống robot phức hợp ghép nối (như khớp robot gồm động cơ điện + hộp số giảm tốc + chất lưu thủy lực) bằng một phương pháp luận toán học thống nhất duy nhất mà không cần giải riêng lẻ từng miền.
          </div>
        </div>

        <table class="academic-table" style="width:100%; margin: 1.5rem 0; border-collapse: collapse;">
          <thead>
            <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
              <th style="padding: 0.75rem;">Miền Năng Lượng</th>
              <th style="padding: 0.75rem;">Biến Nỗ Lực (Effort - $e$)</th>
              <th style="padding: 0.75rem;">Biến Dòng Chảy (Flow - $f$)</th>
              <th style="padding: 0.75rem;">Biến Tích Lũy (Displacement / Momentum)</th>
              <th style="padding: 0.75rem;">Công Suất Tức Thời $P(t) = e \cdot f$</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Cơ học Tịnh tiến</strong></td>
              <td style="padding: 0.75rem;">Lực $F\text{ [N]}$</td>
              <td style="padding: 0.75rem;">Vận tốc $v\text{ [m/s]}$</td>
              <td style="padding: 0.75rem;">Độ dời $x$, Động lượng $p$</td>
              <td style="padding: 0.75rem;">$P = F \cdot v\text{ [W]}$</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Cơ học Quay (Robot)</strong></td>
              <td style="padding: 0.75rem;">Mô-men xoắn $\tau\text{ [N}\cdot\text{m]}$</td>
              <td style="padding: 0.75rem;">Vận tốc góc $\omega\text{ [rad/s]}$</td>
              <td style="padding: 0.75rem;">Góc quay $\theta$, Mô-men động lượng $L$</td>
              <td style="padding: 0.75rem;">$P = \tau \cdot \omega\text{ [W]}$</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Điện từ học</strong></td>
              <td style="padding: 0.75rem;">Điện áp $u\text{ [V]}$</td>
              <td style="padding: 0.75rem;">Dòng điện $i\text{ [A]}$</td>
              <td style="padding: 0.75rem;">Điện tích $q$, Từ thông $\lambda$</td>
              <td style="padding: 0.75rem;">$P = u \cdot i\text{ [W]}$</td>
            </tr>
            <tr>
              <td style="padding: 0.75rem;"><strong>Thủy lực học</strong></td>
              <td style="padding: 0.75rem;">Áp suất $p\text{ [Pa]}$</td>
              <td style="padding: 0.75rem;">Lưu lượng thể tích $Q\text{ [m}^3/\text{s]}$</td>
              <td style="padding: 0.75rem;">Thể tích tích lũy $V$</td>
              <td style="padding: 0.75rem;">$P = p \cdot Q\text{ [W]}$</td>
            </tr>
          </tbody>
        </table>

        <!-- 1.2 -->
        <h2 id="sec-1-2">1.2 Các Phần Tử Lưu Trữ & Tiêu Tán Năng Lượng Lý Tưởng</h2>
        <p>Mọi cơ cấu vật lý đều được cấu thành từ 3 họ phần tử thụ động lý tưởng kết nối với các nguồn năng lượng:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Đặc Tuyến Của 3 Phần Tử Năng Lượng Lý Tưởng</div>
          <div class="formula-math">
            $$\begin{cases}
              \text{Phần tử quán tính (Inductor / Mass } I\text{):} & e(t) = I \frac{df(t)}{dt} \iff p(t) = I \cdot f(t) \\
              \text{Phần tử tích điện/đàn hồi (Capacitor / Spring } C\text{):} & f(t) = C \frac{de(t)}{dt} \iff q(t) = C \cdot e(t) \\
              \text{Phần tử tiêu tán năng lượng (Resistor / Damper } R\text{):} & e(t) = R \cdot f(t) \quad (\text{Năng lượng chuyển hóa thành nhiệt})
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách tham số:</strong> $I$ là khối lượng $m$ (cơ) hoặc độ tự cảm $L$ (điện); $C$ là độ mềm đàn hồi $1/k$ hoặc điện dung $C_e$; $R$ là hệ số cản nhớt $b$ hoặc điện trở thuần $R_e$.
          </div>
        </div>

        <!-- 1.3 -->
        <h2 id="sec-1-3">1.3 Mô Hình Đa Miền & Sơ Đồ Bond Graph / Paynter</h2>
        <p>Sơ đồ Paynter (Paynter's Diagram) biểu diễn mối tương quan giữa các phần tử lưu trữ năng lượng động ($I$), năng lượng thế ($C$), tiêu tán ($R$) và nguồn ($S_e, S_f$) thông qua các cổng năng lượng (power bonds). Mỗi bond mang theo hai biến hướng $(e, f)$ với tích của chúng đại diện cho dòng công suất thực tế chảy qua cổng.</p>

        <!-- 1.4 -->
        <h2 id="sec-1-4">1.4 Mô Hình Không Gian Trạng Thái Phi Tuyến & Điểm Cân Bằng</h2>
        <p>Hệ thống động lực tổng quát bậc $n$ với $m$ tín hiệu điều khiển đầu vào và $p$ tín hiệu đầu ra được mô tả bằng hệ phương trình vi phân trạng thái:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Trạng Thái Phi Tuyến Chuẩn</div>
          <div class="formula-math">
            $$\begin{cases}
              \dot{x}(t) = f(x(t), u(t)) \\
              y(t) = h(x(t), u(t))
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Ký hiệu:</strong> $x(t) \in \mathbb{R}^n$ là vector trạng thái (thường gồm tọa độ vị trí và vận tốc); $u(t) \in \mathbb{R}^m$ là vector tín hiệu điều khiển đầu vào; $y(t) \in \mathbb{R}^p$ là vector đầu ra cảm biến đo lường.
          </div>
        </div>
        <p><strong>Điểm cân bằng (Equilibrium Point):</strong> Điểm $x^* \in \mathbb{R}^n$ được gọi là điểm cân bằng của hệ thống ứng với tín hiệu vào hằng số $u^*$ nếu vận tốc trạng thái triệt tiêu hoàn toàn:</p>
        $$\left. f(x^*, u^*) \right. = 0$$

        <!-- 1.5 -->
        <h2 id="sec-1-5">1.5 Tuyến Tính Hóa Taylor Quanh Điểm Cân Bằng Vận Hành</h2>
        <p>Đặt độ lệch trạng thái $\delta x = x - x^*$ và độ lệch đầu vào $\delta u = u - u^*$. Khai triển chuỗi Taylor bậc 1 của hàm $f(x, u)$ quanh $(x^*, u^*)$:</p>
        <div class="formula-hero">
          <div class="formula-title">Mô Hình Trạng Thái Tuyến Tính Cục Bộ</div>
          <div class="formula-math">
            $$\dot{\delta x} \approx A \delta x + B \delta u, \quad \delta y \approx C \delta x + D \delta u$$
          </div>
          <div class="formula-legend">
            <strong>Ma trận Jacobian:</strong> $A = \left.\frac{\partial f}{\partial x}\right|_{(x^*, u^*)}$, $B = \left.\frac{\partial f}{\partial u}\right|_{(x^*, u^*)}$, $C = \left.\frac{\partial h}{\partial x}\right|_{(x^*, u^*)}$, $D = \left.\frac{\partial h}{\partial u}\right|_{(x^*, u^*)}$.
          </div>
        </div>

        <!-- 1.6 -->
        <h2 id="sec-1-6">1.6 Tính Thụ Động (Passivity) & Biến Sóng Năng Lượng</h2>
        <p>Một hệ thống với đầu vào $u(t)$ và đầu ra $y(t)$ được gọi là <strong>thụ động (passive)</strong> nếu tồn tại hàm lưu trữ năng lượng xác định dương $S(x) \ge 0$ thỏa mãn bất đẳng thức tiêu tán:</p>
        $$S(x(T)) - S(x(0)) \le \int_0^T u^T(t) y(t) dt$$
        <p>Điều này đồng nghĩa với việc hệ thống không thể tự phát sinh năng lượng nội tại, bảo đảm tính ổn định tuyệt đối khi ghép nối phản hồi (Passivity Theorem).</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-1-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Tương Tác: Dòng Năng Lượng Ghép Nối Cơ - Điện</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-01" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Điện áp cấp V (Effort): <input type="range" id="sim01-voltage" min="0" max="24" step="1" value="12"> <span id="sim01-v-val">12.0 V</span></label>
            <label style="font-size: 0.85rem; font-weight: 600;">Điện trở cuộn dây R: <input type="range" id="sim01-res" min="0.5" max="10" step="0.5" value="2.5"> <span id="sim01-r-val">2.5 Ω</span></label>
            <label style="font-size: 0.85rem; font-weight: 600;">Độ cứng lò xo K: <input type="range" id="sim01-spring" min="5" max="50" step="5" value="15"> <span id="sim01-k-val">15.0 N/m</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-1-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tuyến Tính Hóa Hệ Cơ Điện Ghép Nối</h3>
          <p>Xét một cơ cấu chấp hành điện từ gồm cuộn cảm $L=0.05\text{ H}$, điện trở $R=2.0\ \Omega$ sinh lực hút nam châm $F_m = c \cdot \frac{i^2}{x^2}$ tác động lên vật trượt khối lượng $m=0.5\text{ kg}$ có gắn lò xo $k=200\text{ N/m}$. Cho hằng số từ $c = 0.02\text{ N}\cdot\text{m}^2/\text{A}^2$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Khởi tạo thông số & Điểm cân bằng</h5>
              <p>Chọn khe hở cân bằng mong muốn $x^* = 0.01\text{ m}$.</p>
              <p>Tại trạng thái cân bằng: $F_m^* = F_{spring}^* \implies c \frac{(i^*)^2}{(x^*)^2} = k x^*$.</p>
              <p>$$\implies (i^*)^2 = \frac{k (x^*)^3}{c} = \frac{200 \times 10^{-6}}{0.02} = 0.01 \implies i^* = 0.1\text{ A}.$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Thiết lập hệ phương trình vi phân</h5>
              <p>Đặt vector trạng thái $x = [x_1, x_2, x_3]^T = [x, \dot{x}, i]^T$:</p>
              <p>$$\dot{x}_1 = x_2$$</p>
              <p>$$\dot{x}_2 = \frac{1}{m}\left(-k x_1 + c \frac{x_3^2}{x_1^2}\right)$$</p>
              <p>$$\dot{x}_3 = \frac{1}{L}(u - R x_3)$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính toán đạo hàm riêng Jacobian</h5>
              <p>Đạo hàm lực theo vị trí: $\left.\frac{\partial f_2}{\partial x_1}\right|_* = \frac{1}{m}\left(-k - \frac{2 c (i^*)^2}{(x^*)^3}\right) = \frac{-200 - 400}{0.5} = -1200$.</p>
              <p>Đạo hàm theo dòng: $\left.\frac{\partial f_2}{\partial x_3}\right|_* = \frac{1}{m}\frac{2 c i^*}{(x^*)^2} = \frac{2 \times 0.02 \times 0.1}{0.5 \times 10^{-4}} = 80$.</p>
              <p>Đạo hàm điện học: $\left.\frac{\partial f_3}{\partial x_3}\right|_* = -\frac{R}{L} = -\frac{2.0}{0.05} = -40$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Ma trận trạng thái & Kiểm định ổn định</h5>
              <p>Ma trận $A$ tuyến tính hóa:</p>
              <p>$$A = \begin{bmatrix} 0 & 1 & 0 \\ -1200 & 0 & 80 \\ 0 & 0 & -40 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 0 \\ 20 \end{bmatrix}.$$</p>
              <p>Phương trình đặc trưng $\det(sI - A) = (s + 40)(s^2 + 1200) = 0 \implies s_{1} = -40, s_{2,3} = \pm j 34.64\text{ rad/s}$. Hệ thống ở biên giới ổn định dao động không tắt.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-1-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: ROS 2 State Space Estimator Node</h4>
          <p>Trong hệ sinh thái ROS 2, mô hình không gian trạng thái tuyến tính $(\delta \dot{x} = A \delta x + B \delta u)$ được ứng dụng trực tiếp trong bộ ước lượng trạng thái Kalman Filter (EKF) để kết hợp số liệu đo từ encoder và cảm biến dòng điện:</p>
          <div class="code-card">
            <div class="code-header">
              <span>state_space_node.cpp (ROS 2 Humble / C++)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>#include "rclcpp/rclcpp.hpp"
#include &lt;Eigen/Dense&gt;

class StateSpaceEstimator : public rclcpp::Node {
public:
  StateSpaceEstimator() : Node("state_space_estimator") {
    // Khởi tạo ma trận hệ thống 3x3
    A_ &lt;&lt; 0.0, 1.0, 0.0,
         -1200.0, 0.0, 80.0,
         0.0, 0.0, -40.0;
    B_ &lt;&lt; 0.0, 0.0, 20.0;
    x_hat_.setZero();
    RCLCPP_INFO(this->get_logger(), "State Space Estimator Initialized.");
  }
private:
  Eigen::Matrix3d A_;
  Eigen::Vector3d B_;
  Eigen::Vector3d x_hat_;
};</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 02: Động Học Vật Rắn 3D & Biến Đổi Tọa Độ Robot
# ==============================================================================
ch02_sidebar = [
    {"id": "sec-2-1", "title": "2.1 Ma trận Quay SO(3) & Biến đổi SE(3)"},
    {"id": "sec-2-2", "title": "2.2 Góc Euler & Khóa Khớp Gimbal Lock"},
    {"id": "sec-2-3", "title": "2.3 Biểu diễn Quaternions & Đại số Quaternion"},
    {"id": "sec-2-4", "title": "2.4 Vận tốc Góc & Toán tử Ma trận Phản Đối xứng S(ω)"},
    {"id": "sec-2-5", "title": "2.5 Phương trình Vi phân Động học Thái độ"},
    {"id": "sec-2-6", "title": "2.6 Khung Serret-Frenet & Chuyển động Đường cong"},
    {"id": "sec-2-7", "title": "2.7 Bảng Tham số Denavit-Hartenberg (DH)"},
    {"id": "sec-2-8", "title": "2.8 Ma trận Jacobian Hình học & Giải tích"},
    {"id": "sec-2-sim", "title": "⚡ Mô phỏng Quaternions vs Gimbal Lock (Canvas)"},
    {"id": "sec-2-worked", "title": "📐 Ví dụ Tính Số 4 Bước Góc Euler sang Quaternion"},
    {"id": "sec-2-bridge", "title": "🛠️ Cầu nối ROS 2 tf2 Transform Library"}
]

ch02_body = r"""
        <!-- 2.1 -->
        <h2 id="sec-2-1">2.1 Ma Trận Quay Trực Giao $SO(3)$ & Phép Biến Đổi Đồng Nhất $SE(3)$</h2>
        <p>Để định vị một vật rắn (link robot) trong không gian 3 chiều, ta gắn một hệ tọa độ động $\{B\}$ vào tâm vật rắn và khảo sát tương quan với hệ tọa độ tham chiếu cố định $\{A\}$. Hướng thái độ (orientation) được định nghĩa bởi ma trận quay trực giao thuộc nhóm Lie đặc biệt $SO(3)$ (Special Orthogonal group):</p>
        <div class="formula-hero">
          <div class="formula-title">Định Nghĩa Nhóm Quay Trực Giao $SO(3)$</div>
          <div class="formula-math">
            $$SO(3) = \left\{ R \in \mathbb{R}^{3 \times 3} \;\middle|\; R^T R = I_{3 \times 3}, \; \det(R) = +1 \right\}$$
          </div>
          <div class="formula-legend">
            <strong>Ý nghĩa trực giao:</strong> Nghịch đảo của ma trận quay bằng chính chuyển vị của nó: $R^{-1} = R^T$. Độ dài vector không thay đổi qua phép biến đổi quay: $\|R v\| = \|v\|$.
          </div>
        </div>

        <p>Phép biến đổi đồng nhất $4 \times 4$ trong nhóm $SE(3)$ biểu diễn cả phép quay và tịnh tiến:</p>
        $$T = \begin{bmatrix} R & p \\ 0_{1 \times 3} & 1 \end{bmatrix} \in SE(3), \quad T^{-1} = \begin{bmatrix} R^T & -R^T p \\ 0_{1 \times 3} & 1 \end{bmatrix}$$

        <!-- 2.2 -->
        <h2 id="sec-2-2">2.2 Các Bộ Góc Euler & Hiện Tượng Khóa Khớp (Gimbal Lock)</h2>
        <p>Góc Euler biểu diễn thái độ qua 3 góc quay tuần tự quanh các trục tọa độ (ví dụ Roll-Pitch-Yaw tương ứng quanh $X-Y-Z$ hoặc $Z-Y-X$). Ma trận quay kết hợp:</p>
        $$R_{ZYX}(\psi, \theta, \phi) = R_z(\psi) R_y(\theta) R_x(\phi)$$
        <div class="why-matters-box">
          <div class="why-matters-header">⚠️ NGUY HIỂM: HIỆN TƯỢNG KHÓA KHỚP GIMBAL LOCK</div>
          <div class="why-matters-body">
            Khi góc Pitch $\theta = \pm 90^\circ$ ($\pm \pi/2$), hai trục Roll và Yaw bị xếp thẳng hàng (cùng phương trong không gian). Lúc này hệ thống bị mất 1 bậc tự do thái độ, ma trận Jacobian động học thái độ bị suy biến $(\det J = 0)$, dẫn đến hiện tượng thuật toán điều khiển phân kỳ với vận tốc góc tính toán tiến đến vô cùng!
          </div>
        </div>

        <!-- 2.3 -->
        <h2 id="sec-2-3">2.3 Biểu Diễn Quaternions (Tham Số Euler-Rodrigues)</h2>
        <p>Theo Định lý quay Euler, mọi phép quay hữu hạn trong không gian 3D đều tương đương với một phép quay duy nhất một góc $\theta$ quanh một trục đơn vị $\mathbf{u} = [u_x, u_y, u_z]^T$. Đơn vị Quaternion $\mathbf{q}$ được định nghĩa bởi bộ 4 tham số thực:</p>
        <div class="formula-hero">
          <div class="formula-title">Cấu Trúc Đơn Vị Quaternion (Unit Quaternion)</div>
          <div class="formula-math">
            $$\mathbf{q} = \begin{bmatrix} \eta \\ \boldsymbol{\epsilon} \end{bmatrix} = \begin{bmatrix} \cos(\theta/2) \\ \mathbf{u} \sin(\theta/2) \end{bmatrix} \in \mathbb{R}^4, \quad \|\mathbf{q}\|^2 = \eta^2 + \boldsymbol{\epsilon}^T \boldsymbol{\epsilon} = 1$$
          </div>
          <div class="formula-legend">
            <strong>Ưu thế vượt trội:</strong> Quaternions loại bỏ hoàn toàn 100% hiện tượng kỳ dị khóa khớp Gimbal Lock, đồng thời phép nhân Quaternion chỉ tốn 16 phép nhân số thực (thay vì 27 phép nhân ma trận $3 \times 3$).
          </div>
        </div>

        <!-- 2.4 -->
        <h2 id="sec-2-4">2.4 Vận Tốc Góc $\boldsymbol{\omega}$ & Toán Tử Ma Trận Phản Đối Xứng $S(\boldsymbol{\omega})$</h2>
        <p>Xét đạo hàm thời gian của ma trận quay: lấy đạo hàm biểu thức trực giao $R(t) R^T(t) = I$:</p>
        $$\dot{R} R^T + R \dot{R}^T = 0 \iff \dot{R} R^T = -(\dot{R} R^T)^T$$
        <p>Biểu thức $\dot{R} R^T$ là một ma trận phản đối xứng (skew-symmetric matrix). Đặt $\dot{R} R^T = S(\boldsymbol{\omega})$, với $\boldsymbol{\omega} = [\omega_x, \omega_y, \omega_z]^T$ là vector vận tốc góc tức thời của vật rắn:</p>
        <div class="formula-hero">
          <div class="formula-title">Toán Tử Phản Đối Xứng Cross-Product Matrix</div>
          <div class="formula-math">
            $$S(\boldsymbol{\omega}) = [\boldsymbol{\omega}]_\times = \begin{bmatrix} 0 & -\omega_z & \omega_y \\ \omega_z & 0 & -\omega_x \\ -\omega_y & \omega_x & 0 \end{bmatrix} \implies S(\boldsymbol{\omega}) v = \boldsymbol{\omega} \times v$$
          </div>
          <div class="formula-legend">
            <strong>Phương trình vi phân quay cơ bản:</strong> $\dot{R} = S(\boldsymbol{\omega}) R$.
          </div>
        </div>

        <!-- 2.5 -->
        <h2 id="sec-2-5">2.5 Phương Trình Vi Phân Động Học Thái Độ (Kinematic DEs)</h2>
        <p>Tốc độ biến thiên của Quaternions liên hệ trực tiếp với vận tốc góc vật rắn trong hệ tọa độ thân $\boldsymbol{\omega}^b$ thông qua ma trận Jacobi mở rộng:</p>
        $$\begin{bmatrix} \dot{\eta} \\ \dot{\boldsymbol{\epsilon}} \end{bmatrix} = \frac{1}{2} \begin{bmatrix} -\boldsymbol{\epsilon}^T \\ \eta I_{3 \times 3} + S(\boldsymbol{\epsilon}) \end{bmatrix} \boldsymbol{\omega}^b$$

        <!-- 2.6 -->
        <h2 id="sec-2-6">2.6 Bảng Tham Số Denavit-Hartenberg (DH) Robot Cánh Tay</h2>
        <p>Quy ước DH gán hệ tọa độ chuẩn hóa lên từng khớp khâu của robot chuỗi hở thông qua 4 tham số hình học: $\theta_i$ (góc quay khớp), $d_i$ (độ dời dọc trục $z$), $a_i$ (chiều dài thanh nối dọc trục $x$), $\alpha_i$ (góc xoắn giữa hai trục $z$). Ma trận biến đổi từng khâu:</p>
        $$A_i = \text{Rot}(z, \theta_i) \text{Trans}(z, d_i) \text{Trans}(x, a_i) \text{Rot}(x, \alpha_i)$$

        <!-- 2.7 -->
        <h2 id="sec-2-7">2.7 Ma Trận Jacobian Hình Học & Giải Tích (Manipulator Jacobians)</h2>
        <p>Ma trận Jacobian hình học $J(q) \in \mathbb{R}^{6 \times n}$ ánh xạ vận tốc khớp $\dot{q}$ sang vận tốc dài $v_e$ và vận tốc góc $\omega_e$ của khâu thao tác cuối (End-Effector):</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Vi Phân Động Học Thuận</div>
          <div class="formula-math">
            $$\begin{bmatrix} v_e \\ \omega_e \end{bmatrix} = J(q) \dot{q} = \begin{bmatrix} J_v(q) \\ J_\omega(q) \end{bmatrix} \dot{q}$$
          </div>
          <div class="formula-legend">
            <strong>Cột thứ $i$ của Jacobian:</strong> Đối với khớp quay (revolute joint): $J_{v,i} = z_{i-1} \times (p_e - p_{i-1})$ và $J_{\omega,i} = z_{i-1}$.
          </div>
        </div>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-2-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng 3D Quaternions vs Khóa Khớp Gimbal Lock</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-02" width="700" height="320" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Góc Yaw (Z): <input type="range" id="sim02-yaw" min="-180" max="180" step="5" value="30"> <span id="sim02-yaw-val">30°</span></label>
            <label style="font-size: 0.85rem; font-weight: 600;">Góc Pitch (Y): <input type="range" id="sim02-pitch" min="-90" max="90" step="1" value="45"> <span id="sim02-pitch-val">45°</span></label>
            <label style="font-size: 0.85rem; font-weight: 600;">Góc Roll (X): <input type="range" id="sim02-roll" min="-180" max="180" step="5" value="20"> <span id="sim02-roll-val">20°</span></label>
            <div id="sim02-quat-val" style="width: 100%; font-family: monospace; font-size: 0.9rem; color: #38bdf8;">q = [0.893, 0.153i, 0.366j, 0.201k]</div>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-2-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Chuyển Đổi Góc Euler Sang Quaternion</h3>
          <p>Thực hiện tính toán chuyển đổi thái độ của khâu cổ tay robot từ bộ 3 góc Euler $ZYX$ với góc Yaw $\psi = 60^\circ$, Pitch $\theta = 30^\circ$, Roll $\phi = 45^\circ$ sang biểu diễn Quaternion $\mathbf{q} = [q_0, q_1, q_2, q_3]^T$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Chia nửa các góc thái độ</h5>
              <p>$$\frac{\psi}{2} = 30^\circ, \quad \frac{\theta}{2} = 15^\circ, \quad \frac{\phi}{2} = 22.5^\circ$$</p>
              <p>Tính các giá trị lượng giác cơ sở:</p>
              <p>$\cos(\psi/2) = \frac{\sqrt{3}}{2} \approx 0.8660, \sin(\psi/2) = 0.5000$</p>
              <p>$\cos(\theta/2) = 0.9659, \sin(\theta/2) = 0.2588$</p>
              <p>$\cos(\phi/2) = 0.9239, \sin(\phi/2) = 0.3827$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Thiết lập công thức tích đại số</h5>
              <p>$$q_0 = \cos\frac{\phi}{2}\cos\frac{\theta}{2}\cos\frac{\psi}{2} + \sin\frac{\phi}{2}\sin\frac{\theta}{2}\sin\frac{\psi}{2}$$</p>
              <p>$$q_1 = \sin\frac{\phi}{2}\cos\frac{\theta}{2}\cos\frac{\psi}{2} - \cos\frac{\phi}{2}\sin\frac{\theta}{2}\sin\frac{\psi}{2}$$</p>
              <p>$$q_2 = \cos\frac{\phi}{2}\sin\frac{\theta}{2}\cos\frac{\psi}{2} + \sin\frac{\phi}{2}\cos\frac{\theta}{2}\sin\frac{\psi}{2}$$</p>
              <p>$$q_3 = \cos\frac{\phi}{2}\cos\frac{\theta}{2}\sin\frac{\psi}{2} - \sin\frac{\phi}{2}\sin\frac{\theta}{2}\cos\frac{\psi}{2}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính toán từng thành phần số</h5>
              <p>$$q_0 = (0.9239)(0.9659)(0.8660) + (0.3827)(0.2588)(0.5000) = 0.7729 + 0.0495 = 0.8224$$</p>
              <p>$$q_1 = (0.3827)(0.9659)(0.8660) - (0.9239)(0.2588)(0.5000) = 0.3201 - 0.1196 = 0.2005$$</p>
              <p>$$q_2 = (0.9239)(0.2588)(0.8660) + (0.3827)(0.9659)(0.5000) = 0.2071 + 0.1848 = 0.3919$$</p>
              <p>$$q_3 = (0.9239)(0.9659)(0.5000) - (0.3827)(0.2588)(0.8660) = 0.4462 - 0.0858 = 0.3604$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Kiểm tra chuẩn hóa $\|\mathbf{q}\|$</h5>
              <p>Tính bình phương độ dài quaternion:</p>
              <p>$$\|\mathbf{q}\|^2 = 0.8224^2 + 0.2005^2 + 0.3919^2 + 0.3604^2 = 0.6763 + 0.0402 + 0.1536 + 0.1299 = 1.0000$$</p>
              <p>Sai số chuẩn hóa $\Delta \lt 10^{-6}$, nghiệm quaternion hoàn toàn chuẩn xác và sẵn sàng nạp vào bộ điều khiển tư thế robot.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-2-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Thư Viện Biến Đổi Tọa Độ ROS 2 tf2</h4>
          <p>Hệ thống ROS 2 duy trì cây biến đổi hình học toàn diện bằng thư viện `tf2`. Đoạn code sau chuyển đổi góc Euler sang Quaternion và xuất biến đổi `TransformStamped`:</p>
          <div class="code-card">
            <div class="code-header">
              <span>tf2_broadcaster.cpp (ROS 2 Humble / C++)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/transform_broadcaster.h"
#include "geometry_msgs/msg/transform_stamped.hpp"
#include "tf2/LinearMath/Quaternion.h"

void broadcastArmPose(std::shared_ptr&lt;tf2_ros::TransformBroadcaster&gt; br, double yaw, double pitch, double roll) {
  geometry_msgs::msg::TransformStamped t;
  t.header.stamp = rclcpp::Clock().now();
  t.header.frame_id = "base_link";
  t.child_frame_id = "wrist_link";
  
  tf2::Quaternion q;
  q.setRPY(roll, pitch, yaw); // Roll-Pitch-Yaw to Quaternion
  t.transform.rotation.x = q.x();
  t.transform.rotation.y = q.y();
  t.transform.rotation.z = q.z();
  t.transform.rotation.w = q.w();
  br-&gt;sendTransform(t);
}</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 03: Động Lực Học Động Cơ & Khớp Đàn Hồi
# ==============================================================================
ch03_sidebar = [
    {"id": "sec-3-1", "title": "3.1 Động cơ DC & Phương trình Điện - Cơ"},
    {"id": "sec-3-2", "title": "3.2 Động cơ BLDC & Định hướng Từ thông FOC"},
    {"id": "sec-3-3", "title": "3.3 Hộp số Giảm tốc & Phản xạ Quán tính"},
    {"id": "sec-3-4", "title": "3.4 Khớp Đàn hồi & Mô hình Động học Spong"},
    {"id": "sec-3-5", "title": "3.5 Phần tử Cơ điện Hai Cổng & Áp điện"},
    {"id": "sec-3-sim", "title": "⚡ Mô phỏng Khớp Đàn Hồi Spong (Canvas)"},
    {"id": "sec-3-worked", "title": "📐 Ví dụ Tính Số 4 Bước Phản Xạ Quán Tính"},
    {"id": "sec-3-bridge", "title": "🛠️ Cầu nối ros2_control Transmission Interface"}
]

ch03_body = r"""
        <!-- 3.1 -->
        <h2 id="sec-3-1">3.1 Động Cơ Điện Một Chiều DC & Phương Trình Ghép Nối Điện - Cơ</h2>
        <p>Động cơ điện là cơ cấu chấp hành phổ biến nhất trong tay máy công nghiệp. Mô hình động cơ DC kích từ vĩnh cửu bao gồm mạch điện phần ứng kết hợp chuyển động quay của rotor:</p>
        <div class="formula-hero">
          <div class="formula-title">Hệ Phương Trình Vi Phân Ghép Nối Động Cơ DC</div>
          <div class="formula-math">
            $$\begin{cases}
              L_a \frac{di_a(t)}{dt} + R_a i_a(t) + K_b \omega_m(t) = v_a(t) & (\text{Định luật Kirchhoff điện áp}) \\
              J_m \frac{d\omega_m(t)}{dt} + B_m \omega_m(t) + \tau_L(t) = K_t i_a(t) & (\text{Định luật II Newton cho rotor})
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách tham số:</strong> $v_a(t)$ là điện áp cấp phần ứng [V]; $i_a(t)$ là dòng điện [A]; $R_a, L_a$ là điện trở và điện cảm cuộn dây; $\omega_m$ là vận tốc góc rotor [rad/s]; $J_m, B_m$ là mô-men quán tính và ma sát rotor; $K_t$ là hằng số mô-men [N·m/A]; $K_b$ là hằng số s.đ.đ phản kháng [V·s/rad] (trong hệ SI, $K_t = K_b$).
          </div>
        </div>

        <!-- 3.2 -->
        <h2 id="sec-3-2">3.2 Động Cơ Đồng Bộ Nam Châm Vĩnh Cửu BLDC & Điều Khiển FOC</h2>
        <p>Động cơ không chổi than (BLDC / PMSM) sử dụng biến đổi Park-Clarke để chuyển hệ tọa độ 3 pha tĩnh $(a, b, c)$ sang hệ tọa độ quay đồng bộ trực giao $(d, q)$. Nhờ đó, dòng sinh từ thông $i_d$ và dòng sinh mô-men $i_q$ được điều khiển độc lập như động cơ DC kích từ độc lập:</p>
        $$\tau_e = \frac{3}{2} p \lambda_{pm} i_q$$

        <!-- 3.3 -->
        <h2 id="sec-3-3">3.3 Hộp Số Giảm Tốc, Tỷ Số Truyền $N$ & Phản Xạ Quán Tính</h2>
        <p>Do động cơ điện quay ở tốc độ cao nhưng mô-men nhỏ, các khớp robot thường tích hợp hộp số sóng biến dạng (Harmonic Drive) hoặc bánh răng hành tinh với tỷ số truyền cao $N = \omega_m / \dot{q} \gg 1$ ($N$ thường từ 50 đến 160):</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Phản Xạ Quán Tính & Mô-men</div>
          <div class="formula-math">
            $$J_{eff} = J_m + \frac{1}{N^2} J_L, \quad \tau_{joint} = N \cdot \tau_m$$
          </div>
          <div class="formula-legend">
            <strong>Ý nghĩa vật lý then chốt:</strong> Quán tính của cánh tay tải trọng $J_L$ khi phản xạ về trục động cơ bị suy giảm theo bình phương tỷ số truyền $(1/N^2)$. Nhờ vậy động cơ dễ dàng tăng tốc điều khiển khâu thao tác mà không bị quán tính tải kéo trôi.
          </div>
        </div>

        <!-- 3.4 -->
        <h2 id="sec-3-4">3.4 Khớp Đàn Hồi (Flexible Joints) & Mô Hình Động Học Spong</h2>
        <p>Trong các dòng robot chính xác cao hoặc cobot tương tác an toàn, hộp số và trục truyền động có tính đàn hồi đáng kể, tạo ra góc xoắn giữa góc quay rotor $\theta$ và góc quay khâu tải $q$. Mô hình Spong mô tả hiện tượng khớp đàn hồi:</p>
        <div class="formula-hero">
          <div class="formula-title">Mô Hình Động Lực Học Khớp Đàn Hồi Spong</div>
          <div class="formula-math">
            $$\begin{cases}
              M(q)\ddot{q} + C(q,\dot{q})\dot{q} + g(q) = K(\theta - q) & (\text{Phương trình khâu tải}) \\
              J_m \ddot{\theta} + B_m \dot{\theta} + K(\theta - q) = \tau_m & (\text{Phương trình rotor động cơ})
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Đặc điểm:</strong> $K$ là ma trận độ cứng xoắn của khớp [N·m/rad]. Sự chênh lệch $(\theta - q)$ kích hoạt các dao động cộng hưởng nếu vòng lặp điều khiển phản hồi không được bù triệt để.
          </div>
        </div>

        <!-- 3.5 -->
        <h2 id="sec-3-5">3.5 Phần Tử Cơ Điện Hai Cổng & Bộ Chấp Hành Áp Điện</h2>
        <p>Bộ chấp hành áp điện (Piezoelectric actuators) khai thác hiệu ứng phân cực tinh thể dưới điện trường cao để tạo ra các vi dịch chuyển cấp nanomet với tần số đáp ứng lên đến hàng kilohertz, ứng dụng trong vi thao tác tế bào và quang học chính xác.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-3-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Dao Động Khớp Đàn Hồi Robot (Spong Model)</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-03" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Độ cứng lò xo xoắn K: <input type="range" id="sim03-stiffness" min="20" max="300" step="10" value="100"> <span id="sim03-k-val">100 N·m/rad</span></label>
            <label style="font-size: 0.85rem; font-weight: 600;">Mô-men điều khiển Tau: <input type="range" id="sim03-torque" min="-5" max="5" step="0.5" value="2.0"> <span id="sim03-tau-val">2.0 N·m</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-3-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Phản Xạ Quán Tính & Tần Số Cộng Hưởng Khớp Đàn Hồi</h3>
          <p>Một khớp robot công nghiệp sử dụng động cơ DC có mô-men quán tính rotor $J_m = 0.002\text{ kg}\cdot\text{m}^2$, kéo khâu tải có quán tính $J_L = 5.0\text{ kg}\cdot\text{m}^2$ qua hộp số Harmonic Drive có tỷ số truyền $N = 100$. Độ cứng lò xo xoắn của trục truyền động $K = 4000\text{ N}\cdot\text{m/rad}$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính quán tính tải phản xạ về rotor</h5>
              <p>Áp dụng định luật phản xạ quán tính qua hộp số $N=100$:</p>
              <p>$$J_{L,refl} = \frac{J_L}{N^2} = \frac{5.0}{100^2} = \frac{5.0}{10000} = 0.0005\text{ kg}\cdot\text{m}^2$$</p>
              <p>Tổng quán tính tương đương nhìn từ trục động cơ:</p>
              <p>$$J_{eff,m} = J_m + J_{L,refl} = 0.002 + 0.0005 = 0.0025\text{ kg}\cdot\text{m}^2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính quán tính tương đương nhìn từ trục khâu tải</h5>
              <p>Quán tính rotor phản xạ ra trục khâu tải sau hộp số:</p>
              <p>$$J_{m,refl} = N^2 \cdot J_m = 100^2 \times 0.002 = 20.0\text{ kg}\cdot\text{m}^2$$</p>
              <p>Tổng quán tính nhìn từ phía tải:</p>
              <p>$$J_{total,link} = J_{m,refl} + J_L = 20.0 + 5.0 = 25.0\text{ kg}\cdot\text{m}^2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Xác định tần số dao động tự nhiên của khớp</h5>
              <p>Độ quán tính rút gọn (reduced inertia) của hệ 2 khối lượng dao động:</p>
              <p>$$J_{red} = \frac{J_{m,refl} \cdot J_L}{J_{m,refl} + J_L} = \frac{20.0 \times 5.0}{25.0} = 4.0\text{ kg}\cdot\text{m}^2$$</p>
              <p>Tần số góc dao động tự nhiên:</p>
              <p>$$\omega_n = \sqrt{\frac{K}{J_{red}}} = \sqrt{\frac{4000}{4.0}} = \sqrt{1000} \approx 31.62\text{ rad/s}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Quy đổi tần số Hertz & Đánh giá an toàn</h5>
              <p>Tần số dao động tính theo Hertz:</p>
              <p>$$f_n = \frac{\omega_n}{2\pi} = \frac{31.62}{6.283} \approx 5.03\text{ Hz}$$</p>
              <p>Kết luận: Tần số cộng hưởng $5.03\text{ Hz}$ nằm trong dải tần hoạt động của robot, do đó vòng lặp vị trí bắt buộc phải trang bị bộ lọc Notch Filter để tránh kích động rung lắc phá hủy khớp.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-3-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Cấu Hình Transmission Trong ROS 2 Control</h4>
          <p>Khai báo thẻ `<transmission>` trong file robot URDF/XACRO để phần mềm `ros2_control` tự động ánh xạ tỷ số truyền và giới hạn mô-men giữa rotor và trục khâu:</p>
          <div class="code-card">
            <div class="code-header">
              <span>robot_transmission.xacro (URDF / ROS 2)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>&lt;transmission name="joint1_transmission"&gt;
  &lt;type&gt;transmission_interface/SimpleTransmission&lt;/type&gt;
  &lt;joint name="joint1"&gt;
    &lt;hardwareInterface&gt;hardware_interface/EffortJointInterface&lt;/hardwareInterface&gt;
  &lt;/joint&gt;
  &lt;actuator name="joint1_motor"&gt;
    &lt;mechanicalReduction&gt;100.0&lt;/mechanicalReduction&gt;
    &lt;hardwareInterface&gt;hardware_interface/EffortJointInterface&lt;/hardwareInterface&gt;
  &lt;/actuator&gt;
&lt;/transmission&gt;</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 04: Ma Sát Động LuGre & Hệ Truyền Động Thủy Lực
# ==============================================================================
ch04_sidebar = [
    {"id": "sec-4-1", "title": "4.1 Hiện tượng Ma sát Tĩnh & Hiệu ứng Stribeck"},
    {"id": "sec-4-2", "title": "4.2 Mô hình Vi gai Tiếp xúc Đàn hồi Dahl"},
    {"id": "sec-4-3", "title": "4.3 Mô hình Ma sát Động LuGre & Tính Thụ động"},
    {"id": "sec-4-4", "title": "4.4 Mô hình Đàn Dẻo Elasto-Plastic"},
    {"id": "sec-4-5", "title": "4.5 Thủy lực Robot: Xi-lanh & Van Servo"},
    {"id": "sec-4-sim", "title": "⚡ Mô phỏng Hiện tượng Dính - Trượt Stick-Slip"},
    {"id": "sec-4-worked", "title": "📐 Ví dụ Tính Số 4 Bước Dự Báo Ma Sát LuGre"},
    {"id": "sec-4-bridge", "title": "🛠️ Cầu nối ros2_control Friction Compensation"}
]

ch04_body = r"""
        <!-- 4.1 -->
        <h2 id="sec-4-1">4.1 Hiện Tượng Ma Sát Tĩnh (Stiction), Coulomb & Hiệu Ứng Stribeck</h2>
        <p>Ma sát là hiện tượng phi tuyến vật lý xuất hiện tại mọi bề mặt tiếp xúc cơ khí và ổ bi khớp robot. Ở trạng thái chuyển động dừng hoặc vận tốc cực thấp, lực ma sát thể hiện đường cong Stribeck với độ dốc âm (negative damping) đặc thù:</p>
        <div class="formula-hero">
          <div class="formula-title">Đường Cong Ma Sát Trạng Thái Dừng Stribeck</div>
          <div class="formula-math">
            $$F_{ss}(v) = \left[ F_c + (F_s - F_c) e^{-(v/v_s)^2} \right] \text{sgn}(v) + \sigma_2 v$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách tham số:</strong> $F_c$ là lực ma sát Coulomb; $F_s$ là lực ma sát tĩnh cực đại (stiction force, $F_s \gt F_c$); $v_s$ là vận tốc Stribeck đặc trưng; $\sigma_2$ là hệ số ma sát nhớt (viscous damping).
          </div>
        </div>

        <!-- 4.2 -->
        <h2 id="sec-4-2">4.2 Mô Hình Vi Gai Tiếp Xúc Đàn Hồi Dahl</h2>
        <p>Để giải quyết nhược điểm gián đoạn của hàm $\text{sgn}(v)$ gây lỗi số học khi mô phỏng số, Dahl đề xuất mô hình vi biến dạng đàn hồi: bề mặt tiếp xúc được coi như các vi gai (bristles) uốn cong như lò xo nhỏ trước khi trượt thực sự.</p>

        <!-- 4.3 -->
        <h2 id="sec-4-3">4.3 Mô Hình Ma Sát Động Học LuGre & Chứng Minh Tính Thụ Động</h2>
        <p>Mô hình LuGre (Lund-Grenoble model) là tiêu chuẩn vàng trong mô hình hóa ma sát khớp robot, kết hợp cả hiệu ứng đàn hồi vi gai Dahl, hiệu ứng Stribeck và trễ ma sát (frictional lag):</p>
        <div class="formula-hero">
          <div class="formula-title">Hệ Phương Trình Ma Sát Động Học LuGre</div>
          <div class="formula-math">
            $$\begin{cases}
              \frac{dz}{dt} = v - \frac{\sigma_0 |v|}{g(v)} z & (\text{Động học độ lệch vi gai } z) \\
              g(v) = F_c + (F_s - F_c) e^{-(v/v_s)^2} & (\text{Hàm bao Stribeck}) \\
              F_{fric} = \sigma_0 z + \sigma_1 \frac{dz}{dt} + \sigma_2 v & (\text{Tổng lực ma sát sinh ra})
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách tham số:</strong> $z(t)$ là biến trạng thái nội tại biểu thị độ uốn trung bình của vi gai tiếp xúc [m]; $\sigma_0$ là độ cứng đàn hồi vi gai [N/m]; $\sigma_1$ là hệ số giảm chấn vi mô [N·s/m]; $\sigma_2$ là hệ số ma sát nhớt [N·s/m]. Mô hình LuGre đã được Egeland & Gravdahl chứng minh thỏa mãn tính thụ động (passivity) với hàm lưu trữ $V(z) = \frac{1}{2} \sigma_0 z^2$.
          </div>
        </div>

        <!-- 4.4 -->
        <h2 id="sec-4-4">4.4 Mô Hình Đàn Dẻo Elasto-Plastic</h2>
        <p>Mô hình Elasto-Plastic phân tách chuyển vị của vi gai thành hai phần: thành phần đàn hồi hồi phục hoàn toàn $z_e$ và thành phần biến dạng dẻo trôi dạt vĩnh viễn $z_p$, triệt tiêu hoàn toàn hiện tượng trôi vị trí giả lập khi robot chịu tải trọng tĩnh.</p>

        <!-- 4.5 -->
        <h2 id="sec-4-5">4.5 Động Lực Học Hệ Thống Thủy Lực Robot</h2>
        <p>Đối với robot tải trọng siêu nặng (như robot công trình, robot cứu hộ hoặc tay máy tàu ngầm), hệ thống truyền động thủy lực được sử dụng nhờ mật độ công suất trên thể tích cực cao. Động lực học buồng xi-lanh thủy lực:</p>
        $$\frac{V_t}{4\beta} \frac{dP_L}{dt} = Q_L - C_{ip} P_L - A \dot{x}_p$$
        <p>với $P_L$ là chênh lệch áp suất buồng công tác, $\beta$ là mô-đun đàn hồi thể tích của dầu (bulk modulus), $Q_L$ là lưu lượng qua van servo tỷ lệ, và $A$ là diện tích pít-tông.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-4-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Hiện Tượng Dính - Trượt (Stick-Slip Friction)</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-04" width="700" height="280" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Vận tốc kéo trượt v: <input type="range" id="sim04-vel" min="0.005" max="0.2" step="0.005" value="0.05"> <span id="sim04-v-val">0.050 m/s</span></label>
            <label style="font-size: 0.85rem; font-weight: 600;">Độ cứng vi gai σ0: <input type="range" id="sim04-sigma" min="2000" max="20000" step="1000" value="10000"> <span id="sim04-s-val">10000 N/m</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-4-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Dự Báo Lực Ma Sát LuGre Trong Chu Trình Chuyển Động</h3>
          <p>Khâu robot di chuyển với vận tốc trượt tức thời $v = 0.02\text{ m/s}$. Các thông số mô hình ma sát LuGre được nhận dạng như sau: $F_c = 2.0\text{ N}$, $F_s = 4.5\text{ N}$, $v_s = 0.01\text{ m/s}$, $\sigma_0 = 10^5\text{ N/m}$, $\sigma_1 = 300\text{ N}\cdot\text{s/m}$, $\sigma_2 = 0.5\text{ N}\cdot\text{s/m}$. Giả sử độ biến dạng vi gai đang ở giá trị $z = 1.5 \times 10^{-5}\text{ m}$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính hàm bao Stribeck $g(v)$</h5>
              <p>Tỷ số vận tốc trượt trên vận tốc Stribeck: $\frac{v}{v_s} = \frac{0.02}{0.01} = 2.0$.</p>
              <p>Số mũ suy giảm: $e^{-(v/v_s)^2} = e^{-4} \approx 0.0183$.</p>
              <p>$$g(v) = 2.0 + (4.5 - 2.0) \times 0.0183 = 2.0 + 2.5 \times 0.0183 \approx 2.0458\text{ N}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính đạo hàm trạng thái vi gai $\dot{z}$</h5>
              <p>Áp dụng phương trình động học biến vi gai LuGre:</p>
              <p>$$\dot{z} = v - \frac{\sigma_0 |v|}{g(v)} z = 0.02 - \frac{10^5 \times 0.02}{2.0458} (1.5 \times 10^{-5})$$</p>
              <p>$$\dot{z} = 0.02 - \frac{2000 \times 1.5 \times 10^{-5}}{2.0458} = 0.02 - \frac{0.03}{2.0458} = 0.02 - 0.01466 = 0.00534\text{ m/s}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính toán từng thành phần lực ma sát</h5>
              <p>1. Lực đàn hồi vi gai: $F_{\sigma 0} = \sigma_0 z = 10^5 \times 1.5 \times 10^{-5} = 1.500\text{ N}$.</p>
              <p>2. Lực giảm chấn vi gai: $F_{\sigma 1} = \sigma_1 \dot{z} = 300 \times 0.00534 \approx 1.602\text{ N}$.</p>
              <p>3. Lực ma sát nhớt: $F_{\sigma 2} = \sigma_2 v = 0.5 \times 0.02 = 0.010\text{ N}$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Tổng hợp lực ma sát & Đánh giá</h5>
              <p>Tổng lực ma sát tác động lên khâu robot:</p>
              <p>$$F_{fric} = 1.500 + 1.602 + 0.010 = 3.112\text{ N}$$</p>
              <p>So sánh: Lực ma sát tĩnh cực đại là $4.5\text{ N}$, lực Coulomb trượt là $2.0\text{ N}$. Lực $3.112\text{ N}$ phản ánh chính xác trạng thái chuyển tiếp từ dính sang trượt hoàn toàn.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-4-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Bộ Bù Ma Sát LuGre Trong ros2_control</h4>
          <p>Triển khai thuật toán bù ma sát chuyển tiếp trước (Friction Feedforward) vào giao diện điều khiển lực `ros2_control` để triệt tiêu hiện tượng dính trượt:</p>
          <div class="code-card">
            <div class="code-header">
              <span>lugre_compensator.hpp (C++ / ros2_control)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>double computeLuGreTorque(double v, double &z, double dt) {
  const double Fc = 2.0, Fs = 4.5, vs = 0.01;
  const double sigma0 = 100000.0, sigma1 = 300.0, sigma2 = 0.5;
  
  double g_v = Fc + (Fs - Fc) * std::exp(-std::pow(v / vs, 2));
  double dz = v - (sigma0 * std::abs(v) / g_v) * z;
  z += dz * dt; // Euler integration of bristle state
  
  return sigma0 * z + sigma1 * dz + sigma2 * v;
}</code></pre>
          </div>
        </div>
"""

# Generate HTML files
print("Generating Ch 01...")
with open(os.path.join(CHAPTERS_DIR, "ch01.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("01", "Biểu Diễn Hệ Thống Hợp Nhất & Không Gian Trạng Thái", "Unified System Representation & State Space", "TRACK 1: CƠ SỞ & ĐỘNG HỌC", "track-1", "../index.html", "Lộ trình Tổng quan", "ch02.html", "Chương 02: Động Học Vật Rắn 3D", ch01_sidebar, ch01_body))

print("Generating Ch 02...")
with open(os.path.join(CHAPTERS_DIR, "ch02.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("02", "Động Học Vật Rắn 3D & Biến Đổi Tọa Độ Robot", "3D Rigid Body Kinematics & Manipulator Geometry", "TRACK 1: CƠ SỞ & ĐỘNG HỌC", "track-1", "ch01.html", "Chương 01: Biểu Diễn Hệ Thống", "ch03.html", "Chương 03: Động Lực Học Động Cơ", ch02_sidebar, ch02_body))

print("Generating Ch 03...")
with open(os.path.join(CHAPTERS_DIR, "ch03.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("03", "Động Lực Học Động Cơ & Khớp Đàn Hồi", "Electromechanical Actuators & Flexible Transmissions", "TRACK 2: CHẤP HÀNH & MA SÁT", "track-2", "ch02.html", "Chương 02: Động Học Vật Rắn 3D", "ch04.html", "Chương 04: Ma Sát Động LuGre", ch03_sidebar, ch03_body))

print("Generating Ch 04...")
with open(os.path.join(CHAPTERS_DIR, "ch04.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("04", "Ma Sát Động LuGre & Hệ Truyền Động Thủy Lực", "Dynamic Friction & Hydraulic Servo Systems", "TRACK 2: CHẤP HÀNH & MA SÁT", "track-2", "ch03.html", "Chương 03: Động Lực Học Động Cơ", "ch05.html", "Chương 05: Động Lực Học Newton-Euler", ch04_sidebar, ch04_body))

print("Successfully generated Chapters 01, 02, 03, 04!")
