# -*- coding: utf-8 -*-
"""
Chapter 02 Builder: Từ Ý Tưởng Đến Biểu Diễn Toán Học
"""

import os
from template_helpers import render_page
from build_portal import CHAPTER_INFO, CHAPTERS_DIR

ch = CHAPTER_INFO[1]

content_html = r"""
<!-- Layer 2: Why It Matters Box -->
<div class="why-matters-box">
  <div class="why-matters-header">
    <span class="why-matters-icon">💡</span>
    <h3 class="why-matters-title">Tại Sao Cần Hiểu Bản Chất Xác Suất Như Một Histogram Chuyển Động?</h3>
  </div>
  <p class="why-matters-text">
    Toán học xác suất cổ điển đòi hỏi chúng ta giải các tích phân vi phân nhiều chiều (multidimensional Chapman-Kolmogorov integrals) để tính toán phân bố niềm tin hậu nghiệm $p(x_k | z_{1:k})$. Đối với hệ phi tuyến, việc tìm nguyên hàm giải tích đóng là điều bất khả thi về mặt toán học. Phương pháp Monte Carlo mở ra một cuộc cách mạng tư duy: <strong>thay vì tìm kiếm phương trình giải tích của đường cong xác suất, ta thả một đàn mẫu ngẫu nhiên và dùng mật độ phân bố thực nghiệm (empirical density) để xấp xỉ nó</strong>. Chương này làm sáng tỏ nguyên lý biến đổi tích phân thành phép tính trung bình số học, nền tảng Luật Số Lớn, và giải phẫu cấu trúc dữ liệu của một hạt mẫu trong bộ nhớ máy tính.
  </p>
</div>

<!-- Section 2.1 -->
<section id="sec-2-1" class="content-section">
  <h2 class="section-heading">2.1 Khái Niệm Niềm Tin Xác Suất (The Concept of a Belief)</h2>
  <p class="lead-text">
    Trong robot học xác suất, một <em>niềm tin</em> (belief) phản ánh toàn bộ trạng thái tri thức nội tại của robot về thế giới xung quanh, được điều hòa bởi toàn bộ lịch sử các lệnh điều khiển $u_{1:k}$ và các phép đo lường cảm biến $z_{1:k}$.
  </p>
  <div class="formula-card">
    <div class="formula-header">
      <span class="formula-badge">Định Nghĩa Niềm Tin Hậu Nghiệm Bayes</span>
    </div>
    <div class="formula-body">
      $$\text{bel}(x_k) = p(x_k | z_{1:k}, u_{1:k})$$
    </div>
    <div class="formula-legend">
      <strong>Ký hiệu:</strong>
      <ul>
        <li>$x_k$: Trạng thái thực ẩn giấu tại thời điểm $k$.</li>
        <li>$z_{1:k} = \{z_1, z_2, \dots, z_k\}$: Chuỗi các số đo cảm biến từ đầu đến thời điểm $k$.</li>
        <li>$u_{1:k} = \{u_1, u_2, \dots, u_k\}$: Chuỗi các lệnh điều khiển (odometry hoặc vận tốc động cơ).</li>
      </ul>
    </div>
  </div>

  <h3 id="sec-2-1-1" class="subsection-heading">2.1.1 Niềm tin liên tục đối sánh với niềm tin rời rạc</h3>
  <p>
    Thế giới thực liên tục: vị trí robot $x \in \mathbb{R}^3$, vận tốc $v \in \mathbb{R}^3$. Nếu ta rời rạc hóa không gian thành lưới ô vuông (grid cells như trong Markov Localization), với một bản đồ $100\text{ m} \times 100\text{ m}$ và độ phân giải ô $5\text{ cm}$, số lượng ô nhớ trạng thái cần duy trì sẽ là $2000 \times 2000 = 4.000.000$ ô. Nếu thêm góc quay $\theta$ (360 độ rời rạc 1 độ), bộ nhớ bùng nổ lên $1.44 \times 10^9$ trạng thái — vượt xa năng lực xử lý thời gian thực của máy tính nhúng trên robot.
  </p>
  <p>
    Bộ lọc hạt dung hòa cả hai thế giới: mỗi hạt mang một tọa độ thực tế <strong>liên tục tuyệt đối</strong> ($x^{(i)} \in \mathbb{R}^n$), nhưng toàn bộ phân bố được biểu diễn bằng một tập hợp <strong>rời rạc hữu hạn</strong> gồm $N$ hạt mẫu.
  </p>

  <h3 id="sec-2-1-2" class="subsection-heading">2.1.2 Biểu diễn xác suất như một Histogram chuyển động (Histogram in Motion)</h3>
  <p>
    Tác giả Sahil Rajesh Dhayalkar nhấn mạnh một trực giác hình học vô cùng đẹp đẽ: <em>Hãy hình dung niềm tin xác suất như một biểu đồ tần suất (Histogram) liên tục biến dạng và chuyển động trong không gian pha</em>.
  </p>
  <p>
    Khi robot đứng yên và nhận thông tin cảm biến, các cột histogram tại các vị trí phù hợp với dữ liệu cảm biến dâng cao lên, còn các cột ở nơi sai lệch xẹp xuống. Khi robot di chuyển, các cột trôi dạt về phía trước, đồng thời rộng bè ra do nhiễu động học tích lũy. Bộ lọc hạt chính là một cơ cấu vật lý hóa biểu đồ histogram đó thành các hạt cơ bản.
  </p>
</section>

<!-- Section 2.2 -->
<section id="sec-2-2" class="content-section">
  <h2 class="section-heading">2.2 Tại Sao Chọn Phương Pháp Monte Carlo? (Why Monte Carlo?)</h2>
  <p>
    Phương pháp Monte Carlo (được khai sinh bởi Stanislaw Ulam và John von Neumann tại Phòng thí nghiệm Los Alamos trong dự án Manhattan) là công cụ toán học tối thượng để giải quyết các bài toán tích phân nhiều chiều phức tạp bằng phương pháp lấy mẫu ngẫu nhiên lặp đi lặp lại.
  </p>

  <h3 id="sec-2-2-1" class="subsection-heading">2.2.1 Nguyên lý cốt lõi: Chuyển tích phân thành trung bình mẫu</h3>
  <p>
    Trong lý thuyết ước lượng, ta thường xuyên cần tính kỳ vọng của một hàm số bất kỳ $g(x)$ theo phân bố xác suất $p(x)$:
  </p>
  <div class="formula-card">
    <div class="formula-header">
      <span class="formula-badge">Chuyển Đổi Tích Phân Monte Carlo Cốt Lõi</span>
    </div>
    <div class="formula-body">
      $$\mathbb{E}[g(x)] = \int_{-\infty}^{\infty} g(x) p(x) \, dx \;\approx\; \frac{1}{N} \sum_{i=1}^N g(x^{(i)})$$
    </div>
    <div class="formula-legend">
      <strong>Điều kiện:</strong> Các mẫu $x^{(i)}$ ($i = 1, \dots, N$) được rút độc lập và cùng phân bố (i.i.d) từ hàm mật độ xác suất $p(x)$.
    </div>
  </div>

  <h3 id="sec-2-2-2" class="subsection-heading">2.2.2 Luật Số Lớn (Law of Large Numbers - LLN)</h3>
  <p>
    Theo Luật Số Lớn mạnh (Strong Law of Large Numbers), khi số lượng mẫu $N$ tiến dần ra vô cùng, trung bình mẫu thực nghiệm hội tụ hầu chắc chắn (almost surely) về kỳ vọng toán học lý thuyết:
  </p>
  <div class="formula-card">
    <div class="formula-body">
      $$\mathbb{P}\left( \lim_{N \to \infty} \frac{1}{N} \sum_{i=1}^N g(x^{(i)}) = \mathbb{E}[g(x)] \right) = 1$$
    </div>
  </div>
  <p>
    Điều này bảo đảm rằng bất kể hình thù của phân bố xác suất $p(x)$ có phức tạp, gồ ghề hay kỳ quái đến đâu, chỉ cần ta lấy đủ số lượng hạt mẫu $N$, ước lượng Monte Carlo sẽ hội tụ hoàn toàn về đáp án chính xác.
  </p>

  <h3 id="sec-2-2-3" class="subsection-heading">2.2.3 Định lý Giới hạn Trung tâm (Central Limit Theorem - CLT)</h3>
  <p>
    Định lý Giới hạn Trung tâm cung cấp tốc độ hội tụ của xấp xỉ Monte Carlo. Sai số ước lượng giữa trung bình mẫu và kỳ vọng thực tế phân bố chuẩn với độ lệch chuẩn tỷ lệ nghịch với căn bậc hai của số mẫu:
  </p>
  <div class="formula-card">
    <div class="formula-body">
      $$\sigma_{error} \propto \frac{1}{\sqrt{N}}$$
    </div>
  </div>
  <p>
    <strong>Điểm mấu chốt:</strong> Tốc độ hội tụ $\mathcal{O}(1/\sqrt{N})$ của phương pháp Monte Carlo <em>hoàn toàn độc lập với số chiều của không gian trạng thái $n$</em>! Đây là lý do tại sao Monte Carlo đánh bại hoàn toàn các phương pháp tích phân cầu phương lưới đều (Simpson hay Gauss-Legendre có độ phức tạp lũy thừa $\mathcal{O}(K^{-1/n})$).
  </p>
</section>

<!-- Section 2.3 -->
<section id="sec-2-3" class="content-section">
  <h2 class="section-heading">2.3 Giải Phẫu Một Hạt Mẫu (The Anatomy of a Particle)</h2>
  <p>
    Trong mã nguồn lập trình, một "hạt" không phải là một khái niệm trừu tượng mà là một bản ghi cấu trúc dữ liệu cụ thể.
  </p>

  <h3 id="sec-2-3-1" class="subsection-heading">2.3.1 Biểu diễn trạng thái $x^{(i)}$</h3>
  <p>
    Hạt thứ $i$ mang một vector trạng thái hoàn chỉnh biểu thị một giả thuyết cụ thể về hệ thống:
  </p>
  <div class="formula-card">
    <div class="formula-body">
      $$x^{(i)}_k = \begin{bmatrix} p_x^{(i)} \\ p_y^{(i)} \\ \theta^{(i)} \\ v_x^{(i)} \\ v_y^{(i)} \end{bmatrix} \in \mathbb{R}^n$$
    </div>
  </div>

  <h3 id="sec-2-3-2" class="subsection-heading">2.3.2 Trọng số quan trọng $w^{(i)}$ (Importance Weights)</h3>
  <p>
    Mỗi hạt đi kèm một đại lượng vô hướng $w^{(i)}_k \ge 0$, thể hiện "độ tin cậy" hoặc mức độ tương thích của giả thuyết đó đối với tín hiệu cảm biến thực tế đo được tại chu kỳ $k$:
  </p>
  <div class="formula-card">
    <div class="formula-body">
      $$w^{(i)}_k \propto p(z_k | x^{(i)}_k)$$
    </div>
  </div>

  <h3 id="sec-2-3-3" class="subsection-heading">2.3.3 Chuẩn hóa trọng số (Normalization)</h3>
  <p>
    Để tập hợp các hạt tạo thành một phân bố xác suất hợp lệ, tổng tất cả các trọng số trong toàn bộ đám mây hạt bắt buộc phải bằng đúng 1:
  </p>
  <div class="formula-card">
    <div class="formula-body">
      $$\tilde{w}^{(i)}_k = \frac{w^{(i)}_k}{\sum_{j=1}^N w^{(j)}_k}, \quad \sum_{i=1}^N \tilde{w}^{(i)}_k = 1.0$$
    </div>
  </div>
  <p>
    Khi đó, hàm mật độ xác suất liên tục $p(x_k | z_{1:k})$ được biểu diễn xấp xỉ bằng một tổng hàm Dirac delta có trọng số:
  </p>
  <div class="formula-card">
    <div class="formula-body">
      $$p(x_k | z_{1:k}) \approx \sum_{i=1}^N \tilde{w}^{(i)}_k \delta(x_k - x^{(i)}_k)$$
    </div>
  </div>
</section>

<!-- Section 2.4 -->
<section id="sec-2-4" class="content-section">
  <h2 class="section-heading">2.4 Ba Giai Đoạn Vận Hành Cốt Lõi (The Three Core Phases)</h2>
  <p>
    Toàn bộ vòng lặp thời gian thực của Bộ Lọc Hạt quay quanh chu trình tuần hoàn 3 giai đoạn:
  </p>

  <div class="phases-timeline" style="display: flex; flex-direction: column; gap: 1rem; margin: 1.5rem 0;">
    <div class="timeline-step" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 4px solid var(--primary); padding: 1.25rem; border-radius: 6px;">
      <h4 id="sec-2-4-1" style="color: var(--primary); margin-top: 0;">1. Giai Đoạn Dự Đoán (Prediction: Moving particles forward)</h4>
      <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0.5rem;">
        Khi robot di chuyển theo lệnh điều khiển $u_k$, mỗi hạt được dịch chuyển theo mô hình động học kèm thêm nhiễu ngẫu nhiên được rút từ phân bố nhiễu hệ thống:
      </p>
      $$x^{(i)}_k = f(x^{(i)}_{k-1}, u_k) + w^{(i)}_k, \quad w^{(i)}_k \sim p(w_k)$$
      <p style="font-size: 0.9rem; color: var(--text-subtle); margin-bottom: 0;">
        <em>Tác động hình học:</em> Đám mây hạt di chuyển theo hướng chuyển động và tản rộng ra, phản ánh sự gia tăng độ bất định khi chưa có quan sát mới.
      </p>
    </div>

    <div class="timeline-step" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 4px solid var(--accent-amber); padding: 1.25rem; border-radius: 6px;">
      <h4 id="sec-2-4-2" style="color: var(--accent-amber); margin-top: 0;">2. Giai Đoạn Đánh Trọng Số (Weighting: Evaluating likelihoods)</h4>
      <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0.5rem;">
        Cảm biến trả về số đo thực tế $z_k$. Mỗi hạt dự đoán số đo mà cảm biến đáng lẽ phải thấy nếu robot ở trạng thái của hạt đó: $\hat{z}^{(i)}_k = h(x^{(i)}_k)$. Trọng số của hạt được tính theo hàm hợp lý (likelihood):
      </p>
      $$w^{(i)}_k = p(z_k | x^{(i)}_k)$$
      <p style="font-size: 0.9rem; color: var(--text-subtle); margin-bottom: 0;">
        <em>Tác động hình học:</em> Các hạt có dự đoán trùng khớp với cảm biến nhận trọng số lớn; các hạt sai lệch bị giảm trọng số về gần 0.
      </p>
    </div>

    <div class="timeline-step" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 4px solid var(--accent-emerald); padding: 1.25rem; border-radius: 6px;">
      <h4 id="sec-2-4-3" style="color: var(--accent-emerald); margin-top: 0;">3. Giai Đoạn Tái Chọn Mẫu (Resampling: Survival of the fittest)</h4>
      <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0.5rem;">
        Áp dụng quy luật chọn lọc tự nhiên: các hạt có trọng số nhỏ bị loại bỏ; các hạt có trọng số lớn được nhân bản thành nhiều hạt mới có vị trí giống hệt nhưng nhận lại trọng số đồng đều $1/N$:
      </p>
      $$\{x^{(i)}_k, w^{(i)}_k\}_{i=1}^N \xrightarrow{\text{Resample}} \{x^{\prime(j)}_k, \frac{1}{N}\}_{j=1}^N$$
      <p style="font-size: 0.9rem; color: var(--text-subtle); margin-bottom: 0;">
        <em>Tác động hình học:</em> Tập trung tài nguyên tính toán vào các vùng không gian có xác suất cao nhất, đưa đám mây hạt co cụm chính xác quanh robot.
      </p>
    </div>
  </div>
</section>

<!-- Layer 4: Worked Numerical Example -->
<section id="worked-example-ch02" class="content-section">
  <div class="worked-example-card">
    <div class="worked-example-header">
      <span class="worked-badge">VÍ DỤ SỐ HỌC 4 BƯỚC</span>
      <h3 class="worked-title">Tính Toán Tích Phân Kỳ Vọng Monte Carlo Cho Hàm Tín Hiệu Dao Động</h3>
    </div>
    <p class="worked-intro">
      Xét bài toán tính kỳ vọng toán học của hàm số phi tuyến $g(x) = \exp(-0.5 x^2) \cdot \cos(2x)$ dưới phân bố đều $x \sim \mathcal{U}[-2, 2]$. Giá trị giải tích chính xác của tích phân là $I = \frac{1}{4} \int_{-2}^2 \exp(-0.5 x^2) \cos(2x) \, dx \approx 0.1264$. Ta thực hiện xấp xỉ Monte Carlo với $N=4$ hạt mẫu cụ thể.
    </p>

    <div class="worked-step-grid">
      <div class="step-card">
        <div class="step-num">BƯỚC 1</div>
        <div class="step-title">Rút 4 Mẫu Ngẫu Nhiên Đồng Nhất</div>
        <div class="step-body">
          <p>Phân bố đều trên đoạn $[-2, 2]$, độ dài đoạn $L = 4$.</p>
          <p>Bốn mẫu ngẫu nhiên được rút:</p>
          <ul>
            <li>$x^{(1)} = -1.50$</li>
            <li>$x^{(2)} = -0.40$</li>
            <li>$x^{(3)} = 0.60$</li>
            <li>$x^{(4)} = 1.80$</li>
          </ul>
        </div>
      </div>

      <div class="step-card">
        <div class="step-num">BƯỚC 2</div>
        <div class="step-title">Tính Giá Trị Hàm Số $g(x^{(i)})$</div>
        <div class="step-body">
          <p>Hàm số: $g(x) = e^{-0.5 x^2} \cos(2x)$</p>
          <ul>
            <li>$g(x^{(1)}) = e^{-1.125} \cos(-3.0) = 0.3246 \cdot (-0.9899) = -0.3213$</li>
            <li>$g(x^{(2)}) = e^{-0.08} \cos(-0.8) = 0.9231 \cdot 0.6967 = +0.6431$</li>
            <li>$g(x^{(3)}) = e^{-0.18} \cos(1.2) = 0.8353 \cdot 0.3624 = +0.3027$</li>
            <li>$g(x^{(4)}) = e^{-1.62} \cos(3.6) = 0.1979 \cdot (-0.8968) = -0.1775$</li>
          </ul>
        </div>
      </div>

      <div class="step-card">
        <div class="step-num">BƯỚC 3</div>
        <div class="step-title">Tính Trung Bình Mẫu & Sai Số</div>
        <div class="step-body">
          <p>Ước lượng kỳ vọng Monte Carlo:</p>
          $$\hat{I}_4 = \frac{1}{4} \sum_{i=1}^4 g(x^{(i)}) = \frac{-0.3213 + 0.6431 + 0.3027 - 0.1775}{4} = \frac{0.4470}{4} = 0.1118$$
          <p>Đối chiếu với chân giá trị $I = 0.1264$:</p>
          $$\text{Sai số tuyệt đối } |\hat{I}_4 - I| = |0.1118 - 0.1264| = 0.0146 \quad (11.5\%)$$
        </div>
      </div>

      <div class="step-card">
        <div class="step-num">BƯỚC 4</div>
        <div class="step-title">Đánh Giá Hội Tụ Khi Tăng Lên $N=1000$</div>
        <div class="step-body">
          <p>Theo Định lý Giới hạn Trung tâm:</p>
          $$\sigma_{\hat{I}} = \frac{s_g}{\sqrt{N}}$$
          <p>Với $N=1000$ mẫu, sai số tiêu chuẩn giảm xuống $\sqrt{1000/4} \approx 15.8$ lần, sai số tuyệt đối co lại chỉ còn $\pm 0.0009$, đạt độ tin cậy $99.9\%$.</p>
          <p><strong>Kết luận:</strong> Monte Carlo chuyển hóa bài toán tích phân vi phân khó thành các phép cộng trừ nhân chia số học cơ bản cực kỳ phù hợp với GPU và bộ xử lý song song.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Layer 5: Interactive Simulator -->
<section id="sim-ch02" class="content-section">
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title-group">
        <span class="sim-badge">MÔ PHỎNG TƯƠNG TÁC 60 FPS</span>
        <h3 class="sim-title">Biểu Đồ Histogram Động & Truyền Trạng Thái Phi Tuyến Monte Carlo</h3>
      </div>
      <p class="sim-desc">
        Quan sát trực tiếp nguyên lý <em>"Xác suất như một Histogram chuyển động"</em>. Đám mây hạt ban đầu phân bố Gauss được đẩy qua phương trình động học phi tuyến: $x_k = 0.5 x_{k-1} + \frac{25 x_{k-1}}{1 + x_{k-1}^2} + 8 \cos(1.2 t) + \eta_k$. Tinh chỉnh số hạt $N$ từ 50 đến 1000 để thấy rõ Luật Số Lớn làm mượt mà đường cong mật độ xác suất.
      </p>
    </div>

    <!-- Canvas -->
    <div class="sim-canvas-wrapper" style="background: #0f172a; border-radius: 8px; overflow: hidden; margin: 1rem 0;">
      <canvas id="sim-canvas-ch02" style="width: 100%; height: 360px; display: block;"></canvas>
    </div>

    <!-- Controls -->
    <div class="sim-controls-row" style="display: flex; gap: 1rem; flex-wrap: wrap; align-items: center; justify-content: space-between;">
      <div class="controls-left" style="display: flex; gap: 0.5rem; flex-wrap: wrap; align-items: center;">
        <button id="btn-step-ch02" class="btn btn-primary">
          <span>⚡ Bước Phi Tuyến Kế Tiếp (k+1)</span>
        </button>
        <button id="btn-toggle-ch02" class="btn btn-outline">
          <span>▶️ Chạy Liên Tục (Play)</span>
        </button>
        <button id="btn-reset-ch02" class="btn btn-secondary">
          <span>🔄 Đặt Lại Mẫu</span>
        </button>
      </div>

      <div class="controls-right" style="display: flex; align-items: center; gap: 0.75rem;">
        <label for="slider-n-ch02" style="font-size: 0.85rem; color: var(--text-muted);">Số hạt N: <strong id="label-n-ch02" style="color: var(--primary);">350</strong></label>
        <input type="range" id="slider-n-ch02" min="50" max="1000" step="50" value="350" style="width: 130px;">
      </div>
    </div>
  </div>
</section>

<!-- Layer 6: Practical ROS 2 / C++ Architecture Bridge -->
<section id="ros2-bridge-ch02" class="content-section">
  <div class="ros2-bridge-card" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 4px solid var(--accent-emerald); border-radius: 8px; padding: 1.5rem; margin: 2rem 0;">
    <div class="bridge-header" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <span style="font-size: 1.5rem;">⚡</span>
        <h3 style="margin: 0; color: var(--text-main);">Tối Ưu Cấu Trúc Dữ Liệu Bộ Lọc Hạt Trong C++20 & Tăng Tốc OpenMP</h3>
      </div>
      <span class="badge" style="background: rgba(16, 185, 129, 0.1); color: var(--accent-emerald); font-weight: 600; padding: 0.25rem 0.6rem; border-radius: 4px;">C++20 SIMD & OpenMP</span>
    </div>

    <p style="font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">
      Khi lập trình bộ lọc hạt cho xe tự hành chạy trên nền tảng phần cứng giới hạn (như Raspberry Pi 5 hoặc NVIDIA Jetson Orin Nano), cách tổ chức bộ nhớ của hạt quyết định 80% hiệu năng FPS:
    </p>

    <div class="code-header" style="display: flex; justify-content: space-between; align-items: center; background: #1e293b; color: #94a3b8; padding: 0.4rem 0.8rem; border-radius: 6px 6px 0 0; font-family: monospace; font-size: 0.85rem;">
      <span>particle_cloud_simd.hpp (Cấu trúc bộ nhớ SoA thân thiện L1/L2 Cache)</span>
    </div>
    <pre style="margin-top: 0; border-radius: 0 0 6px 6px; background: #0f172a; padding: 1rem; overflow-x: auto;"><code class="language-cpp">#include &lt;vector&gt;
#include &lt;cmath&gt;
#include &lt;omp.h&gt;

// SoA (Structure of Arrays) tối ưu hóa truy cập tuần tự Cache Lines & SIMD Vectorization
struct ParticleCloud2D {
    std::vector&lt;float&gt; x;       // Tọa độ X liên tục trong RAM
    std::vector&lt;float&gt; y;       // Tọa độ Y liên tục
    std::vector&lt;float&gt; theta;   // Góc hướng yaw
    std::vector&lt;float&gt; weight;  // Trọng số chuẩn hóa

    void resize(size_t n) {
        x.resize(n); y.resize(n); theta.resize(n);
        weight.assign(n, 1.0f / static_cast&lt;float&gt;(n));
    }

    // Dự đoán động học song song hóa bằng OpenMP đa luồng (Multi-core scaling)
    void predict(float delta_dist, float delta_rot1, float delta_rot2, 
                 float s_dist, float s_rot1, float s_rot2) {
        const size_t N = x.size();
        #pragma omp parallel for schedule(static)
        for (size_t i = 0; i &lt; N; ++i) {
            // Nhiễu Gauss sinh cục bộ theo từng luồng
            float r1 = delta_rot1 + sample_gaussian(s_rot1);
            float d  = delta_dist + sample_gaussian(s_dist);
            float r2 = delta_rot2 + sample_gaussian(s_rot2);

            theta[i] += r1;
            x[i]     += d * std::cos(theta[i]);
            y[i]     += d * std::sin(theta[i]);
            theta[i] += r2;
        }
    }
};</code></pre>
  </div>
</section>
"""

rendered = render_page(ch, CHAPTER_INFO, content_html)
out_path = os.path.join(CHAPTERS_DIR, "ch02.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(rendered)

print(f"Successfully generated {out_path} ({len(rendered)} bytes)")
