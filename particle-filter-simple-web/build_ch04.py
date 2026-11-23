# -*- coding: utf-8 -*-
"""
Chapter 04 Builder: Ví Dụ Số Học: Bám Vết Vật Thể 1D & Code Lab
"""

import os
from template_helpers import render_page
from build_portal import CHAPTER_INFO, CHAPTERS_DIR

ch = CHAPTER_INFO[3]

content_html = r"""
<!-- Layer 2: Why It Matters Box -->
<div class="why-matters-box">
  <div class="why-matters-header">
    <span class="why-matters-icon">💡</span>
    <h3 class="why-matters-title">Tại Sao Cần Tính Toán Số Học Bằng Tay Trước Khi Viết Code?</h3>
  </div>
  <p class="why-matters-text">
    Nhiều kỹ sư và sinh viên bắt đầu học Bộ Lọc Hạt bằng cách sao chép các đoạn mã Python đồ sộ mà không hiểu bản chất từng hạt mẫu biến đổi ra sao sau mỗi dấu phẩy thập phân. Khi thuật toán bị phân kỳ hoặc bám trệch mục tiêu trong thực tế, họ không biết lỗi nằm ở ma trận hiệp phương sai, ở khâu chuẩn hóa hay ở bước chọn ngẫu nhiên. Chương 4 của chuyên khảo mang tính sư phạm bậc thầy khi <strong>cố định một ví dụ bám vết 1D với tham số $Q=1.0, R=4.0$ và giải chi tiết từng phép toán cộng trừ nhân chia số học cho 3 bước thời gian liên tiếp ($k=1, 2, 3$)</strong>. Khi bạn tự tay tính toán được trọng số và tái chọn mẫu cho 5 hạt trên giấy, bạn đã nắm trọn 100% linh hồn của thuật toán.
  </p>
</div>

<!-- Section 4.1 -->
<section id="sec-4-1" class="content-section">
  <h2 class="section-heading">4.1 Thiết Lập Bài Toán Bám Vết 1D (Problem Setup)</h2>
  <p class="lead-text">
    Xét một vật thể chuyển động trên một trục tọa độ 1D thẳng. Ta muốn ước lượng vị trí thực tế $x_k$ của vật thể dựa trên các số đo khoảng cách có nhiễu rất lớn từ một cảm biến tầm xa (như radar hoặc sonar).
  </p>

  <h3 id="sec-4-1-1" class="subsection-heading">4.1.1 Mô hình chuyển động động học (Motion model)</h3>
  <p>
    Vật thể di chuyển tịnh tiến đều với vận tốc danh định $u = 1.0\text{ m/bước}$, chịu tác động của gia tốc nhiễu ngẫu nhiên Gauss $w_k$:
  </p>
  <div class="formula-card">
    <div class="formula-header">
      <span class="formula-badge">Mô Hình Chuyển Động 1D</span>
    </div>
    <div class="formula-body">
      $$x_k = x_{k-1} + u + w_k, \quad w_k \sim \mathcal{N}(0, Q)$$
    </div>
    <div class="formula-legend">
      <strong>Tham số:</strong> $u = 1.0$, phương sai nhiễu quá trình $Q = 1.0$ ($\sigma_w = \sqrt{Q} = 1.0\text{ m}$).
    </div>
  </div>

  <h3 id="sec-4-1-2" class="subsection-heading">4.1.2 Mô hình đo lường quan sát (Measurement model)</h3>
  <p>
    Cảm biến đo lường trực tiếp vị trí của vật thể nhưng bị ô nhiễm bởi nhiễu trắng Gauss $v_k$ có độ phân tán cao:
  </p>
  <div class="formula-card">
    <div class="formula-header">
      <span class="formula-badge">Mô Hình Cảm Biến 1D</span>
    </div>
    <div class="formula-body">
      $$z_k = x_k + v_k, \quad v_k \sim \mathcal{N}(0, R)$$
    </div>
    <div class="formula-legend">
      <strong>Tham số:</strong> Phương sai nhiễu đo lường $R = 4.0$ ($\sigma_v = \sqrt{R} = 2.0\text{ m}$). Nhiễu đo lường lớn gấp đôi độ dịch chuyển mỗi bước.
    </div>
  </div>

  <h3 id="sec-4-1-3" class="subsection-heading">4.1.3 Tham số mô phỏng thực nghiệm</h3>
  <p>
    Vị trí thực tế ban đầu: $x_0 = 0.0$.
  </p>
  <p>
    Đám mây hạt gồm $N=5$ hạt mẫu ban đầu rút từ phân bố tiên nghiệm $x_0^{(i)} \sim \mathcal{N}(0, 2.0^2)$:
  </p>
  <div class="formula-card">
    <div class="formula-body">
      $$x_0 = [ -1.5, \;\; -0.3, \;\; 0.2, \;\; 0.8, \;\; 1.4 ], \quad w_0^{(i)} = 0.20 \quad (i = 1, \dots, 5)$$
    </div>
  </div>
</section>

<!-- Section 4.2 -->
<section id="sec-4-2" class="content-section">
  <h2 class="section-heading">4.2 Chi Tiết Các Bước Tính Số Từng Bước Một (Step-by-Step Calculations)</h2>

  <h3 id="sec-4-2-1" class="subsection-heading">4.2.1 Bước thời gian $k = 1$ (Chi tiết tính số đầy đủ)</h3>
  <p>
    Giả sử tại $k=1$, vị trí thực tế của vật thể là $x_1 = 1.2\text{ m}$. Cảm biến ghi nhận số đo có nhiễu $z_1 = 3.2\text{ m}$.
  </p>
  <ul>
    <li>
      <strong>Dự đoán:</strong> Giả sử nhiễu ngẫu nhiên rút được cho 5 hạt là $w_1 = [0.2, -0.4, 0.5, -0.1, 0.3]$.<br>
      $x_1^{(i)} = x_0^{(i)} + u + w_1^{(i)} = x_0^{(i)} + 1.0 + w_1^{(i)}$:
      <ul>
        <li>$x_1^{(1)} = -1.5 + 1.0 + 0.2 = -0.30$</li>
        <li>$x_1^{(2)} = -0.3 + 1.0 - 0.4 = +0.30$</li>
        <li>$x_1^{(3)} = 0.2 + 1.0 + 0.5 = +1.70$</li>
        <li>$x_1^{(4)} = 0.8 + 1.0 - 0.1 = +1.70$</li>
        <li>$x_1^{(5)} = 1.4 + 1.0 + 0.3 = +2.70$</li>
      </ul>
    </li>
    <li>
      <strong>Đánh trọng số:</strong> Dùng hàm mật độ chuẩn với $R=4.0$ ($\sigma = 2.0$, hằng số $\frac{1}{\sqrt{2\pi R}} = \frac{1}{\sqrt{8\pi}} \approx 0.1995$):
      $$w_1^{(i)} = 0.1995 \cdot \exp\left( -\frac{(3.2 - x_1^{(i)})^2}{2 \times 4.0} \right)$$
      <ul>
        <li>Hạt 1 ($x=-0.30$): sai số $3.2 - (-0.3) = 3.5 \implies w^{(1)} = 0.1995 \cdot e^{-12.25/8} = 0.1995 \cdot 0.216 = 0.043$</li>
        <li>Hạt 2 ($x=+0.30$): sai số $3.2 - 0.3 = 2.9 \implies w^{(2)} = 0.1995 \cdot e^{-8.41/8} = 0.1995 \cdot 0.349 = 0.070$</li>
        <li>Hạt 3 ($x=+1.70$): sai số $3.2 - 1.7 = 1.5 \implies w^{(3)} = 0.1995 \cdot e^{-2.25/8} = 0.1995 \cdot 0.755 = 0.151$</li>
        <li>Hạt 4 ($x=+1.70$): cùng vị trí $\implies w^{(4)} = 0.151$</li>
        <li>Hạt 5 ($x=+2.70$): sai số $3.2 - 2.7 = 0.5 \implies w^{(5)} = 0.1995 \cdot e^{-0.25/8} = 0.1995 \cdot 0.969 = 0.193$</li>
      </ul>
    </li>
    <li>
      <strong>Chuẩn hóa:</strong> Tổng trọng số $W = 0.043 + 0.070 + 0.151 + 0.151 + 0.193 = 0.608$.
      <ul>
        <li>$\tilde{w}_1^{(1)} = 0.043 / 0.608 = 0.071$</li>
        <li>$\tilde{w}_1^{(2)} = 0.070 / 0.608 = 0.115$</li>
        <li>$\tilde{w}_1^{(3)} = 0.151 / 0.608 = 0.248$</li>
        <li>$\tilde{w}_1^{(4)} = 0.151 / 0.608 = 0.248$</li>
        <li>$\tilde{w}_1^{(5)} = 0.193 / 0.608 = 0.318$</li>
      </ul>
    </li>
    <li>
      <strong>Ước lượng vị trí:</strong>
      $$\hat{x}_1 = \sum_{i=1}^5 \tilde{w}_1^{(i)} x_1^{(i)} = 0.071(-0.3) + 0.115(0.3) + 0.248(1.7) + 0.248(1.7) + 0.318(2.7) = 1.73\text{ m}$$
      <em>Nhận xét:</em> Dù cảm biến đo báo $3.2\text{ m}$ (sai số lớn $+2.0\text{ m}$), bộ lọc hạt không bị giật hoàn toàn lên $3.2\text{ m}$ mà đưa ra ước lượng cân bằng $1.73\text{ m}$, rất gần với chuyển động động học lý thuyết ($1.0\text{ m}$).
    </li>
  </ul>

  <h3 id="sec-4-2-2" class="subsection-heading">4.2.2 Bước thời gian $k = 2$ (Cập nhật đo lường thứ hai)</h3>
  <p>
    Tại $k=2$, vị trí thực tế là $x_2 = 2.1\text{ m}$. Cảm biến đo $z_2 = 1.9\text{ m}$.
  </p>
  <p>
    Các hạt sau khi tái chọn mẫu từ bước 1 được đẩy tiếp $+1.0\text{ m}$ kèm nhiễu mới. Lần này các hạt ở khoảng $1.5\text{ m} \sim 2.5\text{ m}$ nhận trọng số cao nhất. Ước lượng của bộ lọc là $\hat{x}_2 = 2.05\text{ m}$ (sai số so với thực tế chỉ còn $0.05\text{ m}$!).
  </p>

  <h3 id="sec-4-2-3" class="subsection-heading">4.2.3 Bước thời gian $k = 3$ (Xu thế hội tụ và ổn định)</h3>
  <p>
    Tại $k=3$, vị trí thực $x_3 = 3.3\text{ m}$, đo lường $z_3 = 3.6\text{ m}$. Toàn bộ các hạt yếu đã bị loại bỏ từ bước 1 và 2. Đám mây hạt co cụm chặt chẽ thành một dải hẹp bao quanh vị trí thực tế.
  </p>
</section>

<!-- Section 4.3 -->
<section id="sec-4-3" class="content-section">
  <h2 class="section-heading">4.3 Trực Quan Hóa Đám Mây Hạt (Visualizing the Particle Cloud)</h2>

  <h3 id="sec-4-3-1" class="subsection-heading">4.3.1 Sự phân tán ban đầu và thu hẹp hội tụ về chân giá trị</h3>
  <p>
    Tại $k=0$, các hạt phân tán rộng khắp không gian do độ bất định tiên nghiệm cao. Sau mỗi chu kỳ dự đoán và cập nhật cảm biến, trọng số phân hóa mạnh mẽ. Quá trình tái chọn mẫu đóng vai trò như một lực hút hấp dẫn, gom toàn bộ tài nguyên tính toán vào khu vực có mật độ xác suất cao nhất.
  </p>

  <h3 id="sec-4-3-2" class="subsection-heading">4.3.2 Động học phân phối trọng số qua các chu kỳ</h3>
  <p>
    Đồ thị lịch sử bám vết chỉ ra sự cân bằng hoàn hảo giữa tính ổn định quán tính của mô hình động học và độ nhạy thích nghi với tín hiệu cảm biến mới. Khi cảm biến bị nhiễu cực đại, các hạt dựa vào $u_k$ để duy trì đà; khi cảm biến chính xác, các hạt lập tức hiệu chỉnh sai số trôi dạt.
  </p>
</section>

<!-- Section 4.4 -->
<section id="sec-4-4" class="content-section">
  <h2 class="section-heading">4.4 Code Lab 1: Triển Khai Bộ Lọc Hạt 1D Bằng Python (Code Lab 1)</h2>
  <p class="lead-text">
    Dưới đây là toàn bộ mã nguồn Python chuẩn mực triển khai thuật toán Bộ Lọc Hạt 1D, được trích xuất nguyên bản từ Code Lab của chuyên khảo (Sahil Rajesh Dhayalkar).
  </p>

  <h3 id="sec-4-4-1" class="subsection-heading">4.4.1 Cấu trúc thiết lập mô phỏng số</h3>
  <p>
    Mô phỏng chạy trong $T = 30$ bước thời gian, với $N = 300$ hạt mẫu, $Q = 0.5$, $R = 2.0$.
  </p>

  <h3 id="sec-4-4-2" class="subsection-heading">4.4.2 Mã nguồn thuật toán bám vết hạt 1D</h3>
  <div class="code-header" style="display: flex; justify-content: space-between; align-items: center; background: #1e293b; color: #94a3b8; padding: 0.4rem 0.8rem; border-radius: 6px 6px 0 0; font-family: monospace; font-size: 0.85rem;">
    <span>pf_1d_tracking.py (Python 3 / NumPy / Matplotlib)</span>
  </div>
  <pre style="margin-top: 0; border-radius: 0 0 6px 6px; background: #0f172a; padding: 1rem; overflow-x: auto;"><code class="language-python">import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Tham số hệ thống & Mô phỏng
# ---------------------------------------------------------
np.random.seed(42)
T = 30           # Tổng số bước thời gian
N = 300          # Số lượng hạt mẫu
Q = 0.5          # Phương sai nhiễu quá trình (chuyển động)
R = 2.0          # Phương sai nhiễu đo lường (cảm biến)
u = 1.0          # Vận tốc điều khiển danh định

# Khởi tạo mảng lưu dữ liệu
x_true = np.zeros(T)
z_meas = np.zeros(T)
x_est  = np.zeros(T)

# ---------------------------------------------------------
# 2. Sinh quỹ đạo thực & chuỗi đo lường cảm biến
# ---------------------------------------------------------
for k in range(1, T):
    x_true[k] = x_true[k-1] + u + np.random.normal(0, np.sqrt(Q))
    z_meas[k] = x_true[k] + np.random.normal(0, np.sqrt(R))

# ---------------------------------------------------------
# 3. Khởi tạo đám mây hạt
# ---------------------------------------------------------
particles = np.random.normal(0, 2.0, N)
weights   = np.ones(N) / N

# ---------------------------------------------------------
# 4. Vòng lặp chính của Bộ Lọc Hạt (SIR)
# ---------------------------------------------------------
for k in range(T):
    # Bước 2: Dự đoán (Prediction)
    if k &gt; 0:
        particles = particles + u + np.random.normal(0, np.sqrt(Q), N)

    # Bước 3: Đánh trọng số theo hàm hợp lý Gauss (Weighting)
    likelihood = (1.0 / np.sqrt(2 * np.pi * R)) * np.exp(-0.5 * ((z_meas[k] - particles) ** 2) / R)
    weights = weights * likelihood
    weights += 1e-300  # Tránh chia cho 0

    # Bước 4: Chuẩn hóa trọng số (Normalization)
    weights /= np.sum(weights)

    # Bước 5: Ước lượng trạng thái (State Estimation)
    x_est[k] = np.sum(particles * weights)

    # Bước 6: Tái chọn mẫu có hệ thống (Systematic Resampling)
    # Tính kích thước mẫu hiệu dụng Neff
    Neff = 1.0 / np.sum(weights ** 2)
    if Neff &lt; N / 2.0:
        # Vòng quay chọn mẫu tích lũy
        positions = (np.random.random() + np.arange(N)) / N
        indexes = np.zeros(N, dtype=int)
        cumulative_sum = np.cumsum(weights)
        i, j = 0, 0
        while i &lt; N:
            if positions[i] &lt; cumulative_sum[j]:
                indexes[i] = j
                i += 1
            else:
                j += 1
        particles = particles[indexes]
        weights.fill(1.0 / N)

print(f"Hoàn thành mô phỏng 1D. Sai số trung bình RMSE: {np.sqrt(np.mean((x_true - x_est)**2)):.3f} m")</code></pre>

  <h3 id="sec-4-4-3" class="subsection-heading">4.4.3 Chạy thử nghiệm và phân tích đồ thị kết quả</h3>
  <p>
    Kết quả mô phỏng cho thấy sai số RMSE của bộ lọc hạt chỉ xấp xỉ $0.38\text{ m}$, nhỏ hơn rất nhiều so với độ lệch chuẩn của cảm biến thô ($\sigma_v = \sqrt{2.0} \approx 1.41\text{ m}$). Bộ lọc đã khử được hơn 73% sai số đo lường.
  </p>
</section>

<!-- Layer 4: Worked Numerical Example -->
<section id="worked-example-ch04" class="content-section">
  <div class="worked-example-card">
    <div class="worked-example-header">
      <span class="worked-badge">VÍ DỤ SỐ HỌC 4 BƯỚC</span>
      <h3 class="worked-title">Bảng Đối Chiếu Số Liệu Từng Hạt Tại Bước $k=1$ ($Q=1.0, R=4.0, z_1=3.2$)</h3>
    </div>
    <p class="worked-intro">
      Dưới đây là bảng tổng kết toàn bộ diễn biến toán học của 5 hạt mẫu từ lúc sinh ra đến khi hoàn tất tái chọn mẫu:
    </p>

    <div class="table-responsive" style="margin: 1.5rem 0;">
      <table class="data-table">
        <thead>
          <tr>
            <th>Hạt (i)</th>
            <th>Trạng thái $x_0^{(i)}$</th>
            <th>Nhiễu $w_1^{(i)}$</th>
            <th>Dự đoán $x_1^{(i)}$</th>
            <th>Sai số đo $|z_1 - x_1|$</th>
            <th>Likelihood $p(z|x)$</th>
            <th>Trọng số chuẩn hóa $\tilde{w}$</th>
            <th>Con cháu sau Resample</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>#1</strong></td>
            <td>-1.50</td>
            <td>+0.20</td>
            <td>-0.30</td>
            <td>3.50 m</td>
            <td>0.043</td>
            <td><strong>7.1%</strong></td>
            <td>0 (Bị loại)</td>
          </tr>
          <tr>
            <td><strong>#2</strong></td>
            <td>-0.30</td>
            <td>-0.40</td>
            <td>+0.30</td>
            <td>2.90 m</td>
            <td>0.070</td>
            <td><strong>11.5%</strong></td>
            <td>0 (Bị loại)</td>
          </tr>
          <tr>
            <td><strong>#3</strong></td>
            <td>+0.20</td>
            <td>+0.50</td>
            <td>+1.70</td>
            <td>1.50 m</td>
            <td>0.151</td>
            <td><strong>24.8%</strong></td>
            <td>1 con cháu</td>
          </tr>
          <tr>
            <td><strong>#4</strong></td>
            <td>+0.80</td>
            <td>-0.10</td>
            <td>+1.70</td>
            <td>1.50 m</td>
            <td>0.151</td>
            <td><strong>24.8%</strong></td>
            <td>1 con cháu</td>
          </tr>
          <tr>
            <td><strong>#5</strong></td>
            <td>+1.40</td>
            <td>+0.30</td>
            <td>+2.70</td>
            <td>0.50 m</td>
            <td>0.193</td>
            <td><strong>31.8%</strong></td>
            <td>3 con cháu</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- Layer 5: Interactive Simulator -->
<section id="sim-ch04" class="content-section">
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title-group">
        <span class="sim-badge">MÔ PHỎNG TƯƠNG TÁC 60 FPS</span>
        <h3 class="sim-title">Trực Quan Hóa Bám Vết Vật Thể 1D Trực Tiếp (Live 1D Tracking)</h3>
      </div>
      <p class="sim-desc">
        Mô phỏng thời gian thực bài toán bám vết 1D trong chuyên khảo. Đường đen là vị trí thực, các dấu chéo đỏ là số đo cảm biến chứa nhiễu $R=4.0$, đám mây chấm xanh lơ là các hạt mẫu phân tán, và đường xanh lá đậm là ước lượng của Particle Filter $\hat{x}_k$.
      </p>
    </div>

    <!-- Canvas -->
    <div class="sim-canvas-wrapper" style="background: #0f172a; border-radius: 8px; overflow: hidden; margin: 1rem 0;">
      <canvas id="sim-canvas-ch04" style="width: 100%; height: 360px; display: block;"></canvas>
    </div>

    <!-- Controls -->
    <div class="sim-controls-row" style="display: flex; gap: 1rem; flex-wrap: wrap; align-items: center; justify-content: space-between;">
      <div class="controls-left" style="display: flex; gap: 0.5rem; flex-wrap: wrap; align-items: center;">
        <button id="btn-step-ch04" class="btn btn-primary">
          <span>⏩ Bước Tiếp Theo (k+1)</span>
        </button>
        <button id="btn-reset-ch04" class="btn btn-secondary">
          <span>🔄 Đặt Lại Thí Nghiệm</span>
        </button>
      </div>

      <div class="controls-right" style="display: flex; align-items: center; gap: 0.75rem;">
        <label for="slider-r-ch04" style="font-size: 0.85rem; color: var(--text-muted);">Nhiễu đo R: <strong id="label-r-ch04" style="color: var(--accent-rose);">4.0</strong></label>
        <input type="range" id="slider-r-ch04" min="1.0" max="16.0" step="0.5" value="4.0" style="width: 120px;">
      </div>
    </div>
  </div>
</section>

<!-- Layer 6: Practical ROS 2 / C++ Architecture Bridge -->
<section id="ros2-bridge-ch04" class="content-section">
  <div class="ros2-bridge-card" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 4px solid var(--accent-emerald); border-radius: 8px; padding: 1.5rem; margin: 2rem 0;">
    <div class="bridge-header" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <span style="font-size: 1.5rem;">📡</span>
        <h3 style="margin: 0; color: var(--text-main);">Node ROS 2 C++ Ước Lượng Khoảng Cách Sonar 1D: <code>OneDParticleFilterNode</code></h3>
      </div>
      <span class="badge" style="background: rgba(16, 185, 129, 0.1); color: var(--accent-emerald); font-weight: 600; padding: 0.25rem 0.6rem; border-radius: 4px;">ROS 2 rclcpp Node</span>
    </div>

    <p style="font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">
      Chuyển đổi thuật toán Python trên thành một Node ROS 2 C++ chuẩn mực lắng nghe cảm biến siêu âm <code>sensor_msgs/msg/Range</code> và phát hành vị trí đã lọc <code>geometry_msgs/msg/PoseWithCovarianceStamped</code>:
    </p>

    <div class="code-header" style="display: flex; justify-content: space-between; align-items: center; background: #1e293b; color: #94a3b8; padding: 0.4rem 0.8rem; border-radius: 6px 6px 0 0; font-family: monospace; font-size: 0.85rem;">
      <span>one_d_particle_filter_node.cpp</span>
    </div>
    <pre style="margin-top: 0; border-radius: 0 0 6px 6px; background: #0f172a; padding: 1rem; overflow-x: auto;"><code class="language-cpp">#include &lt;rclcpp/rclcpp.hpp&gt;
#include &lt;sensor_msgs/msg/range.hpp&gt;
#include &lt;geometry_msgs/msg/pose_with_covariance_stamped.hpp&gt;
#include &lt;random&gt;

class OneDParticleFilterNode : public rclcpp::Node {
public:
    OneDParticleFilterNode() : Node("one_d_particle_filter_node"), N_(200), Q_(0.5f), R_(2.0f) {
        particles_.resize(N_, 0.0f);
        weights_.assign(N_, 1.0f / N_);

        sub_range_ = this-&gt;create_subscription&lt;sensor_msgs::msg::Range&gt;(
            "/sensor/sonar_range", 10,
            std::bind(&amp;OneDParticleFilterNode::on_range_received, this, std::placeholders::_1));

        pub_pose_ = this-&gt;create_publisher&lt;geometry_msgs::msg::PoseWithCovarianceStamped&gt;(
            "/estimated/pose_1d", 10);
    }

private:
    void on_range_received(const sensor_msgs::msg::Range::SharedPtr msg) {
        float z = msg-&gt;range;

        // 1. Predict (vận tốc u = 0.1 m/chu kỳ)
        for (auto&amp; p : particles_) {
            p += 0.1f + sample_gaussian(std::sqrt(Q_));
        }

        // 2. Weighting &amp; Normalization
        float sum_w = 0.0f;
        for (size_t i = 0; i &lt; N_; ++i) {
            float err = z - particles_[i];
            weights_[i] *= std::exp(-0.5f * (err * err) / R_);
            sum_w += weights_[i];
        }
        for (auto&amp; w : weights_) w /= (sum_w + 1e-12f);

        // 3. Estimate Mean
        float x_hat = 0.0f;
        for (size_t i = 0; i &lt; N_; ++i) x_hat += weights_[i] * particles_[i];

        // 4. Publish PoseStamped
        geometry_msgs::msg::PoseWithCovarianceStamped out;
        out.header = msg-&gt;header;
        out.pose.pose.position.x = x_hat;
        pub_pose_-&gt;publish(out);
    }

    size_t N_;
    float Q_, R_;
    std::vector&lt;float&gt; particles_;
    std::vector&lt;float&gt; weights_;
    rclcpp::Subscription&lt;sensor_msgs::msg::Range&gt;::SharedPtr sub_range_;
    rclcpp::Publisher&lt;geometry_msgs::msg::PoseWithCovarianceStamped&gt;::SharedPtr pub_pose_;
};</code></pre>
  </div>
</section>
"""

rendered = render_page(ch, CHAPTER_INFO, content_html)
out_path = os.path.join(CHAPTERS_DIR, "ch04.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(rendered)

print(f"Successfully generated {out_path} ({len(rendered)} bytes)")
