# -*- coding: utf-8 -*-
"""
build_chapters_t3_t4.py
Biên soạn nội dung chuẩn 6 tầng tri thức cho Track 3 và Track 4 (Chương 05 - Chương 09):
- Ch 05: Động Lực Học Newton-Euler & Thuật Toán Đệ Quy RNEA
- Ch 06: Cơ Học Lagrange & Động Lực Học Robot Cánh Tay
- Ch 07: Động Lực Học Hệ Ràng Buộc & Phương Pháp Kane
- Ch 08: Cơ Học Hamilton & Hệ Port-Hamiltonian Trong Robot
- Ch 09: Dao Động Cơ Học, Dầm Đàn Hồi & Phân Tích Phần Tử Hữu Hạn
"""

import os
from build_chapters_t1_t2 import make_chapter_html, BASE_DIR, CHAPTERS_DIR

# ==============================================================================
# CHƯƠNG 05: Động Lực Học Newton-Euler & Thuật Toán Đệ Quy RNEA
# ==============================================================================
ch05_sidebar = [
    {"id": "sec-5-1", "title": "5.1 Động lượng & Mô-men Động lượng Vật rắn"},
    {"id": "sec-5-2", "title": "5.2 Tensor Quán tính & Định lý Huygens-Steiner"},
    {"id": "sec-5-3", "title": "5.3 Phương trình Newton-Euler Khung Động"},
    {"id": "sec-5-4", "title": "5.4 Thuật toán Đệ quy RNEA O(n)"},
    {"id": "sec-5-5", "title": "5.5 Phân tích Hiệu năng Tính toán RNEA"},
    {"id": "sec-5-6", "title": "5.6 Động lực học Con lắc Furuta"},
    {"id": "sec-5-sim", "title": "⚡ Mô phỏng Con lắc Furuta (Canvas)"},
    {"id": "sec-5-worked", "title": "📐 Ví dụ Tính Số 4 Bước Thuật Toán RNEA"},
    {"id": "sec-5-bridge", "title": "🛠️ Cầu nối Pinocchio C++ RNEA"}
]

ch05_body = r"""
        <!-- 5.1 -->
        <h2 id="sec-5-1">5.1 Động Lượng & Mô-Men Động Lượng Của Vật Rắn Trong Không Gian 3D</h2>
        <p>Xét một vật rắn $i$ có khối lượng $m_i$ và khối tâm $C_i$. Động lượng tịnh tiến $p_i$ và mô-men động lượng $h_{C,i}$ quanh khối tâm được xác định bởi:</p>
        <div class="formula-hero">
          <div class="formula-title">Định Nghĩa Động Lượng & Mô-Men Động Lượng</div>
          <div class="formula-math">
            $$p_i = m_i v_{C,i}, \quad h_{C,i} = I_{C,i} \boldsymbol{\omega}_i$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách tham số:</strong> $v_{C,i}$ là vận tốc dài của khối tâm; $\boldsymbol{\omega}_i$ là vector vận tốc góc tức thời; $I_{C,i}$ là tensor quán tính đối xứng bậc 2 tính tại khối tâm.
          </div>
        </div>

        <!-- 5.2 -->
        <h2 id="sec-5-2">5.2 Tensor Quán Tính & Định Lý Trục Song Song Huygens-Steiner</h2>
        <p>Tensor quán tính (Inertia Tensor / Dyadic) trong hệ quy chiếu gắn liền với khâu vật rắn là một ma trận đối xứng xác định dương $3 \times 3$:</p>
        $$I_C = \begin{bmatrix} I_{xx} & -I_{xy} & -I_{xz} \\ -I_{xy} & I_{yy} & -I_{yz} \\ -I_{xz} & -I_{yz} & I_{zz} \end{bmatrix}, \quad I_{xx} = \int (y^2 + z^2) dm, \; I_{xy} = \int xy dm$$
        <p>Nếu dời tâm tính toán từ khối tâm $C$ sang điểm tựa gốc tọa độ $O$ với vector dời $r_C = [x_C, y_C, z_C]^T$, áp dụng Định lý Steiner dạng ma trận:</p>
        $$I_O = I_C + m \left( (r_C^T r_C) I_{3 \times 3} - r_C r_C^T \right) = I_C - m S^2(r_C)$$

        <!-- 5.3 -->
        <h2 id="sec-5-3">5.3 Phương Trình Newton-Euler Trong Hệ Quy Chiếu Động</h2>
        <p>Đạo hàm thời gian của động lượng và mô-men động lượng trong hệ quy chiếu động xoay với vận tốc góc $\boldsymbol{\omega}_i$ tuân theo phương trình Euler động học:</p>
        <div class="formula-hero">
          <div class="formula-title">Hệ Phương Trình Newton-Euler Cho Từng Khâu Vật Rắn</div>
          <div class="formula-math">
            $$\begin{cases}
              F_i = \dot{p}_i = m_i \dot{v}_{C,i} & (\text{Định luật II Newton cho tịnh tiến}) \\
              N_{C,i} = \dot{h}_{C,i} = I_{C,i} \dot{\boldsymbol{\omega}}_i + \boldsymbol{\omega}_i \times (I_{C,i} \boldsymbol{\omega}_i) & (\text{Phương trình Euler cho chuyển động quay})
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Hiệu ứng hồi chuyển (Gyroscopic effect):</strong> Số hạng $\boldsymbol{\omega}_i \times (I_{C,i} \boldsymbol{\omega}_i)$ là mô-men hồi chuyển phi tuyến sinh ra khi trục quay của vật rắn bị quay trong không gian.
          </div>
        </div>

        <!-- 5.4 -->
        <h2 id="sec-5-4">5.4 Thuật Toán Newton-Euler Đệ Quy (RNEA) Độ Phức Tạp $\mathcal{O}(n)$</h2>
        <p>Thuật toán RNEA (Recursive Newton-Euler Algorithm) do Luh, Walker và Paul phát minh là thuật toán tiêu chuẩn công nghiệp giải bài toán động lực học ngược: Cho trước vị trí $q$, vận tốc $\dot{q}$ và gia tốc mong muốn $\ddot{q}$, tính toán vector mô-men khớp $\tau$ trong thời gian thực.</p>
        <div class="why-matters-box">
          <div class="why-matters-header">💡 ĐỘT PHÁ TÍNH TOÁN CỦA THUẬT TOÁN RNEA</div>
          <div class="why-matters-body">
            Trong khi phương pháp Lagrange truyền thống tính toán ma trận $M(q)$ và Coriolis $C(q,\dot{q})$ tốn độ phức tạp $\mathcal{O}(n^4)$ hoặc $\mathcal{O}(n^3)$, RNEA chia bài toán thành 2 bước đệ quy tuần tự giúp giảm triệt để độ phức tạp tính toán xuống đúng $\mathcal{O}(n)$ tuyến tính! Với robot 6 bậc tự do, RNEA chạy chỉ mất chưa đầy $15\ \mu\text{s}$ trên CPU ARM tiêu chuẩn.
          </div>
        </div>

        <p><strong>Bước 1: Lan truyền động học tiến (Forward Kinematic Pass) từ khâu gốc $i=0 \to n$:</strong></p>
        $$\boldsymbol{\omega}_i = R_i^{i-1} \boldsymbol{\omega}_{i-1} + z_0 \dot{q}_i$$
        $$\dot{\boldsymbol{\omega}}_i = R_i^{i-1} \dot{\boldsymbol{\omega}}_{i-1} + z_0 \ddot{q}_i + \boldsymbol{\omega}_i \times (z_0 \dot{q}_i)$$
        $$\dot{v}_i = R_i^{i-1} \dot{v}_{i-1} + \dot{\boldsymbol{\omega}}_i \times r_{i-1,i} + \boldsymbol{\omega}_i \times (\boldsymbol{\omega}_i \times r_{i-1,i})$$
        $$\dot{v}_{C,i} = \dot{v}_i + \dot{\boldsymbol{\omega}}_i \times r_{i,C_i} + \boldsymbol{\omega}_i \times (\boldsymbol{\omega}_i \times r_{i,C_i})$$
        <p><em>Khởi tạo:</em> $\dot{v}_0 = -g$ (truyền gia tốc trọng trường ngược hướng từ gốc lên, tự động bù trọng lực toàn bộ khâu!).</p>

        <p><strong>Bước 2: Lan truyền nội lực và mô-men lùi (Backward Force Pass) từ khâu thao tác cuối $i=n \to 1$:</strong></p>
        $$F_i = m_i \dot{v}_{C,i}, \quad N_i = I_{C,i} \dot{\boldsymbol{\omega}}_i + \boldsymbol{\omega}_i \times (I_{C,i} \boldsymbol{\omega}_i)$$
        $$f_i = R_{i+1}^i f_{i+1} + F_i$$
        $$n_i = R_{i+1}^i n_{i+1} + r_{i-1,i} \times f_i + r_{i,C_i} \times F_i + N_i$$
        $$\tau_i = n_i^T z_0 \quad (\text{Mô-men khớp tác động})$$

        <!-- 5.5 -->
        <h2 id="sec-5-5">5.5 Phân Tích Động Lực Học Con Lắc Ngược Furuta</h2>
        <p>Con lắc Furuta gồm một tay cần quay chủ động trên mặt phẳng ngang và một con lắc tự do quay trong mặt phẳng đứng. Ứng dụng RNEA giúp tách lập phương trình vi phân chuyển động không gian phi tuyến bậc cao của hệ con lắc quay.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-5-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Động Lực Học Con Lắc Furuta (Newton-Euler)</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-05" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Mô-men kích thích trục quay Tau: <input type="range" id="sim05-tau" min="-3" max="3" step="0.2" value="0"> <span id="sim05-tau-val">0.00 N·m</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-5-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Lực Quán Tính Bằng Bước Tiến RNEA Cho Khâu 1</h3>
          <p>Xét khâu 1 của robot quay quanh trục thẳng đứng $z_0$. Cho góc quay $q_1 = 0$, vận tốc góc $\dot{q}_1 = 2.0\text{ rad/s}$, gia tốc góc $\ddot{q}_1 = 5.0\text{ rad/s}^2$. Khối lượng khâu $m_1 = 3.0\text{ kg}$, khoảng cách từ gốc khớp đến khối tâm $r_{0,C1} = [0.2, 0, 0]^T\text{ m}$. Gia tốc trọng trường hướng xuống: $g = [0, 0, -9.81]^T\text{ m/s}^2$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Khởi tạo gia tốc gốc & Vận tốc góc</h5>
              <p>Khởi tạo điều kiện biên tại đế cố định (khâu 0):</p>
              <p>$$\boldsymbol{\omega}_0 = [0, 0, 0]^T, \quad \dot{\boldsymbol{\omega}}_0 = [0, 0, 0]^T$$</p>
              <p>$$\dot{v}_0 = -g = [0, 0, 9.81]^T\text{ m/s}^2$$</p>
              <p>Vận tốc góc khâu 1: $\boldsymbol{\omega}_1 = \boldsymbol{\omega}_0 + z_0 \dot{q}_1 = [0, 0, 2.0]^T\text{ rad/s}$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính gia tốc góc khâu 1</h5>
              <p>Gia tốc góc khâu 1 tính theo công thức đệ quy:</p>
              <p>$$\dot{\boldsymbol{\omega}}_1 = \dot{\boldsymbol{\omega}}_0 + z_0 \ddot{q}_1 + \boldsymbol{\omega}_1 \times (z_0 \dot{q}_1)$$</p>
              <p>Vì $\boldsymbol{\omega}_1$ cùng phương với $z_0$, tích có hướng $\boldsymbol{\omega}_1 \times z_0 = 0$:</p>
              <p>$$\dot{\boldsymbol{\omega}}_1 = [0, 0, 5.0]^T\text{ rad/s}^2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính gia tốc khối tâm $\dot{v}_{C,1}$</h5>
              <p>Gia tốc gốc khớp 1: $\dot{v}_1 = \dot{v}_0 = [0, 0, 9.81]^T\text{ m/s}^2$.</p>
              <p>Số hạng tiếp tuyến: $\dot{\boldsymbol{\omega}}_1 \times r_{0,C1} = [0, 0, 5] \times [0.2, 0, 0] = [0, 1.0, 0]^T$.</p>
              <p>Số hạng hướng tâm: $\boldsymbol{\omega}_1 \times (\boldsymbol{\omega}_1 \times r_{0,C1}) = [0, 0, 2] \times [0, 0.4, 0] = [-0.8, 0, 0]^T$.</p>
              <p>Gia tốc khối tâm tổng hợp: $\dot{v}_{C,1} = [-0.8, 1.0, 9.81]^T\text{ m/s}^2$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Tính vector lực quán tính D'Alembert</h5>
              <p>Lực quán tính toàn phần tác động lên khối tâm khâu 1:</p>
              <p>$$F_1 = m_1 \dot{v}_{C,1} = 3.0 \times \begin{bmatrix} -0.8 \\ 1.0 \\ 9.81 \end{bmatrix} = \begin{bmatrix} -2.4 \\ 3.0 \\ 29.43 \end{bmatrix}\text{ [N]}$$</p>
              <p>Ý nghĩa: Khâu 1 chịu lực hướng tâm $2.4\text{ N}$, lực tiếp tuyến $3.0\text{ N}$ và lực nâng trọng trường $29.43\text{ N}$.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-5-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Gọi Thuật Toán RNEA C++ Trong Pinocchio</h4>
          <p>Thư viện C++ mã nguồn mở Pinocchio (chuẩn công nghiệp robotics hiện đại) cài đặt thuật toán RNEA tối ưu hóa SIMD AVX2:</p>
          <div class="code-card">
            <div class="code-header">
              <span>pinocchio_rnea.cpp (C++17)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>#include "pinocchio/parsers/urdf.hpp"
#include "pinocchio/algorithm/rnea.hpp"

// Tải mô hình URDF robot
pinocchio::Model model;
pinocchio::urdf::buildModel("robot.urdf", model);
pinocchio::Data data(model);

// Vector trạng thái góc khớp, vận tốc và gia tốc
Eigen::VectorXd q = Eigen::VectorXd::Zero(model.nv);
Eigen::VectorXd v = Eigen::VectorXd::Zero(model.nv);
Eigen::VectorXd a = Eigen::VectorXd::Zero(model.nv);

// Gọi thuật toán RNEA O(n) với thời gian thực thi &lt; 10 micro-giây
const Eigen::VectorXd &amp; tau = pinocchio::rnea(model, data, q, v, a);</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 06: Cơ Học Lagrange & Động Lực Học Robot Cánh Tay
# ==============================================================================
ch06_sidebar = [
    {"id": "sec-6-1", "title": "6.1 Tọa độ Suy rộng & Bậc Tự do"},
    {"id": "sec-6-2", "title": "6.2 Chuyển dời Ảo & Nguyên lý D'Alembert"},
    {"id": "sec-6-3", "title": "6.3 Hàm Lagrange & Phương trình Euler-Lagrange"},
    {"id": "sec-6-4", "title": "6.4 Dạng Phương trình Chuẩn Robot Cánh tay"},
    {"id": "sec-6-5", "title": "6.5 Tính chất Phản Đối xứng Ṁ - 2C = 0"},
    {"id": "sec-6-6", "title": "6.6 Tính Tuyến tính theo Tham số Quán tính"},
    {"id": "sec-6-sim", "title": "⚡ Mô phỏng Robot Cánh Tay 2-DOF (Canvas)"},
    {"id": "sec-6-worked", "title": "📐 Ví dụ Tính Số 4 Bước Ma Trận M(q) & C(q,q̇)"},
    {"id": "sec-6-bridge", "title": "🛠️ Cầu nối Nhận dạng Tham số Quán tính Y(q,q̇,q̈)θ"}
]

ch06_body = r"""
        <!-- 6.1 -->
        <h2 id="sec-6-1">6.1 Tọa Độ Suy Rộng & Bậc Tự Do Của Cơ Hệ Robot</h2>
        <p>Một hệ cơ học gồm $N$ hạt trong không gian 3D chịu $k$ ràng buộc độc lập sẽ có $n = 3N - k$ bậc tự do (Degrees of Freedom - DOF). Một tập hợp $n$ biến số độc lập tối thiểu $q = [q_1, q_2, \dots, q_n]^T$ xác định đơn nhất cấu hình của hệ được gọi là <strong>vector tọa độ suy rộng (Generalized Coordinates)</strong>.</p>

        <!-- 6.2 -->
        <h2 id="sec-6-2">6.2 Chuyển Dời Ảo & Nguyên Lý Công Ảo D'Alembert</h2>
        <p>Chuyển dời ảo $\delta r_i$ là biến thiên vi phân tức thời vô cùng bé của vị trí mà <em>không tốn thời gian</em> ($\delta t = 0$) và phù hợp với mọi ràng buộc hình học của cơ hệ tại thời điểm khảo sát. Theo nguyên lý D'Alembert, tổng công ảo của các lực chủ động kết hợp với lực quán tính triệt tiêu hoàn toàn trên mọi chuyển dời ảo khả dĩ:</p>
        $$\sum_{i=1}^N (F_i - m_i \ddot{r}_i) \cdot \delta r_i = 0$$
        <p>Nguyên lý này tự động triệt tiêu toàn bộ các phản lực liên kết nội tại trong khớp nối, giúp đơn giản hóa việc thiết lập phương trình chuyển động.</p>

        <!-- 6.3 -->
        <h2 id="sec-6-3">6.3 Hàm Lagrange & Phương Trình Euler-Lagrange</h2>
        <p>Định nghĩa hàm Lagrange (Lagrangian) $L(q, \dot{q})$ là hiệu số giữa tổng động năng $T(q, \dot{q})$ và tổng thế năng $V(q)$ của cơ hệ:</p>
        $$L(q, \dot{q}) = T(q, \dot{q}) - V(q)$$
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Vi Phân Euler-Lagrange</div>
          <div class="formula-math">
            $$\frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = \tau_i, \quad i = 1, 2, \dots, n$$
          </div>
          <div class="formula-legend">
            <strong>Ký hiệu:</strong> $\tau_i$ là lực hoặc mô-men suy rộng ngoài tác động lên khớp thứ $i$ (do động cơ sinh ra hoặc ma sát).
          </div>
        </div>

        <!-- 6.4 -->
        <h2 id="sec-6-4">6.4 Dạng Phương Trình Chuẩn Động Lực Học Robot Cánh Tay</h2>
        <p>Áp dụng phương trình Euler-Lagrange cho robot cánh tay chuỗi hở $n$ bậc tự do, phương trình vi phân phi tuyến luôn đưa về dạng ma trận chính tắc:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Động Lực Học Chính Tắc Robot (Manipulator Equation)</div>
          <div class="formula-math">
            $$M(q)\ddot{q} + C(q, \dot{q})\dot{q} + g(q) = \tau$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách các ma trận thành phần:</strong>
            <br>• $M(q) \in \mathbb{R}^{n \times n}$: Ma trận quán tính (Inertia Matrix), đối xứng và xác định dương ($M(q) = M^T(q) \gt 0$).
            <br>• $C(q, \dot{q}) \in \mathbb{R}^{n \times n}$: Ma trận Coriolis và lực ly tâm, chứa các hệ số ký hiệu Christoffel.
            <br>• $g(q) = \frac{\partial V(q)}{\partial q} \in \mathbb{R}^n$: Vector mô-men trọng trường sinh ra do thế năng.
            <br>• $\tau \in \mathbb{R}^n$: Vector mô-men điều khiển do các động cơ khớp cung cấp.
          </div>
        </div>

        <!-- 6.5 -->
        <h2 id="sec-6-5">6.5 Tính Chất Phản Đối Xứng Cốt Tử $\dot{M}(q) - 2C(q, \dot{q}) = 0$</h2>
        <p>Nếu ma trận Coriolis $C(q, \dot{q})$ được tính toán thông qua ký hiệu Christoffel loại 1:</p>
        $$c_{kj} = \sum_{i=1}^n c_{ijk} \dot{q}_i = \frac{1}{2} \sum_{i=1}^n \left( \frac{\partial m_{kj}}{\partial q_i} + \frac{\partial m_{ki}}{\partial q_j} - \frac{\partial m_{ij}}{\partial q_k} \right) \dot{q}_i$$
        <div class="why-matters-box">
          <div class="why-matters-header">💎 TÍNH CHẤT VÀNG: BẢO TOÀN NĂNG LƯỢNG & TÍNH THỤ ĐỘNG</div>
          <div class="why-matters-body">
            Ma trận đạo hàm thời gian $\dot{M}(q) - 2C(q, \dot{q})$ là một ma trận phản đối xứng (skew-symmetric), nghĩa là với mọi vector bất kỳ $x \in \mathbb{R}^n$:
            $$x^T \left( \dot{M}(q) - 2C(q, \dot{q}) \right) x \equiv 0$$
            Đẳng thức này thể hiện trực tiếp định luật bảo toàn năng lượng cơ học của robot và là nền tảng sống còn cho phép thiết kế các bộ điều khiển phi tuyến Lyapunov và điều khiển thụ động (Passivity-Based Control) đạt tính ổn định tiệm cận toàn cục mà không sợ mất kiểm soát.
          </div>
        </div>

        <!-- 6.6 -->
        <h2 id="sec-6-6">6.6 Tính Tuyến Tính Theo Tham Số Quán Tính (Linearity in Parameters)</h2>
        <p>Mặc dù phương trình robot phi tuyến cao theo tọa độ $q$ và vận tốc $\dot{q}$, nó lại hoàn toàn <strong>tuyến tính theo tập hợp các tham số quán tính vật lý</strong> $\theta = [m_i, m_i r_{Ci}, I_{xx,i}, \dots]^T$:</p>
        $$M(q)\ddot{q} + C(q, \dot{q})\dot{q} + g(q) = Y(q, \dot{q}, \ddot{q}) \theta = \tau$$
        <p>Ma trận $Y(q, \dot{q}, \ddot{q}) \in \mathbb{R}^{n \times p}$ được gọi là <strong>ma trận hồi quy (Regressor Matrix)</strong>, cho phép thực hiện bài toán nhận dạng tham số tải trọng tự động bằng phương pháp bình phương bé nhất (Least Squares).</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-6-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Cánh Tay 2-DOF & Kiểm Chứng Đẳng Thức $\dot{M}-2C=0$</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-06" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Mô-men khớp 1 (Tau 1): <input type="range" id="sim06-t1" min="-10" max="10" step="0.5" value="1.0"> <span id="sim06-t1-val">1.0 Nm</span></label>
            <label style="font-size: 0.85rem; font-weight: 600;">Mô-men khớp 2 (Tau 2): <input type="range" id="sim06-t2" min="-5" max="5" step="0.5" value="-0.5"> <span id="sim06-t2-val">-0.5 Nm</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-6-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Toán Ma Trận Khối Lượng $M(q)$ Cho Robot 2 Khâu Phẳng</h3>
          <p>Xét cánh tay robot phẳng 2 khâu (Planar 2R Arm) chuyển động trong mặt phẳng ngang (không có trọng lực $g(q)=0$). Khâu 1 có chiều dài $l_1 = 1.0\text{ m}$, khối lượng tập trung ở đầu khâu $m_1 = 2.0\text{ kg}$. Khâu 2 có chiều dài $l_2 = 0.8\text{ m}$, khối lượng tập trung $m_2 = 1.5\text{ kg}$. Tại thời điểm khảo sát, góc khớp $q_1 = 30^\circ$, $q_2 = 60^\circ$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính các số hạng hình học cơ sở</h5>
              <p>$$\cos(q_2) = \cos(60^\circ) = 0.500, \quad \sin(q_2) = \sin(60^\circ) = 0.866$$</p>
              <p>Tính các thừa số chiều dài bình phương:</p>
              <p>$$l_1^2 = 1.0^2 = 1.0, \quad l_2^2 = 0.8^2 = 0.64$$</p>
              <p>$$l_1 l_2 = 1.0 \times 0.8 = 0.8$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Thiết lập công thức phần tử ma trận quán tính</h5>
              <p>$$M_{11}(q) = (m_1 + m_2) l_1^2 + m_2 l_2^2 + 2 m_2 l_1 l_2 \cos(q_2)$$</p>
              <p>$$M_{12}(q) = M_{21}(q) = m_2 l_2^2 + m_2 l_1 l_2 \cos(q_2)$$</p>
              <p>$$M_{22}(q) = m_2 l_2^2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính toán giá trị số từng phần tử</h5>
              <p>$$M_{11} = (2.0 + 1.5)(1.0) + 1.5(0.64) + 2(1.5)(0.8)(0.5) = 3.5 + 0.96 + 1.2 = 5.66\text{ kg}\cdot\text{m}^2$$</p>
              <p>$$M_{12} = M_{21} = 1.5(0.64) + 1.5(0.8)(0.5) = 0.96 + 0.60 = 1.56\text{ kg}\cdot\text{m}^2$$</p>
              <p>$$M_{22} = 1.5(0.64) = 0.96\text{ kg}\cdot\text{m}^2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Kiểm tra tính xác định dương của $M(q)$</h5>
              <p>Ma trận quán tính thu được:</p>
              <p>$$M(q) = \begin{bmatrix} 5.66 & 1.56 \\ 1.56 & 0.96 \end{bmatrix}$$</p>
              <p>Kiểm tra định thức: $\det(M) = (5.66)(0.96) - 1.56^2 = 5.4336 - 2.4336 = 3.00 \gt 0$.</p>
              <p>Vì $M_{11} = 5.66 \gt 0$ và $\det(M) = 3.00 \gt 0$, ma trận $M(q)$ đối xứng xác định dương tuyệt đối, bảo đảm luôn khả nghịch để giải gia tốc $\ddot{q} = M^{-1}(\tau - C\dot{q})$.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-6-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Tách Ma Trận Hồi Quy $Y(q,\dot{q},\ddot{q})$ Nhận Dạng Tải Trọng</h4>
          <p>Thuật toán nhận dạng tham số động lực học trực tuyến trên robot thực tế bằng cách thu thập dữ liệu di chuyển và giải bài toán bình phương bé nhất đệ quy (Recursive Least Squares - RLS):</p>
          <div class="code-card">
            <div class="code-header">
              <span>parameter_identification.py (Python / ROS 2)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import numpy as np

def compute_regressor(q, dq, ddq, l1=1.0, l2=0.8):
    # Trích xuất ma trận Y kích thước 2 x p cho robot 2R
    c2 = np.cos(q[1])
    s2 = np.sin(q[1])
    
    Y = np.zeros((2, 3))
    # Y * [theta1, theta2, theta3]^T = tau
    Y[0, 0] = ddq[0]
    Y[0, 1] = ddq[0] + ddq[1]
    Y[0, 2] = (2*ddq[0] + ddq[1])*c2 - dq[1]*(2*dq[0] + dq[1])*s2
    
    Y[1, 0] = 0.0
    Y[1, 1] = ddq[0] + ddq[1]
    Y[1, 2] = ddq[0]*c2 + dq[0]**2 * s2
    return Y</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 07: Động Lực Học Hệ Ràng Buộc & Phương Pháp Kane
# ==============================================================================
ch07_sidebar = [
    {"id": "sec-7-1", "title": "7.1 Phân loại Ràng buộc Holonomic & Nonholonomic"},
    {"id": "sec-7-2", "title": "7.2 Ràng buộc Dòng & Nhân tử Lagrange"},
    {"id": "sec-7-3", "title": "7.3 Hệ Phương trình Vi phân Đại số LDAEs"},
    {"id": "sec-7-4", "title": "7.4 Phương pháp Kane & Vận tốc Suy rộng"},
    {"id": "sec-7-5", "title": "7.5 Động học Robot Di động Bánh xe (WMR)"},
    {"id": "sec-7-6", "title": "7.6 Cơ cấu Kín & Robot Song song (Parallel)"},
    {"id": "sec-7-sim", "title": "⚡ Mô phỏng Robot Bánh Xe Nonholonomic (Canvas)"},
    {"id": "sec-7-worked", "title": "📐 Ví dụ Tính Số 4 Bước Khử Nhân Tử Lagrange"},
    {"id": "sec-7-bridge", "title": "🛠️ Cầu nối ROS 2 Nav2 Controller Plugin"}
]

ch07_body = r"""
        <!-- 7.1 -->
        <h2 id="sec-7-1">7.1 Phân Loại Ràng Buộc Cơ Học: Holonomic vs Nonholonomic</h2>
        <p>Ràng buộc cơ học hạn chế quỹ đạo vị trí hoặc hướng vận tốc khả dĩ của hệ thống:</p>
        <div class="formula-hero">
          <div class="formula-title">Định Nghĩa Phân Loại Ràng Buộc</div>
          <div class="formula-math">
            $$\begin{cases}
              \text{Ràng buộc Hình học (Holonomic):} & \phi(q, t) = 0 \\
              \text{Ràng buộc Chuyển động (Non-holonomic):} & A(q) \dot{q} + a_0(q, t) = 0 \quad (\text{Không khả tích về dạng } \phi(q)=0)
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Ví dụ kinh điển:</strong> Robot di động vi sai (WMR), bánh xe lăn trên mặt đường chịu ràng buộc không trượt bên $\dot{y}\cos\theta - \dot{x}\sin\theta = 0$. Ràng buộc này là non-holonomic vì robot vẫn có thể đỗ tại bất kỳ vị trí và hướng nào $(x, y, \theta)$ thông qua việc tiến lùi kết hợp rẽ!
          </div>
        </div>

        <!-- 7.2 -->
        <h2 id="sec-7-2">7.2 Nhân Tử Lagrange & Hệ Phương Trình LDAEs</h2>
        <p>Để giải hệ thống có ràng buộc dạng Pfaffian $A(q)\dot{q} = 0$, ta đưa thêm vector nhân tử Lagrange $\lambda \in \mathbb{R}^m$ đại diện cho phản lực ràng buộc:</p>
        <div class="formula-hero">
          <div class="formula-title">Hệ Phương Trình Lagrangian Differential-Algebraic Equations (LDAEs)</div>
          <div class="formula-math">
            $$\begin{cases}
              M(q)\ddot{q} + C(q,\dot{q})\dot{q} + g(q) = \tau + A^T(q)\lambda \\
              A(q)\dot{q} = 0
            \end{cases}$$
          </div>
          <div class="formula-legend">
            <strong>Bản chất:</strong> Đây là hệ phương trình vi phân đại số (DAEs) chỉ số 2 hoặc 3 (Index-2 / Index-3), đòi hỏi kỹ thuật giải số học đặc thù để tránh suy thoái lời giải.
          </div>
        </div>

        <!-- 7.3 -->
        <h2 id="sec-7-3">7.3 Phương Pháp Kane & Vận Tốc Suy Rộng (Generalized Speeds)</h2>
        <p>Phương pháp Thomas R. Kane (Kane's Dynamics) sử dụng các vận tốc suy rộng độc lập $u_r = \sum_{s=1}^n Y_{rs} \dot{q}_s$ để chiếu trực tiếp lực quán tính và lực chủ động lên không gian chuyển động cho phép:</p>
        $$F_r + F_r^* = 0, \quad r = 1, 2, \dots, p$$
        <p>với $F_r$ là lực chủ động suy rộng và $F_r^*$ là lực quán tính suy rộng. Ưu điểm của Kane là triệt tiêu hoàn toàn các nhân tử Lagrange $\lambda$ mà không cần tính đạo hàm phức tạp của hàm thế như Lagrange.</p>

        <!-- 7.4 -->
        <h2 id="sec-7-4">7.4 Động Học Robot Di Động Bánh Xe Tự Hành (WMR)</h2>
        <p>Xét robot di động 2 bánh vi sai có bán kính bánh xe $r$, khoảng cách hai bánh $2b$. Phương trình động học trong không gian trạng thái:</p>
        $$\begin{bmatrix} \dot{x} \\ \dot{y} \\ \dot{\theta} \end{bmatrix} = \begin{bmatrix} \cos\theta & 0 \\ \sin\theta & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} v \\ \omega \end{bmatrix}$$

        <!-- 7.5 -->
        <h2 id="sec-7-5">7.5 Cơ Cấu Song Song Mạch Kín (Closed-Chain Parallel Robots)</h2>
        <p>Trong các robot song song như Delta robot hoặc cơ cấu Stewart 6 bậc tự do, các khâu tạo thành chuỗi động kín (closed kinematic chains) với ràng buộc hình học khép vòng $\phi(q) = 0$. Phương pháp DAEs cho phép mô phỏng chính xác chuyển động và ứng suất thanh giằng.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-7-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Quỹ Đạo Robot Bánh Xe Ràng Buộc Nonholonomic</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-07" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Vận tốc tiến v: <input type="range" id="sim07-v" min="0.2" max="3.0" step="0.2" value="1.2"> <span id="sim07-v-val">1.20 m/s</span></label>
            <label style="font-size: 0.85rem; font-weight: 600;">Vận tốc góc w: <input type="range" id="sim07-w" min="-1.5" max="1.5" step="0.1" value="0.6"> <span id="sim07-w-val">0.60 rad/s</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-7-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Khử Nhân Tử Lagrange Cho Robot Di Động Bánh Xe</h3>
          <p>Xét robot vi sai có tọa độ $q = [x, y, \theta]^T$, khối lượng $m = 10.0\text{ kg}$, mô-men quán tính $I_z = 0.5\text{ kg}\cdot\text{m}^2$. Ràng buộc bánh xe lăn không trượt bên là $A(q)\dot{q} = -\sin\theta \dot{x} + \cos\theta \dot{y} = 0$. Thiết lập biểu thức phản lực ràng buộc $\lambda$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Ma trận ràng buộc $A(q)$ và không gian rỗng $S(q)$</h5>
              <p>Ma trận ràng buộc kích thước $1 \times 3$:</p>
              <p>$$A(q) = \begin{bmatrix} -\sin\theta & \cos\theta & 0 \end{bmatrix}$$</p>
              <p>Ma trận cơ sở không gian rỗng $S(q)$ thỏa mãn $A(q) S(q) = 0$:</p>
              <p>$$S(q) = \begin{bmatrix} \cos\theta & 0 \\ \sin\theta & 0 \\ 0 & 1 \end{bmatrix} \implies \dot{q} = S(q) \begin{bmatrix} v \\ \omega \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Lấy đạo hàm ràng buộc theo thời gian</h5>
              <p>$$\frac{d}{dt}(A(q)\dot{q}) = A(q)\ddot{q} + \dot{A}(q)\dot{q} = 0$$</p>
              <p>$$\dot{A}(q)\dot{q} = (-\dot{\theta}\cos\theta)\dot{x} + (-\dot{\theta}\sin\theta)\dot{y} = -\omega (\dot{x}\cos\theta + \dot{y}\sin\theta) = -\omega v$$</p>
              <p>$$\implies A(q)\ddot{q} = \omega v$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Thiết lập phương trình gia tốc có nhân tử $\lambda$</h5>
              <p>Phương trình Newton: $M \ddot{q} = \tau + A^T \lambda$, với $M = \text{diag}(m, m, I_z)$:</p>
              <p>$$\ddot{q} = M^{-1}\tau + M^{-1} A^T \lambda$$</p>
              <p>Nhân hai vế với $A(q)$:</p>
              <p>$$A M^{-1} \tau + (A M^{-1} A^T) \lambda = \omega v$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Giải nhân tử $\lambda$ & Ý nghĩa vật lý</h5>
              <p>Tính số hạng ma trận ràng buộc:</p>
              <p>$$A M^{-1} A^T = \frac{\sin^2\theta}{m} + \frac{\cos^2\theta}{m} = \frac{1}{m}$$</p>
              <p>Khi lực tác động ngoài song song với hướng di chuyển ($A M^{-1} \tau = 0$):</p>
              <p>$$\lambda = m \omega v = 10.0 \times 0.6 \times 1.2 = 7.2\text{ [N]}$$</p>
              <p>Ý nghĩa: $\lambda = 7.2\text{ N}$ chính là lực ma sát bám ngang giữ cho bánh xe không bị văng trượt ly tâm khi robot vào cua.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-7-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: ROS 2 DiffDrive Controller Plugin</h4>
          <p>Package `diff_drive_controller` trong `ros2_control` tự động giải phương trình biến đổi từ vận tốc dài và góc $(v, \omega)$ sang vận tốc góc của từng bánh xe $(\omega_L, \omega_R)$:</p>
          <div class="code-card">
            <div class="code-header">
              <span>diff_drive_params.yaml (ROS 2 Humble)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>diff_drive_controller:
  ros__parameters:
    left_wheel_names: ["left_wheel_joint"]
    right_wheel_names: ["right_wheel_joint"]
    wheel_separation: 0.45
    wheel_radius: 0.08
    wheels_per_side: 1
    publish_rate: 50.0
    enable_odom_tf: true
    cmd_vel_timeout: 0.5</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 08: Cơ Học Hamilton & Hệ Port-Hamiltonian Trong Robot
# ==============================================================================
ch08_sidebar = [
    {"id": "sec-8-1", "title": "8.1 Biến đổi Legendre & Động lượng Suy rộng"},
    {"id": "sec-8-2", "title": "8.2 Phương trình Chính tắc Hamilton"},
    {"id": "sec-8-3", "title": "8.3 Cấu trúc Port-Hamiltonian (PCHS)"},
    {"id": "sec-8-4", "title": "8.4 Bảo toàn Năng lượng & Tính Thụ động"},
    {"id": "sec-8-5", "title": "8.5 Điều khiển Gán Năng lượng IDA-PBC"},
    {"id": "sec-8-6", "title": "8.6 Ứng dụng Thao tác Từ xa (Telemanipulation)"},
    {"id": "sec-8-sim", "title": "⚡ Mô phỏng Điều Khiển IDA-PBC (Canvas)"},
    {"id": "sec-8-worked", "title": "📐 Ví dụ Tính Số 4 Bước Luật Điều Khiển IDA-PBC"},
    {"id": "sec-8-bridge", "title": "🛠️ Cầu nối Cartesian Impedance Controller"}
]

ch08_body = r"""
        <!-- 8.1 -->
        <h2 id="sec-8-1">8.1 Biến Đổi Legendre & Động Lượng Suy Rộng</h2>
        <p>Trong cơ học Lagrange, trạng thái hệ thống được mô tả bằng tọa độ và vận tốc $(q, \dot{q})$. Cơ học Hamilton chuyển không gian trạng thái từ $(q, \dot{q})$ sang cặp biến liên hợp <strong>tọa độ và động lượng suy rộng</strong> $(q, p)$ thông qua phép biến đổi Legendre:</p>
        <div class="formula-hero">
          <div class="formula-title">Định Nghĩa Động Lượng Suy Rộng & Biến Đổi Legendre</div>
          <div class="formula-math">
            $$p = \frac{\partial L}{\partial \dot{q}} = M(q)\dot{q} \implies \dot{q} = M^{-1}(q) p$$
            $$H(q, p) = p^T \dot{q} - L(q, \dot{q}) = \frac{1}{2} p^T M^{-1}(q) p + V(q)$$
          </div>
          <div class="formula-legend">
            <strong>Bản chất:</strong> Hàm Hamilton $H(q, p)$ chính là <strong>tổng cơ năng</strong> của hệ thống (Động năng + Thế năng).
          </div>
        </div>

        <!-- 8.2 -->
        <h2 id="sec-8-2">8.2 Phương Trình Vi Phân Chính Tắc Hamilton</h2>
        <p>Hệ phương trình vi phân cấp 2 Euler-Lagrange được chuyển thành hệ $2n$ phương trình vi phân cấp 1 đối xứng:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Chính Tắc Hamilton (Canonical Equations)</div>
          <div class="formula-math">
            $$\dot{q} = \frac{\partial H}{\partial p}, \quad \dot{p} = -\frac{\partial H}{\partial q} + \tau$$
          </div>
          <div class="formula-legend">
            <strong>Dạng ma trận symplectic:</strong> $\begin{bmatrix} \dot{q} \\ \dot{p} \end{bmatrix} = \begin{bmatrix} 0 & I \\ -I & 0 \end{bmatrix} \begin{bmatrix} \nabla_q H \\ \nabla_p H \end{bmatrix} + \begin{bmatrix} 0 \\ I \end{bmatrix} \tau$.
          </div>
        </div>

        <!-- 8.3 -->
        <h2 id="sec-8-3">8.3 Cấu Trúc Hệ Port-Controlled Hamiltonian Systems (PCHS)</h2>
        <p>Để mô hình hóa toàn diện các hệ thống robot có trao đổi năng lượng với môi trường ngoài (các cổng công suất port), dạng PCHS mở rộng được chuẩn hóa:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Port-Controlled Hamiltonian Chuẩn</div>
          <div class="formula-math">
            $$\dot{x} = \left[ J(x) - R(x) \right] \nabla H(x) + g(x) u, \quad y = g^T(x) \nabla H(x)$$
          </div>
          <div class="formula-legend">
            <strong>Tính chất ma trận cốt lõi:</strong>
            <br>• $J(x) = -J^T(x)$: Ma trận tương hỗ phản đối xứng (Interconnection Matrix), đại diện cho sự luân chuyển năng lượng nội tại không làm mất mát cơ năng.
            <br>• $R(x) = R^T(x) \ge 0$: Ma trận suy giảm xác định bán dương (Damping Matrix), đại diện cho tiêu tán năng lượng do ma sát hoặc điện trở.
          </div>
        </div>

        <!-- 8.4 -->
        <h2 id="sec-8-4">8.4 Định Lý Tiêu Tán Năng Lượng & Tính Thụ Động</h2>
        <p>Lấy đạo hàm thời gian của hàm năng lượng $H(x)$ dọc theo quỹ đạo nghiệm của PCHS:</p>
        $$\dot{H} = \nabla H^T \dot{x} = \nabla H^T \left[ J(x) - R(x) \right] \nabla H + \nabla H^T g(x) u$$
        <p>Vì $\nabla H^T J(x) \nabla H \equiv 0$ do tính phản đối xứng, ta có đẳng thức năng lượng sống còn:</p>
        $$\dot{H} = -\nabla H^T R(x) \nabla H + y^T u \le y^T u$$
        <p>Nếu không có năng lượng bơm từ bên ngoài ($u = 0$), cơ năng hệ thống luôn giảm dần theo thời gian: $\dot{H} \le 0$.</p>

        <!-- 8.5 -->
        <h2 id="sec-8-5">8.5 Phương Pháp Điều Khiển Gán Cấu Trúc & Giảm Chấn (IDA-PBC)</h2>
        <p>Thuật toán IDA-PBC (Interconnection and Damping Assignment Passivity-Based Control) thiết kế tín hiệu điều khiển $u$ sao cho hệ thống khép vòng biến thành một hệ Port-Hamiltonian mong muốn với hàm năng lượng mới $H_d(x)$ có cực tiểu toàn cục tại điểm cân bằng mong muốn $x^*$:</p>
        $$\dot{x} = \left[ J_d(x) - R_d(x) \right] \nabla H_d(x)$$

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-8-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng Suy Giảm Năng Lượng IDA-PBC Về Trạng Thái Bền</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-08" width="700" height="280" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Hệ số giảm chấn gán R_d: <input type="range" id="sim08-damping" min="0.5" max="5.0" step="0.5" value="1.5"> <span id="sim08-d-val">1.5</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-8-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Thiết Kế Bộ Điều Khiển IDA-PBC Cho Khớp Robot</h3>
          <p>Xét 1 khớp quay robot có phương trình Euler-Lagrange: $J \ddot{q} + B \dot{q} + m g l \sin q = u$. Đổi sang biến Hamilton $x = [q, p]^T$ với $p = J \dot{q}$. Yêu cầu thiết kế luật điều khiển IDA-PBC đưa khớp về vị trí mong muốn $q^* = \pi/3\text{ rad}$ ($60^\circ$) với độ cứng gán $K_p = 50\text{ N}\cdot\text{m/rad}$ và giảm chấn gán $R_d = 5.0\text{ N}\cdot\text{m}\cdot\text{s/rad}$. Cho $m g l = 10.0\text{ N}\cdot\text{m}$, $B = 0.5$, $J = 0.2\text{ kg}\cdot\text{m}^2$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Chọn hàm năng lượng mong muốn $H_d(q, p)$</h5>
              <p>Hàm năng lượng khép vòng có cực tiểu tại $(q^*, 0)$:</p>
              <p>$$H_d(q, p) = \frac{1}{2J} p^2 + \frac{1}{2} K_p (q - q^*)^2$$</p>
              <p>Gradient năng lượng: $\nabla_q H_d = K_p (q - q^*)$, $\nabla_p H_d = \frac{p}{J} = \dot{q}$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Ráp cấu trúc ma trận PCHS mục tiêu</h5>
              <p>Chọn ma trận tương hỗ và giảm chấn:</p>
              <p>$$J_d = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}, \quad R_d = \begin{bmatrix} 0 & 0 \\ 0 & R_a \end{bmatrix}$$</p>
              <p>$$\begin{bmatrix} \dot{q} \\ \dot{p} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -1 & -R_a \end{bmatrix} \begin{bmatrix} K_p (q - q^*) \\ \dot{q} \end{bmatrix} = \begin{bmatrix} \dot{q} \\ -K_p(q - q^*) - R_a \dot{q} \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Cân bằng phương trình tìm luật điều khiển $u$</h5>
              <p>Phương trình thực tế: $\dot{p} = -m g l \sin q - B \dot{q} + u$.</p>
              <p>Đồng nhất với phương trình mục tiêu:</p>
              <p>$$-m g l \sin q - B \dot{q} + u = -K_p (q - q^*) - R_a \dot{q}$$</p>
              <p>$$\implies u = m g l \sin q - K_p (q - q^*) - (R_a - B) \dot{q}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Thay số & Kiểm định ổn định Lyapunov</h5>
              <p>Với $R_a = R_d = 5.0$, số hạng giảm chấn thêm vào là $R_a - B = 5.0 - 0.5 = 4.5$.</p>
              <p>Luật điều khiển hoàn chỉnh:</p>
              <p>$$u = 10.0 \sin q - 50(q - \pi/3) - 4.5 \dot{q}$$</p>
              <p>Đạo hàm năng lượng khép vòng: $\dot{H}_d = -R_a \dot{q}^2 = -5.0 \dot{q}^2 \le 0$. Theo nguyên lý bất biến LaSalle, khớp hội tụ tiệm cận toàn cục về điểm $q^* = \pi/3$.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-8-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Cartesian Impedance Controller</h4>
          <p>Nguyên lý Port-Hamiltonian được hiện thực hóa trực tiếp trong bộ điều khiển trở kháng không gian làm việc (Cartesian Impedance) cho Cobot an toàn:</p>
          <div class="code-card">
            <div class="code-header">
              <span>cartesian_impedance_controller.cpp (Cobot / ROS 2)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>// Tính toán lực điều khiển trở kháng F_cmd = K_x * e_x + D_x * de_x
Eigen::Vector6d error;
error.head&lt;3&gt;() = x_desired - x_current;
error.tail&lt;3&gt;() = orientation_error(q_desired, q_current);

Eigen::Vector6d F_cartesian = K_matrix * error - D_matrix * v_current;
// Ánh xạ sang mô-men khớp thông qua chuyển vị Jacobian: tau = J^T * F
Eigen::VectorXd tau_impedance = J.transpose() * F_cartesian + gravity_compensation;</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 09: Dao Động Cơ Học, Dầm Đàn Hồi & Phân Tích Phần Tử Hữu Hạn
# ==============================================================================
ch09_sidebar = [
    {"id": "sec-9-1", "title": "9.1 Dao động Hệ Khối lượng Tập trung"},
    {"id": "sec-9-2", "title": "9.2 Phân tích Modal & Bài toán Trị riêng"},
    {"id": "sec-9-3", "title": "9.3 Phương trình Vi phân Dầm Euler-Bernoulli"},
    {"id": "sec-9-4", "title": "9.4 Phương pháp Galerkin với Hàm dạng Trực giao"},
    {"id": "sec-9-5", "title": "9.5 Phương pháp Phần tử Hữu hạn (FEM)"},
    {"id": "sec-9-6", "title": "9.6 Cánh tay Robot Linh hoạt Siêu nhẹ"},
    {"id": "sec-9-sim", "title": "⚡ Mô phỏng Dao Động Dầm Euler-Bernoulli (Canvas)"},
    {"id": "sec-9-worked", "title": "📐 Ví dụ Tính Số 4 Bước Tần Số Tự Nhiên Galerkin"},
    {"id": "sec-9-bridge", "title": "🛠️ Cầu nối Input Shaping Filter Rung Động"}
]

ch09_body = r"""
        <!-- 9.1 -->
        <h2 id="sec-9-1">9.1 Dao Động Cơ Học Hệ Nhiều Khối Lượng Tập Trung</h2>
        <p>Mô hình hóa kết cấu robot thực tế không thể bỏ qua tính đàn hồi của vật liệu. Phương trình vi phân dao động của hệ nhiều bậc tự do có ma trận khối lượng $M$, ma trận cản $D$ và ma trận độ cứng $K$:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Vi Phân Dao Động Tuyến Tính MDOF</div>
          <div class="formula-math">
            $$M \ddot{x}(t) + D \dot{x}(t) + K x(t) = F(t)$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách tham số:</strong> $M = M^T \gt 0$ (khối lượng); $D = D^T \ge 0$ (giảm chấn nhớt); $K = K^T \gt 0$ (độ cứng đàn hồi).
          </div>
        </div>

        <!-- 9.2 -->
        <h2 id="sec-9-2">9.2 Phân Tích Modal & Bài Toán Trị Riêng (Modal Analysis)</h2>
        <p>Xét dao động tự do không cản ($D=0, F=0$). Đặt nghiệm điều hòa $x(t) = \phi e^{j \omega t}$, phương trình đưa về bài toán trị riêng tổng quát:</p>
        $$(K - \omega^2 M) \phi = 0 \iff \det(K - \omega^2 M) = 0$$
        <p>Giải phương trình định thức ta thu được $n$ tần số dao động tự nhiên $\omega_1 \le \omega_2 \le \dots \le \omega_n$ và các vector dạng dao động riêng (eigenmodes) $\phi_i$ thỏa mãn tính chất trực giao:</p>
        $$\phi_i^T M \phi_j = \delta_{ij}, \quad \phi_i^T K \phi_j = \omega_i^2 \delta_{ij}$$

        <!-- 9.3 -->
        <h2 id="sec-9-3">9.3 Phương Trình Vi Phân Đạo Hàm Riêng (PDE) Dầm Euler-Bernoulli</h2>
        <p>Đối với thanh nối khâu robot thon dài có khối lượng và độ đàn hồi phân bố liên tục, độ võng uốn $w(x, t)$ tại vị trí $x$ và thời gian $t$ tuân theo phương trình đạo hàm riêng Euler-Bernoulli:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Đạo Hàm Riêng Dầm Đàn Hồi Liên Tục</div>
          <div class="formula-math">
            $$\rho A \frac{\partial^2 w(x, t)}{\partial t^2} + \frac{\partial^2}{\partial x^2}\left( EI \frac{\partial^2 w(x, t)}{\partial x^2} \right) = p(x, t)$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách tham số:</strong> $\rho$ là khối lượng riêng [kg/m$^3$]; $A$ là diện tích mặt cắt ngang [m$^2$]; $E$ là mô-đun đàn hồi Young [Pa]; $I$ là mô-men quán tính diện tích mặt cắt [m$^4$]; $p(x,t)$ là tải trọng phân bố ngoài.
          </div>
        </div>

        <!-- 9.4 -->
        <h2 id="sec-9-4">9.4 Phương Pháp Galerkin Với Hệ Hàm Dạng Trực Giao</h2>
        <p>Phương pháp tách biến và xấp xỉ Galerkin khai triển độ võng liên tục $w(x,t)$ thành tổng hữu hạn của các hàm dạng không gian $\psi_i(x)$ và tọa độ modal thời gian $\eta_i(t)$:</p>
        $$w(x, t) \approx \sum_{i=1}^m \psi_i(x) \eta_i(t)$$
        <p>với các hàm $\psi_i(x)$ thỏa mãn điều kiện biên hình học (như ngàm chặt ở gốc $x=0$: $\psi(0)=0, \psi'(0)=0$).</p>

        <!-- 9.5 -->
        <h2 id="sec-9-5">9.5 Phương Pháp Phần Tử Hữu Hạn (FEM) Rời Rạc Hóa Khâu Robot</h2>
        <p>Trong FEM, khâu robot được chia nhỏ thành các phần tử dầm bậc 3 (Hermite cubic beam elements). Mỗi phần tử có 2 nút và 4 bậc tự do (độ võng và góc xoay tại mỗi đầu nút), giúp xây dựng ma trận độ cứng $K_e$ và ma trận khối lượng $M_e$ cục bộ.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-9-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Mô Phỏng 3 Dạng Dao Động Dầm Mềm Euler-Bernoulli</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-09" width="700" height="280" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Chọn Mode dao động: 
              <select id="sim09-mode" style="padding: 0.25rem 0.75rem; border-radius: 4px; background: var(--card-bg); color: var(--text-color); border: 1px solid var(--border-color);">
                <option value="1">Mode 1: Uốn cơ bản (Cộng hưởng thấp)</option>
                <option value="2">Mode 2: Điểm nút thứ nhất (Uốn bậc 2)</option>
                <option value="3">Mode 3: Điểm nút kép (Tần số cao)</option>
              </select>
            </label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-9-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Tần Số Dao Động Uốn Bậc 1 Của Cánh Tay Robot Bằng Galerkin</h3>
          <p>Cánh tay robot làm bằng nhôm dài $L = 1.2\text{ m}$, tiết diện chữ nhật đặc rộng $b = 0.05\text{ m}$, dày $h = 0.01\text{ m}$. Khối lượng riêng nhôm $\rho = 2700\text{ kg/m}^3$, mô-đun Young $E = 7.0 \times 10^{10}\text{ Pa}$. Đầu gốc bị ngàm chặt vào trục động cơ, đầu ngọn tự do. Tính tần số dao động tự nhiên uốn bậc 1.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính diện tích và mô-men quán tính tiết diện</h5>
              <p>Diện tích mặt cắt ngang:</p>
              <p>$$A = b \cdot h = 0.05 \times 0.01 = 5.0 \times 10^{-4}\text{ m}^2$$</p>
              <p>Mô-men quán tính diện tích quanh trục uốn:</p>
              <p>$$I = \frac{b h^3}{12} = \frac{0.05 \times (0.01)^3}{12} = \frac{5.0 \times 10^{-8}}{12} \approx 4.167 \times 10^{-9}\text{ m}^4$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính độ cứng uốn $EI$ và khối lượng đơn vị dài $\mu$</h5>
              <p>Độ cứng uốn uốn dầm:</p>
              <p>$$EI = (7.0 \times 10^{10}) \times (4.167 \times 10^{-9}) = 291.67\text{ N}\cdot\text{m}^2$$</p>
              <p>Khối lượng trên một đơn vị chiều dài:</p>
              <p>$$\mu = \rho A = 2700 \times (5.0 \times 10^{-4}) = 1.35\text{ kg/m}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Nghiệm phương trình đặc trưng biên dầm ngàm - tự do</h5>
              <p>Với dầm ngàm một đầu và tự do một đầu (Clamped-Free), giá trị riêng nghiệm của phương trình $\cos(\beta L)\cosh(\beta L) = -1$ đối với Mode 1:</p>
              <p>$$\beta_1 L \approx 1.8751 \implies \beta_1 = \frac{1.8751}{1.2} \approx 1.5626\text{ m}^{-1}$$</p>
              <p>Tần số góc dao động tự nhiên bậc 1:</p>
              <p>$$\omega_1 = \beta_1^2 \sqrt{\frac{EI}{\mu}} = (1.5626)^2 \sqrt{\frac{291.67}{1.35}} = 2.4417 \times \sqrt{216.05} = 2.4417 \times 14.70 = 35.89\text{ rad/s}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Quy đổi sang Hertz & Khuyến nghị điều khiển</h5>
              <p>Tần số dao động tính theo đơn vị Hertz:</p>
              <p>$$f_1 = \frac{\omega_1}{2\pi} = \frac{35.89}{6.283} \approx 5.71\text{ Hz}$$</p>
              <p>Nhận xét kỹ thuật: Tần số rung uốn $5.71\text{ Hz}$ rất thấp. Khi robot chuyển động tăng tốc đột ngột, quán tính đầu gắp sẽ kích hoạt dao động biên độ lớn. Bắt buộc phải áp dụng bộ lọc Input Shaping ZVD (Zero Vibration and Derivative) để triệt rung.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-9-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Bộ Lọc Định Hình Xung Input Shaping ZVD Triệt Rung</h4>
          <p>Thuật toán Input Shaping tạo chuỗi xung trễ thời gian sao cho sóng phản xạ tự triệt tiêu lẫn nhau, loại bỏ 100% rung lắc tại tần số tự nhiên $f_1 = 5.71\text{ Hz}$:</p>
          <div class="code-card">
            <div class="code-header">
              <span>input_shaper.cpp (ROS 2 Trajectory Generation)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>// Thiết lập bộ lọc ZVD Shaper cho tần số fn = 5.71 Hz, hệ số cản zeta = 0.05
const double omega_d = 2.0 * M_PI * 5.71 * std::sqrt(1.0 - 0.05 * 0.05);
const double K = std::exp(-0.05 * M_PI / std::sqrt(1.0 - 0.05 * 0.05));
const double dt_shaper = M_PI / omega_d; // Thời gian trễ nửa chu kỳ dao động

// Biên độ 3 xung ZVD
const double A1 = 1.0 / std::pow(1.0 + K, 2);
const double A2 = 2.0 * K / std::pow(1.0 + K, 2);
const double A3 = std::pow(K, 2) / std::pow(1.0 + K, 2);

double filterTrajectory(double cmd, double t) {
  // Lọc xung tín hiệu đặt điều khiển góc khớp
  return A1 * cmd + A2 * delay_buffer(cmd, dt_shaper) + A3 * delay_buffer(cmd, 2.0 * dt_shaper);
}</code></pre>
          </div>
        </div>
"""

# Generate HTML files
print("Generating Ch 05...")
with open(os.path.join(CHAPTERS_DIR, "ch05.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("05", "Động Lực Học Newton-Euler & Thuật Toán Đệ Quy RNEA", "Newton-Euler Formulation & Recursive Algorithm", "TRACK 3: CƠ HỌC GIẢI TÍCH & ĐA VẬT", "track-3", "ch04.html", "Chương 04: Ma Sát Động LuGre", "ch06.html", "Chương 06: Cơ Học Lagrange", ch05_sidebar, ch05_body))

print("Generating Ch 06...")
with open(os.path.join(CHAPTERS_DIR, "ch06.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("06", "Cơ Học Lagrange & Động Lực Học Robot Cánh Tay", "Lagrangian Mechanics & Manipulator Dynamics", "TRACK 3: CƠ HỌC GIẢI TÍCH & ĐA VẬT", "track-3", "ch05.html", "Chương 05: Động Lực Học Newton-Euler", "ch07.html", "Chương 07: Động Lực Học Hệ Ràng Buộc", ch06_sidebar, ch06_body))

print("Generating Ch 07...")
with open(os.path.join(CHAPTERS_DIR, "ch07.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("07", "Động Lực Học Hệ Ràng Buộc & Phương Pháp Kane", "Constrained Multibody Dynamics & Kane's Formulation", "TRACK 3: CƠ HỌC GIẢI TÍCH & ĐA VẬT", "track-3", "ch06.html", "Chương 06: Cơ Học Lagrange", "ch08.html", "Chương 08: Cơ Học Hamilton", ch07_sidebar, ch07_body))

print("Generating Ch 08...")
with open(os.path.join(CHAPTERS_DIR, "ch08.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("08", "Cơ Học Hamilton & Hệ Port-Hamiltonian Trong Robot", "Hamiltonian Mechanics & Port-Based Robotics", "TRACK 3: CƠ HỌC GIẢI TÍCH & ĐA VẬT", "track-3", "ch07.html", "Chương 07: Động Lực Học Hệ Ràng Buộc", "ch09.html", "Chương 09: Dao Động Cơ Học", ch08_sidebar, ch08_body))

print("Generating Ch 09...")
with open(os.path.join(CHAPTERS_DIR, "ch09.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("09", "Dao Động Cơ Học, Dầm Đàn Hồi & Phân Tích Phần Tử Hữu Hạn", "Mechanical Vibrations, Flexible Beams & FEM", "TRACK 4: DAO ĐỘNG & TAY MÁY ĐÀN HỒI", "track-4", "ch08.html", "Chương 08: Cơ Học Hamilton", "ch10.html", "Chương 10: Tích Phân Số ODEs", ch09_sidebar, ch09_body))

print("Successfully generated Chapters 05, 06, 07, 08, 09!")
