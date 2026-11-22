# -*- coding: utf-8 -*-
"""
build_chapters_t5_t6.py
Biên soạn nội dung chuẩn 6 tầng tri thức cho Track 5 và Track 6 (Chương 09 - Chương 14):
- Ch 09: Học Bắt Chước Chỉ Từ Quan Sát (Imitation from Observation - IfO)
- Ch 10: Học Từ Chuyên Gia Lỗi & Ngoại Suy Phần Thưởng (T-REX & D-REX)
- Ch 11: Bất Đồng Hình Thái & Chuyển Đổi Sim-to-Real (Correspondence & Cross-Embodiment)
- Ch 12: Giao Diện HRI, Dạy Học Động Học & Tự Chủ Chia Sẻ (Shared Autonomy)
- Ch 13: Thước Đo Đánh Giá & Các Bộ Benchmark Tiêu Chuẩn (RoboMimic, DTW, Jerk)
- Ch 14: Kiến Trúc Triển Khai Thực Tế: HuggingFace LeRobot, ALOHA & ROS 2
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
            <span>📚 Nguồn tài liệu: <strong>Boyuan Zheng et al. (UTS 2021) & Carlos Celemin et al. (2022)</strong></span>
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
# CHƯƠNG 09: Học Bắt Chước Chỉ Từ Quan Sát (Imitation from Observation - IfO)
# ==============================================================================
ch09_sidebar = [
    {"id": "sec-9-1", "title": "9.1 Đặt Vấn Đề: Dữ Liệu Biểu Diễn Không Nhãn Hành Động"},
    {"id": "sec-9-2", "title": "9.2 Khung Toán Học IfO & Không Gian Quan Sát"},
    {"id": "sec-9-3", "title": "9.3 Thuật Toán BCO & Mô Hình Động Lực Học Nghịch"},
    {"id": "sec-9-4", "title": "9.4 Khớp Phân Phối Chuyển Dịch GAIfO"},
    {"id": "sec-9-sim", "title": "⚡ Mô Phỏng Suy Luận Hành Động BCO (Canvas)"},
    {"id": "sec-9-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Suy Luận Mô-men Khớp"},
    {"id": "sec-9-bridge", "title": "🛠️ Cầu Nối Kỹ Thuật: Pipeline Huấn Luyện BCO Trong Python"}
]

ch09_body = r"""
        <!-- 9.1 -->
        <h2 id="sec-9-1">9.1 Đặt Vấn Đề: Khai Thác Kho Tàng Video Khổng Lồ Không Có Nhãn Hành Động</h2>
        <p>Trong tất cả các thuật toán Imitation Learning truyền thống (BC, DAgger, IRL), một giả định cốt yếu luôn được đưa ra: <em>Tập dữ liệu phải chứa đầy đủ cặp trạng thái - hành động $(s, a)$.</em> Tuy nhiên, việc thu thập nhãn hành động thực tế (như góc quay động cơ, lực ép giác hút, mô-men xoắn) đòi hỏi hệ thống cảm biến phức tạp, đồ gá đắt tiền hoặc người làm mẫu phải đeo găng tay đo lực rườm rà.</p>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 HỌC TỪ QUAN SÁT (IfO) ĐỂ LÀM GÌ?</div>
          <div class="why-matters-body">
            Con người học được vô số kỹ năng chỉ bằng mắt nhìn: xem video dạy nấu ăn trên YouTube, quan sát thợ mộc cưa gỗ. Chúng ta không hề đo được áp lực cơ bắp hay tín hiệu thần kinh của họ. <strong>Imitation from Observation (IfO)</strong> cho phép robot bắt chước trực tiếp từ các chuỗi quan sát thuần túy $\mathcal{D}_O = \{(s_0, s_1, \dots, s_T)\}$ (video RGB, chuỗi tọa độ đám mây điểm 3D), mở ra khả năng khai thác toàn bộ kho tàng dữ liệu video mở trên Internet cho robot học.
          </div>
        </div>

        <!-- 9.2 -->
        <h2 id="sec-9-2">9.2 Khung Toán Học Imitation From Observation (IfO)</h2>
        <p>Tập dữ liệu biểu diễn của chuyên gia không còn nhãn hành động:</p>
        $$\mathcal{D}_E = \{\tau_1, \tau_2, \dots, \tau_N\}, \quad \tau_i = (s_0, s_1, s_2, \dots, s_{T_i}), \quad s_t \in \mathcal{S}$$
        <p>Mục tiêu của robot là tìm kiếm một chính sách $\pi_\theta(a \mid s)$ tương tác với môi trường MDP $\mathcal{M}$ (có không gian hành động $\mathcal{A}$ riêng của nó) sao cho chuỗi trạng thái sinh ra $P(\tau \mid \pi_\theta)$ khớp với phân phối trạng thái chuyên gia $P(\tau \mid \mathcal{D}_E)$.</p>

        <!-- 9.3 -->
        <h2 id="sec-9-3">9.3 Thuật Toán Behavioral Cloning From Observation (BCO)</h2>
        <p>Thuật toán <strong>BCO (Faraz Torabi et al., IJCAI 2018)</strong> giải quyết bài toán qua hai giai đoạn tự thân:</p>

        <div class="formula-hero">
          <div class="formula-title">1. Học Mô Hình Động Lực Học Nghịch Đảo (Inverse Dynamics Model)</div>
          <div class="formula-math">
            $$\hat{a}_t = f_\phi^{-1}(s_t, s_{t+1})$$
          </div>
          <div class="formula-legend">
            <strong>Cơ chế:</strong> Robot tự mình thực hiện các hành động ngẫu nhiên hoặc khám phá trong môi trường để thu thập dữ liệu tự thân $\mathcal{D}_{\text{self}} = \{(s_t, a_t, s_{t+1})\}$. Sau đó, mạng nơ-ron $f_\phi^{-1}$ học cách giải mã: <em>"Hành động $a_t$ nào đã khiến robot chuyển từ trạng thái $s_t$ sang $s_{t+1}$?"</em>
            $$\min_\phi \sum_{(s, a, s') \in \mathcal{D}_{\text{self}}} \| a - f_\phi^{-1}(s, s') \|^2$$
          </div>
        </div>

        <div class="formula-hero" style="margin-top: 1.5rem;">
          <div class="formula-title">2. Gán Nhãn Giả Cho Dữ Liệu Chuyên Gia & Huấn Luyện BC</div>
          <div class="formula-math">
            $$\mathcal{D}_{\text{labeled}} = \left\{ \left(s_t^E, f_\phi^{-1}(s_t^E, s_{t+1}^E)\right) \right\}$$
          </div>
          <div class="formula-legend">
            Dùng mô hình nghịch đảo đã học để gán nhãn hành động giả định $\hat{a}_t^E$ cho toàn bộ video mẫu của chuyên gia, sau đó huấn luyện chính sách $\pi_\theta(a \mid s)$ bằng Behavioral Cloning chuẩn. Quy trình được lặp lại nhiều vòng để cải thiện dần độ chính xác của $f_\phi^{-1}$.
          </div>
        </div>

        <!-- 9.4 -->
        <h2 id="sec-9-4">9.4 Khớp Phân Phối Chuyển Dịch Trạng Thái GAIfO</h2>
        <p>Bên cạnh BCO, trường phái đối nghịch phát triển thuật toán <strong>GAIfO (Generative Adversarial Imitation from Observation)</strong>. Thay vì phân biệt cặp $(s, a)$ như GAIL, Discriminator của GAIfO nhận đầu vào là cặp trạng thái chuyển tiếp liên tiếp $(s_t, s_{t+1})$:</p>
        $$\max_D \mathbb{E}_{\tau \sim \mathcal{D}_E} \left[ \log D(s_t, s_{t+1}) \right] + \mathbb{E}_{\tau \sim \pi_\theta} \left[ \log(1 - D(s_t, s_{t+1})) \right]$$
        <p>Discriminator đóng vai trò thẩm định xem sự biến đổi không gian giữa hai khung hình có tự nhiên và ăn khớp với cách chuyên gia dịch chuyển hay không.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-9-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Khôi Phục Hành Động Từ Cặp Quan Sát (BCO)</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-09" width="700" height="280" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-9-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Suy Luận Mô-men Khớp Từ Cặp Trạng Thái Khớp $(q_t, q_{t+1})$</h3>
          <p>Một khớp robot xoay có khối lượng quán tính $I = 0.5$ kg$\cdot$m$^2$, hệ số ma sát cản $b = 0.2$ Nms/rad, chu kỳ lấy mẫu $\Delta t = 0.02$ s. Từ video quan sát, góc khớp tại hai thời điểm liên tiếp là $q_t = 0.50$ rad và $q_{t+1} = 0.54$ rad. Vận tốc trước đó là $\dot{q}_t = 1.8$ rad/s. Giả sử gia tốc trong khoảng $\Delta t$ xấp xỉ không đổi, hãy dùng mô hình động lực học nghịch đảo giải tích tính mô-men xoắn $\hat{\tau}_t$ mà động cơ phải sinh ra.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính vận tốc trung bình và vận tốc tại thời điểm $t+1$</h5>
              <p>Vận tốc trung bình trong bước nhảy thời gian:</p>
              <p>$$\bar{v} = \frac{q_{t+1} - q_t}{\Delta t} = \frac{0.54 - 0.50}{0.02} = \frac{0.04}{0.02} = 2.0\text{ rad/s}$$</p>
              <p>Vận tốc cuối bước: $\dot{q}_{t+1} = 2 \bar{v} - \dot{q}_t = 2(2.0) - 1.8 = 2.2\text{ rad/s}$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính gia tốc góc của khớp $\ddot{q}_t$</h5>
              <p>$$\ddot{q}_t = \frac{\dot{q}_{t+1} - \dot{q}_t}{\Delta t} = \frac{2.2 - 1.8}{0.02} = \frac{0.4}{0.02} = 20.0\text{ rad/s}^2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Thiết lập phương trình động lực học nghịch đảo</h5>
              <p>Phương trình vi phân chuyển động của trục khớp đơn:</p>
              <p>$$\hat{\tau}_t = I \ddot{q}_t + b \dot{q}_t$$</p>
              <p>• Mô-men quán tính: $I \ddot{q} = 0.5 \times 20.0 = 10.0\text{ Nm}$</p>
              <p>• Mô-men ma sát cản: $b \dot{q} = 0.2 \times 1.8 = 0.36\text{ Nm}$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Tổng hợp mô-men suy luận $\hat{\tau}_t$ & Gán nhãn</h5>
              <p>$$\hat{\tau}_t = 10.0 + 0.36 = 10.36\text{ Nm}$$</p>
              <p>Cặp dữ liệu $(s_t, \hat{a}_t) = (0.50\text{ rad}, 10.36\text{ Nm})$ được bổ sung vào tập dữ liệu giám sát $\mathcal{D}_{\text{labeled}}$ để huấn luyện chính sách robot.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-9-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Huấn Luyện Mạng Động Lực Học Nghịch Đảo Trong PyTorch</h4>
          <p>Triển khai mô hình $f_\phi^{-1}(s, s')$ dự đoán vector điều khiển từ chuỗi chuyển trạng thái:</p>
          <div class="code-card">
            <div class="code-header">
              <span>inverse_dynamics_model.py (PyTorch)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import torch
import torch.nn as nn

class InverseDynamicsModel(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim * 2, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim)
        )
        self.optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        self.loss_fn = nn.MSELoss()

    def forward(self, s, s_next):
        x = torch.cat([s, s_next], dim=-1)
        return self.net(x)

    def train_step(self, s, a, s_next):
        pred_a = self.forward(s, s_next)
        loss = self.loss_fn(pred_a, a)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return loss.item()</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 10: Học Từ Chuyên Gia Lỗi & Ngoại Suy Phần Thưởng (T-REX & D-REX)
# ==============================================================================
ch10_sidebar = [
    {"id": "sec-10-1", "title": "10.1 Giới Hạn Của Giả Định Chuyên Gia Hoàn Hảo"},
    {"id": "sec-10-2", "title": "10.2 Mô Hình Xếp Hạng Quỹ Đạo Bradley-Terry"},
    {"id": "sec-10-3", "title": "10.3 Thuật Toán T-REX & D-REX Tạo Quỹ Đạo Suy Biến"},
    {"id": "sec-10-4", "title": "10.4 Hiện Tượng Ngoại Suy Vượt Trần (Super-Human)"},
    {"id": "sec-10-sim", "title": "⚡ Mô Phỏng Ngoại Suy Phần Thưởng T-REX (Canvas)"},
    {"id": "sec-10-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Cập Nhật Loss Bradley-Terry"},
    {"id": "sec-10-bridge", "title": "🛠️ Cầu Nối Kỹ Thuật: Loss Function Xếp Hạng Quỹ Đạo"}
]

ch10_body = r"""
        <!-- 10.1 -->
        <h2 id="sec-10-1">10.1 Thực Tế Khốc Liệt: Con Người Luôn Mắc Sai Lầm & Dữ Liệu Biểu Diễn Kém Hoàn Hảo</h2>
        <p>Hầu hết các lý thuyết IL đều giả định tập dữ liệu $\mathcal{D}_E$ được cung cấp bởi một chuyên gia tối ưu toàn diện (Optimal Oracle). Nhưng trong thực tế triển khai robot:</p>
        <ul>
          <li>Người điều khiển từ xa bị rung tay, mỏi mắt, hoặc phản xạ chậm.</li>
          <li>Dữ liệu thị phạm thu được từ nhiều người với trình độ và phong cách không đồng nhất (Suboptimal / Noisy Demonstrations).</li>
          <li>Nếu áp dụng Behavioral Cloning thuần túy, robot sẽ "sao chép trọn gói" cả các thói quen xấu và sai lầm chết người của người điều khiển.</li>
        </ul>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 T-REX & D-REX GIẢI QUYẾT BÀI TOÁN NÀY NHƯ THẾ NÀO?</div>
          <div class="why-matters-body">
            Phát minh đột phá của Daniel Brown et al. (ICML 2019) chứng minh rằng: <strong>Con người có thể làm mẫu dở, nhưng lại cực kỳ xuất sắc trong việc phân xử xem "quỹ đạo nào tốt hơn quỹ đạo nào".</strong>
            <br>Thay vì cố bắt chước trực tiếp các thao tác dở dang, thuật toán <strong>T-REX (Trajectory-ranked Reward EXtrapolation)</strong> chỉ cần danh sách xếp hạng chất lượng quỹ đạo $\tau_1 \prec \tau_2 \prec \dots \prec \tau_K$ để khôi phục hàm thưởng tiềm ẩn, và đặc biệt là có khả năng <em>ngoại suy (Extrapolate)</em> để huấn luyện robot đạt hiệu năng vượt xa chính người làm mẫu (Super-Human Performance)!
          </div>
        </div>

        <!-- 10.2 -->
        <h2 id="sec-10-2">10.2 Mô Hình Xác Suất Xếp Hạng Quỹ Đạo Bradley-Terry / Luce-Shepard</h2>
        <p>Giả sử ta có mạng nơ-ron tham số hóa hàm phần thưởng trạng thái $\hat{R}_\theta(s)$. Phần thưởng tích lũy của một quỹ đạo $\tau = (s_0, s_1, \dots, s_T)$ là:</p>
        $$\hat{R}_\theta(\tau) = \sum_{t=0}^T \hat{R}_\theta(s_t)$$
        <p>Theo mô hình lựa chọn xác suất Bradley-Terry, khi đem so sánh hai quỹ đạo $\tau_i$ và $\tau_j$, xác suất để chuyên gia đánh giá quỹ đạo $\tau_i$ vượt trội hơn $\tau_j$ ($\tau_i \succ \tau_j$) được biểu diễn bằng hàm Softmax mũ:</p>
        <div class="formula-hero">
          <div class="formula-title">Xác Suất Ưu Tiên Cặp Quỹ Đạo (Pairwise Preference)</div>
          <div class="formula-math">
            $$P(\tau_i \succ \tau_j \mid \theta) = \frac{\exp\left( \hat{R}_\theta(\tau_i) \right)}{\exp\left( \hat{R}_\theta(\tau_i) \right) + \exp\left( \hat{R}_\theta(\tau_j) \right)} = \frac{1}{1 + \exp\left( \hat{R}_\theta(\tau_j) - \hat{R}_\theta(\tau_i) \right)}$$
          </div>
          <div class="formula-legend">
            <strong>Hàm mất mát Binary Cross Entropy trên toàn bộ các cặp xếp hạng $\mathcal{P}$:</strong>
            $$\mathcal{L}(\theta) = -\sum_{(\tau_i \succ \tau_j) \in \mathcal{P}} \log P(\tau_i \succ \tau_j \mid \theta)$$
          </div>
        </div>

        <!-- 10.3 -->
        <h2 id="sec-10-3">10.3 Thuật Toán D-REX: Tự Sinh Chuỗi Suy Biến Bằng Nhiễu Động Không Cần Người Gán Nhãn</h2>
        <p>Nếu việc nhờ con người ngồi chấm điểm xếp hạng hàng ngàn cặp quỹ đạo vẫn còn tốn công sức, <strong>D-REX (Disturbance-based Reward EXtrapolation)</strong> tự động hóa hoàn toàn quá trình này:</p>
        <p>1. Lấy một vài quỹ đạo thị phạm sẵn có (dù chất lượng chỉ ở mức trung bình).</p>
        <p>2. Thêm dần các mức độ nhiễu Gauss $\epsilon \sim \mathcal{N}(0, \sigma_k^2 \mathbf{I})$ vào chính sách điều khiển với độ lệch chuẩn tăng dần: $\sigma_0 \lt \sigma_1 \lt \sigma_2 \lt \dots \lt \sigma_M$.</p>
        <p>3. Dễ dàng suy ra định đề hiển nhiên: Quỹ đạo bị nhiễu ít hơn chắc chắn sẽ tốt hơn quỹ đạo bị phá hoại bởi mức nhiễu lớn hơn:</p>
        $$\tau_{\sigma_M} \prec \dots \prec \tau_{\sigma_2} \prec \tau_{\sigma_1} \prec \tau_{\sigma_0}$$
        <p>Nhờ vậy, thuật toán tự động sinh ra hàng vạn cặp dữ liệu xếp hạng mà không cần con người can thiệp dù chỉ một giây!</p>

        <!-- 10.4 -->
        <h2 id="sec-10-4">10.4 Hiện Tượng Ngoại Suy Phần Thưởng Siêu Phàm (Super-Human Extrapolation)</h2>
        <p>Hàm phần thưởng $\hat{R}_\theta(s)$ học được từ mạng T-REX là một hàm tuyến tính hoặc phi tuyến trơn tru trong không gian trạng thái. Khi chạy RL tối ưu hóa hàm thưởng này, robot không bị chặn trần bởi quỹ đạo mẫu tốt nhất của chuyên gia, mà tiếp tục đẩy các trạng thái tích cực lên giá trị cực hạn, đạt điểm số cao hơn chuyên gia con người từ 150% đến 300% trên các môi trường thử nghiệm khắt khe.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-10-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Đường Ngoại Suy Phần Thưởng Vượt Trần Chuyên Gia (T-REX)</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-10" width="700" height="280" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-10-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Xác Suất Ưu Tiên & Gradient Cập Nhật Mạng Thưởng T-REX</h3>
          <p>Cho cặp quỹ đạo gồm $\tau_1$ (chuyên gia làm mẫu khá tốt) và $\tau_2$ (chuyên gia mắc lỗi trượt tay), với thứ bậc đã biết là $\tau_1 \succ \tau_2$. Mạng phần thưởng hiện tại ước lượng tổng điểm thưởng của hai quỹ đạo là $\hat{R}(\tau_1) = 4.2$ và $\hat{R}(\tau_2) = 3.0$. Vector đặc trưng tích lũy của hai quỹ đạo là $\Phi(\tau_1) = [6.0, 2.0]^T$ và $\Phi(\tau_2) = [4.0, 5.0]^T$. Tính xác suất ưu tiên $P(\tau_1 \succ \tau_2)$, tổn thất Cross-Entropy $\mathcal{L}$, và gradient cập nhật trọng số thưởng $\nabla_\theta \mathcal{L}$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính hiệu số phần thưởng ước lượng</h5>
              <p>$$\Delta R = \hat{R}(\tau_1) - \hat{R}(\tau_2) = 4.2 - 3.0 = +1.2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính xác suất dự đoán theo hàm Sigmoid</h5>
              <p>$$P = \sigma(\Delta R) = \frac{1}{1 + e^{-1.2}} = \frac{1}{1 + 0.3012} = \frac{1}{1.3012} \approx 0.7685$$</p>
              <p>Mạng hiện tại đánh giá xác suất $\tau_1 \succ \tau_2$ đạt $76.85\%$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính hàm tổn thất Binary Cross Entropy</h5>
              <p>$$\mathcal{L} = -\ln P = -\ln(0.7685) \approx 0.2633$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Tính gradient lan truyền ngược để cập nhật mạng thưởng</h5>
              <p>Đạo hàm tổn thất theo tham số thưởng (với mô hình tuyến tính $\hat{R} = \theta^T \Phi$):</p>
              <p>$$\nabla_\theta \mathcal{L} = -(1 - P) \cdot (\Phi(\tau_1) - \Phi(\tau_2))$$</p>
              <p>• Hiệu đặc trưng: $\Phi(\tau_1) - \Phi(\tau_2) = [6.0 - 4.0, 2.0 - 5.0]^T = [2.0, -3.0]^T$</p>
              <p>• Sai số xác suất: $1 - P = 1 - 0.7685 = 0.2315$</p>
              <p>$$\nabla_\theta \mathcal{L} = -0.2315 \times [2.0, -3.0]^T = [-0.463, +0.695]^T$$</p>
              <p>Cập nhật Gradient Descent: $\theta \leftarrow \theta - \eta \nabla \mathcal{L}$ sẽ tăng trọng số đặc trưng thứ nhất và giảm đặc trưng thứ hai.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-10-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Cài Đặt Hàm Mất Mát Xếp Hạng Quỹ Đạo Trong PyTorch</h4>
          <p>Đoạn mã tinh gọn thực thi tính toán Loss Function Bradley-Terry trên GPU:</p>
          <div class="code-card">
            <div class="code-header">
              <span>trex_ranking_loss.py (PyTorch)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import torch
import torch.nn as nn

class TREXRewardLoss(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, reward_net, traj_better, traj_worse):
        # traj_better: Tensor [B, T, obs_dim]
        # traj_worse: Tensor [B, T, obs_dim]
        r_better = torch.sum(reward_net(traj_better), dim=1) # [B, 1]
        r_worse = torch.sum(reward_net(traj_worse), dim=1)   # [B, 1]
        
        # Binary Cross Entropy Loss qua Sigmoid(r_better - r_worse)
        diff = r_better - r_worse
        loss = -torch.mean(torch.log(torch.sigmoid(diff) + 1e-8))
        return loss</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 11: Bất Đồng Hình Thái & Chuyển Đổi Sim-to-Real
# ==============================================================================
ch11_sidebar = [
    {"id": "sec-11-1", "title": "11.1 Bài Toán Bất Đồng Hình Thái (Correspondence Problem)"},
    {"id": "sec-11-2", "title": "11.2 Kinematic vs Dynamic Correspondence"},
    {"id": "sec-11-3", "title": "11.3 Chuyển Đổi Miền Sim-to-Real & Domain Randomization"},
    {"id": "sec-11-4", "title": "11.4 Cross-Embodiment Learning (Open X-Embodiment)"},
    {"id": "sec-11-sim", "title": "⚡ Mô Phỏng Đồng Bộ Cặp Điểm Bàn Tay - Tay Kẹp (Canvas)"},
    {"id": "sec-11-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Nghịch Đảo Jacobian Chuyển Tọa Độ"},
    {"id": "sec-11-bridge", "title": "🛠️ Cầu Nối ROS 2: Node Retargeting Từ MediaPipe Sang Robot"}
]

ch11_body = r"""
        <!-- 11.1 -->
        <h2 id="sec-11-1">11.1 Bài Toán Bất Đồng Hình Thái (The Correspondence Problem) Là Gì?</h2>
        <p>Khi con người làm mẫu cho robot, một rào cản vật lý tự nhiên xuất hiện: <strong>Cơ thể người và robot hoàn toàn khác nhau về mặt cơ sinh học.</strong></p>
        <ul>
          <li>Bàn tay người có 27 bậc tự do (DOF) với các khớp linh hoạt và đầu ngón tay mềm có độ bám dính cao.</li>
          <li>Tay kẹp robot công nghiệp phổ biến chỉ có 1 bậc tự do đóng mở song song (Parallel-jaw Gripper) hoặc 3 ngón cứng.</li>
          <li>Chiều dài cánh tay, giới hạn góc quay khớp, và giới hạn gia tốc mô-men động cơ hoàn toàn không tương thích.</li>
        </ul>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 GIẢI PHÁP CHO BÀI TOÁN TƯƠNG ỨNG HÌNH THÁI</div>
          <div class="why-matters-body">
            Bài toán ánh xạ từ không gian hành động chuyên gia $\mathcal{A}_E$ sang không gian robot $\mathcal{A}_R$ được chia thành:
            <br>1. <strong>Kinematic Correspondence (Ánh xạ Động học):</strong> Bỏ qua hình dáng khớp bên trong, chỉ đồng bộ hóa vị trí và hướng của điểm tiếp xúc công tác (End-Effector Pose Tracking).
            <br>2. <strong>Contact-Point Correspondence (Tương ứng Điểm Tiếp Xúc):</strong> Thay vì bắt chước cả bàn tay, chỉ đồng bộ hóa lực ép và khoảng cách giữa hai đầu ngón tay cái và trỏ với hai má kẹp của robot.
          </div>
        </div>

        <!-- 11.2 -->
        <h2 id="sec-11-2">11.2 Chuyển Đổi Miền Thực - Ảo (Sim-to-Real Transfer) & Domain Randomization</h2>
        <p>Thu thập hàng vạn giờ biểu diễn trên robot thật là cực kỳ tốn kém và mòn hỏng cơ khí. Do đó, phần lớn dữ liệu thị phạm được tạo trong môi trường mô phỏng vật lý (Isaac Gym, MuJoCo, PyBullet). Tuy nhiên, khi đưa chính sách đã học sang robot thật, hiện tượng <strong>Reality Gap (Khoảng cách Thực tế)</strong> làm chính sách thất bại vì khác biệt ánh sáng, độ ma sát bề mặt, và độ trễ động cơ.</p>
        <p>Kỹ thuật <strong>Domain Randomization (DR)</strong> giải quyết bài toán này bằng cách biến đổi ngẫu nhiên toàn bộ các tham số vật lý trong mỗi màn mô phỏng:</p>
        $$m \sim \mathcal{U}(0.8 m_0, 1.2 m_0), \quad \mu_{\text{friction}} \sim \mathcal{U}(0.2, 0.9), \quad \tau_{\text{delay}} \sim \mathcal{U}(0\text{ ms}, 40\text{ ms})$$
        <p>Chính sách học được sẽ buộc phải hội tụ về một chiến lược điều khiển bền vững, thích nghi ngay lập tức khi thả vào thế giới thực mà không cần tinh chỉnh lại (Zero-shot Sim-to-Real).</p>

        <!-- 11.3 -->
        <h2 id="sec-11-3">11.3 Kỷ Nguyên Cross-Embodiment Learning (Open X-Embodiment / RT-X)</h2>
        <p>Năm 2023 - 2024 đánh dấu bước nhảy vọt với sáng kiến <strong>Open X-Embodiment</strong> (Google DeepMind hợp tác với 33 phòng lab toàn cầu): Tập hợp hơn 1 triệu quỹ đạo biểu diễn từ 22 dòng robot hoàn toàn khác nhau (từ Franka Emika, UR5, ALOHA đến Google Robot). Bằng cách chuẩn hóa không gian hành động thành vận tốc di chuyển 6D của bàn kẹp $\Delta x, \Delta y, \Delta z, \Delta \text{roll}, \Delta \text{pitch}, \Delta \text{yaw}$ cộng với trạng thái kẹp, một mô hình thị giác - ngôn ngữ - hành động duy nhất (VLA Model) có thể điều khiển đa dạng các loại robot khác nhau một cách linh hoạt.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-11-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Ánh Xạ Điểm Tiếp Xúc Bàn Tay Người Sang Tay Kẹp Song Song</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-11" width="700" height="280" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-11-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Vận Tốc Khớp $\dot{q}$ Bằng Nghịch Đảo Ma Trận Jacobian $\mathbf{J}^{-1}$ Khi Theo Dõi Bàn Tay Người</h3>
          <p>Camera theo dõi bàn tay con người ghi nhận vận tốc điểm đầu ngón tay trong không gian Descartes 2D là $\mathbf{v}_{\text{human}} = [0.08, -0.04]^T$ m/s. Robot 2 khớp có chiều dài các khâu $l_1 = 0.4$ m, $l_2 = 0.3$ m, đang ở cấu hình góc khớp $q_1 = 30^\circ$ ($0.5236$ rad), $q_2 = 45^\circ$ ($0.7854$ rad). Ma trận Jacobian tính được tại điểm này là:
          $$\mathbf{J} = \begin{bmatrix} -0.412 & -0.212 \\ 0.559 & 0.212 \end{bmatrix}$$
          Tính định thức $\det(\mathbf{J})$, nghịch đảo $\mathbf{J}^{-1}$, và vector vận tốc góc đặt cho các khớp robot $\dot{\mathbf{q}}$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính định thức của ma trận Jacobian 2x2</h5>
              <p>$$\det(\mathbf{J}) = (-0.412)(0.212) - (-0.212)(0.559)$$</p>
              <p>• $(-0.412) \times 0.212 = -0.087344$</p>
              <p>• $(-0.212) \times 0.559 = -0.118508$</p>
              <p>$$\det(\mathbf{J}) = -0.087344 - (-0.118508) = +0.031164 \neq 0$$</p>
              <p>Hệ thống không nằm ở điểm kỳ dị (Singularity), có thể nghịch đảo an toàn.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tìm ma trận nghịch đảo $\mathbf{J}^{-1}$</h5>
              <p>$$\mathbf{J}^{-1} = \frac{1}{\det(\mathbf{J})} \begin{bmatrix} J_{22} & -J_{12} \\ -J_{21} & J_{11} \end{bmatrix} = \frac{1}{0.031164} \begin{bmatrix} 0.212 & 0.212 \\ -0.559 & -0.412 \end{bmatrix}$$</p>
              <p>$$\mathbf{J}^{-1} \approx \begin{bmatrix} 6.803 & 6.803 \\ -17.937 & -13.220 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Thực hiện phép nhân ma trận để tìm vận tốc khớp $\dot{\mathbf{q}}$</h5>
              <p>$$\dot{\mathbf{q}} = \mathbf{J}^{-1} \mathbf{v}_{\text{human}} = \begin{bmatrix} 6.803 & 6.803 \\ -17.937 & -13.220 \end{bmatrix} \begin{bmatrix} 0.08 \\ -0.04 \end{bmatrix}$$</p>
              <p>• $\dot{q}_1 = 6.803(0.08) + 6.803(-0.04) = 6.803 \times 0.04 = +0.2721\text{ rad/s}$</p>
              <p>• $\dot{q}_2 = -17.937(0.08) - 13.220(-0.04) = -1.4350 + 0.5288 = -0.9062\text{ rad/s}$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Kiểm tra giới hạn vận tốc và đóng gói lệnh điều khiển</h5>
              <p>Vận tốc tính toán: $\dot{q}_1 \approx 0.27$ rad/s, $\dot{q}_2 \approx -0.91$ rad/s đều nằm an toàn trong giới hạn động cơ servo ($|\dot{q}| \le 2.5$ rad/s). Lệnh này được gửi tới bộ điều khiển vị trí vòng kín với tần số cao.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-11-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Retargeting Node Từ Cảm Biến Không Gian Sang Khớp ROS 2</h4>
          <p>Mã nguồn chuyển đổi tọa độ từ camera thị giác bám tay sang lệnh dịch chuyển tay máy:</p>
          <div class="code-card">
            <div class="code-header">
              <span>hand_retargeting_node.py (ROS 2 / Python)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32MultiArray
import numpy as np

class HandRetargetingNode(Node):
    def __init__(self):
        super().__init__('hand_retargeting_node')
        self.sub_hand = self.create_subscription(Point, '/camera/hand_position', self.hand_cb, 10)
        self.pub_joints = self.create_publisher(Float32MultiArray, '/robot/target_joint_angles', 10)
        self.scale_factor = np.array([1.2, 1.2, 0.8]) # Co dãn không gian thao tác

    def hand_cb(self, msg):
        human_pos = np.array([msg.x, msg.y, msg.z])
        # Ánh xạ tỉ lệ không gian làm việc
        robot_target_cartesian = human_pos * self.scale_factor
        # Giải động học nghịch (IK)
        target_joints = self.solve_ik(robot_target_cartesian)
        
        out_msg = Float32MultiArray()
        out_msg.data = target_joints.tolist()
        self.pub_joints.publish(out_msg)

    def solve_ik(self, pos):
        # Bộ giải IK xấp xỉ
        return np.clip(pos * 1.5, -2.8, 2.8)</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 12: Giao Diện HRI, Dạy Học Động Học & Tự Chủ Chia Sẻ (Shared Autonomy)
# ==============================================================================
ch12_sidebar = [
    {"id": "sec-12-1", "title": "12.1 Các Giao Diện HRI Thu Thập Biểu Diễn Mẫu"},
    {"id": "sec-12-2", "title": "12.2 Dạy Học Động Học & Gravity Compensation"},
    {"id": "sec-12-3", "title": "12.3 Khung Toán Học Tự Chủ Chia Sẻ (Shared Autonomy)"},
    {"id": "sec-12-4", "title": "12.4 Bộ Điều Khiển Trộn Tín Hiệu Alpha-Blending"},
    {"id": "sec-12-sim", "title": "⚡ Mô Phỏng Tự Chủ Chia Sẻ Alpha-Blending (Canvas)"},
    {"id": "sec-12-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Trộn Tín Hiệu u = α u_h + (1-α) u_r"},
    {"id": "sec-12-bridge", "title": "🛠️ Cầu Nối C++ / ROS 2: Node Bù Trọng Lực Cho Cầm Tay Chỉ Việc"}
]

ch12_body = r"""
        <!-- 12.1 -->
        <h2 id="sec-12-1">12.1 Các Giao Diện Tương Tác Người - Robot (HRI) Trong Thu Thập Dữ Liệu</h2>
        <p>Chất lượng của dữ liệu học bắt chước phụ thuộc trực tiếp vào tính công thái học (Ergonomics) và độ trực quan của giao diện truyền lệnh từ con người sang robot. Ba phương thức chủ đạo hiện nay:</p>
        <table class="academic-table" style="width:100%; margin: 1.5rem 0; border-collapse: collapse;">
          <thead>
            <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
              <th style="padding: 0.75rem;">Phương Thức</th>
              <th style="padding: 0.75rem;">Cơ Chế Kỹ Thuật</th>
              <th style="padding: 0.75rem;">Ưu Điểm</th>
              <th style="padding: 0.75rem;">Nhược Điểm</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Kinesthetic Teaching (Cầm tay chỉ việc)</strong></td>
              <td style="padding: 0.75rem;">Người trực tiếp cầm nắm thân robot, kích hoạt chế độ bù trọng lực (Zero-gravity mode)</td>
              <td style="padding: 0.75rem;">Trực quan 100%, ghi lại chính xác góc quay mọi khớp</td>
              <td style="padding: 0.75rem;">Người che khuất tầm nhìn camera, khó thao tác tốc độ cao</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Leader-Follower Teleoperation</strong></td>
              <td style="padding: 0.75rem;">Người cầm một cánh tay dẫn động nhỏ (Puppet/Leader) truyền tín hiệu sang cánh tay chính (Follower)</td>
              <td style="padding: 0.75rem;">Không che khuất camera, thu thập dữ liệu tự nhiên, giá thành thấp</td>
              <td style="padding: 0.75rem;">Người cần luyện tập phối hợp mắt - tay để làm quen</td>
            </tr>
            <tr>
              <td style="padding: 0.75rem;"><strong>Giao Diện Không Gian VR / AR</strong></td>
              <td style="padding: 0.75rem;">Kính VR theo dõi tay trong không gian 6D và truyền lệnh qua mạng không dây</td>
              <td style="padding: 0.75rem;">Thao tác từ xa xuyên lục địa, hiển thị trực quan lớp giao diện số</td>
              <td style="padding: 0.75rem;">Độ trễ mạng gây khó khăn khi thao tác vật thể nhỏ</td>
            </tr>
          </tbody>
        </table>

        <!-- 12.2 -->
        <h2 id="sec-12-2">12.2 Khái Niệm Tự Chủ Chia Sẻ (Shared Autonomy)</h2>
        <div class="why-matters-box">
          <div class="why-matters-header">💡 TỰ CHỦ CHIA SẺ (SHARED AUTONOMY) ĐỂ LÀM GÌ?</div>
          <div class="why-matters-body">
            Trong nhiều tác vụ phức tạp, con người cung cấp ý định cấp cao (High-level Intent) nhưng lại dễ mắc lỗi thao tác chi tiết (run tay, phản xạ trễ). Ngược lại, robot có năng lực cảm biến laser/camera phản xạ cực nhanh nhưng lại không hiểu mục đích tổng quát. <strong>Tự Chủ Chia Sẻ (Shared Autonomy)</strong> hòa trộn hai nguồn lực: con người chỉ huy hướng đi, còn thuật toán tự động đảm bảo an toàn cơ học và bám quỹ đạo chính xác.
          </div>
        </div>

        <!-- 12.3 -->
        <h2 id="sec-12-3">12.3 Bộ Điều Khiển Trộn Tín Hiệu Alpha-Blending</h2>
        <p>Lệnh điều khiển cuối cùng $u_t$ gửi tới động cơ robot là tổ hợp lồi giữa tín hiệu con người $u_h$ và tín hiệu can thiệp an toàn của robot $u_r$:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Trộn Tín Hiệu Tuyến Tính $\alpha$-Blending</div>
          <div class="formula-math">
            $$u_t = \alpha_t u_{\text{human}} + (1 - \alpha_t) u_{\text{robot}}$$
          </div>
          <div class="formula-legend">
            <strong>Cơ chế điều tiết động của trọng số $\alpha_t \in [0, 1]$:</strong>
            <br>• Khi robot ở trong vùng không gian thoáng và an toàn: $\alpha_t \to 1.0$ (Trao toàn quyền quyết định cho con người).
            <br>• Khi robot tiến sát vật cản hoặc vượt quá giới hạn mô-men động cơ: $\alpha_t \to 0.0$ (Bộ điều khiển an toàn Control Barrier Function - CBF tự động can thiệp triệt để để chặn va chạm).
          </div>
        </div>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-12-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Bộ Điều Khiển Tự Chủ Chia Sẻ $\alpha$-Blending Trong Hành Lang Hẹp</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-12" width="700" height="280" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Hệ số quyền con người $\alpha$: <input type="range" id="sim12-alpha" min="0.0" max="1.0" step="0.05" value="0.6"> <span id="sim12-a-val">Trọng số người α = 0.60</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-12-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Lực Điều Khiển Trộn $\alpha$-Blending Khi Can Thiệp Nguy Cơ Va Chạm</h3>
          <p>Một xe tự hành AGV đang di chuyển trong hành lang có trục giữa an toàn tại $y_{\text{safe}} = 0.0$ m, hai bên tường tại $y = \pm 0.5$ m. Người lái xe do mất tập trung đang đánh lái sang phải với lệnh vận tốc $v_{y, \text{human}} = +0.6$ m/s, vị trí xe hiện tại là $y = 0.35$ m (rất sát tường nguy hiểm). Robot kích hoạt bộ điều khiển an toàn hồi vị $v_{y, \text{robot}} = -K_p (y - y_{\text{safe}})$ với $K_p = 2.0\text{ s}^{-1}$. Trọng số can thiệp an toàn được tính theo khoảng cách tới tường: $\alpha(y) = \max\left(0, \frac{0.5 - |y|}{0.5 - 0.2}\right)$. Tính trọng số $\alpha$, lệnh của robot, và vận tốc trộn thực thi $v_{y, \text{final}}$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính lệnh vận tốc an toàn của robot</h5>
              <p>$$v_{y, \text{robot}} = -2.0 \times (0.35 - 0.0) = -0.70\text{ m/s}$$</p>
              <p>Robot chủ động sinh vận tốc kéo ngược vào giữa hành lang.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính trọng số quyền con người $\alpha$</h5>
              <p>Khoảng cách an toàn còn lại: $0.5 - 0.35 = 0.15$ m.</p>
              <p>$$\alpha = \frac{0.15}{0.30} = 0.50$$</p>
              <p>Tại vị trí này, quyền điều khiển được chia đều 50-50 giữa người và thuật toán.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính vận tốc trộn $\alpha$-Blending thực thi</h5>
              <p>$$v_{y, \text{final}} = \alpha v_{y, \text{human}} + (1 - \alpha) v_{y, \text{robot}}$$</p>
              <p>$$v_{y, \text{final}} = 0.50 \times (+0.60) + (1 - 0.50) \times (-0.70)$$</p>
              <p>$$v_{y, \text{final}} = +0.30 - 0.35 = -0.05\text{ m/s}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Nhận định kết quả thực thi cơ học</h5>
              <p>Nhờ lực hãm can thiệp của robot, vận tốc sang phải nguy hiểm của người lái $+0.60$ m/s đã bị vô hiệu hóa hoàn toàn và đảo chiều thành $-0.05$ m/s, giúp xe từ từ lùi ra xa bức tường mà người lái vẫn cảm nhận được vô lăng tự điều chỉnh mượt mà không bị khựng giật.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-12-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Bù Trọng Lực Thời Gian Thực (Gravity Compensation) Trong C++</h4>
          <p>Thuật toán bù trọng lực $\mathbf{\tau}_{\text{cmd}} = \mathbf{G}(\mathbf{q})$ cho phép người dùng nhấc bổng cánh tay robot bằng một ngón tay:</p>
          <div class="code-card">
            <div class="code-header">
              <span>gravity_compensation_controller.cpp (ROS 2 / C++)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>#include &lt;rclcpp/rclcpp.hpp&gt;
#include &lt;sensor_msgs/msg/joint_state.hpp&gt;
#include &lt;std_msgs/msg/float64_multi_array.hpp&gt;
#include &lt;vector&gt;
#include &lt;cmath&gt;

class GravityCompensationController : public rclcpp::Node {
public:
  GravityCompensationController() : Node("gravity_compensation_controller") {
    sub_joints_ = this->create_subscription&lt;sensor_msgs::msg::JointState&gt;(
      "/joint_states", 10, std::bind(&GravityCompensationController::jointCallback, this, std::placeholders::_1));
    pub_torques_ = this->create_publisher&lt;std_msgs::msg::Float64MultiArray&gt;("/forward_effort_controller/commands", 10);
  }

private:
  void jointCallback(const sensor_msgs::msg::JointState::SharedPtr msg) {
    std_msgs::msg::Float64MultiArray torque_msg;
    // Mô hình hóa ma trận trọng lực G(q) cho khớp 2 và 3
    double q2 = msg->position[1];
    double q3 = msg->position[2];
    double tau_g2 = 14.5 * std::cos(q2) + 4.2 * std::cos(q2 + q3);
    double tau_g3 = 4.2 * std::cos(q2 + q3);

    torque_msg.data = {0.0, tau_g2, tau_g3, 0.0, 0.0, 0.0};
    pub_torques_->publish(torque_msg);
  }
  rclcpp::Subscription&lt;sensor_msgs::msg::JointState&gt;::SharedPtr sub_joints_;
  rclcpp::Publisher&lt;std_msgs::msg::Float64MultiArray&gt;::SharedPtr pub_torques_;
};</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 13: Thước Đo Đánh Giá & Các Bộ Benchmark Tiêu Chuẩn Trong Robot Học
# ==============================================================================
ch13_sidebar = [
    {"id": "sec-13-1", "title": "13.1 Các Chỉ Số Đánh Giá Thành Công & Sai Lệch Quỹ Đạo"},
    {"id": "sec-13-2", "title": "13.2 Dynamic Time Warping (DTW) & Fréchet Distance"},
    {"id": "sec-13-3", "title": "13.3 Chỉ Số An Toàn Cơ Học & Rung Giật (Jerk Metric)"},
    {"id": "sec-13-4", "title": "13.4 Các Bộ Benchmark Tiêu Chuẩn: RoboMimic & RLBench"},
    {"id": "sec-13-sim", "title": "⚡ Mô Phỏng So Sánh DTW & Jerk Metric (Canvas)"},
    {"id": "sec-13-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Ma Trận Quy Hoạch Động DTW"},
    {"id": "sec-13-bridge", "title": "🛠️ Cầu Nối Kỹ Thuật: Script Đánh Giá Quỹ Đạo Robot Trong Python"}
]

ch13_body = r"""
        <!-- 13.1 -->
        <h2 id="sec-13-1">13.1 Tại Sao Chỉ Đo Tỷ Lệ Hoàn Thành Tác Vụ (Success Rate) Là Chưa Đủ?</h2>
        <p>Trong các bài báo khoa học về học bắt chước, chỉ số phổ biến nhất được báo cáo là <strong>Task Success Rate</strong> (Tỷ lệ gắp trúng đích / tổng số lần thử). Tuy nhiên, một chính sách đạt 95% tỷ lệ thành công vẫn có thể là một chính sách tồi tệ trong công nghiệp vì:</p>
        <ul>
          <li><strong>Rung giật cơ khí:</strong> Động cơ phát ra tiếng kêu rít, giật cục liên tục làm mòn bánh răng giảm tốc Harmonic sau vài tuần.</li>
          <li><strong>Không tự nhiên:</strong> Quỹ đạo đi vòng vèo, kỳ dị làm người đứng cạnh cảm thấy bất an.</li>
          <li><strong>Thời gian chu kỳ dài:</strong> Mất 30 giây để hoàn thành tác vụ mà con người chỉ làm trong 2 giây.</li>
        </ul>

        <!-- 13.2 -->
        <h2 id="sec-13-2">13.2 Đo Lường Sai Lệch Hình Dáng: Dynamic Time Warping (DTW)</h2>
        <p>Hai quỹ đạo thực thi và biểu diễn mẫu thường có tốc độ khác nhau. Khoảng cách Euclidean thông thường $\sum_t \|x_t - y_t\|^2$ hoàn toàn thất bại nếu một quỹ đạo chỉ đơn giản là đi chậm hơn 0.1 giây. <strong>Dynamic Time Warping (DTW)</strong> tìm kiếm đường căn chỉnh tối ưu $\mathcal{W}$ giữa hai chuỗi thời gian có độ dài khác nhau:</p>
        $$\text{DTW}(P, Q) = \min_{W} \sqrt{\sum_{k=1}^K c(w_k)}$$
        <p>với ma trận chi phí tích lũy được giải bằng quy hoạch động 2D $D(i, j) = \|p_i - q_j\| + \min(D(i-1, j), D(i, j-1), D(i-1, j-1))$.</p>

        <!-- 13.3 -->
        <h2 id="sec-13-3">13.3 Chỉ Số An Toàn Cơ Học: Tích Phân Giật Jerk Metric</h2>
        <p>Để đánh giá độ êm ái và bảo vệ hộp số động cơ robot, <strong>Chỉ số Jerk (Đạo hàm bậc 3 của vị trí)</strong> được sử dụng làm chuẩn mực vàng trong điều khiển robot:</p>
        <div class="formula-hero">
          <div class="formula-title">Định Nghĩa Chỉ Số Rung Giật Jerk Metric</div>
          <div class="formula-math">
            $$\text{Jerk} = \int_0^T \| \dddot{q}(t) \|^2 dt \approx \sum_{k=1}^{N-2} \left\| \frac{\ddot{q}_{k+1} - \ddot{q}_k}{\Delta t} \right\|^2 \Delta t$$
          </div>
          <div class="formula-legend">
            <strong>Ý nghĩa vật lý:</strong> Jerk là tốc độ biến thiên của gia tốc. Khi Jerk cao, lực tác động lên các bánh răng và liên kết cơ khí biến đổi đột ngột, gây ứng suất phá hủy cấu trúc vật liệu. Một chính sách học bắt chước xuất sắc bắt buộc phải có chỉ số Jerk xấp xỉ quỹ đạo mượt mà của con người.
          </div>
        </div>

        <!-- 13.4 -->
        <h2 id="sec-13-4">13.4 Các Bộ Benchmark Chuẩn Mực Trong Giới Nghiên Cứu</h2>
        <p>1. <strong>RoboMimic (Mandlekar et al., CoRL 2021):</strong> Cung cấp tập dữ liệu chuẩn hóa đa dạng các cấp độ chuyên gia (Proficient-Human, Multi-Human, Ph-Better, Machine-Generated) trên các tác vụ kinh điển như Can, Square, Transport.</p>
        <p>2. <strong>RLBench (James et al., IEEE RA-L 2020):</strong> Môi trường mô phỏng trên CoppeliaSim với hơn 100 tác vụ thao tác cánh tay robot 7 bậc tự do.</p>
        <p>3. <strong>ALOHA Bimanual Benchmark:</strong> Thử nghiệm thao tác hai tay tinh xảo (xỏ chỉ luồn kim, bấm khóa kéo túi xách) trên phần cứng thật.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-13-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Căn Chỉnh Quỹ Đạo Bằng Dynamic Time Warping (DTW) & Chỉ Số Jerk</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-13" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-13-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Ma Trận Quy Hoạch Động DTW 3x3 Giữa Hai Quỹ Đạo 1D</h3>
          <p>Cho quỹ đạo mẫu chuyên gia $X = [1.0, 3.0, 4.0]$ và quỹ đạo robot $Y = [1.0, 2.0, 4.0]$. Hàm chi phí điểm là khoảng cách trị tuyệt đối $c(x_i, y_j) = |x_i - y_j|$. Tính ma trận chi phí cục bộ $\mathbf{C}$, ma trận tích lũy $\mathbf{D}$, và chi phí DTW tổng thể tối ưu.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Lập ma trận chi phí cục bộ $C(i, j) = |X_i - Y_j|$</h5>
              <p>• Hàng 1 ($X_1 = 1.0$): $|1-1|=0, |1-2|=1, |1-4|=3 \Rightarrow [0, 1, 3]$</p>
              <p>• Hàng 2 ($X_2 = 3.0$): $|3-1|=2, |3-2|=1, |3-4|=1 \Rightarrow [2, 1, 1]$</p>
              <p>• Hàng 3 ($X_3 = 4.0$): $|4-1|=3, |4-2|=2, |4-4|=0 \Rightarrow [3, 2, 0]$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Khởi tạo hàng 1 và cột 1 ma trận tích lũy $D$</h5>
              <p>• $D(1, 1) = C(1, 1) = 0$</p>
              <p>• $D(1, 2) = D(1, 1) + C(1, 2) = 0 + 1 = 1$</p>
              <p>• $D(1, 3) = D(1, 2) + C(1, 3) = 1 + 3 = 4$</p>
              <p>• $D(2, 1) = D(1, 1) + C(2, 1) = 0 + 2 = 2$</p>
              <p>• $D(3, 1) = D(2, 1) + C(3, 1) = 2 + 3 = 5$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Điền các ô còn lại theo công thức $D(i, j) = C(i, j) + \min(D_{i-1, j}, D_{i, j-1}, D_{i-1, j-1})$</h5>
              <p>• Ô $(2, 2)$: $C(2, 2) + \min(D_{1,2}, D_{2,1}, D_{1,1}) = 1 + \min(1, 2, 0) = 1 + 0 = 1$</p>
              <p>• Ô $(2, 3)$: $C(2, 3) + \min(D_{1,3}, D_{2,2}, D_{1,2}) = 1 + \min(4, 1, 1) = 1 + 1 = 2$</p>
              <p>• Ô $(3, 2)$: $C(3, 2) + \min(D_{2,2}, D_{3,1}, D_{2,1}) = 2 + \min(1, 5, 2) = 2 + 1 = 3$</p>
              <p>• Ô $(3, 3)$: $C(3, 3) + \min(D_{2,3}, D_{3,2}, D_{2,2}) = 0 + \min(2, 3, 1) = 0 + 1 = 1$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Kết luận khoảng cách DTW tối ưu</h5>
              <p>Giá trị tại ô góc phải dưới: $$D(3, 3) = 1.0$$</p>
              <p>Khoảng cách căn chỉnh tối ưu theo thời gian giữa robot và người là $1.0$, minh chứng hai quỹ đạo có hình dạng gần như đồng nhất tuyệt đối dù có độ lệch tốc độ ở bước trung gian.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-13-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Module Đánh Giá Tự Động Chỉ Số Jerk & DTW Trong Python</h4>
          <p>Mã nguồn chuẩn kiểm thử chất lượng quỹ đạo thu được từ dữ liệu thực nghiệm:</p>
          <div class="code-card">
            <div class="code-header">
              <span>trajectory_evaluator.py (Python)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import numpy as np
from scipy.spatial.distance import cdist

def compute_jerk(trajectory, dt=0.02):
    # trajectory: numpy array [T, DOF]
    vel = np.gradient(trajectory, dt, axis=0)
    acc = np.gradient(vel, dt, axis=0)
    jerk = np.gradient(acc, dt, axis=0)
    # Tích phân Jerk metric: tổng bình phương chia thời gian
    return np.mean(np.sum(jerk**2, axis=-1))

def fast_dtw(traj_a, traj_b):
    # traj_a: [N, D], traj_b: [M, D]
    cost_matrix = cdist(traj_a, traj_b, metric='euclidean')
    N, M = cost_matrix.shape
    D = np.zeros((N, M))
    D[0, 0] = cost_matrix[0, 0]
    for i in range(1, N): D[i, 0] = D[i-1, 0] + cost_matrix[i, 0]
    for j in range(1, M): D[0, j] = D[0, j-1] + cost_matrix[0, j]
    for i in range(1, N):
        for j in range(1, M):
            D[i, j] = cost_matrix[i, j] + min(D[i-1, j], D[i, j-1], D[i-1, j-1])
    return D[-1, -1]</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 14: Kiến Trúc Triển Khai Thực Tế: HuggingFace LeRobot, ALOHA & ROS 2
# ==============================================================================
ch14_sidebar = [
    {"id": "sec-14-1", "title": "14.1 Hệ Sinh Thái HuggingFace LeRobot & Chuẩn ALOHA"},
    {"id": "sec-14-2", "title": "14.2 Vòng Lặp Suy Luận 50 Hz & Đồng Bộ Cảm Biến"},
    {"id": "sec-14-3", "title": "14.3 Chuẩn Đóng Gói Dữ Liệu Zarr / Parquet / Codec AV1"},
    {"id": "sec-14-4", "title": "14.4 Tích Hợp Toàn Diện LeRobot Với ROS 2 Humble"},
    {"id": "sec-14-sim", "title": "⚡ Mô Phỏng Vòng Lặp Suy Luận 50 Hz Thực Tế (Canvas)"},
    {"id": "sec-14-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Băng Thông & Độ Trễ Đường Truyền"},
    {"id": "sec-14-bridge", "title": "🛠️ Cầu Nối ROS 2 Hoàn Chỉnh: Node Điều Khiển LeRobot ALOHA"}
]

ch14_body = r"""
        <!-- 14.1 -->
        <h2 id="sec-14-1">14.1 Hệ Sinh Thái Mã Nguồn Mở SOTA: HuggingFace LeRobot & Phần Cứng ALOHA</h2>
        <p>Năm 2024, thế giới Robotics chứng kiến một cuộc cách mạng tương tự như những gì Hugging Face Transformers đã làm cho Xử lý Ngôn ngữ Tự nhiên: <strong>Dự án Hugging Face LeRobot (Cadene et al., 2024)</strong> chính thức chuẩn hóa toàn bộ ngăn xếp công nghệ của Robot Manipulation:</p>
        <ul>
          <li><strong>Mô hình SOTA tích hợp sẵn:</strong> ACT (Action Chunking Transformers), Diffusion Policy, TD-MPC, VQ-BeT.</li>
          <li><strong>Khả năng tái lập phần cứng giá rẻ:</strong> Hỗ trợ hệ thống cánh tay robot hai tay ALOHA ($20,000 USD thay vì $200,000 USD của cánh tay công nghiệp) và Koch Arm ($300 USD cho học sinh sinh viên).</li>
          <li><strong>Chia sẻ mô hình & Trọng số trực tiếp:</strong> Đẩy và tải các checkpoint chính sách đã huấn luyện lên Hugging Face Hub bằng một dòng lệnh đơn giản.</li>
        </ul>

        <!-- 14.2 -->
        <h2 id="sec-14-2">14.2 Vòng Lặp Điều Khiển Thời Gian Thực 50 Hz (50 Hz Real-Time Execution Loop)</h2>
        <p>Để robot thao tác vật thể mềm mại và phản xạ kịp thời với ngoại cảnh, vòng lặp điều khiển bắt buộc phải giữ vững tần số <strong>50 Hz</strong> (chu kỳ lấy mẫu mục tiêu $\Delta t = 20$ ms):</p>
        <div class="formula-hero">
          <div class="formula-title">Phân Bổ Ngân Sách Thời Gian Trong 1 Chu Kỳ 20 ms</div>
          <div class="formula-math">
            $$\Delta t_{\text{total}} = \Delta t_{\text{cam}} + \Delta t_{\text{inference}} + \Delta t_{\text{comm}} + \Delta t_{\text{motor}} \le 20.0\text{ ms}$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách từng mili-giây sống còn:</strong>
            <br>• $\Delta t_{\text{cam}} \approx 6 - 8$ ms: Chụp và giải mã khung hình đa luồng từ 3-4 camera USB/RealSense (cổ tay, góc nhìn chính diện).
            <br>• $\Delta t_{\text{inference}} \approx 7 - 10$ ms: Chạy mạng nơ-ron sâu trên card đồ họa NVIDIA RTX 4090 / Orin thông qua bộ tối ưu hóa TensorRT FP16 để dự đoán chunk hành động.
            <br>• $\Delta t_{\text{comm}} \approx 1 - 2$ ms: Truyền dữ liệu qua cổng nối tiếp USB-to-RS485 tới bus servo Dynamixel.
            <br>• $\Delta t_{\text{motor}} \approx 2$ ms: Bộ điều khiển PID phần cứng đọc phản hồi encoder và xuất dòng điện lái cuộn cảm.
          </div>
        </div>

        <!-- 14.3 -->
        <h2 id="sec-14-3">14.3 Chuẩn Đóng Gói Dữ Liệu Zarr, Parquet & Video Codec Nén Tối Đa</h2>
        <p>Hàng ngàn giờ video độ phân giải cao sẽ làm nghẽn hoàn toàn đường truyền đĩa cứng nếu dùng định dạng ảnh rời rạc thông thường. Chuẩn LeRobot sử dụng:</p>
        <p>• <strong>Video MP4 / Codec AV1:</strong> Nén video nhiều góc quay với tỉ lệ nén gấp 50 lần mà không giảm độ nét không gian.</p>
        <p>• <strong>Định dạng Zarr & Apache Parquet:</strong> Cho phép truy xuất ngẫu nhiên đa luồng không đồng bộ (Asynchronous Multithreaded Slicing) trực tiếp vào GPU VRAM, triệt tiêu thời gian chờ nạp dữ liệu khi huấn luyện mạng lớn.</p>

        <!-- 14.4 -->
        <h2 id="sec-14-4">14.4 Kiến Trúc Hệ Thống: Cầu Nối Giữa ROS 2 Humble & LeRobot Inference Service</h2>
        <p>Trong môi trường sản xuất thực tế, việc ghép nối giữa ngăn xếp ROS 2 (chịu trách nhiệm quản lý phần cứng, an toàn, lập bản đồ) và LeRobot (chạy mô hình học sâu) được thực hiện qua cơ chế ZeroMQ / Shared Memory hoặc ROS 2 Custom Node để đảm bảo độ trễ thấp nhất dưới 1 ms.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-14-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Giám Sát Độ Trễ Vòng Lặp Điều Khiển ALOHA 50 Hz (20 ms Ticker)</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-14" width="700" height="280" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-14-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Băng Thông Dữ Liệu & Khả Năng Đáp Ứng Thời Gian Thực 50 Hz</h3>
          <p>Hệ thống robot hai tay ALOHA trang bị 4 camera màu RGB kích thước $640 \times 480$, độ sâu màu 24-bit (3 byte/pixel), tốc độ quay 50 FPS. Cùng lúc đó, 14 động cơ servo Dynamixel truyền dữ liệu vị trí và dòng điện ở tần số 50 Hz (mỗi động cơ chiếm 16 byte/mẫu). Tính thông lượng dữ liệu camera thô (Raw Camera Bandwidth), thông lượng dữ liệu servo, tổng băng thông USB cần thiết, và đánh giá xem cổng USB 3.0 (5 Gbps) có bị nghẽn không.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính kích thước 1 khung hình và thông lượng 1 camera</h5>
              <p>• Số byte của 1 khung hình $640 \times 480$: $640 \times 480 \times 3\text{ bytes} = 921,600\text{ bytes} \approx 0.9216\text{ MB}$</p>
              <p>• Thông lượng 1 camera ở 50 FPS: $0.9216\text{ MB} \times 50 = 46.08\text{ MB/s}$ ($368.64\text{ Mbps}$)</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính tổng thông lượng của toàn bộ 4 camera</h5>
              <p>$$\text{BW}_{\text{cameras}} = 4 \times 46.08\text{ MB/s} = 184.32\text{ MB/s} \approx 1.475\text{ Gbps}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính thông lượng dữ liệu mạng truyền động cơ servo</h5>
              <p>• Dữ liệu 1 mẫu từ 14 động cơ: $14 \times 16\text{ bytes} = 224\text{ bytes}$</p>
              <p>• Thông lượng servo ở 50 Hz: $224 \times 50 = 11,200\text{ bytes/s} \approx 11.2\text{ KB/s}$ (Rất nhỏ so với camera)</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Đánh giá khả năng đáp ứng phần cứng</h5>
              <p>Tổng băng thông dữ liệu hệ thống: $\approx 1.48$ Gbps.</p>
              <p>Cổng USB 3.0 tiêu chuẩn hỗ trợ tối đa 5.0 Gbps (băng thông hữu dụng thực tế $\sim 3.2$ Gbps). Như vậy, $1.48 \lt 3.2$ Gbps, hệ thống hoàn toàn đảm bảo đường truyền trơn tru mà không bị trễ rơi khung hình (Frame Drop), thỏa mãn hoàn hảo điều kiện hoạt động 50 Hz thời gian thực.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-14-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Node ROS 2 Hoàn Chỉnh Thực Thi Action Chunking LeRobot Ở 50 Hz</h4>
          <p>Mã nguồn chuẩn tích hợp suy luận mô hình ACT / Diffusion Policy với hệ thống tay kẹp qua ROS 2:</p>
          <div class="code-card">
            <div class="code-header">
              <span>lerobot_ros2_controller.py (ROS 2 Humble / PyTorch)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from cv_bridge import CvBridge
import torch
import numpy as np

class LeRobotInferenceNode(Node):
    def __init__(self):
        super().__init__('lerobot_inference_node')
        self.bridge = CvBridge()
        self.latest_image = None
        self.latest_joints = None
        
        # Đăng ký nhận ảnh camera và trạng thái khớp
        self.sub_cam = self.create_subscription(Image, '/camera/top/image_raw', self.cam_cb, 1)
        self.sub_joints = self.create_subscription(JointState, '/joint_states', self.joint_cb, 1)
        self.pub_action = self.create_publisher(JointTrajectory, '/leader_follower/commands', 1)
        
        # Hẹn giờ vòng lặp điều khiển 50 Hz (0.02s)
        self.timer = self.create_timer(0.02, self.control_loop)
        self.action_buffer = []

    def cam_cb(self, msg):
        self.latest_image = self.bridge.imgmsg_to_cv2(msg, 'rgb8')

    def joint_cb(self, msg):
        self.latest_joints = np.array(msg.position[:6])

    def control_loop(self):
        if self.latest_image is None or self.latest_joints is None:
            return
            
        # Nếu bộ đệm rỗng, chạy suy luận Action Chunk mới (16 bước)
        if len(self.action_buffer) == 0:
            # Chạy mô hình PyTorch GPU
            action_chunk = self.predict_chunk(self.latest_image, self.latest_joints)
            self.action_buffer = list(action_chunk)
            
        # Lấy hành động bước tiếp theo từ bộ đệm (Temporal Execution)
        target_joint_step = self.action_buffer.pop(0)
        
        # Đóng gói và phát xung ROS 2
        cmd = JointTrajectory()
        pt = JointTrajectoryPoint()
        pt.positions = target_joint_step.tolist()
        cmd.points.append(pt)
        self.pub_action.publish(cmd)

    def predict_chunk(self, img, joints):
        # Giả lập mô hình ACT suy luận 16 bước tương lai
        return np.tile(joints, (16, 1)) + np.random.normal(0, 0.005, (16, 6))

def main():
    rclpy.init()
    node = LeRobotInferenceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# Generate HTML files for Track 5 and Track 6
# ==============================================================================
print("Generating Ch 09...")
with open(os.path.join(CHAPTERS_DIR, "ch09.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("09", "Học Bắt Chước Chỉ Từ Quan Sát (Imitation from Observation - IfO)", "Imitation from Observation, BCO & Inverse Dynamics", "TRACK 5: QUAN SÁT & CHÊNH LỆCH MIỀN", "track-5", "ch08.html", "Chương 08: Học Bắt Chước Đối Nghịch GAIL", "ch10.html", "Chương 10: Chuyên Gia Lỗi & T-REX", ch09_sidebar, ch09_body))

print("Generating Ch 10...")
with open(os.path.join(CHAPTERS_DIR, "ch10.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("10", "Học Từ Chuyên Gia Lỗi & Ngoại Suy Phần Thưởng (T-REX & D-REX)", "Reward Extrapolation from Suboptimal Demonstrations", "TRACK 5: QUAN SÁT & CHÊNH LỆCH MIỀN", "track-5", "ch09.html", "Chương 09: Học Bắt Chước Từ Quan Sát", "ch11.html", "Chương 11: Bất Đồng Hình Thái & Sim-to-Real", ch10_sidebar, ch10_body))

print("Generating Ch 11...")
with open(os.path.join(CHAPTERS_DIR, "ch11.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("11", "Bất Đồng Hình Thái & Chuyển Đổi Sim-to-Real", "The Correspondence Problem, Domain Adaptation & Cross-Embodiment", "TRACK 5: QUAN SÁT & CHÊNH LỆCH MIỀN", "track-5", "ch10.html", "Chương 10: Chuyên Gia Lỗi & T-REX", "ch12.html", "Chương 12: Giao Diện HRI & Shared Autonomy", ch11_sidebar, ch11_body))

print("Generating Ch 12...")
with open(os.path.join(CHAPTERS_DIR, "ch12.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("12", "Giao Diện HRI, Dạy Học Động Học & Tự Chủ Chia Sẻ (Shared Autonomy)", "Kinesthetic Teaching, Teleoperation & Shared Autonomy", "TRACK 6: HRI, BENCHMARKS & TRIỂN KHAI THỰC TẾ", "track-6", "ch11.html", "Chương 11: Bất Đồng Hình Thái & Sim-to-Real", "ch13.html", "Chương 13: Thước Đo Đánh Giá & Benchmarks", ch12_sidebar, ch12_body))

print("Generating Ch 13...")
with open(os.path.join(CHAPTERS_DIR, "ch13.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("13", "Thước Đo Đánh Giá & Các Bộ Benchmark Tiêu Chuẩn Trong Robot Học", "Evaluation Metrics, DTW, Jerk & Standardization Benchmarks", "TRACK 6: HRI, BENCHMARKS & TRIỂN KHAI THỰC TẾ", "track-6", "ch12.html", "Chương 12: Giao Diện HRI & Shared Autonomy", "ch14.html", "Chương 14: Kiến Trúc LeRobot & ALOHA 50Hz", ch13_sidebar, ch13_body))

print("Generating Ch 14...")
with open(os.path.join(CHAPTERS_DIR, "ch14.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("14", "Kiến Trúc Triển Khai Thực Tế: HuggingFace LeRobot, ALOHA & ROS 2", "Production Deployment, LeRobot, ALOHA Hardware & ROS 2 Loop", "TRACK 6: HRI, BENCHMARKS & TRIỂN KHAI THỰC TẾ", "track-6", "ch13.html", "Chương 13: Thước Đo Đánh Giá & Benchmarks", "../index.html", "Lộ trình Tổng quan", ch14_sidebar, ch14_body))

print("Successfully generated Chapters 09, 10, 11, 12, 13, 14 for Imitation Learning!")
