# -*- coding: utf-8 -*-
"""
build_chapters_t1_t2.py
Biên soạn nội dung chuẩn 6 tầng tri thức cho Track 1 và Track 2 (Chương 01 - Chương 04):
- Ch 01: Giới Thiệu Học Bắt Chước & Khung Quyết Định Toán Học
- Ch 02: Nhân Bản Hành Vi (BC) & Tích Lũy Sai Số Covariate Shift
- Ch 03: Phản Hồi Đánh Giá (Evaluative) & RLHF Trong Robot (TAMER/COACH)
- Ch 04: Phản Hồi Hiệu Chỉnh & Họ Thuật Toán DAgger / SafeDAgger
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
            <span>📚 Nguồn tài liệu: <strong>Carlos Celemin et al. (FnT Robotics 2022) & Boyuan Zheng et al. (2021)</strong></span>
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
# CHƯƠNG 01: Giới Thiệu Học Bắt Chước & Khung Quyết Định Toán Học
# ==============================================================================
ch01_sidebar = [
    {"id": "sec-1-1", "title": "1.1 Bối cảnh & So sánh IL vs RL"},
    {"id": "sec-1-2", "title": "1.2 Tiêu chí Hiệu quả Mẫu & An toàn Cơ khí"},
    {"id": "sec-1-3", "title": "1.3 Khung Toán học Markov Decision Process (MDP)"},
    {"id": "sec-1-4", "title": "1.4 Tập Dữ liệu Biểu diễn Chuyên gia D_E"},
    {"id": "sec-1-5", "title": "1.5 Phân loại 3 Trường phái: BC, IRL và IIL"},
    {"id": "sec-1-sim", "title": "⚡ Mô phỏng 3 Trường Phái IL (Canvas)"},
    {"id": "sec-1-worked", "title": "📐 Ví dụ Tính Số 4 Bước Phân Phối Quỹ Đạo"},
    {"id": "sec-1-bridge", "title": "🛠️ Cầu nối Khởi tạo Dataset HDF5 Trong Python"}
]

ch01_body = r"""
        <!-- 1.1 -->
        <h2 id="sec-1-1">1.1 Bối Cảnh Lịch Sử & So Sánh Học Bắt Chước (IL) vs Học Tăng Cường (RL)</h2>
        <p>Học Bắt Chước (Imitation Learning - IL), còn được gọi là Học qua Thị phạm (Learning from Demonstration - LfD) hay Lập trình bằng Thị phạm (Programming by Demonstration - PbD), là phương pháp luận cho phép robot tiếp thu các kỹ năng vận động phức tạp trực tiếp từ dữ liệu thực nghiệm của con người mà không cần kỹ sư phải lập trình tường minh từng dòng lệnh điều khiển.</p>
        
        <div class="why-matters-box">
          <div class="why-matters-header">💡 Ý NGHĨA & TẠI SAO CẦN HỌC BẮT CHƯỚC?</div>
          <div class="why-matters-body">
            Trong Học Tăng Cường (Reinforcement Learning - RL), robot phải tự khám phá hành vi thông qua hàng triệu lần thử và sai (trial-and-error). Điều này hoàn toàn bất khả thi hoặc nguy hiểm trên phần cứng robot thật vì có thể phá hủy động cơ, va chạm môi trường, và việc thiết kế hàm phần thưởng toán học (Reward Engineering) cho các tác vụ khéo léo (như cắm cáp, gắp vật mềm) là cực kỳ khó khăn. Học Bắt Chước giải quyết triệt để vấn đề này bằng cách tận dụng trực tiếp tri thức thị phạm của chuyên gia.
          </div>
        </div>

        <table class="academic-table" style="width:100%; margin: 1.5rem 0; border-collapse: collapse;">
          <thead>
            <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
              <th style="padding: 0.75rem;">Đặc Tính Kỹ Thuật</th>
              <th style="padding: 0.75rem;">Học Tăng Cường (RL)</th>
              <th style="padding: 0.75rem;">Học Bắt Chước (IL)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Nguồn học tập</strong></td>
              <td style="padding: 0.75rem;">Hàm phần thưởng $R(s, a)$ thiết kế thủ công</td>
              <td style="padding: 0.75rem;">Tập biểu diễn mẫu của chuyên gia $\mathcal{D}_E$</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Hiệu quả mẫu (Sample Efficiency)</strong></td>
              <td style="padding: 0.75rem;">Thấp ($10^6 \sim 10^8$ bước tương tác thử-sai)</td>
              <td style="padding: 0.75rem;">Rất cao ($10 \sim 100$ quỹ đạo thị phạm)</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>An toàn cơ khí</strong></td>
              <td style="padding: 0.75rem;">Nguy hiểm khi khám phá ngẫu nhiên trên robot thật</td>
              <td style="padding: 0.75rem;">An toàn tuyệt đối do bám sát hành vi chuyên gia</td>
            </tr>
            <tr>
              <td style="padding: 0.75rem;"><strong>Trần hiệu năng</strong></td>
              <td style="padding: 0.75rem;">Có thể vượt qua con người (Super-human)</td>
              <td style="padding: 0.75rem;">Thường bị chặn bởi chất lượng người làm mẫu</td>
            </tr>
          </tbody>
        </table>

        <!-- 1.2 -->
        <h2 id="sec-1-2">1.2 Khung Toán Học: Quá Trình Quyết Định Markov (MDPs)</h2>
        <p>Hệ thống tương tác giữa robot và môi trường được chuẩn hóa bằng một Quá trình Quyết định Markov (Markov Decision Process - MDP) biểu diễn bởi bộ 5 thành phần:</p>
        <div class="formula-hero">
          <div class="formula-title">Định Nghĩa Quá Trình Quyết Định Markov $\mathcal{M}$</div>
          <div class="formula-math">
            $$\mathcal{M} = \langle \mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma \rangle$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách tham số:</strong>
            <br>• $\mathcal{S}$: Không gian trạng thái (góc khớp, vận tốc, ảnh camera, vị trí vật thể).
            <br>• $\mathcal{A}$: Không gian hành động (mô-men khớp $\tau$, vận tốc góc đặt, độ mở tay gắp).
            <br>• $\mathcal{P}(s' \mid s, a)$: Xác suất chuyển trạng thái mô tả động lực học của robot và môi trường.
            <br>• $\mathcal{R}(s, a)$: Hàm phần thưởng (thường <em>ẩn không biết trước</em> trong bài toán IL).
            <br>• $\gamma \in [0, 1)$: Hệ số chiết khấu thời gian.
          </div>
        </div>

        <!-- 1.3 -->
        <h2 id="sec-1-3">1.3 Tập Dữ Liệu Biểu Diễn Chuyên Gia $\mathcal{D}_E$</h2>
        <p>Tập dữ liệu chuyên gia gồm $N$ quỹ đạo được ghi nhận từ người làm mẫu:</p>
        $$\mathcal{D}_E = \{\tau_1, \tau_2, \dots, \tau_N\}, \quad \tau_i = (s_0, a_0, s_1, a_1, \dots, s_{T_i})$$
        <p>Xác suất sinh ra một quỹ đạo $\tau$ theo chính sách chuyên gia $\pi_E(a \mid s)$ và động lực học môi trường:</p>
        $$P(\tau \mid \pi_E) = \rho_0(s_0) \prod_{t=0}^{T-1} \pi_E(a_t \mid s_t) \mathcal{P}(s_{t+1} \mid s_t, a_t)$$

        <!-- 1.4 -->
        <h2 id="sec-1-4">1.4 Phân Loại 3 Trường Phái Lớn Trong Học Bắt Chước</h2>
        <p>Theo khảo cứu chuẩn mực của Carlos Celemin và Boyuan Zheng, các thuật toán học bắt chước được chia thành 3 trường phái chính:</p>
        <p>1. <strong>Nhân bản hành vi (Behavioral Cloning - BC):</strong> Coi bài toán như học có giám sát (Supervised Learning) ánh xạ trực tiếp từ trạng thái sang hành động $\pi_\theta: s \mapsto a$. Không cần tương tác với môi trường trong lúc học.</p>
        <p>2. <strong>Học tăng cường nghịch đảo (Inverse RL - IRL):</strong> Khôi phục hàm phần thưởng ẩn $R(s, a)$ giải thích vì sao chuyên gia lại hành động như vậy, sau đó dùng RL tối ưu hóa chính sách bám theo phần thưởng đó.</p>
        <p>3. <strong>Học bắt chước tương tác (Interactive IL - IIL):</strong> Đưa con người vào vòng lặp học tập thời gian thực (Human-in-the-loop), chuyên gia liên tục can thiệp sửa sai hoặc cung cấp phản hồi đánh giá khi robot gặp tình huống nguy cấp.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-1-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: So Sánh 3 Trường Phái BC vs IRL vs IIL</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-01" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Chọn trường phái: 
              <select id="sim01-type" style="padding: 0.25rem 0.5rem; border-radius: 4px; background: var(--card-bg); color: var(--text-color); border: 1px solid var(--border-color);">
                <option value="bc">Behavioral Cloning (BC) - Học Giám Sát</option>
                <option value="irl">Inverse RL (IRL) - Khôi Phục Phần Thưởng</option>
                <option value="iil">Interactive IL (IIL) - Người Kèm Trực Tuyến</option>
              </select>
            </label>
            <label style="font-size: 0.85rem; font-weight: 600;">Số lượng mẫu N: <input type="range" id="sim01-demos" min="2" max="50" step="2" value="10"> <span id="sim01-demos-val">10 biểu diễn</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-1-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Xác Suất Quỹ Đạo Chuyên Gia Trong MDP Rời Rạc</h3>
          <p>Xét một robot di động trong lưới 3 trạng thái $S=\{s_1, s_2, s_3\}$ với 2 hành động $A=\{a_1, a_2\}$. Trạng thái khởi đầu $s_1$ với xác suất $\rho_0(s_1) = 1.0$. Chính sách chuyên gia là $\pi_E(a_1 \mid s_1) = 0.8$, $\pi_E(a_2 \mid s_1) = 0.2$; tại $s_2$ chuyên gia chọn $\pi_E(a_1 \mid s_2) = 0.9$. Xác suất động học chuyển dịch: $\mathcal{P}(s_2 \mid s_1, a_1) = 0.85$, $\mathcal{P}(s_3 \mid s_2, a_1) = 0.95$. Tính xác suất xuất hiện quỹ đạo mẫu $\tau = (s_1, a_1, s_2, a_1, s_3)$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tách các thừa số xác suất theo công thức nhân</h5>
              <p>Phân tích xác suất quỹ đạo $\tau$ theo xích Markov:</p>
              <p>$$P(\tau) = \rho_0(s_1) \cdot \pi_E(a_1 \mid s_1) \cdot \mathcal{P}(s_2 \mid s_1, a_1) \cdot \pi_E(a_1 \mid s_2) \cdot \mathcal{P}(s_3 \mid s_2, a_1)$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Thay thế các giá trị xác suất thành phần</h5>
              <p>• Phân phối ban đầu: $\rho_0(s_1) = 1.0$</p>
              <p>• Hành động bước 1: $\pi_E(a_1 \mid s_1) = 0.80$</p>
              <p>• Chuyển trạng thái bước 1: $\mathcal{P}(s_2 \mid s_1, a_1) = 0.85$</p>
              <p>• Hành động bước 2: $\pi_E(a_1 \mid s_2) = 0.90$</p>
              <p>• Chuyển trạng thái bước 2: $\mathcal{P}(s_3 \mid s_2, a_1) = 0.95$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Thực hiện phép nhân số học</h5>
              <p>$$P(\tau) = 1.0 \times 0.80 \times 0.85 \times 0.90 \times 0.95$$</p>
              <p>$$0.80 \times 0.85 = 0.680$$</p>
              <p>$$0.680 \times 0.90 = 0.612$$</p>
              <p>$$P(\tau) = 0.612 \times 0.95 = 0.5814$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Diễn giải ý nghĩa & Log-Likelihood</h5>
              <p>Xác suất sinh ra quỹ đạo là $58.14\%$.</p>
              <p>Log-Likelihood của quỹ đạo:</p>
              <p>$$\log P(\tau) = \ln(0.5814) \approx -0.5423$$</p>
              <p>Giá trị này dùng làm hàm mục tiêu trong thuật toán Maximum Likelihood để tối ưu hóa trọng số mạng nơ-ron chính sách.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-1-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Cấu Trúc Lưu Trữ Quỹ Đạo Chuẩn HDF5 / Zarr</h4>
          <p>Tập dữ liệu biểu diễn $\mathcal{D}_E$ trong các thư viện SOTA (RoboMimic, LeRobot) được đóng gói trong tệp HDF5 phân cấp để đọc nạp siêu tốc vào bộ nhớ GPU:</p>
          <div class="code-card">
            <div class="code-header">
              <span>create_dataset.py (Python / HDF5)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import h5py
import numpy as np

def save_demonstration(filename, demo_id, states, actions):
    with h5py.File(filename, "a") as f:
        grp = f.create_group(f"data/demo_{demo_id}")
        grp.create_dataset("obs/joint_positions", data=np.array(states, dtype=np.float32))
        grp.create_dataset("actions", data=np.array(actions, dtype=np.float32))
        grp.attrs["num_samples"] = len(actions)
    print(f"Saved demo_{demo_id} with {len(actions)} steps.")</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 02: Nhân Bản Hành Vi (BC) & Tích Lũy Sai Số Covariate Shift
# ==============================================================================
ch02_sidebar = [
    {"id": "sec-2-1", "title": "2.1 Behavioral Cloning dưới góc nhìn Supervised Learning"},
    {"id": "sec-2-2", "title": "2.2 Chứng minh Toán học Sai số Tích lũy O(T²ε)"},
    {"id": "sec-2-3", "title": "2.3 Hiện tượng Causal Confusion trong Điều khiển Thị giác"},
    {"id": "sec-2-4", "title": "2.4 Các Giải pháp Chống Trôi: Jittering & Action Chunking"},
    {"id": "sec-2-sim", "title": "⚡ Mô phỏng Lệch Phân Phối Covariate Shift (Canvas)"},
    {"id": "sec-2-worked", "title": "📐 Ví dụ Tính Số 4 Bước Cận Sai Số Tích Lũy"},
    {"id": "sec-2-bridge", "title": "🛠️ Cầu nối Huấn Luyện Behavioral Cloning với PyTorch"}
]

ch02_body = r"""
        <!-- 2.1 -->
        <h2 id="sec-2-1">2.1 Nhân Bản Hành Vi (BC) Dưới Góc Nhìn Học Có Giám Sát</h2>
        <p>Nhân bản hành vi (Behavioral Cloning - BC) do Pomerleau đề xuất lần đầu năm 1989 (hệ thống ALVINN lái xe tự hành). Ý tưởng cốt lõi: coi bài toán tìm chính sách $\pi_\theta(a \mid s)$ như một bài toán hồi quy (Regression) hoặc phân loại (Classification) có giám sát thông thường:</p>
        <div class="formula-hero">
          <div class="formula-title">Hàm Mục Tiêu Tối Ưu Hóa Của Behavioral Cloning</div>
          <div class="formula-math">
            $$\min_\theta \mathbb{E}_{(s, a) \sim \mathcal{D}_E} \left[ \mathcal{L}(\pi_\theta(s), a) \right]$$
          </div>
          <div class="formula-legend">
            <strong>Hàm mất mát thông dụng:</strong> Với hành động liên tục (mô-men, vận tốc): $\mathcal{L} = \|\pi_\theta(s) - a\|^2$ (Mean Squared Error); Với hành động xác suất Gaussian: cực tiểu hóa khoảng cách phân phối Maximum Likelihood Estimation $-\log \pi_\theta(a \mid s)$.
          </div>
        </div>

        <!-- 2.2 -->
        <h2 id="sec-2-2">2.2 Chứng Minh Toán Học Hiện Tượng Tích Lũy Sai Số Bậc Hai $O(T^2 \epsilon)$</h2>
        <p>Mặc dù đơn giản, BC mắc phải điểm yếu chí tử gọi là <strong>Hiện tượng Lệch Phân Phối (Covariate Shift / Distribution Drift)</strong>. Trong học máy truyền thống, dữ liệu huấn luyện và kiểm thử được giả định độc lập cùng phân phối (i.i.d). Tuy nhiên trong robot học, hành động hiện tại $a_t$ quyết định trạng thái tiếp theo $s_{t+1}$, vi phạm hoàn toàn giả định i.i.d!</p>

        <div class="why-matters-box">
          <div class="why-matters-header">⚠️ ĐỊNH LÝ ROSS & BAGNELL (2010): SAI SỐ TÍCH LŨY BẬC HAI</div>
          <div class="why-matters-body">
            Giả sử chính sách học được $\hat{\pi}$ mắc sai số nhỏ $\epsilon$ tại mỗi bước so với chuyên gia: $\mathbb{E}_{s \sim d_{\pi_E}} [\mathbb{I}(\hat{\pi}(s) \ne \pi_E(s))] \le \epsilon$.
            <br>Khi triển khai độc lập trong $T$ bước, tổng kỳ vọng số bước mắc lỗi bùng nổ theo hàm bình phương thời gian:
            $$\mathbb{E} \left[ \sum_{t=1}^T \text{Loss}(s_t) \right] \le \epsilon T^2$$
            <strong>Cơ chế phân kỳ:</strong> Một sai sót nhỏ ở bước $t$ đẩy robot sang trạng thái lạ chưa từng có trong tập huấn luyện $\mathcal{D}_E$. Tại trạng thái lạ này, robot tiếp tục ra quyết định sai lầm lớn hơn, khiến robot trôi dạt hoàn toàn ra khỏi vùng hoạt động an toàn và gặp tai nạn!
          </div>
        </div>

        <!-- 2.3 -->
        <h2 id="sec-2-3">2.3 Hiện Tượng Nhầm Lẫn Nguyên Nhân - Kết Quả (Causal Confusion)</h2>
        <p>Trong các bài toán điều khiển dựa trên thị giác (Visual Servoing), mạng nơ-ron thường bị đánh lừa bởi các đặc trưng tương quan giả tạo (Spurious Correlations). Ví dụ: Xe tự hành nhìn thấy đèn phanh trên táp-lô sáng lên thì mới đạp phanh, nhầm lẫn kết quả thành nguyên nhân của hành động phanh!</p>

        <!-- 2.4 -->
        <h2 id="sec-2-4">2.4 Các Giải Pháp Chống Trôi: Jittering & Action Chunking</h2>
        <p>Để khắc phục nhược điểm của BC mà không cần người kèm trực tiếp:</p>
        <p>• <strong>Bơm nhiễu phục hồi (Noise Injection / Jittering):</strong> Khi thu thập mẫu, chủ động làm lệch tay robot một chút và yêu cầu chuyên gia thực hiện thao tác kéo về quỹ đạo chuẩn.</p>
        <p>• <strong>Action Chunking:</strong> Dự đoán đồng thời một chuỗi $k$ hành động liên tiếp thay vì chỉ 1 hành động tức thời, giúp triệt tiêu hiện tượng giật cục và trôi dạt tích lũy.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-2-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Trôi Dạt Quỹ Đạo Covariate Shift Xe Tự Hành</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-02" width="700" height="280" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Sai số một bước ε: <input type="range" id="sim02-eps" min="0.01" max="0.15" step="0.01" value="0.05"> <span id="sim02-eps-val">ε = 0.050</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-2-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Cận Trên Xác Suất Thất Bại Của Chính Sách BC</h3>
          <p>Một cánh tay robot thực hiện nhiệm vụ lắp ráp linh kiện gồm $T = 50$ bước thời gian. Mô hình Behavioral Cloning huấn luyện đạt độ chính xác $98\%$ trên tập kiểm tra nội suy ($\epsilon = 0.02$). Tính xác suất robot đi chệch quỹ đạo và so sánh giữa cận trên lý thuyết bậc hai $T^2 \epsilon$ với trường hợp lý tưởng i.i.d.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính kỳ vọng lỗi trong giả định i.i.d lý tưởng</h5>
              <p>Nếu phân phối trạng thái không bị trôi dạt (mỗi bước độc lập):</p>
              <p>$$\text{Error}_{iid} = T \cdot \epsilon = 50 \times 0.02 = 1.0\text{ lỗi}$$</p>
              <p>Xác suất hoàn thành trọn vẹn: $P_{success} = (1 - \epsilon)^T = (0.98)^{50} \approx 0.364$ ($36.4\%$).</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính cận trên tích lũy lỗi bậc hai của Ross & Bagnell</h5>
              <p>Do hiện tượng lệch phân phối trạng thái (Covariate Shift):</p>
              <p>$$\text{Bound}_{BC} = T^2 \cdot \epsilon = 50^2 \times 0.02 = 2500 \times 0.02 = 50.0$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Xác định thời điểm phân kỳ tới hạn $t_{diverge}$</h5>
              <p>Thời điểm mà sai số tích lũy vượt quá ngưỡng an toàn $\delta = 1.0$:</p>
              <p>$$t^2 \cdot \epsilon \ge 1.0 \implies t \ge \sqrt{\frac{1.0}{\epsilon}} = \sqrt{\frac{1.0}{0.02}} = \sqrt{50} \approx 7.07\text{ bước}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Đánh giá & Rút ra kết luận kỹ thuật</h5>
              <p>Mặc dù chính sách đạt độ chính xác $98\%$, nhưng chỉ sau vỏn vẹn $\approx 7$ bước di chuyển, robot đã rơi vào vùng phân phối lạ và nguy cơ thất bại tiến đến $100\%$.</p>
              <p>Kết luận: Không thể dùng BC đơn thuần cho các tác vụ dài hạn ($T \gt 20$) nếu không có cơ chế can thiệp tương tác (như DAgger) hoặc Action Chunking.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-2-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Pipeline Huấn Luyện Behavioral Cloning Bằng PyTorch</h4>
          <p>Mô hình MLP Behavioral Cloning ánh xạ trạng thái khớp sang vận tốc đặt:</p>
          <div class="code-card">
            <div class="code-header">
              <span>train_bc.py (PyTorch / C++)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import torch
import torch.nn as nn

class BCPolicy(nn.Module):
    def __init__(self, state_dim=6, action_dim=6):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim)
        )
    def forward(self, state):
        return self.net(state)

# Huấn luyện tối ưu hàm mất mát MSE
policy = BCPolicy()
optimizer = torch.optim.Adam(policy.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 03: Phản Hồi Đánh Giá (Evaluative) & RLHF Trong Robot (TAMER/COACH)
# ==============================================================================
ch03_sidebar = [
    {"id": "sec-3-1", "title": "3.1 Không gian Phản hồi Đánh giá (Evaluative Space)"},
    {"id": "sec-3-2", "title": "3.2 Thuật toán TAMER: Học từ Tín hiệu Khen/Chê"},
    {"id": "sec-3-3", "title": "3.3 Thuật toán COACH: Hướng dẫn Gradient Trực tiếp"},
    {"id": "sec-3-4", "title": "3.4 Phản hồi Ưu tiên Cặp Quỹ đạo (Preference RLHF)"},
    {"id": "sec-3-sim", "title": "⚡ Mô phỏng Đánh Giá TAMER Thời Gian Thực (Canvas)"},
    {"id": "sec-3-worked", "title": "📐 Ví dụ Tính Số 4 Bước Cập Nhật Trọng Số TAMER"},
    {"id": "sec-3-bridge", "title": "🛠️ Cầu nối ROS 2 Human Feedback Interface"}
]

ch03_body = r"""
        <!-- 3.1 -->
        <h2 id="sec-3-1">3.1 Không Gian Phản Hồi Đánh Giá Của Con Người (Evaluative Space)</h2>
        <p>Trong học bắt chước tương tác (Interactive Imitation Learning - IIL), con người đóng vai trò như một người thầy theo dõi quá trình robot thực thi và cung cấp tín hiệu phản hồi. Không gian phản hồi đánh giá không yêu cầu con người phải biết cách lái robot, mà chỉ cần đánh giá hành vi là <strong>Tốt hay Xấu</strong>:</p>
        <div class="formula-hero">
          <div class="formula-title">Các Dạng Tín Hiệu Phản Hồi Đánh Giá $h \in \mathcal{H}$</div>
          <div class="formula-math">
            $$\begin{cases}
              \text{Nhị phân (Binary):} & h \in \{-1, +1\} \quad (\text{Chê / Khen}) \\
              \text{Vô hướng (Scalar):} & h \in [-1.0, +1.0] \quad (\text{Mức độ hài lòng}) \\
              \text{Sở thích so sánh cặp (Preference):} & \tau_1 \succ \tau_2 \quad (\text{Quỹ đạo 1 tốt hơn Quỹ đạo 2})
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Ưu điểm lớn nhất:</strong> Rất thân thiện với người dùng phổ thông không có chuyên môn kỹ thuật robot, giảm thiểu áp lực điều khiển phức tạp.
          </div>
        </div>

        <!-- 3.2 -->
        <h2 id="sec-3-2">3.2 Thuật Toán TAMER (Training an Agent Manually via Evaluative Reinforcement)</h2>
        <p>Knox & Stone (2009) đề xuất thuật toán TAMER: robot huấn luyện một mạng xấp xỉ hàm đánh giá của con người $\hat{H}(s, a)$ mô phỏng tín hiệu khen thưởng tức thời của người thầy:</p>
        <div class="formula-hero">
          <div class="formula-title">Quy Tắc Cập Nhật Trọng Số Mạng Đánh Giá TAMER</div>
          <div class="formula-math">
            $$w \leftarrow w + \alpha \left[ h - \hat{H}_w(s, a) \right] \nabla_w \hat{H}_w(s, a)$$
            $$\pi(s) = \arg\max_a \hat{H}_w(s, a)$$
          </div>
          <div class="formula-legend">
            <strong>Gán trách nhiệm theo thời gian (Credit Assignment):</strong> Do con người có độ trễ phản xạ từ $0.2 \sim 0.8\text{ s}$, tín hiệu phản hồi $h$ được phân bổ ngược về các cặp trạng thái - hành động trong quá khứ gần theo phân phối xác suất trễ $f_{delay}(t)$.
          </div>
        </div>

        <!-- 3.3 -->
        <h2 id="sec-3-3">3.3 Thuật Toán COACH (COrrective Advice Communicated by Humans)</h2>
        <p>Thuật toán COACH (Celemin et al., 2019) sử dụng phản hồi nhị phân $h \in \{-1, 0, +1\}$ trực tiếp như một hệ số định hướng cho gradient chính sách trong không gian hành động liên tục:</p>
        $$\Delta \theta = \alpha \cdot h \cdot \nabla_\theta \log \pi_\theta(a \mid s)$$
        <p>Khi $h = +1$, thuật toán tăng xác suất thực hiện hành động $a$; khi $h = -1$, thuật toán đẩy hành động ra xa theo hướng ngược lại.</p>

        <!-- 3.4 -->
        <h2 id="sec-3-4">3.4 Phản Hồi Ưu Tiên Cặp Quỹ Đạo (Preference-based RL / RLHF)</h2>
        <p>Thay vì đánh giá tức thời, con người quan sát 2 đoạn video thực hiện của robot $(\tau_1, \tau_2)$ và chọn ra đoạn video tốt hơn ($\tau_1 \succ \tau_2$). Xác suất ưu tiên tuân theo mô hình lựa chọn Bradley-Terry:</p>
        $$P(\tau_1 \succ \tau_2) = \frac{\exp\left(\sum_{t} \hat{r}(s_t^{(1)}, a_t^{(1)})\right)}{\exp\left(\sum_{t} \hat{r}(s_t^{(1)}, a_t^{(1)})\right) + \exp\left(\sum_{t} \hat{r}(s_t^{(2)}, a_t^{(2)})\right)}$$

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-3-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng TAMER: Dạy Robot Bằng Nút Khen / Chê Thời Gian Thực</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-03" width="700" height="280" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color); align-items: center;">
            <button id="sim03-reward" style="padding: 0.5rem 1rem; background: #10b981; color: #fff; border: none; border-radius: 6px; font-weight: 700; cursor: pointer;">👍 KHEN (+1)</button>
            <button id="sim03-punish" style="padding: 0.5rem 1rem; background: #ef4444; color: #fff; border: none; border-radius: 6px; font-weight: 700; cursor: pointer;">👎 CHÊ (-1)</button>
            <span id="sim03-score" style="font-family: monospace; font-size: 0.9rem; color: #38bdf8;">Trọng số H(s,a) = 0.50</span>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-3-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Cập Nhật Trọng Số Mạng Nơ-Ron TAMER Khi Nhận Tín Hiệu Khen</h3>
          <p>Mô hình TAMER sử dụng xấp xỉ tuyến tính $\hat{H}(s, a) = w^T \phi(s, a)$. Tại thời điểm $t$, vector đặc trưng trạng thái - hành động là $\phi = [1.0, 0.5, -0.2]^T$. Vector trọng số hiện tại $w = [0.2, 0.4, 0.1]^T$. Tốc độ học $\alpha = 0.1$. Người hướng dẫn nhấn nút Khen thưởng với giá trị $h = +1.0$. Tính vector trọng số mới $w'$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính dự báo giá trị đánh giá hiện tại $\hat{H}$</h5>
              <p>$$\hat{H} = w^T \phi = (0.2)(1.0) + (0.4)(0.5) + (0.1)(-0.2)$$</p>
              <p>$$\hat{H} = 0.20 + 0.20 - 0.02 = 0.38$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính sai số phản hồi của con người (Error)</h5>
              <p>Sai số giữa tín hiệu người thầy $h$ và mô hình dự báo:</p>
              <p>$$\delta = h - \hat{H} = 1.0 - 0.38 = 0.62$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính số gia cập nhật trọng số $\Delta w$</h5>
              <p>Vì mô hình tuyến tính, gradient $\nabla_w \hat{H} = \phi$:</p>
              <p>$$\Delta w = \alpha \cdot \delta \cdot \phi = 0.1 \times 0.62 \times \begin{bmatrix} 1.0 \\ 0.5 \\ -0.2 \end{bmatrix} = 0.062 \times \begin{bmatrix} 1.0 \\ 0.5 \\ -0.2 \end{bmatrix} = \begin{bmatrix} 0.0620 \\ 0.0310 \\ -0.0124 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Cập nhật trọng số & Kiểm tra giá trị mới</h5>
              <p>$$w' = w + \Delta w = \begin{bmatrix} 0.2000 + 0.0620 \\ 0.4000 + 0.0310 \\ 0.1000 - 0.0124 \end{bmatrix} = \begin{bmatrix} 0.2620 \\ 0.4310 \\ 0.0876 \end{bmatrix}$$</p>
              <p>Đánh giá lại: $\hat{H}_{new} = (0.262)(1.0) + (0.431)(0.5) + (0.0876)(-0.2) = 0.262 + 0.2155 - 0.0175 = 0.460$. Giá trị đánh giá tăng từ $0.38 \to 0.46$, tiến gần hơn về mong muốn của con người.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-3-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: ROS 2 Feedback Listener Node</h4>
          <p>Node ROS 2 lắng nghe thông điệp đánh giá từ nút bấm gamepad hoặc bàn phím để kích hoạt cập nhật trực tuyến cho thuật toán TAMER:</p>
          <div class="code-card">
            <div class="code-header">
              <span>tamer_node.py (ROS 2 Humble / Python)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>from rclpy.node import Node
from std_msgs.msg import Float32

class TamerFeedbackNode(Node):
    def __init__(self, tamer_agent):
        super().__init__("tamer_feedback_node")
        self.agent = tamer_agent
        self.sub = self.create_subscription(
            Float32, "/human_feedback", self.feedback_cb, 10
        )
    def feedback_cb(self, msg):
        human_eval = msg.data # +1.0 hoặc -1.0
        self.agent.update_from_human(human_eval)
        self.get_logger().info(f"Received human feedback: {human_eval}")</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 04: Phản Hồi Hiệu Chỉnh & Họ Thuật Toán DAgger / SafeDAgger
# ==============================================================================
ch04_sidebar = [
    {"id": "sec-4-1", "title": "4.1 Không gian Phản hồi Hiệu chỉnh (Transition Space)"},
    {"id": "sec-4-2", "title": "4.2 Thuật toán DAgger & Chứng minh Hội tụ O(Tε)"},
    {"id": "sec-4-3", "title": "4.3 Biến thể An toàn: HG-DAgger & SafeDAgger"},
    {"id": "sec-4-4", "title": "4.4 Thuật toán AggreVaTe & Dự đoán Hàm Giá trị"},
    {"id": "sec-4-sim", "title": "⚡ Mô phỏng Thuật Toán DAgger (Canvas)"},
    {"id": "sec-4-worked", "title": "📐 Ví dụ Tính Số 4 Bước Phân Phối Hòa Trộn DAgger"},
    {"id": "sec-4-bridge", "title": "🛠️ Cầu nối ROS 2 Teleoperation Override System"}
]

ch04_body = r"""
        <!-- 4.1 -->
        <h2 id="sec-4-1">4.1 Không Gian Phản Hồi Hiệu Chỉnh (Transition / Action Space)</h2>
        <p>Khác với phản hồi đánh giá (chỉ khen/chê), phản hồi hiệu chỉnh cung cấp trực tiếp <strong>hành động đúng đắn mà robot nên thực hiện</strong> ngay tại trạng thái mà robot đang đứng:</p>
        <div class="formula-hero">
          <div class="formula-title">Đặc Tuyến Phản Hồi Hiệu Chỉnh Của Chuyên Gia</div>
          <div class="formula-math">
            $$a^* = \pi_E(s) \in \mathcal{A} \quad \text{hoặc} \quad \Delta a = a^* - \hat{\pi}(s)$$
          </div>
          <div class="formula-legend">
            <strong>Phương thức can thiệp thực tế:</strong> Chuyên gia cầm cần điều khiển (joystick), đeo kính thực tế ảo VR, hoặc cầm trực tiếp vào cánh tay robot (kinesthetic teaching) để bẻ lái hướng đi khi robot sắp va chạm.
          </div>
        </div>

        <!-- 4.2 -->
        <h2 id="sec-4-2">4.2 Thuật Toán DAgger & Chứng Minh Giảm Sai Số Xuống Bậc Nhất $O(T\epsilon)$</h2>
        <p>Thuật toán DAgger (Dataset Aggregation - Ross et al., 2011) là bước ngoặt vĩ đại nhất trong lịch sử học bắt chước, giải quyết triệt để vấn đề Covariate Shift:</p>
        <div class="why-matters-box">
          <div class="why-matters-header">💡 NGUYÊN LÝ HOẠT ĐỘNG CỦA THUẬT TOÁN DAGGER</div>
          <div class="why-matters-body">
            1. Khởi tạo chính sách $\hat{\pi}_1$ từ tập mẫu ban đầu $\mathcal{D}_0$ bằng BC.
            <br>2. Tại vòng lặp $k$: Cho robot tự chạy chính sách hỗn hợp $\pi_k = \beta_k \pi_E + (1-\beta_k) \hat{\pi}_k$ để thăm dò môi trường.
            <br>3. Thu thập tập trạng thái robot đã đi qua: $S_k = \{s_1, s_2, \dots, s_T\}$.
            <br>4. <strong>Hỏi ý kiến chuyên gia:</strong> Yêu cầu chuyên gia gán nhãn hành động tối ưu cho các trạng thái robot đã viếng thăm: $\mathcal{D}_k = \{(s, \pi_E(s)) \mid s \in S_k\}$.
            <br>5. <strong>Gộp dữ liệu:</strong> $\mathcal{D} \leftarrow \mathcal{D} \cup \mathcal{D}_k$ và huấn luyện lại chính sách $\hat{\pi}_{k+1}$.
            <br><strong>Kết quả định lý:</strong> Sai số tích lũy giảm từ bậc hai $O(T^2 \epsilon)$ xuống <strong>bậc nhất tuyến tính $O(T \epsilon)$</strong>!
          </div>
        </div>

        <!-- 4.3 -->
        <h2 id="sec-4-3">4.3 Các Biến Thể Giảm Tải & An Toàn: HG-DAgger & SafeDAgger</h2>
        <p>Nhược điểm của DAgger gốc là bắt chuyên gia phải ngồi gán nhãn lại toàn bộ $100\%$ các bước thời gian, gây kiệt sức cho con người. Hai biến thể cải tiến hàng đầu:</p>
        <p>• <strong>HG-DAgger (Human-Gated DAgger):</strong> Robot tự động chạy chính sách của mình; chuyên gia chỉ can thiệp nắm quyền điều khiển khi robot có dấu hiệu nguy hiểm hoặc đi sai lệch lớn.</p>
        <p>• <strong>SafeDAgger (Zhang & Cho, 2016):</strong> Robot tự huấn luyện thêm một mạng phụ trợ dự báo độ bất định (Safety/Discrepancy Network) $K_\phi(s) \in [0, 1]$. Khi độ bất định vượt ngưỡng an toàn ($K_\phi(s) \gt \tau$), robot chủ động dừng lại và gọi người hỗ trợ.</p>

        <!-- 4.4 -->
        <h2 id="sec-4-4">4.4 Thuật Toán AggreVaTe (Aggregate Values to Target)</h2>
        <p>Thay vì chỉ bắt chước hành động tức thời $\pi_E(s)$, AggreVaTe sử dụng hàm giá trị $Q^*(s, a)$ của chuyên gia để huấn luyện chính sách chọn hành động cực đại hóa hàm lợi thế (Advantage function), kết nối trực tiếp Imitation Learning với Reinforcement Learning.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-4-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Quá Trình Hội Tụ Của Thuật Toán DAgger</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-04" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Vòng lặp DAgger k: <input type="range" id="sim04-iter" min="1" max="8" step="1" value="1"> <span id="sim04-iter-val">Vòng lặp DAgger: N = 1</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-4-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Lịch Trình Hòa Trộn Chính Sách $\beta_k$ Trong DAgger</h3>
          <p>Thuật toán DAgger sử dụng lịch trình suy giảm tham số hòa trộn mũ: $\beta_k = \beta_0^k$ với $\beta_0 = 0.7$. Ban đầu $k=1$, robot chạy theo chính sách có $70\%$ chuyên gia kèm cặp. Tính tỷ lệ đóng góp của chuyên gia qua các vòng $k=1, 2, 3, 4$ và số mẫu dữ liệu gộp tích lũy khi mỗi vòng chạy $T = 100$ bước.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính hệ số hòa trộn $\beta_k$ qua 4 vòng</h5>
              <p>• Vòng 1 ($k=1$): $\beta_1 = 0.7^1 = 0.700$ ($70\%$ chuyên gia)</p>
              <p>• Vòng 2 ($k=2$): $\beta_2 = 0.7^2 = 0.490$ ($49\%$ chuyên gia)</p>
              <p>• Vòng 3 ($k=3$): $\beta_3 = 0.7^3 = 0.343$ ($34.3\%$ chuyên gia)</p>
              <p>• Vòng 4 ($k=4$): $\beta_4 = 0.7^4 = 0.2401$ ($24.0\%$ chuyên gia)</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính số bước robot tự hành không có chuyên gia can thiệp</h5>
              <p>Tỷ lệ robot tự quyết định là $1 - \beta_k$:</p>
              <p>• Vòng 1: $100 \times (1 - 0.700) = 30\text{ bước tự hành}$</p>
              <p>• Vòng 2: $100 \times (1 - 0.490) = 51\text{ bước tự hành}$</p>
              <p>• Vòng 3: $100 \times (1 - 0.343) = 65.7 \approx 66\text{ bước tự hành}$</p>
              <p>• Vòng 4: $100 \times (1 - 0.240) = 76\text{ bước tự hành}$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính kích thước tập dữ liệu tổng hợp $\mathcal{D}_k$</h5>
              <p>Mỗi vòng lặp gom thêm $T=100$ mẫu trạng thái được chuyên gia gán nhãn:</p>
              <p>• Ban đầu: $|\mathcal{D}_0| = 100$</p>
              <p>• Sau vòng 1: $|\mathcal{D}_1| = 100 + 100 = 200\text{ mẫu}$</p>
              <p>• Sau vòng 2: $|\mathcal{D}_2| = 200 + 100 = 300\text{ mẫu}$</p>
              <p>• Sau vòng 4: $|\mathcal{D}_4| = 100 + 4 \times 100 = 500\text{ mẫu}$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Ước lượng cận sai số lý thuyết $O(T\epsilon)$</h5>
              <p>Với sai số huấn luyện đơn bước $\epsilon = 0.05$ và $T = 100$:</p>
              <p>• Cận sai số BC cổ điển: $\text{Bound}_{BC} = T^2 \epsilon = 100^2 \times 0.05 = 500$</p>
              <p>• Cận sai số DAgger: $\text{Bound}_{DAgger} = T \epsilon = 100 \times 0.05 = 5.0$</p>
              <p>Nhận xét: DAgger giảm thiểu sai số tích lũy tới <strong>100 lần</strong> so với BC đơn thuần!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-4-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Hệ Thống Ghi Đè Can Thiệp Trong ROS 2 Control</h4>
          <p>Triển khai cơ chế can thiệp an toàn HG-DAgger thông qua bộ ghép kênh `twist_mux` hoặc controller switcher trong ROS 2:</p>
          <div class="code-card">
            <div class="code-header">
              <span>dagger_override_node.py (ROS 2 Humble / Python)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>from rclpy.node import Node
from geometry_msgs.msg import Twist

class DAggerOverrideNode(Node):
    def __init__(self):
        super().__init__("dagger_override_node")
        self.human_override = False
        self.sub_human = self.create_subscription(Twist, "/teleop_cmd", self.human_cb, 10)
        self.sub_robot = self.create_subscription(Twist, "/policy_cmd", self.robot_cb, 10)
        self.pub_final = self.create_publisher(Twist, "/cmd_vel", 10)

    def human_cb(self, msg):
        # Nếu người lái lắc cần điều khiển, chiếm quyền ngay lập tức
        if abs(msg.linear.x) &gt; 0.01 or abs(msg.angular.z) &gt; 0.01:
            self.human_override = True
            self.pub_final.publish(msg)
            self.save_expert_sample(msg) # Lưu mẫu gộp DAgger
        else:
            self.human_override = False

    def robot_cb(self, msg):
        if not self.human_override:
            self.pub_final.publish(msg)</code></pre>
          </div>
        </div>
"""

# Generate HTML files
print("Generating Ch 01...")
with open(os.path.join(CHAPTERS_DIR, "ch01.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("01", "Giới Thiệu Học Bắt Chước & Khung Quyết Định Toán Học", "Foundations of Imitation Learning & Decision Theory", "TRACK 1: NỀN TẢNG & LỆCH PHÂN PHỐI", "track-1", "../index.html", "Lộ trình Tổng quan", "ch02.html", "Chương 02: Nhân Bản Hành Vi BC", ch01_sidebar, ch01_body))

print("Generating Ch 02...")
with open(os.path.join(CHAPTERS_DIR, "ch02.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("02", "Nhân Bản Hành Vi (BC) & Tích Lũy Sai Số Covariate Shift", "Behavioral Cloning & Covariate Shift Analysis", "TRACK 1: NỀN TẢNG & LỆCH PHÂN PHỐI", "track-1", "ch01.html", "Chương 01: Giới Thiệu Học Bắt Chước", "ch03.html", "Chương 03: Phản Hồi Đánh Giá TAMER", ch02_sidebar, ch02_body))

print("Generating Ch 03...")
with open(os.path.join(CHAPTERS_DIR, "ch03.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("03", "Phản Hồi Đánh Giá (Evaluative) & RLHF Trong Robot", "Evaluative Feedback, TAMER & COACH Frameworks", "TRACK 2: HỌC TƯƠNG TÁC IIL", "track-2", "ch02.html", "Chương 02: Nhân Bản Hành Vi BC", "ch04.html", "Chương 04: Họ Thuật Toán DAgger", ch03_sidebar, ch03_body))

print("Generating Ch 04...")
with open(os.path.join(CHAPTERS_DIR, "ch04.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("04", "Phản Hồi Hiệu Chỉnh & Họ Thuật Toán DAgger / SafeDAgger", "Corrective Feedback & DAgger Family Algorithms", "TRACK 2: HỌC TƯƠNG TÁC IIL", "track-2", "ch03.html", "Chương 03: Phản Hồi Đánh Giá TAMER", "ch05.html", "Chương 05: Động Tác Nguyên Mẫu DMPs", ch04_sidebar, ch04_body))

print("Successfully generated Chapters 01, 02, 03, 04 for Imitation Learning!")
