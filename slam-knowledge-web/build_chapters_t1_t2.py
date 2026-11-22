# -*- coding: utf-8 -*-
"""
build_chapters_t1_t2.py
Biên soạn nội dung chuẩn 6 tầng tri thức cho Track 1 và Track 2 (Chương 01 - Chương 04):
- Ch 01: Động Học Robot Di Động & Tích Lũy Sai Số Đo Quãng Đường (Dead Reckoning)
- Ch 02: Mô Hình Đo Cảm Biến Cự Ly & Bản Đồ Lưới Chiếm Chỗ (Occupancy Grid Mapping)
- Ch 03: Bộ Lọc Bayes, Extended Kalman Filter (EKF) & Phân Tích Hiệp Phương Sai
- Ch 04: Bộ Lọc Hạt (Particle Filter), MCL & Khung FastSLAM
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
            <span>📚 Nguồn tài liệu: <strong>Mordechai Ben-Ari & Francesco Mondada (Elements of Robotics, Springer)</strong></span>
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
# CHƯƠNG 01: Động Học Robot Di Động & Tích Lũy Sai Số Đo Quãng Đường
# ==============================================================================
ch01_sidebar = [
    {"id": "sec-1-1", "title": "1.1 Động Học Xe Vi Sai & Mô Hình Unicycle"},
    {"id": "sec-1-2", "title": "1.2 Tích Phân Vận Tốc Sang Vị Trí (Runge-Kutta)"},
    {"id": "sec-1-3", "title": "1.3 Phân Tích Sai Số Hệ Thống & Ngẫu Nhiên"},
    {"id": "sec-1-4", "title": "1.4 Thử Nghiệm Chuẩn UMBmark"},
    {"id": "sec-1-sim", "title": "⚡ Mô Phỏng Trôi Lệch Dead Reckoning (Canvas)"},
    {"id": "sec-1-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Hiệp Phương Sai Sai Số"},
    {"id": "sec-1-bridge", "title": "🛠️ Cầu Nối ROS 2: Node Xuất Bản Odom & TF2"}
]

ch01_body = r"""
        <!-- 1.1 -->
        <h2 id="sec-1-1">1.1 Động Học Robot Di Động Vi Sai & Mô Hình Xe Một Bánh (Unicycle Model)</h2>
        <p>Hầu hết các robot di động trong nhà (như robot hút bụi, xe tự hành công nghiệp AMR) sử dụng cơ cấu dẫn động vi sai (Differential Drive) với hai bánh chủ động độc lập có bán kính $r$ cách nhau một khoảng cách trục $b$.</p>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 TẠI SAO CẦN HIỂU RÕ ĐO QUÃNG ĐƯỜNG (ODOMETRY)?</div>
          <div class="why-matters-body">
            Đo quãng đường bằng encoder bánh xe (Wheel Odometry) là nguồn dữ liệu thời gian thực có tần số cao nhất (50 - 100 Hz) trên robot. Tuy nhiên, odometry mang một điểm yếu chết người: <strong>Sai số tích lũy không giới hạn theo thời gian (Unbounded Drift)</strong>. Nếu không có các cảm biến mốc bên ngoài (LiDAR, Camera) trong hệ thống SLAM để hiệu chỉnh, chỉ sau vài chục mét di chuyển, robot sẽ hoàn toàn mất phương hướng và lao vào tường.
          </div>
        </div>

        <p>Vận tốc dài $v$ và vận tốc góc $\omega$ của khung thân robot được xác định từ tốc độ góc của bánh phải $\omega_R$ và bánh trái $\omega_L$:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Động Học Vi Sai Thuận</div>
          <div class="formula-math">
            $$\begin{bmatrix} v \\ \omega \end{bmatrix} = \begin{bmatrix} \frac{r}{2} & \frac{r}{2} \\ \frac{r}{b} & -\frac{r}{b} \end{bmatrix} \begin{bmatrix} \omega_R \\ \omega_L \end{bmatrix}$$
          </div>
          <div class="formula-legend">
            <strong>Ý nghĩa các đại lượng:</strong>
            <br>• $r$: Bán kính danh định của bánh xe dẫn động (m).
            <br>• $b$: Khoảng cách giữa hai điểm tiếp xúc của bánh xe với mặt sàn (Track gauge, m).
            <br>• $v$: Vận tốc tịnh tiến tức thời của trọng tâm robot (m/s).
            <br>• $\omega$: Vận tốc quay góc hướng thân robot quanh trục $z$ thẳng đứng (rad/s).
          </div>
        </div>

        <!-- 1.2 -->
        <h2 id="sec-1-2">1.2 Tích Phân Vận Tốc Sang Tọa Độ Không Gian Toàn Cục (Runge-Kutta)</h2>
        <p>Tư thế của robot trong mặt phẳng 2D được biểu diễn bởi vector trạng thái $\mathbf{x} = [x, y, \theta]^T \in \mathrm{SE}(2)$. Phương trình vi phân phi tuyến mô tả chuyển động:</p>
        $$\dot{x} = v \cos\theta, \quad \dot{y} = v \sin\theta, \quad \dot{\theta} = \omega$$
        <p>Trong một chu kỳ lấy mẫu nhỏ $\Delta t$, phương pháp tích phân bậc hai Runge-Kutta giúp xấp xỉ chính xác vị trí mới:</p>
        $$\theta_{k+1} = \theta_k + \omega_k \Delta t$$
        $$\Delta s = v_k \Delta t, \quad x_{k+1} = x_k + \Delta s \cos\left(\theta_k + \frac{\omega_k \Delta t}{2}\right), \quad y_{k+1} = y_k + \Delta s \sin\left(\theta_k + \frac{\omega_k \Delta t}{2}\right)$$

        <!-- 1.3 -->
        <h2 id="sec-1-3">1.3 Phân Tích Nguồn Gốc Sai Số: Sai Số Hệ Thống vs Sai Số Ngẫu Nhiên</h2>
        <p>Theo phân tích chuẩn mực của Borenstein & Feng, sai số đo quãng đường được chia làm 2 nhóm:</p>
        <table class="academic-table" style="width:100%; margin: 1.5rem 0; border-collapse: collapse;">
          <thead>
            <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
              <th style="padding: 0.75rem;">Đặc Tính</th>
              <th style="padding: 0.75rem;">Sai Số Hệ Thống (Systematic Errors)</th>
              <th style="padding: 0.75rem;">Sai Số Ngẫu Nhiên (Non-Systematic Errors)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Nguyên nhân</strong></td>
              <td style="padding: 0.75rem;">Bán kính bánh xe thực tế khác nhau ($r_R \neq r_L$), sai lệch khoảng cách trục $b$ so với thiết kế.</td>
              <td style="padding: 0.75rem;">Bánh xe bị trượt trên sàn trơn, sàn gồ ghề, va chạm nhẹ với vật cản.</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color);">
              <td style="padding: 0.75rem;"><strong>Quy luật tích lũy</strong></td>
              <td style="padding: 0.75rem;">Tích lũy đơn điệu theo hàm số xác định (khiến robot luôn bị quẹo về một bên dù đi thẳng).</td>
              <td style="padding: 0.75rem;">Dao động ngẫu nhiên, mô hình hóa bằng nhiễu trắng Gauss $\mathcal{N}(0, \mathbf{Q})$.</td>
            </tr>
            <tr>
              <td style="padding: 0.75rem;"><strong>Khả năng bù trừ</strong></td>
              <td style="padding: 0.75rem;">Có thể hiệu chuẩn (Calibration) bằng phương pháp UMBmark.</td>
              <td style="padding: 0.75rem;">Bắt buộc phải dùng bộ lọc trạng thái (EKF, Particle Filter) và cảm biến ngoài để triệt tiêu.</td>
            </tr>
          </tbody>
        </table>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-1-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Sự Trôi Lệch Sai Số Dead Reckoning Khi Chạy Hình Vuông</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-01" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <label style="font-size: 0.85rem; font-weight: 600;">Hệ số lệch bánh xe / trượt sàn: <input type="range" id="sim01-slip" min="0.0" max="0.15" step="0.01" value="0.05"> <span id="sim01-slip-val">Hệ số trượt/lệch bánh: 5%</span></label>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-1-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Lan Truyền Hiệp Phương Sai Sai Số Vị Trí Qua Ma Trận Jacobian</h3>
          <p>Một robot vi sai đang ở tư thế $x = 0$ m, $y = 0$ m, $\theta = 0^\circ$ ($0$ rad). Ma trận hiệp phương sai ban đầu $\mathbf{P}_0 = \mathbf{0}$. Robot nhận lệnh di chuyển thẳng một quãng đường $\Delta s = 1.0$ m với góc quay $\Delta \theta = 0.0$ rad. Sai số đo quãng đường của bánh xe có phương sai $\sigma_s^2 = 0.01\text{ m}^2$ và sai số góc quay có phương sai $\sigma_\theta^2 = 0.0025\text{ rad}^2$. Tính ma trận Jacobian của mô hình chuyển động và ma trận hiệp phương sai $\mathbf{P}_1$ sau bước di chuyển.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Thiết lập phương trình cập nhật trạng thái</h5>
              <p>$$\mathbf{x}_1 = \mathbf{f}(\mathbf{x}_0, \mathbf{u}) = \begin{bmatrix} x_0 + \Delta s \cos(\theta_0) \\ y_0 + \Delta s \sin(\theta_0) \\ \theta_0 + \Delta \theta \end{bmatrix}$$</p>
              <p>Thay số: $x_1 = 0 + 1.0 \cos(0) = 1.0$ m; $y_1 = 0 + 1.0 \sin(0) = 0.0$ m; $\theta_1 = 0.0$ rad.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính ma trận Jacobian theo điều khiển $\mathbf{G}_u = \frac{\partial \mathbf{f}}{\partial \mathbf{u}}$</h5>
              <p>Vector điều khiển $\mathbf{u} = [\Delta s, \Delta \theta]^T$:</p>
              <p>$$\mathbf{G}_u = \begin{bmatrix} \cos\theta_0 & 0 \\ \sin\theta_0 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} \cos(0) & 0 \\ \sin(0) & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{bmatrix}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Lập ma trận hiệp phương sai nhiễu điều khiển $\mathbf{M}$</h5>
              <p>$$\mathbf{M} = \begin{bmatrix} \sigma_s^2 & 0 \\ 0 & \sigma_\theta^2 \end{bmatrix} = \begin{bmatrix} 0.01 & 0 \\ 0 & 0.0025 \end{bmatrix}$$</p>
              <p>Ma trận lan truyền nhiễu: $\mathbf{Q} = \mathbf{G}_u \mathbf{M} \mathbf{G}_u^T$.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Tính ma trận hiệp phương sai mới $\mathbf{P}_1$</h5>
              <p>$$\mathbf{P}_1 = \mathbf{G}_u \mathbf{M} \mathbf{G}_u^T = \begin{bmatrix} 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0.01 & 0 \\ 0 & 0.0025 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0.01 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0.0025 \end{bmatrix}$$</p>
              <p>Độ không chắc chắn theo trục $x$ là $\sigma_x = \sqrt{0.01} = 0.1$ m, theo góc hướng là $\sigma_\theta = \sqrt{0.0025} = 0.05$ rad ($\approx 2.86^\circ$).</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-1-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Node Xuất Bản Odometry Chuẩn ROS 2 C++</h4>
          <p>Mã nguồn chuẩn tích hợp encoder xuất bản chủ đề `nav_msgs/msg/Odometry` và phát khung biến đổi `tf2` giữa `odom` $\to$ `base_link`:</p>
          <div class="code-card">
            <div class="code-header">
              <span>diffdrive_odometry_node.cpp (ROS 2 / C++)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>#include &lt;rclcpp/rclcpp.hpp&gt;
#include &lt;nav_msgs/msg/odometry.hpp&gt;
#include &lt;tf2_ros/transform_broadcaster.h&gt;
#include &lt;geometry_msgs/msg/transform_stamped.hpp&gt;
#include &lt;cmath&gt;

class DiffDriveOdometryNode : public rclcpp::Node {
public:
  DiffDriveOdometryNode() : Node("diffdrive_odometry_node"), x_(0.0), y_(0.0), th_(0.0) {
    odom_pub_ = this->create_publisher&lt;nav_msgs::msg::Odometry&gt;("/odom", 50);
    tf_broadcaster_ = std::make_unique&lt;tf2_ros::TransformBroadcaster&gt;(*this);
    last_time_ = this->now();
    timer_ = this->create_wall_timer(std::chrono::milliseconds(20), std::bind(&DiffDriveOdometryNode::update, this));
  }

private:
  void update() {
    auto current_time = this->now();
    double dt = (current_time - last_time_).seconds();
    last_time_ = current_time;

    double v = 0.5; // Giả lập vận tốc dài 0.5 m/s
    double w = 0.1; // Vận tốc góc 0.1 rad/s

    th_ += w * dt;
    x_ += v * std::cos(th_) * dt;
    y_ += v * std::sin(th_) * dt;

    // Phát TF2 Transform odom -> base_link
    geometry_msgs::msg::TransformStamped tf_msg;
    tf_msg.header.stamp = current_time;
    tf_msg.header.frame_id = "odom";
    tf_msg.child_frame_id = "base_link";
    tf_msg.transform.translation.x = x_;
    tf_msg.transform.translation.y = y_;
    tf_msg.transform.translation.z = 0.0;
    tf_msg.transform.rotation.z = std::sin(th_ / 2.0);
    tf_msg.transform.rotation.w = std::cos(th_ / 2.0);
    tf_broadcaster_->sendTransform(tf_msg);

    // Xuất bản bản tin Odometry
    nav_msgs::msg::Odometry odom;
    odom.header.stamp = current_time;
    odom.header.frame_id = "odom";
    odom.child_frame_id = "base_link";
    odom.pose.pose.position.x = x_;
    odom.pose.pose.position.y = y_;
    odom.pose.pose.orientation = tf_msg.transform.rotation;
    odom_pub_->publish(odom);
  }
  double x_, y_, th_;
  rclcpp::Time last_time_;
  rclcpp::Publisher&lt;nav_msgs::msg::Odometry&gt;::SharedPtr odom_pub_;
  std::unique_ptr&lt;tf2_ros::TransformBroadcaster&gt; tf_broadcaster_;
  rclcpp::TimerBase::SharedPtr timer_;
};</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 02: Mô Hình Đo Cảm Biến Cự Ly & Bản Đồ Lưới Chiếm Chỗ
# ==============================================================================
ch02_sidebar = [
    {"id": "sec-2-1", "title": "2.1 Các Loại Cảm Biến Cự Ly & Đặc Tính Đo"},
    {"id": "sec-2-2", "title": "2.2 Mô Hình Cảm Biến Nghịch Đảo (Inverse Sensor Model)"},
    {"id": "sec-2-3", "title": "2.3 Biểu Diễn Log-Odds Của Bản Đồ Chiếm Chỗ"},
    {"id": "sec-2-4", "title": "2.4 Thuật Toán Raycasting Bresenham"},
    {"id": "sec-2-sim", "title": "⚡ Mô Phỏng Lập Bản Đồ Log-Odds (Canvas)"},
    {"id": "sec-2-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Cập Nhật Ô Lưới Chiếm Chỗ"},
    {"id": "sec-2-bridge", "title": "🛠️ Cầu Nối ROS 2: Node Tạo Occupancy Grid Từ LaserScan"}
]

ch02_body = r"""
        <!-- 2.1 -->
        <h2 id="sec-2-1">2.1 Các Loại Cảm Biến Đo Khoảng Cách & Đặc Tính Kỹ Thuật</h2>
        <p>Bản đồ môi trường được xây dựng từ các quan sát cự ly đo được từ robot tới chướng ngại vật xung quanh:</p>
        <ul>
          <li><strong>LiDAR 2D/3D (Laser Scanner):</strong> Phát chùm tia laser và đo thời gian bay (Time of Flight - ToF). Độ chính xác cực cao ($\pm 1 - 2$ cm), tầm quét rộng ($360^\circ$, tầm xa $12 - 30$ m), đóng vai trò xương sống của SLAM 2D.</li>
          <li><strong>Cảm biến siêu âm (Sonar):</strong> Đo thời gian phản hồi của sóng âm. Búp sóng mở rộng ($15^\circ - 30^\circ$) gây hiện tượng phản xạ gương (Specular reflection), độ phân giải góc thấp.</li>
          <li><strong>Cảm biến quang học hồng ngoại (IR Triangulation):</strong> Sử dụng nguyên lý tam giác quang học. Rẻ tiền, tầm quét ngắn ($0.1 - 1.5$ m), nhạy cảm với ánh sáng mặt trời.</li>
        </ul>

        <!-- 2.2 -->
        <h2 id="sec-2-2">2.2 Mô Hình Cảm Biến Nghịch Đảo (Inverse Measurement Model)</h2>
        <p>Mô hình cảm biến thuận tính xác suất đo được $z$ khi biết trước bản đồ $p(z \mid m, x)$. Nhưng khi lập bản đồ, ta cần tính điều ngược lại: <em>"Biết vị trí robot $x$ và giá trị cảm biến đo được $z$, xác suất ô lưới $m_i$ bị chiếm chỗ là bao nhiêu?"</em></p>

        <!-- 2.3 -->
        <h2 id="sec-2-3">2.3 Biểu Diễn Log-Odds Của Bản Đồ Chiếm Chỗ (Occupancy Grid Mapping)</h2>
        <p>Không gian được chia thành một mạng lưới 2D gồm các ô vuông độc lập $m_i \in \{0, 1\}$ (0: Free, 1: Occupied). Để tránh việc nhân liên tiếp các số xác suất nhỏ gây tràn số dưới (Underflow), Moravec và Elfes đưa ra dạng biểu diễn <strong>Tỷ số chẵn lẻ Log-Odds</strong>:</p>
        <div class="formula-hero">
          <div class="formula-title">Phương Trình Cập Nhật Lưới Chiếm Chỗ Dạng Log-Odds</div>
          <div class="formula-math">
            $$l_t(m_i) = l_{t-1}(m_i) + \text{inv\_sensor}(m_i, x_t, z_t) - l_0$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách công thức:</strong>
            <br>• $l_t(m_i) = \ln \frac{p(m_i \mid z_{1:t})}{1 - p(m_i \mid z_{1:t})}$: Tỷ số Log-Odds tại thời điểm $t$.
            <br>• $l_0 = \ln \frac{p(m_i)}{1 - p(m_i)}$: Tiền nghiệm ban đầu (khi chưa có thông tin $p(m_i) = 0.5 \Rightarrow l_0 = \ln(1) = 0$).
            <br>• $\text{inv\_sensor}(m_i, x_t, z_t)$: Trả về giá trị dương ($l_{\text{occ}} \gt 0$) nếu tia laser dừng tại ô đó, và trả về giá trị âm ($l_{\text{free}} \lt 0$) nếu tia laser xuyên qua ô đó.
          </div>
        </div>

        <p>Chuyển đổi ngược lại từ Log-Odds $l$ sang xác suất phần trăm $p(m_i) \in [0, 1]$:</p>
        $$p(m_i) = 1 - \frac{1}{1 + \exp(l_t(m_i))}$$

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-2-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Lập Bản Đồ Bằng Tia Quét Laser Bresenham & Log-Odds</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-02" width="700" height="320" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-2-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Cập Nhật Xác Suất Ô Lưới Chiếm Chỗ Qua 3 Lần Quét LiDAR</h3>
          <p>Xét một ô lưới $m_i$ ban đầu chưa biết ($p_0 = 0.5 \Rightarrow l_0 = 0$). Cảm biến có tham số đo: khi tia xuyên qua trả về $l_{\text{free}} = -0.7$ ($p = 0.33$), khi tia chạm chướng ngại vật trả về $l_{\text{occ}} = +1.2$ ($p = 0.77$). Qua 3 lần robot quét cự ly liên tiếp:
          <br>• Lần 1: Tia xuyên qua ô lưới.
          <br>• Lần 2: Tia tiếp tục xuyên qua ô lưới.
          <br>• Lần 3: Tia chạm và kết thúc tại ô lưới.
          Tính giá trị Log-Odds tích lũy $l_1, l_2, l_3$ và xác suất chiếm chỗ $p_3(m_i)$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Cập nhật sau lần quét 1 (Tia xuyên qua)</h5>
              <p>$$l_1 = l_0 + l_{\text{free}} - l_0 = 0 + (-0.7) - 0 = -0.7$$</p>
              <p>Xác suất: $p_1 = 1 - \frac{1}{1 + e^{-0.7}} = 1 - \frac{1}{1 + 0.4966} = 1 - 0.6682 = 0.3318$ ($33.18\%$).</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Cập nhật sau lần quét 2 (Tia tiếp tục xuyên qua)</h5>
              <p>$$l_2 = l_1 + l_{\text{free}} - l_0 = -0.7 + (-0.7) - 0 = -1.4$$</p>
              <p>Xác suất: $p_2 = 1 - \frac{1}{1 + e^{-1.4}} = 1 - \frac{1}{1 + 0.2466} \approx 0.1978$ ($19.78\%$).</p>
              <p>Độ tin cậy ô trống tăng lên vững chắc.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Cập nhật sau lần quét 3 (Tia chạm chướng ngại vật)</h5>
              <p>$$l_3 = l_2 + l_{\text{occ}} - l_0 = -1.4 + (+1.2) - 0 = -0.2$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Tính xác suất cuối cùng $p_3$ & Nhận định</h5>
              <p>$$p_3 = 1 - \frac{1}{1 + e^{-0.2}} = 1 - \frac{1}{1 + 0.8187} = 1 - 0.5498 = 0.4502\text{ (45.02\%) }$$</p>
              <p>Nhận xét: Mặc dù lần 3 phát hiện vật cản, nhưng do 2 lần trước đã xác nhận ô trống nên xác suất chỉ tăng lên $45\%$, bảo vệ bản đồ khỏi các tia quét sai số ngẫu nhiên tức thời!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-2-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Cấu Trúc Bản Đồ OccupancyGrid Trong ROS 2</h4>
          <p>Đoạn mã Python xuất bản mảng 2D biểu diễn bản đồ chướng ngại vật `nav_msgs/msg/OccupancyGrid`:</p>
          <div class="code-card">
            <div class="code-header">
              <span>occupancy_grid_publisher.py (ROS 2 / Python)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
import numpy as np

class MapPublisher(Node):
    def __init__(self):
        super().__init__('occupancy_grid_publisher')
        self.pub_map = self.create_publisher(OccupancyGrid, '/map', 1)
        self.timer = self.create_timer(1.0, self.publish_map)
        self.width = 100
        self.height = 100
        self.resolution = 0.05 # 5 cm / ô

    def publish_map(self):
        grid = OccupancyGrid()
        grid.header.stamp = self.get_clock().now().to_msg()
        grid.header.frame_id = "map"
        grid.info.resolution = self.resolution
        grid.info.width = self.width
        grid.info.height = self.height
        grid.info.origin.position.x = -2.5
        grid.info.origin.position.y = -2.5

        # Dữ liệu bản đồ: 0 (Free), 100 (Occupied), -1 (Unknown)
        data = np.zeros((self.height, self.width), dtype=np.int8)
        data[0, :] = 100 # Bức tường trên
        data[-1, :] = 100 # Bức tường dưới
        data[:, 0] = 100 # Bức tường trái
        data[:, -1] = 100 # Bức tường phải

        grid.data = data.flatten().tolist()
        self.pub_map.publish(grid)</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 03: Bộ Lọc Bayes, Extended Kalman Filter (EKF) & Phân Tích Hiệp Phương Sai
# ==============================================================================
ch03_sidebar = [
    {"id": "sec-3-1", "title": "3.1 Khung Lọc Bayes Đệ Quy Tổng Quát"},
    {"id": "sec-3-2", "title": "3.2 Tuyến Tính Hóa Taylor & Extended Kalman Filter (EKF)"},
    {"id": "sec-3-3", "title": "3.3 Phân Tích Ma Trận Hiệp Phương Sai P_t & Elip Tin Cậy"},
    {"id": "sec-3-4", "title": "3.4 EKF-SLAM Ước Lượng Đồng Thời Robot & Mốc"},
    {"id": "sec-3-sim", "title": "⚡ Mô Phỏng Elip Tin Cậy EKF Localization (Canvas)"},
    {"id": "sec-3-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Cập Nhật Kalman Gain K"},
    {"id": "sec-3-bridge", "title": "🛠️ Cầu Nối ROS 2: Tích Hợp Robot Localization EKF YAML"}
]

ch03_body = r"""
        <!-- 3.1 -->
        <h2 id="sec-3-1">3.1 Khung Lọc Bayes Đệ Quy Tổng Quát Trong Định Vị Robot</h2>
        <p>Ước lượng trạng thái trong robot học được mô hình hóa qua hai phương trình phân phối xác suất:</p>
        <p>1. <strong>Mô hình chuyển động (Motion Model):</strong> $p(x_t \mid x_{t-1}, u_t)$</p>
        <p>2. <strong>Mô hình đo lường (Measurement Model):</strong> $p(z_t \mid x_t)$</p>

        <!-- 3.2 -->
        <h2 id="sec-3-2">3.2 Extended Kalman Filter (EKF) Cho Các Hệ Thống Phi Tuyến</h2>
        <p>Trong thực tế, cả chuyển động của robot vi sai và phép đo khoảng cách/góc quay tới mốc chuẩn đều là hàm phi tuyến:</p>
        $$\mathbf{x}_t = \mathbf{f}(\mathbf{x}_{t-1}, \mathbf{u}_t) + \mathbf{w}_t, \quad \mathbf{w}_t \sim \mathcal{N}(0, \mathbf{Q}_t)$$
        $$\mathbf{z}_t = \mathbf{h}(\mathbf{x}_t) + \mathbf{v}_t, \quad \mathbf{v}_t \sim \mathcal{N}(0, \mathbf{R}_t)$$
        <p>Thuật toán EKF xấp xỉ tuyến tính hóa bậc nhất chuỗi Taylor quanh điểm kỳ vọng hiện tại qua hai ma trận Jacobian:</p>
        $$\mathbf{F}_t = \left. \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right|_{\hat{\mathbf{x}}_{t-1}, \mathbf{u}_t}, \quad \mathbf{H}_t = \left. \frac{\partial \mathbf{h}}{\partial \mathbf{x}} \right|_{\hat{\mathbf{x}}_t^-}$$

        <div class="formula-hero">
          <div class="formula-title">Chu Trình Hai Giai Đoạn Của Bộ Lọc EKF</div>
          <div class="formula-math">
            $$\begin{aligned}
              \text{1. Dự báo: } & \hat{\mathbf{x}}_t^- = \mathbf{f}(\hat{\mathbf{x}}_{t-1}, \mathbf{u}_t), \quad \mathbf{P}_t^- = \mathbf{F}_t \mathbf{P}_{t-1} \mathbf{F}_t^T + \mathbf{Q}_t \\
              \text{2. Hiệu chỉnh: } & \mathbf{K}_t = \mathbf{P}_t^- \mathbf{H}_t^T (\mathbf{H}_t \mathbf{P}_t^- \mathbf{H}_t^T + \mathbf{R}_t)^{-1} \\
              & \hat{\mathbf{x}}_t = \hat{\mathbf{x}}_t^- + \mathbf{K}_t (\mathbf{z}_t - \mathbf{h}(\hat{\mathbf{x}}_t^-)), \quad \mathbf{P}_t = (\mathbf{I} - \mathbf{K}_t \mathbf{H}_t) \mathbf{P}_t^-
            \end{aligned}$$
          </div>
          <div class="formula-legend">
            <strong>Bóc tách thành phần:</strong>
            <br>• $\mathbf{P}_t$: Ma trận hiệp phương sai sai số kích thước $n \times n$.
            <br>• $\mathbf{K}_t$: Ma trận độ lợi Kalman (Kalman Gain) điều tiết mức độ tin cậy giữa dự báo mô hình chuyển động và số đo cảm biến.
            <br>• $(\mathbf{z}_t - \mathbf{h}(\hat{\mathbf{x}}_t^-))$: Phần dư đổi mới (Innovation / Residual).
          </div>
        </div>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-3-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Elip Tin Cậy Hiệp Phương Sai EKF Co Giãn Khi Đo Mốc Chuẩn</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-03" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-3-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Toán Kalman Gain $\mathbf{K}$ & Cập Nhật Tọa Độ Robot 1D</h3>
          <p>Xét robot chuyển động trên trục $x$. Dự báo vị trí hiện tại $\hat{x}^- = 10.0$ m với phương sai $P^- = 4.0\text{ m}^2$ (độ bất định cao). Cảm biến cự ly đo được khoảng cách tới gốc tọa độ là $z = 11.2$ m với phương sai nhiễu đo $R = 1.0\text{ m}^2$. Ma trận đo $H = 1.0$. Tính độ lợi Kalman $K$, phần dư đổi mới, vị trí hiệu chỉnh $\hat{x}$, và phương sai cập nhật $P$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính toán Kalman Gain $K$</h5>
              <p>$$K = \frac{P^- H^T}{H P^- H^T + R} = \frac{4.0 \times 1.0}{(1.0 \times 4.0 \times 1.0) + 1.0} = \frac{4.0}{5.0} = 0.80$$</p>
              <p>Kalman Gain đạt $0.80$ (gần $1.0$), thể hiện hệ thống sẽ tin tưởng phần lớn vào số đo cảm biến chính xác.</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Tính phần dư đổi mới (Innovation)</h5>
              <p>$$\nu = z - H \hat{x}^- = 11.2 - (1.0 \times 10.0) = +1.2\text{ m}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Hiệu chỉnh vị trí ước lượng $\hat{x}$</h5>
              <p>$$\hat{x} = \hat{x}^- + K \nu = 10.0 + 0.80 \times (+1.2) = 10.0 + 0.96 = 10.96\text{ m}$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Cập nhật phương sai sai số $P$</h5>
              <p>$$P = (1 - K H) P^- = (1 - 0.80 \times 1.0) \times 4.0 = 0.20 \times 4.0 = 0.80\text{ m}^2$$</p>
              <p>Độ lệch chuẩn sai số giảm mạnh từ $\sigma = \sqrt{4.0} = 2.0$ m xuống còn $\sigma = \sqrt{0.8} \approx 0.89$ m!</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-3-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Cấu Hình Chuẩn Robot Localization EKF Trong ROS 2</h4>
          <p>Tệp cấu hình YAML chuẩn tích hợp Odometry và IMU cho gói `robot_localization`:</p>
          <div class="code-card">
            <div class="code-header">
              <span>ekf_localization.yaml (ROS 2)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>ekf_filter_node:
  ros__parameters:
    frequency: 30.0
    sensor_timeout: 0.1
    two_d_mode: true
    publish_tf: true
    map_frame: map
    odom_frame: odom
    base_link_frame: base_link
    world_frame: odom

    # Nguồn 1: Wheel Odometry
    odom0: /odom
    odom0_config: [true,  true,  false,
                   false, false, true,
                   true,  false, false,
                   false, false, true,
                   false, false, false]

    # Nguồn 2: IMU
    imu0: /imu/data
    imu0_config: [false, false, false,
                  false, false, true,
                  false, false, false,
                  false, false, true,
                  true,  false, false]</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# CHƯƠNG 04: Bộ Lọc Hạt (Particle Filter), MCL & Khung FastSLAM
# ==============================================================================
ch04_sidebar = [
    {"id": "sec-4-1", "title": "4.1 Giới Hạn Của Phân Phối Đơn Mốt & Kidnapped Robot"},
    {"id": "sec-4-2", "title": "4.2 Nguyên Lý Lấy Mẫu Quan Trọng (Importance Sampling)"},
    {"id": "sec-4-3", "title": "4.3 Thuật Toán Tái Lấy Mẫu Phương Sai Thấp (Low-Variance)"},
    {"id": "sec-4-4", "title": "4.4 Phân Rã Rao-Blackwellized & Khung FastSLAM 1.0/2.0"},
    {"id": "sec-4-sim", "title": "⚡ Mô Phỏng Định Vị Hạt Monte Carlo MCL (Canvas)"},
    {"id": "sec-4-worked", "title": "📐 Ví Dụ Tính Số 4 Bước Cập Nhật Trọng Số Hạt"},
    {"id": "sec-4-bridge", "title": "🛠️ Cầu Nối ROS 2: Thuật Toán Low-Variance Resampler Bằng Python"}
]

ch04_body = r"""
        <!-- 4.1 -->
        <h2 id="sec-4-1">4.1 Giới Hạn Của Phân Phối Đơn Mốt & Sự Cần Thiết Của Định Vị Monte Carlo (MCL)</h2>
        <p>Bộ lọc Kalman (EKF) xuất sắc khi robot đã biết xấp xỉ vị trí của mình và nhiễu tuân theo phân phối chuẩn đơn mốt (Unimodal Gaussian). Tuy nhiên, trong các tình huống thực tế:</p>
        <ul>
          <li><strong>Môi trường đối xứng đa mốt:</strong> Robot đứng trong một hành lang có 4 cửa giống hệt nhau, phân phối niềm tin có 4 đỉnh xác suất bằng nhau. EKF lấy trung bình cộng của 4 đỉnh sẽ dẫn đến vị trí vô lý ở giữa tường!</li>
          <li><strong>Bài toán bắt cóc robot (Kidnapped Robot Problem):</strong> Robot bị nhấc bổng đặt sang vị trí mới mà encoder không ghi nhận. EKF hoàn toàn bất lực và sụp đổ vì nghiệm nằm ngoài elip tin cậy.</li>
        </ul>

        <div class="why-matters-box">
          <div class="why-matters-header">💡 BỘ LỌC HẠT (PARTICLE FILTER) GIẢI QUYẾT BÀI TOÁN NHƯ THẾ NÀO?</div>
          <div class="why-matters-body">
            Định vị Monte Carlo (MCL) sử dụng tập hợp $N$ mẫu giả thuyết ngẫu nhiên (gọi là các hạt - Particles) $S_t = \{ \langle x_t^{[i]}, w_t^{[i]} \rangle \}_{i=1}^N$ để xấp xỉ phân phối xác suất tùy ý (Non-Gaussian, Multimodal). Các hạt tự động phân tán bao phủ toàn bộ không gian khi mất phương hướng, và nhanh chóng cô đọng hội tụ thành cụm duy nhất khi nhận được các quan sát đo khoảng cách đặc trưng.
          </div>
        </div>

        <!-- 4.2 -->
        <h2 id="sec-4-2">4.2 Nguyên Lý Lấy Mẫu Quan Trọng & Tái Lấy Mẫu Phương Sai Thấp (Low-Variance Resampling)</h2>
        <p>Ba bước lặp của bộ lọc hạt:</p>
        <p>1. <strong>Dự báo:</strong> Mỗi hạt được truyền qua mô hình chuyển động ngẫu nhiên $x_t^{[i]} \sim p(x_t \mid x_{t-1}^{[i]}, u_t)$.</p>
        <p>2. <strong>Cập nhật trọng số:</strong> Đánh giá xác suất của số đo thực tế $z_t$ theo vị trí giả định của hạt: $w_t^{[i]} = p(z_t \mid x_t^{[i]})$.</p>
        <p>3. <strong>Tái lấy mẫu (Resampling):</strong> Loại bỏ các hạt có trọng số thấp và nhân bản các hạt có trọng số cao.</p>

        <!-- 4.3 -->
        <h2 id="sec-4-3">4.3 Phân Rã Rao-Blackwellized & Khung Thuật Toán FastSLAM</h2>
        <p>Trong bài toán SLAM đầy đủ (vừa ước lượng quỹ đạo robot vừa ước lượng hàng ngàn tọa độ mốc $m$), không gian trạng thái bùng nổ lên hàng ngàn chiều khiến Particle Filter thông thường bị "cạn kiệt hạt" (Curse of dimensionality). <strong>FastSLAM (Montemerlo & Thrun, 2002)</strong> đưa ra phân tích toán học then chốt:</p>
        $$p(x_{1:t}, m \mid z_{1:t}, u_{1:t}) = p(x_{1:t} \mid z_{1:t}, u_{1:t}) \prod_{j=1}^M p(m_j \mid x_{1:t}, z_{1:t})$$
        <p><em>Nếu biết trước quỹ đạo robot $x_{1:t}$, vị trí của các mốc $m_j$ trở nên độc lập có điều kiện với nhau!</em> Nhờ đó, FastSLAM dùng Particle Filter cho quỹ đạo robot, và gắn kèm theo mỗi hạt là $M$ bộ lọc EKF độc lập kích thước $2 \times 2$ cho từng mốc, giảm độ phức tạp tính toán từ $O(M^2)$ xuống chỉ còn $O(N \log M)$.</p>

        <!-- SIMULATOR -->
        <div class="sim-card" id="sec-4-sim">
          <div class="sim-header">
            <span class="sim-badge">CANVAS 2D 60 FPS</span>
            <span class="sim-title">Khảo Sát Tương Tác: Định Vị Monte Carlo (MCL) & Giải Quyết Bài Toán Bắt Cóc Robot</span>
          </div>
          <div class="sim-canvas-wrapper" style="text-align: center; padding: 1rem; background: var(--sim-bg);">
            <canvas id="sim-canvas-04" width="700" height="300" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--sim-border);"></canvas>
          </div>
          <div class="sim-controls" style="padding: 1rem; display: flex; gap: 1.5rem; flex-wrap: wrap; background: var(--sim-control-bg); border-top: 1px solid var(--border-color);">
            <button id="sim04-kidnap-btn" style="padding: 0.5rem 1rem; background: #ef4444; color: #fff; font-weight: bold; border: none; border-radius: 6px; cursor: pointer;">🚨 Bắt Cóc Robot (Kidnap Robot)</button>
          </div>
        </div>

        <!-- 4-STEP WORKED EXAMPLE -->
        <div class="worked-step-card" id="sec-4-worked" style="margin-top: 2.5rem;">
          <h3 style="margin-top: 0; color: var(--primary);">📐 Ví Dụ Tính Số 4 Bước: Tính Trọng Số Hạt & Số Lượng Hạt Hiệu Quả $N_{\text{eff}}$</h3>
          <p>Có 3 hạt giả thuyết vị trí: $x^{[1]} = 2.1$ m, $x^{[2]} = 2.9$ m, $x^{[3]} = 4.0$ m. Cảm biến laser đo được khoảng cách tới tường là $z = 3.0$ m với phương sai $\sigma^2 = 0.5\text{ m}^2$. Hàm khả năng đo chuẩn Gauss $p(z \mid x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{(z - x)^2}{2\sigma^2}\right)$. Tính trọng số chưa chuẩn hóa, chuẩn hóa trọng số $\tilde{w}^{[i]}$, và tính số lượng hạt hiệu quả $N_{\text{eff}}$.</p>

          <div class="worked-step-grid">
            <div class="worked-step-card">
              <h5>Bước 1: Tính trọng số chưa chuẩn hóa của từng hạt</h5>
              <p>Hệ số chuẩn hóa: $\frac{1}{\sqrt{2\pi \times 0.5}} = \frac{1}{\sqrt{3.1416}} \approx 0.5642$. Mẫu số số mũ: $2\sigma^2 = 1.0$.</p>
              <p>• Hạt 1: $|3.0 - 2.1| = 0.9 \Rightarrow w^{[1]} = 0.5642 \times e^{-(0.9)^2 / 1.0} = 0.5642 \times e^{-0.81} \approx 0.2510$</p>
              <p>• Hạt 2: $|3.0 - 2.9| = 0.1 \Rightarrow w^{[2]} = 0.5642 \times e^{-(0.1)^2 / 1.0} = 0.5642 \times e^{-0.01} \approx 0.5586$</p>
              <p>• Hạt 3: $|3.0 - 4.0| = 1.0 \Rightarrow w^{[3]} = 0.5642 \times e^{-(1.0)^2 / 1.0} = 0.5642 \times e^{-1.0} \approx 0.2076$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 2: Chuẩn hóa tổng trọng số về 1.0</h5>
              <p>Tổng: $W_{\text{sum}} = 0.2510 + 0.5586 + 0.2076 = 1.0172$</p>
              <p>• $\tilde{w}^{[1]} = \frac{0.2510}{1.0172} \approx 0.2468$ ($24.68\%$)</p>
              <p>• $\tilde{w}^{[2]} = \frac{0.5586}{1.0172} \approx 0.5491$ ($54.91\%$ - Hạt sát số đo nhất)</p>
              <p>• $\tilde{w}^{[3]} = \frac{0.2076}{1.0172} \approx 0.2041$ ($20.41\%$)</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 3: Tính số lượng hạt hiệu quả $N_{\text{eff}}$</h5>
              <p>$$N_{\text{eff}} = \frac{1}{\sum_{i=1}^3 (\tilde{w}^{[i]})^2}$$</p>
              <p>• $(0.2468)^2 = 0.0609$</p>
              <p>• $(0.5491)^2 = 0.3015$</p>
              <p>• $(0.2041)^2 = 0.0417$</p>
              <p>Tổng bình phương: $0.0609 + 0.3015 + 0.0417 = 0.4041$</p>
              <p>$$N_{\text{eff}} = \frac{1}{0.4041} \approx 2.47$$</p>
            </div>
            <div class="worked-step-card">
              <h5>Bước 4: Đánh giá điều kiện tái lấy mẫu (Resampling Threshold)</h5>
              <p>Do $N_{\text{eff}} = 2.47 \gt \frac{N}{2} = 1.5$, quần thể hạt vẫn giữ được độ đa dạng tốt, chưa bị hiện tượng cạn kiệt hạt (Particle Depletion). Thuật toán có thể trì hoãn bước tái lấy mẫu sang chu kỳ sau.</p>
            </div>
          </div>
        </div>

        <!-- ROS 2 BRIDGE -->
        <div class="ros2-bridge-card" id="sec-4-bridge" style="margin-top: 2.5rem;">
          <h4>🛠️ Cầu Nối Kiến Trúc Kỹ Thuật: Thuật Toán Low-Variance Resampling Bằng Python</h4>
          <p>Mã nguồn chuẩn triển khai giải thuật tái lấy mẫu phương sai thấp độ phức tạp $O(N)$:</p>
          <div class="code-card">
            <div class="code-header">
              <span>low_variance_resampler.py (Python)</span>
              <button class="copy-btn">Copy</button>
            </div>
            <pre><code>import numpy as np

def low_variance_resampling(particles, weights):
    # particles: danh sách N tư thế
    # weights: mảng trọng số đã chuẩn hóa
    N = len(particles)
    new_particles = []
    r = np.random.uniform(0, 1.0 / N)
    c = weights[0]
    i = 0
    
    for m in range(N):
        u = r + m * (1.0 / N)
        while u \gt c:
            i += 1
            c += weights[i]
        new_particles.append(particles[i])
        
    return new_particles</code></pre>
          </div>
        </div>
"""

# ==============================================================================
# Generate HTML files for Track 1 and Track 2
# ==============================================================================
print("Generating Ch 01...")
with open(os.path.join(CHAPTERS_DIR, "ch01.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("01", "Động Học Robot Di Động & Tích Lũy Sai Số Đo Quãng Đường", "Differential Drive Kinematics & Dead Reckoning Error Accumulation", "TRACK 1: NỀN TẢNG ĐỘNG HỌC & CẢM BIẾN", "track-1", "../index.html", "Lộ trình Tổng quan", "ch02.html", "Chương 02: Mô Hình Cảm Biến & Occupancy Grid", ch01_sidebar, ch01_body))

print("Generating Ch 02...")
with open(os.path.join(CHAPTERS_DIR, "ch02.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("02", "Mô Hình Đo Cảm Biến Cự Ly & Bản Đồ Lưới Chiếm Chỗ", "Range Sensors & Log-Odds Occupancy Grid Mapping", "TRACK 1: NỀN TẢNG ĐỘNG HỌC & CẢM BIẾN", "track-1", "ch01.html", "Chương 01: Động Học & Dead Reckoning", "ch03.html", "Chương 03: Bộ Lọc Bayes & EKF", ch02_sidebar, ch02_body))

print("Generating Ch 03...")
with open(os.path.join(CHAPTERS_DIR, "ch03.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("03", "Bộ Lọc Bayes, Extended Kalman Filter (EKF) & Phân Tích Hiệp Phương Sai", "Probabilistic Bayes Filter, EKF & Covariance Ellipses", "TRACK 2: ƯỚC LƯỢNG TRẠNG THÁI & ĐỊNH VỊ", "track-2", "ch02.html", "Chương 02: Mô Hình Cảm Biến & Occupancy Grid", "ch04.html", "Chương 04: Bộ Lọc Hạt MCL & FastSLAM", ch03_sidebar, ch03_body))

print("Generating Ch 04...")
with open(os.path.join(CHAPTERS_DIR, "ch04.html"), "w", encoding="utf-8") as f:
    f.write(make_chapter_html("04", "Bộ Lọc Hạt (Particle Filter), MCL & Khung FastSLAM", "Monte Carlo Localization & Rao-Blackwellized FastSLAM", "TRACK 2: ƯỚC LƯỢNG TRẠNG THÁI & ĐỊNH VỊ", "track-2", "ch03.html", "Chương 03: Bộ Lọc Bayes & EKF", "ch05.html", "Chương 05: Pose Graph SLAM & GTSAM", ch04_sidebar, ch04_body))

print("Successfully generated Chapters 01, 02, 03, 04 for SLAM Portal!")
