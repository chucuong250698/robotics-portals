# -*- coding: utf-8 -*-
"""
Chapter 01 Builder: Giới Thiệu & Nhu Cầu Của Bộ Lọc Hạt
"""

import os
from template_helpers import render_page
from build_portal import CHAPTER_INFO, CHAPTERS_DIR

ch = CHAPTER_INFO[0]

content_html = r"""
<!-- Layer 2: Why It Matters Box -->
<div class="why-matters-box">
  <div class="why-matters-header">
    <span class="why-matters-icon">💡</span>
    <h3 class="why-matters-title">Tại Sao Cần Bộ Lọc Hạt Trong Robot Học & Xe Tự Hành?</h3>
  </div>
  <p class="why-matters-text">
    Trong thế giới lý thuyết lý tưởng, mọi chuyển động đều thẳng và mọi nhiễu đều tuân theo phân bố chuẩn Gauss hình chuông đối xứng. Bộ lọc Kalman (KF) và Kalman Mở rộng (EKF) đã thống trị kỹ thuật điều khiển hàng không vũ trụ suốt nửa thế kỷ nhờ tính tối ưu toán học tuyệt đối trong môi trường tuyến tính. Tuy nhiên, khi một robot di động hoạt động trong tòa nhà nhiều phòng đối xứng, di chuyển trượt bánh trên thảm, hoặc cảm biến LiDAR gặp hiện tượng phản xạ gương, niềm tin xác suất về vị trí của robot bị xé nhỏ thành <strong>nhiều đỉnh khả dĩ (multimodal distribution)</strong>. Bộ lọc Kalman bị ép buộc phải ép toàn bộ niềm tin đó vào một đỉnh Gauss duy nhất, dẫn đến việc ước lượng robot nằm... xuyên qua bức tường ngăn giữa hai phòng! <strong>Bộ lọc hạt (Particle Filter / Monte Carlo Localization)</strong> ra đời để phá bỏ xiềng xích tham số hóa, cho phép robot duy trì hàng nghìn giả thuyết song song và giải quyết dứt điểm bài toán định vị toàn cục cũng như sự cố "bắt cóc robot" (Kidnapped Robot Problem).
  </p>
</div>

<!-- Section 1.1 -->
<section id="sec-1-1" class="content-section">
  <h2 class="section-heading">1.1 Nhu Cầu Cấp Thiết Của Bộ Lọc Hạt (The Need for Particle Filters)</h2>
  <p class="lead-text">
    Mọi thuật toán ước lượng trạng thái trong kỹ thuật tự động hóa đều bắt đầu từ một khát vọng nguyên bản: <em>khám phá chân giá trị ẩn giấu đằng sau chuỗi dữ liệu đo lường ồn ào, bất định và chứa đầy sai số</em>.
  </p>
  <p>
    Trong hệ thống robot thực tế, chúng ta không bao giờ có thể đo lường trực tiếp toàn bộ vector trạng thái thực $x_k \in \mathbb{R}^n$ (chẳng hạn vị trí tọa độ tuyệt đối, vận tốc góc, độ trượt bánh xe). Thay vào đó, bộ điều khiển chỉ nhận được chuỗi quan sát $z_{1:k} = \{z_1, z_2, \dots, z_k\}$ từ các cảm biến gián tiếp như IMU, Odometry bánh xe, camera hoặc LiDAR:
  </p>
  
  <div class="formula-card">
    <div class="formula-header">
      <span class="formula-badge">Phương Trình Trạng Thái Hệ Thống Tổng Quát</span>
    </div>
    <div class="formula-body">
      $$\begin{cases} x_k = f(x_{k-1}, u_k) + w_k & \text{(Mô hình chuyển động / Động học)} \\ z_k = h(x_k) + v_k & \text{(Mô hình quan sát / Cảm biến)} \end{cases}$$
    </div>
    <div class="formula-legend">
      <strong>Bảng giải nghĩa tham số & đơn vị SI:</strong>
      <ul>
        <li>$x_k \in \mathbb{R}^n$: Vector trạng thái thực tại thời điểm rời rạc $k$ (ví dụ: $[x, y, \theta]^T$ tính bằng $[\text{m}, \text{m}, \text{rad}]$).</li>
        <li>$u_k \in \mathbb{R}^m$: Vector lệnh điều khiển đầu vào (ví dụ: vận tốc dài $v$ và vận tốc góc $\omega$).</li>
        <li>$z_k \in \mathbb{R}^p$: Vector quan sát đo lường từ cảm biến tại thời điểm $k$.</li>
        <li>$f(\cdot), h(\cdot)$: Các hàm toán học ánh xạ động học chuyển động và cơ chế tạo tín hiệu cảm biến.</li>
        <li>$w_k, v_k$: Nhiễu hệ thống (process noise) và nhiễu đo lường (measurement noise).</li>
      </ul>
    </div>
  </div>

  <p>
    Bộ lọc Kalman (Kalman Filter - KF) phát minh năm 1960 đã đưa ra lời giải giải tích đẹp đẽ khi $f(\cdot)$ và $h(\cdot)$ là các toán tử tuyến tính, đồng thời $w_k \sim \mathcal{N}(0, Q)$ và $v_k \sim \mathcal{N}(0, R)$ là các phân bố chuẩn Gauss. Nhưng khi robot va chạm vật cản, bánh xe quay trượt trên nền ướt, hoặc cảm biến khoảng cách trả về các xung tín hiệu rời rạc, các giả định tuyến tính và chuẩn hóa của Kalman hoàn toàn sụp đổ.
  </p>
</section>

<!-- Section 1.2 -->
<section id="sec-1-2" class="content-section">
  <h2 class="section-heading">1.2 Những Giới Hạn Cốt Lõi Của Bộ Lọc Kalman (Limitations of the Kalman Filter)</h2>
  <p>
    Để thấu hiểu tại sao Bộ Lọc Hạt trở thành trụ cột của robot học hiện đại, ta cần mổ xẻ chính xác 3 giới hạn nền tảng khiến họ bộ lọc Kalman (KF, EKF) thất bại trong thực tế:
  </p>

  <h3 id="sec-1-2-1" class="subsection-heading">1.2.1 Tính phi tuyến nghiêm trọng (Nonlinearity)</h3>
  <p>
    Trong hầu hết cơ cấu robot, động học góc quay lượng giác $\cos(\theta), \sin(\theta)$ và mô hình cảm biến đo cự ly $d = \sqrt{(x - x_{landmark})^2 + (y - y_{landmark})^2}$ có tính phi tuyến rất gắt. Bộ lọc Kalman Mở rộng (EKF) cố gắng giải quyết bằng cách xấp xỉ tuyến tính Taylor bậc 1 quanh điểm ước lượng hiện tại:
  </p>
  <div class="formula-card">
    <div class="formula-body">
      $$F_k = \left. \frac{\partial f}{\partial x} \right|_{\hat{x}_{k-1}}, \quad H_k = \left. \frac{\partial h}{\partial x} \right|_{\hat{x}_k^-}$$
    </div>
  </div>
  <p>
    Phép xấp xỉ tiếp tuyến này chỉ hợp lệ trong một lân cận vô cùng nhỏ. Khi hệ thống có độ cong lớn hoặc độ bất định ban đầu rộng, ma trận Jacobian làm biến dạng hoàn toàn elip sai số, khiến EKF đánh giá quá lạc quan về độ chính xác của chính mình và nhanh chóng dẫn đến <em>phân kỳ nghiệm (filter divergence)</em>.
  </p>

  <h3 id="sec-1-2-2" class="subsection-heading">1.2.2 Phân bố xác suất phi Gauss và đa đỉnh (Non-Gaussian distributions)</h3>
  <p>
    Giới hạn nghiêm trọng nhất của Kalman là tiên đề: <strong>Niềm tin xác suất luôn là một phân bố đơn đỉnh Gauss (unimodal Gaussian)</strong> được đặc trưng duy nhất bởi cặp tham số $(\mu, \Sigma)$. Hãy xem xét kịch bản kinh điển: một robot di chuyển trong hành lang đối xứng có hai cánh cửa giống hệt nhau tại $x = 10\text{ m}$ và $x = 40\text{ m}$. Cảm biến thông báo: <em>"Robot đang đứng trước một cánh cửa"</em>.
  </p>
  <p>
    Lúc này, hàm mật độ xác suất thực tế của robot sở hữu hai đỉnh nhọn đối xứng (Bimodal distribution) tại $10\text{ m}$ và $40\text{ m}$. Do Kalman chỉ có thể duy trì một đỉnh duy nhất, nó sẽ lấy trung bình cộng và đặt $\mu = 25\text{ m}$ với độ lệch chuẩn lớn $\sigma$. Hậu quả là bộ lọc khẳng định robot có khả năng cao nhất đang đứng ở vị trí $25\text{ m}$ — nơi thực tế chỉ là một bức tường trơn láng không có cửa!
  </p>

  <h3 id="sec-1-2-3" class="subsection-heading">1.2.3 Nhiễu đo lường có đuôi dày và giá trị ngoại lai (Non-Gaussian noise)</h3>
  <p>
    Phân bố chuẩn Gauss $\mathcal{N}(0, \sigma^2)$ gán xác suất gần như bằng 0 cho các sự kiện vượt quá $3\sigma$. Tuy nhiên, cảm biến thực tế thường xuyên hứng chịu các xung nhiễu đuôi dày (heavy-tailed Cauchy / Laplace noise), chẳng hạn như tia laser LiDAR xuyên qua cửa kính, hoặc sóng siêu âm bị phản xạ đa đường (multipath specular reflection). Khi một số đo ngoại lai xuất hiện, bộ lọc Kalman kéo giật giá trị ước lượng trung bình $\mu$ về phía sai số đó, phá hủy hoàn toàn quỹ đạo ước lượng.
  </p>
</section>

<!-- Section 1.3 -->
<section id="sec-1-3" class="content-section">
  <h2 class="section-heading">1.3 Những Ưu Thế Vượt Trội Của Bộ Lọc Hạt (Key Strengths)</h2>
  <p>
    Bộ lọc hạt giải phóng kỹ sư khỏi việc cố gắng gò ép thế giới thực vào các công thức giải tích đóng. Bốn ưu thế quyết định bao gồm:
  </p>

  <div class="features-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
    <div class="feature-card" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
      <h4 id="sec-1-3-1" style="color: var(--primary); margin-top: 0;">1.3.1 Biểu Diễn Mọi Phân Bố Xác Suất</h4>
      <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0;">
        Không cần giả định tham số $(\mu, \Sigma)$. Bằng cách phân tán hàng trăm nghìn mẫu ngẫu nhiên, đám mây hạt có thể uốn lượn, phân tách thành nhiều cụm (multimodal), tạo thành hình vành khăn, chữ L hoặc bất kỳ hình thái hình học phức tạp nào.
      </p>
    </div>

    <div class="feature-card" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
      <h4 id="sec-1-3-2" style="color: var(--accent-emerald); margin-top: 0;">1.3.2 Dung Nạp Trực Tiếp Mọi Hàm Phi Tuyến</h4>
      <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0;">
        Không cần tính đạo hàm riêng ma trận Jacobian hay xấp xỉ chuỗi Taylor bậc cao. Mỗi hạt mẫu được đưa trực tiếp qua hàm phi tuyến thực $x^{(i)}_k = f(x^{(i)}_{k-1}, u_k) + w^{(i)}_k$ mà không làm mất mát bất kỳ thông tin bậc cao nào.
      </p>
    </div>

    <div class="feature-card" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
      <h4 id="sec-1-3-3" style="color: var(--accent-amber); margin-top: 0;">1.3.3 Kháng Nhiễu Cực Đoan & Outliers</h4>
      <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0;">
        Nếu cảm biến bị mất gói dữ liệu hoặc bắn ra một số đo vô lý, các hạt chỉ đơn giản nhận trọng số likelihood thấp trong chu kỳ đó. Cấu trúc đám mây hạt không bị biến dạng vĩnh viễn như ma trận hiệp phương sai của Kalman.
      </p>
    </div>

    <div class="feature-card" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
      <h4 id="sec-1-3-4" style="color: var(--accent-purple); margin-top: 0;">1.3.4 Khả Năng Co Giãn Tính Toán Linh Hoạt</h4>
      <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 0;">
        Kỹ sư có thể tự do đánh đổi giữa độ chính xác ước lượng và thời gian tính toán CPU bằng cách tinh chỉnh tham số số lượng hạt $N$. Khi CPU bận, giảm $N$ xuống 200 hạt; khi cần độ chính xác milimet, nâng lên 2000 hạt.
      </p>
    </div>
  </div>
</section>

<!-- Section 1.4 -->
<section id="sec-1-4" class="content-section">
  <h2 class="section-heading">1.4 Phép Ẩn Dụ Trực Quan: Tìm Bạn Trong Đám Đông (Finding a Friend in a Crowd)</h2>
  <p>
    Tác giả Sahil Rajesh Dhayalkar đưa ra một hình tượng trực quan sâu sắc: Hãy tưởng tượng bạn đang tìm kiếm người bạn thân trong một sân vận động âm nhạc chật kín 50.000 khán giả:
  </p>
  <ul>
    <li><strong>Khởi tạo:</strong> Bạn cử 200 thám tử (các hạt mẫu) tỏa đi khắp các khán đài ngẫu nhiên. Lúc này niềm tin phân bố đều trên toàn sân.</li>
    <li><strong>Thông tin gợi ý 1 (Quan sát):</strong> Bạn nhận được tin nhắn: <em>"Bạn đang mặc áo sơ mi màu xanh lá"</em>. Các thám tử đối chiếu người đứng gần họ: thám tử nào thấy người áo đỏ thì nhận điểm rất thấp ($w \to 0$), thám tử nào thấy người áo xanh lá thì nhận điểm rất cao ($w \gg 0$).</li>
    <li><strong>Tái chọn mẫu (Resampling):</strong> Bạn thu hồi các thám tử ở khu vực áo đỏ và điều động thêm thám tử tập trung dày đặc vào các khu vực phát hiện nhiều người mặc áo xanh.</li>
    <li><strong>Thông tin gợi ý 2:</strong> Tin nhắn tiếp theo: <em>"Bạn đang đứng gần quầy bán nước số 3"</em>. Các thám tử quanh quầy nước số 3 tiếp tục được nhân bản, nhanh chóng hội tụ chính xác vào vị trí người bạn.</li>
  </ul>
  <p>
    Đó chính là nguyên lý vận hành kỳ diệu của Bộ Lọc Hạt: <strong>Dự đoán — Đánh trọng số — Tái phân bố</strong>.
  </p>
</section>

<!-- Section 1.5 -->
<section id="sec-1-5" class="content-section">
  <h2 class="section-heading">1.5 Lộ Trình Tri Thức Của Toàn Bộ Chuyên Khảo (What Lies Ahead)</h2>
  <p>
    Toàn bộ chuyên khảo <em>Particle Filter Made Simple</em> được tinh gọn trong 5 chương học thuật liên kết hữu cơ theo 2 Trục kiến thức (Tracks):
  </p>
  <div class="table-responsive">
    <table class="data-table">
      <thead>
        <tr>
          <th>Track</th>
          <th>Chương</th>
          <th>Nội Dung Trọng Tâm</th>
          <th>Đích Đến Kỹ Thuật</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td rowspan="3"><strong>Track 1: Cơ Sở Lý Thuyết & Thuật Toán SIR</strong></td>
          <td>Chương 01</td>
          <td>Giới thiệu, hạn chế Kalman, triết lý đám mây hạt</td>
          <td>Định vị tư duy phi tuyến và phi Gauss</td>
        </tr>
        <tr>
          <td>Chương 02</td>
          <td>Biểu diễn niềm tin, Histogram in motion, Monte Carlo</td>
          <td>Toán học lấy mẫu tầm quan trọng và LLN</td>
        </tr>
        <tr>
          <td>Chương 03</td>
          <td>Thuật toán SIR 6 bước, thoái hóa mẫu, Neff, Systematic Resampling</td>
          <td>Làm chủ thuật toán lọc chuẩn mực toàn diện</td>
        </tr>
        <tr>
          <td rowspan="2"><strong>Track 2: Thực Hành Số Học & Lọc Đa Chiều</strong></td>
          <td>Chương 04</td>
          <td>Tính toán số học từng bước 1D (k=1,2,3), Python Code Lab 1D</td>
          <td>Thành thạo từng phép toán nhân chia ma trận số</td>
        </tr>
        <tr>
          <td>Chương 05</td>
          <td>Vector trạng thái đa biến, mô hình 2D/4D, Code Lab 2D, Kidnap Recovery</td>
          <td>Sẵn sàng triển khai trên Robot ROS 2 thực tế</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<!-- Layer 4: Worked Numerical Example -->
<section id="worked-example-ch01" class="content-section">
  <div class="worked-example-card">
    <div class="worked-example-header">
      <span class="worked-badge">VÍ DỤ SỐ HỌC 4 BƯỚC</span>
      <h3 class="worked-title">So Sánh Truyền Bất Định Tuyến Tính Hóa (Kalman) vs Truyền Mẫu Mật Độ (Monte Carlo)</h3>
    </div>
    <p class="worked-intro">
      Xét bài toán truyền trạng thái qua hàm phi tuyến bậc ba gắt: $y = f(x) = x^3 - 3x$, với trạng thái đầu vào là biến ngẫu nhiên Gauss $x \sim \mathcal{N}(0, 1^2)$. Ta thực hiện so sánh việc xấp xỉ kỳ vọng $E[y]$ và phương sai $\text{Var}(y)$ bằng phương pháp tiếp tuyến EKF đối sánh với bộ 5 hạt mẫu Monte Carlo.
    </p>

    <div class="worked-step-grid">
      <div class="step-card">
        <div class="step-num">BƯỚC 1</div>
        <div class="step-title">Khởi Tạo & Tuyến Tính Hóa Taylor (EKF)</div>
        <div class="step-body">
          <p>Điểm trung bình ban đầu: $\bar{x} = 0, \sigma_x^2 = 1.0$.</p>
          <p>Hàm phi tuyến: $f(x) = x^3 - 3x$.</p>
          <p>Đạo hàm tiếp tuyến EKF tại $\bar{x} = 0$:</p>
          $$F = \left. \frac{df}{dx} \right|_{x=0} = 3x^2 - 3 = -3$$
          <p>Ước lượng của EKF:</p>
          $$\hat{y}_{EKF} = f(\bar{x}) = 0$$
          $$\sigma_{y, EKF}^2 = F^2 \cdot \sigma_x^2 = (-3)^2 \cdot 1.0 = 9.0$$
        </div>
      </div>

      <div class="step-card">
        <div class="step-num">BƯỚC 2</div>
        <div class="step-title">Tạo 5 Hạt Mẫu Monte Carlo Đầu Vào</div>
        <div class="step-body">
          <p>Lấy ngẫu nhiên $N=5$ hạt mẫu từ phân bố chuẩn $x^{(i)} \sim \mathcal{N}(0, 1)$:</p>
          <ul>
            <li>$x^{(1)} = -1.20$</li>
            <li>$x^{(2)} = -0.50$</li>
            <li>$x^{(3)} = 0.10$</li>
            <li>$x^{(4)} = 0.80$</li>
            <li>$x^{(5)} = 1.50$</li>
          </ul>
          <p>Trọng số ban đầu đồng đều: $w^{(i)} = \frac{1}{5} = 0.20$.</p>
        </div>
      </div>

      <div class="step-card">
        <div class="step-num">BƯỚC 3</div>
        <div class="step-title">Truyền Hạt Trực Tiếp Qua Hàm Phi Tuyến</div>
        <div class="step-body">
          <p>Tính trực tiếp $y^{(i)} = f(x^{(i)}) = (x^{(i)})^3 - 3x^{(i)}$:</p>
          <ul>
            <li>$y^{(1)} = (-1.2)^3 - 3(-1.2) = -1.728 + 3.600 = +1.872$</li>
            <li>$y^{(2)} = (-0.5)^3 - 3(-0.5) = -0.125 + 1.500 = +1.375$</li>
            <li>$y^{(3)} = (0.1)^3 - 3(0.1) = 0.001 - 0.300 = -0.299$</li>
            <li>$y^{(4)} = (0.8)^3 - 3(0.8) = 0.512 - 2.400 = -1.888$</li>
            <li>$y^{(5)} = (1.5)^3 - 3(1.5) = 3.375 - 4.500 = -1.125$</li>
          </ul>
        </div>
      </div>

      <div class="step-card">
        <div class="step-num">BƯỚC 4</div>
        <div class="step-title">Tổng Hợp Thống Kê & Kết Luận Kỹ Thuật</div>
        <div class="step-body">
          <p>Kỳ vọng mẫu Monte Carlo:</p>
          $$\bar{y}_{MC} = \frac{1}{5} \sum_{i=1}^5 y^{(i)} = \frac{1.872 + 1.375 - 0.299 - 1.888 - 1.125}{5} = -0.013 \approx 0$$
          <p>Phương sai mẫu Monte Carlo:</p>
          $$s_y^2 = \frac{1}{5}\sum (y^{(i)} - \bar{y})^2 \approx 2.46$$
          <p><strong>Bài học kỹ thuật:</strong> EKF dự báo phương sai $9.0$ (thổi phồng sai số lên gấp 3.6 lần thực tế!) do tiếp tuyến bậc 1 quá dốc tại gốc tọa độ. Monte Carlo phản ánh trung thực phân bố hình học thực sự.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Layer 5: Interactive Simulator -->
<section id="sim-ch01" class="content-section">
  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title-group">
        <span class="sim-badge">MÔ PHỎNG TƯƠNG TÁC 60 FPS</span>
        <h3 class="sim-title">Thí Nghiệm So Sánh: Giới Hạn Kalman Đơn Đỉnh vs Đám Mây Hạt Đa Đỉnh</h3>
      </div>
      <p class="sim-desc">
        Robot di chuyển trong hành lang đối xứng có 2 cánh cửa ($x=180\text{m}$ và $x=480\text{m}$). Quan sát cách phân bố chuẩn Gauss của Kalman bị ép vào giữa 2 cánh cửa (sai lầm nghiêm trọng) trong khi Đám mây hạt tự nhiên tách cụm thành 2 đỉnh xác suất chuẩn xác.
      </p>
    </div>

    <!-- Canvas -->
    <div class="sim-canvas-wrapper" style="background: #0f172a; border-radius: 8px; overflow: hidden; margin: 1rem 0;">
      <canvas id="sim-canvas-ch01" style="width: 100%; height: 360px; display: block;"></canvas>
    </div>

    <!-- Controls -->
    <div class="sim-controls-row" style="display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center; justify-content: space-between;">
      <div class="controls-left" style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
        <button id="btn-measure-ch01" class="btn btn-primary">
          <span>📡 Nhận Đo Lường Cửa (Sensor Update)</span>
        </button>
        <button id="btn-move-ch01" class="btn btn-outline">
          <span>🚗 Di Chuyển Robot (+50m)</span>
        </button>
        <button id="btn-reset-ch01" class="btn btn-secondary">
          <span>🔄 Đặt Lại Thí Nghiệm</span>
        </button>
      </div>
      <div class="controls-right" style="font-size: 0.85rem; color: var(--text-muted);">
        <span>💡 Bấm nút đo lường liên tiếp để thấy Kalman thất bại khi gặp môi trường đối xứng.</span>
      </div>
    </div>
  </div>
</section>

<!-- Layer 6: Practical ROS 2 / C++ Architecture Bridge -->
<section id="ros2-bridge-ch01" class="content-section">
  <div class="ros2-bridge-card" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-left: 4px solid var(--accent-emerald); border-radius: 8px; padding: 1.5rem; margin: 2rem 0;">
    <div class="bridge-header" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <span style="font-size: 1.5rem;">🤖</span>
        <h3 style="margin: 0; color: var(--text-main);">Cầu Nối Kiến Trúc Thực Tế: robot_localization (EKF) vs nav2_amcl (Particle Filter)</h3>
      </div>
      <span class="badge" style="background: rgba(16, 185, 129, 0.1); color: var(--accent-emerald); font-weight: 600; padding: 0.25rem 0.6rem; border-radius: 4px;">ROS 2 Humble / Iron / Jazzy</span>
    </div>

    <p style="font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">
      Trong ngăn xếp điều hướng tự hành tiêu chuẩn của ROS 2 (Nav2), hai bộ lọc này không triệt tiêu nhau mà phối hợp theo kiến trúc phân tầng:
    </p>

    <div class="bridge-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
      <div style="background: var(--bg-sidebar); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color);">
        <h4 style="color: var(--primary); margin-top: 0;">1. EKF Tần Số Cao: <code>robot_localization</code></h4>
        <ul style="font-size: 0.88rem; color: var(--text-muted); padding-left: 1.2rem; margin-bottom: 0;">
          <li><strong>Tần số:</strong> 50 Hz - 100 Hz.</li>
          <li><strong>Đầu vào:</strong> IMU raw data + Wheel Odometry.</li>
          <li><strong>Đặc tính:</strong> Tuyến tính hóa nhanh, giữ liên tục khung tọa độ <code>odom -&gt; base_link</code>. Không bị trễ nhịp điều khiển động cơ.</li>
          <li><strong>Hạn chế:</strong> Lũy tích sai số trôi dạt (drift) theo thời gian, không khử được sai số toàn cục.</li>
        </ul>
      </div>

      <div style="background: var(--bg-sidebar); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color);">
        <h4 style="color: var(--accent-emerald); margin-top: 0;">2. Particle Filter Toàn Cục: <code>nav2_amcl</code></h4>
        <ul style="font-size: 0.88rem; color: var(--text-muted); padding-left: 1.2rem; margin-bottom: 0;">
          <li><strong>Tần số:</strong> 5 Hz - 10 Hz (tiết kiệm CPU).</li>
          <li><strong>Đầu vào:</strong> 2D LaserScan / LiDAR + Bản đồ Occupancy Grid tĩnh.</li>
          <li><strong>Đặc tính:</strong> Xuất khung biến đổi <code>map -&gt; odom</code>, khử hoàn toàn sai số trôi dạt, giải quyết sự cố lạc đường (Global Localization).</li>
          <li><strong>Cơ chế thích nghi (KLD-sampling):</strong> Tự động co giãn số hạt từ 500 đến 2000 tùy vào mức độ tin cậy.</li>
        </ul>
      </div>
    </div>

    <div class="code-header" style="display: flex; justify-content: space-between; align-items: center; background: #1e293b; color: #94a3b8; padding: 0.4rem 0.8rem; border-radius: 6px 6px 0 0; font-family: monospace; font-size: 0.85rem;">
      <span>nav2_amcl_params.yaml (Cấu hình chuẩn công nghiệp)</span>
    </div>
    <pre style="margin-top: 0; border-radius: 0 0 6px 6px; background: #0f172a; padding: 1rem; overflow-x: auto;"><code class="language-yaml">amcl:
  ros__parameters:
    use_sim_time: True
    alpha1: 0.2  # Nhiễu góc quay do chuyển động quay
    alpha2: 0.2  # Nhiễu góc quay do chuyển động tịnh tiến
    alpha3: 0.2  # Nhiễu tịnh tiến do chuyển động tịnh tiến
    alpha4: 0.2  # Nhiễu tịnh tiến do chuyển động quay
    min_particles: 500
    max_particles: 2000
    pf_err: 0.05
    pf_z: 0.99
    resample_interval: 1
    update_min_d: 0.2    # Cập nhật khi đi được 20 cm
    update_min_a: 0.2    # Cập nhật khi xoay được 0.2 rad
    laser_model_type: "likelihood_field"
    z_hit: 0.5
    z_short: 0.05
    z_max: 0.05
    z_rand: 0.5</code></pre>
  </div>
</section>
"""

rendered = render_page(ch, CHAPTER_INFO, content_html)
out_path = os.path.join(CHAPTERS_DIR, "ch01.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(rendered)

print(f"Successfully generated {out_path} ({len(rendered)} bytes)")
