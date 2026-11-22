# -*- coding: utf-8 -*-
"""
build_chapters_t5_t6.py
Biên soạn nội dung chuẩn 6 tầng tri thức cho Track 5 và Track 6 (Chương 10 - Chương 14):
- Ch 10: Thuật Toán Tích Phân Số ODEs Cho Động Lực Học
- Ch 11: Hệ Cứng, Tích Phân Symplectic & Phương Pháp Đa Bước
- Ch 12: Giải Hệ Phương Trình DAEs & Động Lực Học Va Chạm
- Ch 13: Phân Tích Ổn Định Lyapunov & Điều Khiển Mô-Men Tính Toán
- Ch 14: Kiến Trúc Thực Tế: URDF, Pinocchio, ros2_control & Gazebo
"""

import os
from build_chapters_t1_t2 import make_chapter_html, BASE_DIR, CHAPTERS_DIR

# ==============================================================================
# CHƯƠNG 10: Thuật Toán Tích Phân Số ODEs Cho Động Lực Học
# ==============================================================================
ch10_sidebar = [
    {"id": "sec-10-1", "title": "10.1 Bài toán Giá trị Ban đầu (IVP)"},
    {"id": "sec-10-2", "title": "10.2 Phương pháp Euler Hiện & Ẩn"},
    {"id": "sec-10-3", "title": "10.3 Phương pháp Runge-Kutta Bậc 4 (RK4)"},
    {"id": "sec-10-4", "title": "10.4 Bảng Butcher & Điều kiện Bậc"},
    {"id": "sec-10-5", "title": "10.5 Thuật toán Thích nghi Bước RK45"},
    {"id": "sec-10-6", "title": "10.6 Sai số Cắt cụt & Miền Ổn định Tuyệt đối"},
    {"id": "sec-10-sim", "title": "⚡ Mô phỏng Euler vs Midpoint vs RK4 (Canvas)"},
    {"id": "sec-10-worked", "title": "📐 Ví dụ Tính Số 4 Bước Tích Phân RK4 Thủ Công"},
    {"id": "sec-10-bridge", "title": "🛠️ Cầu nối Vòng lặp Số Học ROS 2 Controller"}
]

ch10_body = r"""
        <!-- 10.1 -->
        <h2 id="sec-10-1">10.1 Bài Toán Giá Trị Ban Đầu (Initial Value Problem - IVP)</h2>
        <p>Để mô phỏng động tác chuyển động của robot trên máy tính số, hệ phương trình vi phân cấp 2 của robot $M(q)\ddot{q} + C(q,\dot{q})\dot{q} + g(q) = \tau$ được chuyển đổi về hệ phương trình vi phân thường cấp 1 (ODEs) trong không gian trạng thái $x = [q^T, \dot{q}^T]^T \in \mathbb{R}^{2n}$:</p>
        <div class="formula-hero">
          <div class="formula-title">Hệ Phương Trình Vi Phân Thường Cấp 1 Tương Đương</div>
          <div class="formula-math">
            $$\dot{x}(t) = f(t, x(t)), \quad x(t_0) = x_0$$
            $$f(t, x) = \begin{bmatrix} \dot{q} \\ M^{-1}(q) \left( \tau - C(q,\dot{q})\dot{q} - g(q) \right) \end{bmatrix}$$
          </div>
          <div class="formula-legend">
            <strong>Nhiệm vụ của bộ tích phân số:</strong> Tính toán xấp xỉ vector trạng thái rời rạc $x_{n+1} \approx x(t_n + h)$ từ trạng thái hiện tại $x_n$ với bước thời gian $h \gt 0$.
          </div>
        </div>

        <!-- 10.2 -->
        <h2 id="sec-10-2">10.2 Các Phương Pháp Euler: Hiện, Ẩn & Bán Ẩn (Semi-Implicit)</h2>
        <p>1. <strong>Euler Hiện (Forward / Explicit Euler):</strong></p>
        $$x_{n+1} = x_n + h f(t_n, x_n)$$
        <p>Đặc điểm: Cực kỳ đơn giản, nhưng sai số tích lũy lớn $O(h)$ và miền ổn định rất hẹp. Khi bước $h$ lớn, hệ số phân kỳ nổ tung.</p>

        <p>2. <strong>Euler Bán Ẩn (Semi-Implicit / Symplectic Euler):</strong> Thường được dùng trong các game engine và mô phỏng vật lý đồ họa:</p>
        $$v_{n+1} = v_n + h a(q_n, v_n), \quad q_{n+1} = q_n + h v_{n+1}$$

        <!-- 10.3 -->
        <h2 id="sec-10-3">10.3 Phương Pháp Runge-Kutta Cổ Điển Bậc 4 (RK4)</h2>
        <p>Phương pháp Runge-Kutta bậc 4 (RK4) là thuật toán tích phân số phổ biến nhất trong mô phỏng cơ học chính xác nhờ độ chính xác cắt cụt địa phương đạt đến bậc 5 ($O(h^5)$) và toàn cục đạt bậc 4 ($O(h^4)$):</p>
        <div class="formula-hero">
          <div class="formula-title">Thuật Toán Runge-Kutta Bậc 4 Cổ Điển (Classical RK4)</div>
          <div class="formula-math">
            $$\begin{cases}
              k_1 = f(t_n, x_n) \\
              k_2 = f\left(t_n + \frac{h}{2}, x_n + \frac{h}{2} k_1\right) \\
              k_3 = f\left(t_n + \frac{h}{2}, x_n + \frac{h}{2} k_2\right) \\
              k_4 = f(t_n + h, x_n + h k_3) \\
              x_{n+1} = x_n + \frac{h}{6}\left( k_1 + 2k_2 + 2k_3 + k_4 \right)
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Bản chất hình học:</strong> $k_1, k_2, k_3, k_4$ là các vector hệ số góc tại điểm đầu, hai điểm giữa và điểm cuối khoảng tích phân. Nghiệm cập nhật là trung bình có trọng số theo quy tắc hình thang Simpson.
          </div>
        </div>

        <!-- 10.4 -->
        <h2 id="sec-10-4">10.4 Bảng Butcher (Butcher Tableau) & Điều Kiện Bậc</h2>
        <p>Mọi phương pháp Runge-Kutta $s$ tầng (s-stage) đều được biểu diễn thu gọn bằng bảng Butcher:</p>
        $$\begin{array}{c|c} c & A \\ \hline & b^T \end{array} = \begin{array}{c|cccc} c_1 & a_{11} & a_{12} & \dots & a_{1s} \\ c_2 & a_{21} & a_{22} & \dots & a_{2s} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ c_s & a_{s1} & a_{s2} & \dots & a_{ss} \\ \hline & b_1 & b_2 & \dots & b_s \end{array}$$
        <p>Đối với phương pháp hiện, ma trận $A$ là tam giác dưới nghiêm ngặt ($a_{ij} = 0$ khi $j \ge i$). Đối với phương pháp ẩn, ma trận $A$ đầy, đòi hỏi phải giải hệ phương trình phi tuyến tại mỗi bước tích phân.</p>

        <!-- 10.5 -->
        <h2 id="sec-10-5">10.5 Thuật Toán RK45 Thích Nghi Bước Thời Gian (Dormand-Prince)</h2>
        <p>Thuật toán Runge-Kutta-Fehlberg (RK45) hoặc Dormand-Prince tính toán đồng thời nghiệm bậc 4 và bậc 5 từ cùng một tập hợp giá trị hàm để ước lượng sai số cục bộ $\epsilon = \|x^{(5)} - x^{(4)}\|$. Bước thời gian mới được tự động co giãn thích nghi:</p>
        $$h_{new} = h \cdot \left( \frac{\text{Tol}}{\epsilon} \right)^{0.2}$$

        <!-- 10.6 -->
        <h2 id="sec-10-6">10.6 Miền Ổn Định Tuyệt Đối (Absolute Stability Regions)</h2>
        <p>Áp dụng thuật toán tích phân lên phương trình kiểm tra vô hướng $\dot{x} = \lambda x$ ($\lambda \in \mathbb{C}$):</p>
        $$x_{n+1} = R(z) x_n, \quad z = \lambda h \in \mathbb{C}$$
        <p>Miền ổn định tuyệt đối là tập hợp các số phức $z$ sao cho hệ số khuếch đại $|R(z)| \le 1$. Với Euler hiện, miền ổn định là hình tròn tâm $(-1, 0)$ bán kính 1; với RK4, miền ổn định phình to bao trọn một phần lớn nửa mặt phẳng trái.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-10-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">So Sánh Sai Số & Độ Ổn Định: Euler vs Midpoint vs RK4</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-10" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Bước tích phân h: <input type="range" id="sim10-step" min="0.05" max="0.75" step="0.05" value="0.15"> <span id="sim10-h-val">0.15 s</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-10-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tích Phân Thủ Công 1 Bước Bằng Thuật Toán RK4</h3>
          <p>Xét phương trình vi phân mô tả chuyển động của khâu robot có cản nhớt: $\dot{y} = -2y + 4$, với điều kiện ban đầu $y(0) = 1.0$. Tính giá trị nghiệm tại $t = 0.1\text{ s}$ bằng thuật toán RK4 với bước nhảy $h = 0.1\text{ s}$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính hệ số góc $k_1$ tại đầu khoảng</h5>
              <p>Hàm số: $f(t, y) = -2y + 4$.</p>
              <p>Tại $t_0 = 0$, $y_0 = 1.0$:</p>
              <p>$$k_1 = f(0, 1.0) = -2(1.0) + 4 = 2.0$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính các hệ số góc giữa khoảng $k_2$ và $k_3$</h5>
              <p>Điểm giữa 1: $y_A = y_0 + \frac{h}{2} k_1 = 1.0 + 0.05(2.0) = 1.10$.</p>
              <p>$$k_2 = f(0.05, 1.10) = -2(1.10) + 4 = 1.80$$</p>
              <p>Điểm giữa 2: $y_B = y_0 + \frac{h}{2} k_2 = 1.0 + 0.05(1.80) = 1.09$.</p>
              <p>$$k_3 = f(0.05, 1.09) = -2(1.09) + 4 = 1.82$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính hệ số góc cuối khoảng $k_4$</h5>
              <p>Điểm cuối: $y_C = y_0 + h k_3 = 1.0 + 0.1(1.82) = 1.182$.</p>
              <p>$$k_4 = f(0.1, 1.182) = -2(1.182) + 4 = -2.364 + 4 = 1.636$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Cập nhật nghiệm RK4 & So sánh nghiệm giải tích</h5>
              <p>Nghiệm RK4 tại $t = 0.1\text{ s}$:</p>
              <p>$$y(0.1) = 1.0 + \frac{0.1}{6}\left( 2.0 + 2(1.80) + 2(1.82) + 1.636 \right) = 1.0 + \frac{0.1}{6}(10.876) \approx 1.18127$$</p>
              <p>Nghiệm giải tích chính xác: $y_{exact}(t) = 2 - e^{-2t} \implies y(0.1) = 2 - e^{-0.2} = 2 - 0.818731 = 1.181269$.</p>
              <p>Sai số tuyệt đối: $|\epsilon| = |1.18127 - 1.181269| = 1 \times 10^{-6}$ (chính xác đến 6 chữ số thập phân!).</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-10-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Tích Phân Số Trong ROS 2 Simulation Loop</h4>
          <p>Hàm tích phân RK4 cho hệ robot đa khớp trong C++ tối ưu hóa không cấp phát bộ nhớ động:</p>
          <div class="code-card">
            <div class="code-header">
              <span>rk4_integrator.hpp (C++17)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>template &lt;typename SystemDynamics&gt;
void stepRK4(SystemDynamics&amp; sys, Eigen::VectorXd&amp; x, double t, double dt) {
  Eigen::VectorXd k1 = sys(t, x);
  Eigen::VectorXd k2 = sys(t + 0.5 * dt, x + 0.5 * dt * k1);
  Eigen::VectorXd k3 = sys(t + 0.5 * dt, x + 0.5 * dt * k2);
  Eigen::VectorXd k4 = sys(t + dt, x + dt * k3);
  x += (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4);
}</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 11: Hệ Cứng, Tích Phân Symplectic & Phương Pháp Đa Bước
# ==============================================================================
ch11_sidebar = [
    {"id": "sec-11-1", "title": "11.1 Bản chất Hệ Vi phân Cứng (Stiff Systems)"},
    {"id": "sec-11-2", "title": "11.2 Ổn định A-Stability & L-Stability"},
    {"id": "sec-11-3", "title": "11.3 Tích phân Symplectic Verlet / Leapfrog"},
    {"id": "sec-11-4", "title": "11.4 Phương pháp Đa bước Adams"},
    {"id": "sec-11-5", "title": "11.5 Thuật toán Dự đoán - Hiệu chỉnh"},
    {"id": "sec-11-6", "title": "11.6 Phương pháp Vi phân Ngược BDF"},
    {"id": "sec-11-sim", "title": "⚡ Mô phỏng Symplectic Verlet vs RK4 (Canvas)"},
    {"id": "sec-11-worked", "title": "📐 Ví dụ Tính Số 4 Bước BDF-2 Cho Hệ Cứng"},
    {"id": "sec-11-bridge", "title": "🛠️ Cầu nối MuJoCo & Isaac Sim Solver"}
]

ch11_body = r"""
        <!-- 11.1 -->
        <h2 id="sec-11-1">11.1 Bản Chất Của Hệ Vi Phân Cứng (Stiff Systems) Trong Robot Học</h2>
        <p>Hệ phương trình vi phân được gọi là <strong>cứng (stiff)</strong> khi tồn tại đồng thời các thành phần biến thiên với tốc độ cực kỳ khác biệt: một thành phần tắt rất nhanh (tần số cao, hằng số thời gian $\tau_{nhanh} \ll 1$) và một thành phần biến thiên chậm chạp. Tỷ số độ cứng (Stiffness Ratio):</p>
        <div class="formula-hero">
          <div class="formula-title">Định Nghĩa Tỷ Số Độ Cứng Của Hệ Thống</div>
          <div class="formula-math">
            $$\text{Stiffness Ratio} = \frac{\max_i |\text{Re}(\lambda_i)|}{\min_i |\text{Re}(\lambda_i)|} \gg 1 \quad (10^4 \sim 10^7)$$
          </div>
          <div class="formula-legend">
            <strong>Nguồn gốc thực tế:</strong> Khớp nối robot có lò xo giảm chấn độ cứng lớn, cáp truyền động thép không co giãn, hoặc hiện tượng tiếp xúc va chạm chân robot với mặt sàn cứng.
          </div>
        </div>

        <!-- 11.2 -->
        <h2 id="sec-11-2">11.2 Khái Niệm Ổn Định A-Stability & L-Stability</h2>
        <p>Để giải hệ cứng mà không bị ép phải chọn bước tích phân $h$ siêu nhỏ (dẫn đến mô phỏng chạy chậm hàng nghìn lần), phương pháp tích phân số phải có miền ổn định bao phủ toàn bộ nửa mặt phẳng trái:</p>
        <div class="why-matters-box">
          <div class="why-matters-header">💡 ĐỊNH NGHĨA A-STABILITY VÀ L-STABILITY</div>
          <div class="why-matters-body">
            • <strong>A-Stability:</strong> Phương pháp có miền ổn định chứa trọn nửa mặt phẳng phức bên trái: $\{z \in \mathbb{C} \mid \text{Re}(z) \le 0\} \subseteq S$. Các phương pháp Euler ẩn, Quy tắc Hình thang (Trapezoidal Rule) là A-stable.
            <br>• <strong>L-Stability:</strong> Phương pháp vừa A-stable vừa thỏa mãn điều kiện triệt tiêu vô cùng: $\lim_{\text{Re}(z) \to -\infty} R(z) = 0$. Thuộc tính này dập tắt tức thời các dao động tần số cao giả tạo không mong muốn.
          </div>
        </div>

        <!-- 11.3 -->
        <h2 id="sec-11-3">11.3 Tích Phân Symplectic Runge-Kutta & Thuật Toán Verlet / Leapfrog</h2>
        <p>Trong các mô phỏng dài hạn (hàng nghìn chu kỳ dao động), các phương pháp cổ điển như RK4 hay Euler liên tục làm hao hụt hoặc khuếch đại năng lượng cơ học (trôi năng lượng). <strong>Tích phân Symplectic</strong> bảo toàn dạng vi phân symplectic $dp \wedge dq$ trong không gian pha, bảo đảm năng lượng dao động dao động quanh một giá trị không đổi vĩnh viễn:</p>
        <div class="formula-hero">
          <div class="formula-title">Thuật Toán Velocity Verlet (Symplectic Integrator)</div>
          <div class="formula-math">
            $$\begin{cases}
              q_{n+1} = q_n + v_n h + \frac{1}{2} a_n h^2 \\
              a_{n+1} = M^{-1}(q_{n+1}) \left( \tau_{n+1} - C(q_{n+1}, v_n) v_n - g(q_{n+1}) \right) \\
              v_{n+1} = v_n + \frac{1}{2}\left( a_n + a_{n+1} \right) h
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Ưu điểm cốt tử:</strong> Bảo toàn năng lượng tuyệt đối, không có sai số tiêu tán nhân tạo, chi phí tính toán chỉ bằng một nửa RK4!
          </div>
        </div>

        <!-- 11.4 -->
        <h2 id="sec-11-4">11.4 Phương Pháp Đa Bước Tuyến Tính (Linear Multistep Methods)</h2>
        <p>Thay vì tính nhiều tầng trung gian như Runge-Kutta, phương pháp đa bước tận dụng lại kết quả của các bước trước đó ($x_n, x_{n-1}, x_{n-2}, \dots$):</p>
        $$\sum_{j=0}^k \alpha_j x_{n+j} = h \sum_{j=0}^k \beta_j f_{n+j}$$
        <p>• <strong>Adams-Bashforth:</strong> Phương pháp đa bước tường minh ($\beta_k = 0$).</p>
        <p>• <strong>Adams-Moulton:</strong> Phương pháp đa bước ẩn ($\beta_k \ne 0$).</p>

        <!-- 11.5 -->
        <h2 id="sec-11-5">11.5 Kỹ Thuật Dự Đoán - Hiệu Chỉnh (Predictor-Corrector)</h2>
        <p>Thuật toán PECE (Predict - Evaluate - Correct - Evaluate) kết hợp Adams-Bashforth bậc $k$ làm bộ dự đoán (Predictor) để ước lượng $x_{n+1}^{(0)}$, sau đó dùng Adams-Moulton bậc $k$ làm bộ hiệu chỉnh (Corrector) để tinh chỉnh độ chính xác mà không cần giải lặp Newton.</p>

        <!-- 11.6 -->
        <h2 id="sec-11-6">11.6 Phương Pháp Vi Phân Ngược BDF (Backward Differentiation Formula)</h2>
        <p>Phương pháp BDF là vũ khí tối thượng giải hệ vi phân cứng và DAEs. Công thức BDF bậc 2 (BDF-2):</p>
        $$x_{n+1} - \frac{4}{3} x_n + \frac{1}{3} x_{n-1} = \frac{2}{3} h f(t_{n+1}, x_{n+1})$$

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-11-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Kiểm Chứng Bảo Toàn Năng Lượng: Symplectic Verlet vs RK4</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-11" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <span style="font-size: 0.85rem; color: #10b981; font-weight: 600;">● Con lắc bên trái: Symplectic Verlet (Bảo toàn năng lượng vĩnh viễn)</span>
            <span style="font-size: 0.85rem; color: #38bdf8; font-weight: 600;">● Con lắc bên phải: RK4 Cổ điển (Dần trôi năng lượng sau chu kỳ dài)</span>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-11-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Ứng Dụng Thuật Toán BDF-2 Giải Hệ Vi Phân Cứng</h3>
          <p>Xét phương trình vi phân mô tả khớp robot có giảm chấn cứng: $\dot{y} = -50 y$, với bước thời gian $h = 0.1\text{ s}$. Giả sử hai điểm nghiệm ban đầu là $y_0 = 1.0$ và $y_1 = e^{-50(0.1)} = e^{-5} \approx 0.006738$. Tính bước tiếp theo $y_2$ bằng BDF-2.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Thiết lập phương trình sai phân BDF-2</h5>
              <p>Công thức tổng quát BDF bậc 2:</p>
              <p>$$y_2 - \frac{4}{3} y_1 + \frac{1}{3} y_0 = \frac{2}{3} h f(t_2, y_2)$$</p>
              <p>Thay hàm số $f(t_2, y_2) = -50 y_2$ vào vế phải:</p>
              <p>$$y_2 - \frac{4}{3} y_1 + \frac{1}{3} y_0 = \frac{2}{3} (0.1) (-50 y_2) = -\frac{10}{3} y_2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Gom các số hạng chứa ẩn $y_2$ về vế trái</h5>
              <p>$$y_2 + \frac{10}{3} y_2 = \frac{4}{3} y_1 - \frac{1}{3} y_0$$</p>
              <p>$$\frac{13}{3} y_2 = \frac{4}{3} y_1 - \frac{1}{3} y_0 \iff 13 y_2 = 4 y_1 - y_0$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Thay số và giải nghiệm đại số</h5>
              <p>$$13 y_2 = 4(0.006738) - 1.0 = 0.026952 - 1.0 = -0.973048$$</p>
              <p>$$y_2 = \frac{-0.973048}{13} \approx -0.07485$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: So sánh tính ổn định với Euler hiện</h5>
              <p>Nếu dùng Euler hiện với $h=0.1$: $y_{n+1} = (1 - 50 \times 0.1) y_n = -4 y_n$. Nghiệm sẽ nổ tung phân kỳ: $y_1 = -4, y_2 = +16, y_3 = -64$!</p>
              <p>Kết luận: Dù $h=0.1$ rất lớn so với hằng số thời gian $\tau = 0.02\text{ s}$, BDF-2 vẫn giữ nghiệm bị chặn và triệt tiêu ổn định về 0.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-11-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Cấu Hình Physics Solver Trong MuJoCo & Gazebo</h4>
          <p>Các engine vật lý đa vật hiện đại sử dụng các bộ tích phân Symplectic (Semi-implicit Euler / Verlet) để đạt tính ổn định vô hạn:</p>
          <div class="code-card">
            <div class="code-header">
              <span>mujoco_config.xml (MuJoCo Physics)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>&lt;mujoco model="robot_arm"&gt;
  &lt;option timestep="0.001" integrator="implicitfast"&gt;
    &lt;flag warmstart="enable" contact="enable"/&gt;
  &lt;/option&gt;
&lt;/mujoco&gt;</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 12: Giải Hệ Phương Trình DAEs & Động Lực Học Va Chạm
# ==============================================================================
ch12_sidebar = [
    {"id": "sec-12-1", "title": "12.1 Hệ Phương trình Vi phân Đại số DAEs"},
    {"id": "sec-12-2", "title": "12.2 Kỹ thuật Giảm Chỉ số & Baumgarte"},
    {"id": "sec-12-3", "title": "12.3 Điều kiện Ban đầu Tương thích"},
    {"id": "sec-12-4", "title": "12.4 Khử Gauss & Phân rã Ma trận LU"},
    {"id": "sec-12-5", "title": "12.5 Bài toán Tiếp xúc LCP trong Physics Engine"},
    {"id": "sec-12-sim", "title": "⚡ Mô phỏng Ổn Định Hóa Baumgarte (Canvas)"},
    {"id": "sec-12-worked", "title": "📐 Ví dụ Tính Số 4 Bước Phân Rã LU Ma Trận Khối Lượng"},
    {"id": "sec-12-bridge", "title": "🛠️ Cầu nối Bullet / ODE Constraint Solver"}
]

ch12_body = r"""
        <!-- 12.1 -->
        <h2 id="sec-12-1">12.1 Hệ Phương Trình Vi Phân Đại Số (DAEs) & Chỉ Số Vi Phân (Differential Index)</h2>
        <p>Hệ DAEs là hệ phương trình kết hợp giữa các phương trình vi phân động lực học và các phương trình đại số biểu thị ràng buộc cơ học:</p>
        <div class="formula-hero">
          <div class="formula-title">Hệ Phương Trình DAEs Bậc 2 Cơ Học</div>
          <div class="formula-math">
            $$\begin{cases}
              M(q)\ddot{q} + C(q,\dot{q})\dot{q} + g(q) + G^T(q)\lambda = \tau \\
              \phi(q) = 0 \quad (\text{Ràng buộc vị trí hình học})
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Chỉ số vi phân (Differential Index):</strong> Là số lần tối thiểu phải lấy đạo hàm theo thời gian phương trình ràng buộc đại số $\phi(q) = 0$ để đưa hệ thống về dạng hệ phương trình vi phân thường (ODEs) thuần túy. Hệ cơ học trên là <strong>DAE Index-3</strong>!
          </div>
        </div>

        <!-- 12.2 -->
        <h2 id="sec-12-2">12.2 Kỹ Thuật Giảm Chỉ Số & Ổn Định Hóa Baumgarte Stabilization</h2>
        <p>Khi đạo hàm ràng buộc $\phi(q)=0$ hai lần theo thời gian để thu được phương trình gia tốc: $\ddot{\phi} = G(q)\ddot{q} + \dot{G}(q)\dot{q} = 0$, việc tích phân số trực tiếp sẽ khiến sai số cắt cụt tích lũy làm trôi dạt ràng buộc vị trí $(\phi(q) \ne 0)$. Baumgarte đề xuất thay phương trình $\ddot{\phi} = 0$ bằng phương trình vi phân ổn định bậc 2:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Ổn Định Hóa Baumgarte (Baumgarte Stabilization)</div>
          <div class="formula-math">
            $$\ddot{\phi} + 2\alpha \dot{\phi} + \beta^2 \phi = 0$$
          </div>
          <div class="formula-legend">
            <strong>Bản chất vật lý:</strong> $\alpha, \beta \gt 0$ là các hệ số hồi tiếp tỷ lệ và vi phân ảo. Bất kỳ sai số vi phạm ràng buộc vị trí $\phi$ hay vận tốc $\dot{\phi}$ đều tự động bị dập tắt tiệm cận về 0 như một hệ dao động tắt dần!
          </div>
        </div>

        <!-- 12.3 -->
        <h2 id="sec-12-3">12.3 Tính Toán Điều Kiện Ban Đầu Tương Thích (Consistent Initial Conditions)</h2>
        <p>Đối với hệ DAEs, người dùng không thể tùy tiện chọn điều kiện ban đầu $(q_0, \dot{q}_0)$. Điều kiện ban đầu bắt buộc phải thỏa mãn đồng thời 2 đẳng thức ràng buộc:</p>
        $$\phi(q_0) = 0, \quad G(q_0)\dot{q}_0 = 0$$
        <p>Nếu không, bộ giải số sẽ nổ tung ngay tại bước tích phân đầu tiên $t = 0$.</p>

        <!-- 12.4 -->
        <h2 id="sec-12-4">12.4 Giải Đại Số Tuyến Tính Bằng Khử Gauss & Phân Rã LU Có Chọn Trục (Pivoting)</h2>
        <p>Tại mỗi chu kỳ điều khiển robot, ta phải giải hệ phương trình tuyến tính tìm gia tốc góc $\ddot{q}$ từ: $M(q)\ddot{q} = b$, với $b = \tau - C\dot{q} - g$. Thay vì tính ma trận nghịch đảo $M^{-1}$ tốn kém và kém ổn định số học, phương pháp chuẩn là <strong>phân rã LU có chọn trục từng phần (PA = LU)</strong>:</p>
        $$P M = L U \implies L y = P b \implies U \ddot{q} = y$$

        <!-- 12.5 -->
        <h2 id="sec-12-5">12.5 Bài Toán Bù Tuyến Tính LCP (Linear Complementarity Problem) Trong Va Chạm Tiếp Xúc</h2>
        <p>Khi robot tiếp xúc với môi trường, lực pháp tuyến không thể hút mặt sàn ($f_N \ge 0$) và khoảng cách khe hở không thể xuyên thủng ($\delta \ge 0$). Hiện tượng này tạo thành bài toán bù tuyến tính LCP:</p>
        $$w = M_c z + q_c, \quad w \ge 0, \; z \ge 0, \; w^T z = 0$$
        <p>Đây là hạt nhân tính toán xử lý tiếp xúc va chạm thời gian thực trong các physics engine hàng đầu như ODE, Bullet và MuJoCo.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-12-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Trôi Ràng Buộc DAEs & Ổn Định Hóa Baumgarte</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-12" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">
              <input type="checkbox" id="sim12-baumgarte" checked> Kích hoạt Ổn Định Hóa Baumgarte (alpha = beta = 5.0)
            </label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-12-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Phân Rã LU Có Chọn Trục Giải Gia Tốc Khớp Robot</h3>
          <p>Cần giải gia tốc khớp $\ddot{q}$ từ phương trình ma trận khối lượng $M \ddot{q} = b$, với $M = \begin{bmatrix} 2 & 4 \\ 4 & 20 \end{bmatrix}$ và vector lực hiệu dụng $b = \begin{bmatrix} 8 \\ 28 \end{bmatrix}$. Thực hiện phân rã LU có hoán đổi hàng (Partial Pivoting).</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Hoán đổi hàng (Pivoting) & Ma trận hoán vị $P$</h5>
              <p>Xét cột 1: phần tử hàng 2 ($|4|$) lớn hơn hàng 1 ($|2|$), đổi chỗ hàng 1 và hàng 2:</p>
              <p>$$P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \implies P M = \begin{bmatrix} 4 & 20 \\ 2 & 4 \end{bmatrix}, \quad P b = \begin{bmatrix} 28 \\ 8 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Phân rã ma trận tam giác dưới $L$ và trên $U$</h5>
              <p>Hệ số khử hàng 2: $l_{21} = \frac{2}{4} = 0.5$.</p>
              <p>Hàng 2 mới của $U$: $4 - (0.5)(20) = 4 - 10 = -6$.</p>
              <p>$$L = \begin{bmatrix} 1 & 0 \\ 0.5 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 4 & 20 \\ 0 & -6 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Giải thế tiến $L y = P b$</h5>
              <p>$$\begin{bmatrix} 1 & 0 \\ 0.5 & 1 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 28 \\ 8 \end{bmatrix}$$</p>
              <p>$$y_1 = 28$$</p>
              <p>$$0.5 y_1 + y_2 = 8 \implies y_2 = 8 - 0.5(28) = 8 - 14 = -6$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Giải thế lùi $U \ddot{q} = y$ & Nghiệm gia tốc</h5>
              <p>$$\begin{bmatrix} 4 & 20 \\ 0 & -6 \end{bmatrix} \begin{bmatrix} \ddot{q}_1 \\ \ddot{q}_2 \end{bmatrix} = \begin{bmatrix} 28 \\ -6 \end{bmatrix}$$</p>
              <p>$$-6 \ddot{q}_2 = -6 \implies \ddot{q}_2 = 1.0\text{ rad/s}^2$$</p>
              <p>$$4 \ddot{q}_1 + 20(1.0) = 28 \implies 4 \ddot{q}_1 = 8 \implies \ddot{q}_1 = 2.0\text{ rad/s}^2$$</p>
              <p>Kiểm tra: $M \ddot{q} = \begin{bmatrix} 2 & 4 \\ 4 & 20 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 + 4 \\ 8 + 20 \end{bmatrix} = \begin{bmatrix} 8 \\ 28 \end{bmatrix} = b$. Nghiệm chính xác tuyệt đối!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-12-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Giải Hệ Tuyến Tính Bằng Eigen3 Trong ROS 2</h4>
          <p>Sử dụng phân rã Cholesky $LL^T$ hoặc $LDLT$ tối ưu cho ma trận đối xứng xác định dương $M(q)$ của robot:</p>
          <div class="code-card">
            <div class="code-header">
              <span>solve_acceleration.cpp (Eigen3 / C++)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>#include &lt;Eigen/Dense&gt;

Eigen::VectorXd computeJointAccelerations(const Eigen::MatrixXd&amp; M, const Eigen::VectorXd&amp; tau_net) {
  // Phân rã LDLT siêu tốc độ và ổn định số học tối đa
  return M.ldlt().solve(tau_net);
}</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 13: Phân Tích Ổn Định Lyapunov & Điều Khiển Mô-Men Tính Toán
# ==============================================================================
ch13_sidebar = [
    {"id": "sec-13-1", "title": "13.1 Điểm Cân Bằng & Định Nghĩa Ổn Định"},
    {"id": "sec-13-2", "title": "13.2 Phương Pháp Gián Tiếp Lyapunov"},
    {"id": "sec-13-3", "title": "13.3 Phương Pháp Trực Tiếp & Hàm Ứng Viên"},
    {"id": "sec-13-4", "title": "13.4 Định Lý Lagrange & Nguyên Lý LaSalle"},
    {"id": "sec-13-5", "title": "13.5 Bộ Điều Khiển PD + Bù Trọng Lực"},
    {"id": "sec-13-6", "title": "13.6 Điều Khiển Mô-Men Tính Toán (CTC)"},
    {"id": "sec-13-sim", "title": "⚡ Mô phỏng Điều Khiển Mô-Men CTC (Canvas)"},
    {"id": "sec-13-worked", "title": "📐 Ví dụ Tính Số 4 Bước Chứng Minh Ổn Định Lyapunov"},
    {"id": "sec-13-bridge", "title": "🛠️ Cầu nối ros2_control Effort Controller Plugin"}
]

ch13_body = r"""
        <!-- 13.1 -->
        <h2 id="sec-13-1">13.1 Điểm Cân Bằng & Định Nghĩa Tính Ổn Định Lyapunov</h2>
        <p>Hệ phi tuyến tự trị $\dot{x} = f(x)$ có điểm cân bằng $x^* = 0$. Điểm cân bằng được gọi là:</p>
        <p>• <strong>Ổn định (Stable theo Lyapunov):</strong> Nếu với mọi $\epsilon \gt 0$, tồn tại $\delta \gt 0$ sao cho nếu $\|x(0)\| \lt \delta$ thì $\|x(t)\| \lt \epsilon, \forall t \ge 0$.</p>
        <p>• <strong>Ổn định tiệm cận (Asymptotically Stable):</strong> Nếu ổn định và $\lim_{t \to \infty} x(t) = 0$.</p>
        <p>• <strong>Ổn định mũ (Exponentially Stable):</strong> Nếu $\|x(t)\| \le k \|x(0)\| e^{-\lambda t}$ với $k, \lambda \gt 0$.</p>

        <!-- 13.2 -->
        <h2 id="sec-13-2">13.2 Phương Pháp Trực Tiếp Lyapunov (Direct Method)</h2>
        <p>Định lý trực tiếp Lyapunov cho phép đánh giá tính ổn định mà không cần giải phương trình vi phân:</p>
        <div class="formula-hero">
          <div class="formula-title">Định Lý Trực Tiếp Lyapunov Cho Hệ Phi Tuyến</div>
          <div class="formula-math">
            $$\begin{cases}
              V(x) \gt 0, \quad \forall x \ne 0 \quad (\text{Hàm xác định dương, } V(0)=0) \\
              \dot{V}(x) = \nabla V^T(x) f(x) \le 0 \quad (\text{Đạo hàm dọc quỹ đạo xác định âm hoặc nửa âm})
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Ý nghĩa vật lý:</strong> $V(x)$ đóng vai trò như tổng năng lượng tổng quát. Nếu năng lượng luôn suy hao theo thời gian ($\dot{V} \le 0$), hệ thống tất yếu sẽ hội tụ về điểm cực tiểu năng lượng.
          </div>
        </div>

        <!-- 13.3 -->
        <h2 id="sec-13-3">13.3 Định Lý Ổn Định Lagrange & Nguyên Lý Bất Biến LaSalle</h2>
        <p>Khi đạo hàm Lyapunov chỉ nửa xác định âm ($\dot{V}(x) \le 0$, có thể triệt tiêu tại các điểm $x \ne 0$), Định lý bất biến LaSalle khẳng định rằng quỹ đạo trạng thái sẽ hội tụ về <strong>tập bất biến lớn nhất</strong> chứa bên trong tập hợp $\{x \mid \dot{V}(x) = 0\}$.</p>

        <!-- 13.4 -->
        <h2 id="sec-13-4">13.4 Bộ Điều Khiển PD Có Bù Trọng Lực (PD with Gravity Compensation)</h2>
        <p>Để điều khiển robot bám điểm đặt vị trí mong muốn $q_d$ (Regulation Problem), luật điều khiển PD kết hợp bù trọng lực feedforward:</p>
        <div class="formula-hero">
          <div class="formula-title">Luật Điều Khiển PD Bù Trọng Lực</div>
          <div class="formula-math">
            $$\tau = K_p (q_d - q) - K_d \dot{q} + g(q)$$
          </div>
          <div class="formula-legend">
            <strong>Chứng minh ổn định tiệm cận toàn cục bằng hàm Lyapunov:</strong>
            $$V(e, \dot{q}) = \frac{1}{2} \dot{q}^T M(q) \dot{q} + \frac{1}{2} e^T K_p e \gt 0$$
            $$\dot{V} = \dot{q}^T M \ddot{q} + \frac{1}{2}\dot{q}^T \dot{M}\dot{q} - e^T K_p \dot{q} = \dot{q}^T (\tau - C\dot{q} - g) + \frac{1}{2}\dot{q}^T \dot{M}\dot{q} - e^T K_p \dot{q}$$
            Áp dụng luật điều khiển $\tau$ và đẳng thức $\dot{q}^T (\dot{M} - 2C)\dot{q} \equiv 0$:
            $$\dot{V} = -\dot{q}^T K_d \dot{q} \le 0$$
            Theo LaSalle, $\dot{V} = 0 \implies \dot{q} = 0 \implies \ddot{q} = 0 \implies K_p e = 0 \implies e = 0$. Robot hội tụ chính xác 100% về vị trí đặt!
          </div>
        </div>

        <!-- 13.5 -->
        <h2 id="sec-13-5">13.5 Kỹ Thuật Điều Khiển Mô-Men Tính Toán (Computed Torque Control - CTC)</h2>
        <p>Cho bài toán bám quỹ đạo động học $q_d(t)$, kỹ thuật CTC (tuyến tính hóa phản hồi - Feedback Linearization) triệt tiêu toàn bộ các thành phần phi tuyến của robot:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Điều Khiển Mô-Men Tính Toán (CTC)</div>
          <div class="formula-math">
            $$\tau = M(q)\left( \ddot{q}_d + K_d \dot{e} + K_p e \right) + C(q,\dot{q})\dot{q} + g(q)$$
          </div>
          <div class="formula-legend">
            <strong>Động lực học sai số tuyến tính khép vòng:</strong>
            $$\ddot{e} + K_d \dot{e} + K_p e = 0$$
            Hệ phi tuyến hoàn toàn biến thành hệ tuyến tính bậc 2 độc lập cho từng khớp, cho phép triệt tiêu sai số bám với tốc độ mong muốn tùy chọn qua $K_p, K_d$.
          </div>
        </div>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-13-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Bám Quỹ Đạo CTC Khi Có Nhiễu Tải Trọng Bất Định</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-13" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Tải trọng đột ngột đầu gắp (Payload): <input type="range" id="sim13-dist" min="0" max="5.0" step="0.5" value="1.5"> <span id="sim13-d-val">1.5 kg</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-13-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Thiết Kế Ma Trận Khuếch Đại $K_p, K_d$ Cho Bộ Điều Khiển CTC</h3>
          <p>Yêu cầu thiết kế bộ điều khiển CTC cho khớp robot sao cho sai số bám quỹ đạo có hệ số tắt dần tới hạn $\zeta = 1.0$ (không vọt lố) và thời gian xác lập $t_s \approx 0.2\text{ s}$ (tiêu chuẩn 2%).</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Xác định tần số dao động tự nhiên mong muốn $\omega_n$</h5>
              <p>Với hệ bậc 2 tắt dần tới hạn ($\zeta = 1.0$), thời gian xác lập tiêu chuẩn 2%:</p>
              <p>$$t_s \approx \frac{4}{\zeta \omega_n} \implies \omega_n = \frac{4}{\zeta t_s} = \frac{4}{1.0 \times 0.2} = 20.0\text{ rad/s}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính toán ma trận hệ số khuếch đại $K_p$ và $K_d$</h5>
              <p>Phương trình đặc trưng mong muốn: $s^2 + 2\zeta\omega_n s + \omega_n^2 = 0$.</p>
              <p>Hệ số khuếch đại vị trí:</p>
              <p>$$K_p = \omega_n^2 = 20.0^2 = 400.0$$</p>
              <p>Hệ số khuếch đại vận tốc:</p>
              <p>$$K_d = 2 \zeta \omega_n = 2 \times 1.0 \times 20.0 = 40.0$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Thiết lập luật điều khiển mô-men cho khớp 1</h5>
              <p>Cho $q = 0.5\text{ rad}$, $\dot{q} = 0.2\text{ rad/s}$, mục tiêu: $q_d = 0.8\text{ rad}$, $\dot{q}_d = 0$, $\ddot{q}_d = 0$.</p>
              <p>Sai số: $e = 0.8 - 0.5 = 0.3\text{ rad}$, $\dot{e} = 0 - 0.2 = -0.2\text{ rad/s}$.</p>
              <p>Gia tốc tổng hợp ảo:</p>
              <p>$$a = \ddot{q}_d + K_d \dot{e} + K_p e = 0 + 40(-0.2) + 400(0.3) = -8 + 120 = 112.0\text{ rad/s}^2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Tính mô-men đầu ra động cơ $\tau$</h5>
              <p>Cho quán tính $M = 0.5\text{ kg}\cdot\text{m}^2$, số hạng Coriolis $C\dot{q} = 0.1\text{ N}\cdot\text{m}$, trọng lực $g(q) = 3.5\text{ N}\cdot\text{m}$:</p>
              <p>$$\tau = M \cdot a + C\dot{q} + g(q) = 0.5(112.0) + 0.1 + 3.5 = 56.0 + 3.6 = 59.6\text{ N}\cdot\text{m}$$</p>
              <p>Đánh giá: Mô-men $59.6\text{ N}\cdot\text{m}$ bảo đảm đưa khớp về vị trí mong muốn trong vòng $0.2\text{ s}$ mà hoàn toàn không xảy ra vọt lố.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-13-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Computed Torque Controller Plugin Trong ros2_control</h4>
          <p>Triển khai thuật toán CTC trong controller kế thừa từ `controller_interface::ControllerInterface`:</p>
          <div class="code-card">
            <div class="code-header">
              <span>computed_torque_controller.cpp (ROS 2 Humble / C++)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>controller_interface::return_type update(const rclcpp::Time &amp; time, const rclcpp::Duration &amp; period) {
  // 1. Đọc trạng thái vị trí và vận tốc từ command interfaces
  for (size_t i = 0; i &lt; num_joints_; ++i) {
    q_(i) = state_interfaces_[2*i].get_value();
    dq_(i) = state_interfaces_[2*i + 1].get_value();
  }
  
  // 2. Tính toán ma trận M, C, g bằng thư viện Pinocchio
  pinocchio::crba(model_, data_, q_);
  pinocchio::nonLinearEffects(model_, data_, q_, dq_);
  
  // 3. Tính toán gia tốc ảo a = ddq_d + Kd*de + Kp*e
  Eigen::VectorXd a = ddq_d_ + Kd_ * (dq_d_ - dq_) + Kp_ * (q_d_ - q_);
  
  // 4. Nhân với ma trận khối lượng và bù trọng lực
  Eigen::VectorXd tau = data_.M * a + data_.nle;
  
  // 5. Gửi lệnh mô-men xuống phần cứng
  for (size_t i = 0; i &lt; num_joints_; ++i) {
    command_interfaces_[i].set_value(tau(i));
  }
  return controller_interface::return_type::OK;
}</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 14: Kiến Trúc Thực Tế: URDF, Pinocchio, ros2_control & Gazebo
# ==============================================================================
ch14_sidebar = [
    {"id": "sec-14-1", "title": "14.1 Từ URDF/XACRO sang Ma trận Động lực học"},
    {"id": "sec-14-2", "title": "14.2 Thư viện Pinocchio & C++ AVX2"},
    {"id": "sec-14-3", "title": "14.3 Kiến trúc Vòng lặp 1000 Hz trong ros2_control"},
    {"id": "sec-14-4", "title": "14.4 Cầu nối Gazebo Sim & Isaac Sim"},
    {"id": "sec-14-5", "title": "14.5 Hardware-in-the-Loop & Giám sát Jitter"},
    {"id": "sec-14-sim", "title": "⚡ Mô phỏng Real-Time Jitter 1000 Hz (Canvas)"},
    {"id": "sec-14-worked", "title": "📐 Ví dụ Tính Số 4 Bước Ngân Sách Thời Gian Thực"},
    {"id": "sec-14-bridge", "title": "🛠️ Cầu nối ros2_control.xacro Hoàn Chỉnh"}
]

ch14_body = r"""
        <!-- 14.1 -->
        <h2 id="sec-14-1">14.1 Từ Mô Hình Hình Học URDF/XACRO Sang Các Ma Trận Động Lực Học</h2>
        <p>File URDF (Unified Robot Description Format) chứa toàn bộ các thuộc tính quán tính vật lý thực nghiệm của từng khâu thông qua thẻ `<inertial>`:</p>
        <div class="formula-hero">
          <div class="formula-title">Cấu Trúc Thẻ Quán Tính URDF</div>
          <div class="formula-math">
            $$\text{Thẻ URDF: } \begin{cases}
              \text{Khối lượng } m: & \texttt{&lt;mass value="1.5"/&gt;} \\
              \text{Khối tâm } r_C: & \texttt{&lt;origin xyz="0.1 0.0 0.05" rpy="0 0 0"/&gt;} \\
              \text{Tensor quán tính } I_C: & \texttt{&lt;inertia ixx="..." ixy="..." ixz="..." iyy="..." iyz="..." izz="..."/&gt;}
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Nguyên lý nạp mô hình:</strong> Bộ parser của hệ thống đọc cấu trúc cây động học từ file XML/XACRO, tự động xây dựng các ma trận biến đổi tọa độ $SE(3)$ và tính toán ma trận khối lượng $M(q)$ bằng thuật toán Composite Rigid Body Algorithm (CRBA).
          </div>
        </div>

        <!-- 14.2 -->
        <h2 id="sec-14-2">14.2 Thư Viện Động Lực Học Không Gian Siêu Tốc Độ Pinocchio</h2>
        <p>Pinocchio là thư viện mã nguồn mở viết bằng C++ hiện đại, sử dụng đại số Lie không gian $SE(3)$ kết hợp tối ưu hóa SIMD AVX-512. Thời gian tính toán cho tay máy 6-DOF:</p>
        <p>• Động học thuận và Jacobian: $\approx 1.2\ \mu\text{s}$</p>
        <p>• Động lực học ngược RNEA: $\approx 2.5\ \mu\text{s}$</p>
        <p>• Ma trận khối lượng CRBA: $\approx 4.0\ \mu\text{s}$</p>
        <p>• Động lực học thuận ABA: $\approx 5.5\ \mu\text{s}$</p>

        <!-- 14.3 -->
        <h2 id="sec-14-3">14.3 Kiến Trúc Vòng Lặp Điều Khiển Thời Gian Thực 1000 Hz Trong `ros2_control`</h2>
        <p>Để bảo đảm tính ổn định khi điều khiển mô-men, vòng lặp điều khiển bắt buộc phải chạy ở tần số cố định **1000 Hz** (chu kỳ $T = 1.0\text{ ms}$) trên nhân hệ điều hành Linux Real-Time (PREEMPT_RT). Cấu trúc gồm 3 tầng:</p>
        <p>1. <strong>Hardware Component:</strong> Đọc giá trị encoder, dòng điện qua bus truyền thông công nghiệp thời gian thực (EtherCAT / CANopen).</p>
        <p>2. <strong>Resource Manager:</strong> Quản lý bản quyền tài nguyên phần cứng, ngăn ngừa tranh chấp lệnh.</p>
        <p>3. <strong>Controller Manager:</strong> Thực thi hàm `update(time, period)` của các controller theo thứ tự ưu tiên thời gian thực.</p>

        <!-- 14.4 -->
        <h2 id="sec-14-4">14.4 Cầu Nối Đồng Bộ Hóa Gazebo Sim & NVIDIA Isaac Sim</h2>
        <p>Package `gz_ros2_control` cung cấp plugin phần cứng ảo kết nối mô hình vật lý đa vật trong Gazebo Harmonic/Jazzy với vòng lặp `ros2_control`, cho phép dùng <strong>chung 100% mã nguồn điều khiển</strong> giữa robot mô phỏng và robot thật ngoài đời (Sim-to-Real).</p>

        <!-- 14.5 -->
        <h2 id="sec-14-5">14.5 Hardware-in-the-Loop (HIL) & Giám Sát Độ Trễ Jitter Thời Gian Thực</h2>
        <p>Jitter là độ sai lệch ngẫu nhiên của chu kỳ thực tế so với chu kỳ lý thuyết ($|T_{real} - 1.0\text{ ms}|$). Trên hệ điều hành không thời gian thực (Non-RT), jitter có thể vọt lên $5 \sim 15\text{ ms}$, gây sốc dòng phá hủy động cơ robot!</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-14-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Giám Sát Vòng Lặp Thời Gian Thực ROS 2 Control (1000 Hz)</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-14" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <span style="font-size: 0.85rem; color: #10b981; font-weight: 600;">● Đường xanh lá: Chu kỳ chuẩn 1000 μs (1 ms)</span>
            <span style="font-size: 0.85rem; color: #38bdf8; font-weight: 600;">● Dạng sóng xanh dương: Đo đạc dao động trễ thời gian thực tế (Jitter)</span>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-14-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Toán Ngân Sách Thời Gian Thực (Time Budget) Vòng Lặp 1000 Hz</h3>
          <p>Thiết kế hệ thống điều khiển lực cho robot 6 bậc tự do chạy ở tần số 1000 Hz trên vi xử lý công nghiệp. Ngân sách chu kỳ tối đa $T_{max} = 1000\ \mu\text{s}$. Khảo sát các thành phần thời gian thực thi.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính thời gian truyền thông bus EtherCAT</h5>
              <p>Khung truyền EtherCAT chứa 6 gói PDO đọc encoder và 6 gói ghi mô-men:</p>
              <p>$$\Delta t_{comm} = 150\ \mu\text{s}$$</p>
              <p>Bao gồm trễ truyền dẫn cáp và trễ DMA card mạng.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính thời gian giải thuật toán động lực học Pinocchio</h5>
              <p>Động học thuận + Thuật toán RNEA $O(n)$ tính bù trọng lực và Coriolis:</p>
              <p>$$\Delta t_{dynamics} \approx 25\ \mu\text{s}$$</p>
              <p>Giải hệ bù ma sát LuGre cho 6 khớp:</p>
              <p>$$\Delta t_{friction} \approx 10\ \mu\text{s}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Thời gian thuật toán điều khiển & Giới hạn an toàn</h5>
              <p>Thuật toán điều khiển PID + Lọc Notch Filter triệt rung:</p>
              <p>$$\Delta t_{control} \approx 35\ \mu\text{s}$$</p>
              <p>Kiểm tra giới hạn an toàn phần mềm (Safety limits, collision check):</p>
              <p>$$\Delta t_{safety} \approx 30\ \mu\text{s}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Tổng hợp ngân sách & Đánh giá biên độ an toàn</h5>
              <p>Tổng thời gian thực thi của vòng lặp:</p>
              <p>$$T_{used} = 150 + 25 + 10 + 35 + 30 = 250\ \mu\text{s}$$</p>
              <p>Biên độ thời gian rảnh rỗi (Slack Margin):</p>
              <p>$$T_{margin} = 1000 - 250 = 750\ \mu\text{s} \quad (75\% \text{ nhàn rỗi})$$</p>
              <p>Kết luận: Hệ thống đạt độ an toàn thời gian thực cực cao, CPU hoạt động ở mức tải $25\%$, hoàn toàn miễn nhiễm với hiện tượng tràn chu kỳ (overrun deadline).</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-14-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: File Cấu Hình ros2_control.xacro Hoàn Chỉnh</h4>
          <p>Khai báo cấu hình phần cứng chuẩn giao tiếp với `gz_ros2_control` và driver thật:</p>
          <div class="code-card">
            <div class="code-header">
              <span>robot_control.xacro (ROS 2 Humble / Iron / Jazzy)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>&lt;ros2_control name="RobotHardwareInterface" type="system"&gt;
  &lt;hardware&gt;
    &lt;plugin&gt;gz_ros2_control/GazeboSimSystem&lt;/plugin&gt;
  &lt;/hardware&gt;
  
  &lt;joint name="joint1"&gt;
    &lt;command_interface name="effort"&gt;
      &lt;param name="min"&gt;-150.0&lt;/param&gt;
      &lt;param name="max"&gt;150.0&lt;/param&gt;
    &lt;/command_interface&gt;
    &lt;state_interface name="position"/&gt;
    &lt;state_interface name="velocity"/&gt;
    &lt;state_interface name="effort"/&gt;
  &lt;/joint&gt;
&lt;/ros2_control&gt;</code></pre>
          </div>
        </div>
"""

# Generate HTML files
print("Generating Ch 10...")
with open(os.path.join(CHAPTERS_DIR, "ch10.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("10", "Thuật Toán Tích Phân Số ODEs Cho Động Lực Học", "Numerical ODE Integration for Dynamics", "TRACK 5: GIẢI TÍCH SỐ & MÔ PHỎNG", "track-5", "ch09.html", "Chương 09: Dao Động Cơ Học", "ch11.html", "Chương 11: Hệ Cứng & Symplectic", ch10_sidebar, ch10_body))

print("Generating Ch 11...")
with open(os.path.join(CHAPTERS_DIR, "ch11.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("11", "Hệ Cứng, Tích Phân Symplectic & Phương Pháp Đa Bước", "Stiff ODE Solvers, Symplectic Integrators & Multistep", "TRACK 5: GIẢI TÍCH SỐ & MÔ PHỎNG", "track-5", "ch10.html", "Chương 10: Tích Phân Số ODEs", "ch12.html", "Chương 12: Giải DAEs & Va Chạm", ch11_sidebar, ch11_body))

print("Generating Ch 12...")
with open(os.path.join(CHAPTERS_DIR, "ch12.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("12", "Giải Hệ Phương Trình DAEs & Động Lực Học Va Chạm", "Numerical DAE Solvers & Contact Physics", "TRACK 5: GIẢI TÍCH SỐ & MÔ PHỎNG", "track-5", "ch11.html", "Chương 11: Hệ Cứng & Symplectic", "ch13.html", "Chương 13: Ổn Định Lyapunov", ch12_sidebar, ch12_body))

print("Generating Ch 13...")
with open(os.path.join(CHAPTERS_DIR, "ch13.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("13", "Phân Tích Ổn Định Lyapunov & Điều Khiển Mô-Men Tính Toán", "Lyapunov Stability & Computed Torque Control", "TRACK 6: ỔN ĐỊNH & TRIỂN KHAI", "track-6", "ch12.html", "Chương 12: Giải DAEs & Va Chạm", "ch14.html", "Chương 14: Kiến Trúc Thực Tế", ch13_sidebar, ch13_body))

print("Generating Ch 14...")
with open(os.path.join(CHAPTERS_DIR, "ch14.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("14", "Kiến Trúc Thực Tế: URDF, Pinocchio, ros2_control & Gazebo", "Production Robot Simulation Architecture", "TRACK 6: ỔN ĐỊNH & TRIỂN KHAI", "track-6", "ch13.html", "Chương 13: Ổn Định Lyapunov", "../index.html", "Lộ trình Tổng quan", ch14_sidebar, ch14_body))

print("Successfully generated Chapters 10, 11, 12, 13, 14!")
