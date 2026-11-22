# TRƯNG CẤT TRI THỨC TOÀN DIỆN: ELEMENTS OF ROBOTICS
> **Tác phẩm gốc:** *Elements of Robotics* (Springer Open, 311 trang, 16 chương)  
> **Tác giả:** GS. Mordechai Ben-Ari & GS. Francesco Mondada  
> **Kiến trúc:** 7 Master Tracks • 16 Chương chuẩn mực • 16 Ví dụ tính số 4 bước • Cầu nối ROS 2 Humble/Jazzy  
> **Nền tảng Tương tác Web:** Xem bản trực quan đầy đủ tại [index.html](../index.html) với 8 mô phỏng Canvas và 8 đồ thị Vector SVG.

---

## MỤC LỤC LỘ TRÌNH TRI THỨC (CURRICULUM ROADMAP)
- **Track 1: Foundations & Cảm biến (Chương 01 - 02)**
  - Chương 01: Robot là gì? - Khái niệm Chuẩn quốc tế & Giải phẫu Cơ điện tử
  - Chương 02: Hệ thống Cảm biến Thu nhận Môi trường (PSD, ToF, LiDAR, Encoders, Nhiễu Gauss)
- **Track 2: Hành vi Phản xạ & Máy trạng thái (Chương 03 - 04)**
  - Chương 03: Hành vi Phản xạ & 4 Loại Xe Braitenberg (Sợ hãi, Hung hăng, Yêu thương, Thám hiểm)
  - Chương 04: Máy trạng thái hữu hạn (FSM) & Kỹ thuật Dải trễ (Hysteresis Deadband) Khử Chattering
- **Track 3: Động học & Điều khiển Vòng kín PID (Chương 05 - 06)**
  - Chương 05: Động học Robot Vi sai (Differential Drive), Tâm quay tức thời ICC & Định vị Odometry
  - Chương 06: Điều khiển Vòng kín PID, Chống Bão hòa Tích phân (Anti-Windup Clamping) & Ziegler-Nichols
- **Track 4: Dẫn đường & Định vị Xác suất Bayes (Chương 07 - 08)**
  - Chương 07: Định vị Trực tiếp & Phương pháp Hình học (Trilateration & Triangulation)
  - Chương 08: Định vị Xác suất & Bộ lọc Bayes Đệ quy 1D (Prediction & Measurement Update)
- **Track 5: Bản đồ Môi trường & Quy hoạch Đường đi (Chương 09 - 10)**
  - Chương 09: Bản đồ Lưới Chiếm chỗ (Occupancy Grid), Biến đổi Log-Odds & Nghịch lý SLAM
  - Chương 10: Không gian Cấu hình C-Space (Minkowski Sum) & Thuật toán Tìm đường Tối ưu A*
- **Track 6: Trí tuệ Nhân tạo & Học máy (Chương 11 - 14)**
  - Chương 11: Môi trường Phức tạp & Điều khiển Logic Mờ (Fuzzy Logic & Trọng tâm Centroid)
  - Chương 12: Xử lý Ảnh Số & Thị giác Máy tính cho Robot (Lọc Gauss, Sobel, Harris Corner)
  - Chương 13: Mạng Nơ-ron & Học máy Sinh học (Hebbian Learning, Perceptron của Rosenblatt)
  - Chương 14: Bộ phân loại Tuyến tính Fisher LDA & Trực giác Học tăng cường (Q-Learning)
- **Track 7: Swarm Robotics & Cánh tay Thao tác 3D (Chương 15 - 16)**
  - Chương 15: Robot Bầy đàn (Swarm Robotics) & Thuật toán Tụ hội Nguồn nhiệt BeeClust
  - Chương 16: Cánh tay Thao tác 2-DOF, Động học Thuận/Ngược (Elbow-Up/Down) & Xoay 3D Quaternions
- **Phụ lục A & B**
  - Phụ lục A: Nền tảng Toán học Cho Kỹ thuật Robot (Lượng giác, Đại số tuyến tính, Xác suất)
  - Phụ lục B: Cầu nối Kiến trúc sang Hệ điều hành Robot ROS 2 Humble / Jazzy

---

# TRACK 1: FOUNDATIONS & HỆ THỐNG CẢM BIẾN

## CHƯƠNG 01: ROBOT LÀ GÌ? - KHÁI NIỆM & GIẢI PHẪU HỆ THỐNG
### 1. Khái niệm Cốt lõi & Chu trình Sense - Think - Act
Một robot được định nghĩa học thuật là cỗ máy cơ điện tử có khả năng tự động thực hiện các tác vụ phức tạp bằng cách tương tác với môi trường vật lý qua chu trình khép kín:
- **Sense (Nhận thức):** Thu thập đại lượng vật lý (khoảng cách, quang thông, vận tốc góc).
- **Think (Xử lý):** Vi xử lý tính toán thuật toán, duy trì trạng thái và sinh quyết định.
- **Act (Hành động):** Tác động lực cơ học qua động cơ, bánh xe, cánh tay cơ khí.

### 2. Giải phẫu Cơ điện tử của Robot Di động
1. **Khung gầm & Cơ cấu truyền động (Chassis & Drivetrain):** Khung chịu tải, bánh xe vi sai / bánh xích.
2. **Cơ cấu chấp hành (Actuators):** Động cơ DC có chổi than / không chổi than (BLDC) kèm hộp giảm tốc (Gearbox).
3. **Cảm biến (Sensors):** Cảm biến nội tại (Encoders, IMU) và cảm biến ngoại tại (ToF, LiDAR, Camera).
4. **Vi điều khiển & Máy tính nhúng:** Vi điều khiển thời gian thực (MCU) tầng thấp và SBC (Raspberry Pi/Jetson) chạy ROS 2.
5. **Bộ nguồn (Power):** Pin LiPo / LiFePO4, mạch quản lý pin BMS và mạch ổn áp buck-boost.

### 3. Ví dụ Tính số 4 Bước: Công suất & Mô-men xoắn Động cơ Vượt dốc
- **Đầu vào:** $m = 4	ext{ kg}, R = 0.05	ext{ m}, lpha = 15^\circ, v = 0.3	ext{ m/s}, f_r = 0.02, g = 9.81	ext{ m/s}^2$.
- **Bước 1:** Lực cản tổng: $F_{total} = mg\sinlpha + f_r mg\coslpha = 10.16 + 0.76 = 10.92	ext{ N}$.
- **Bước 2:** Lực trên mỗi bánh: $F_{wheel} = 5.46	ext{ N}$.
- **Bước 3:** Mô-men xoắn trục bánh: $	au = F_{wheel} \cdot R = 5.46 	imes 0.05 = 0.273	ext{ N}\cdot	ext{m}$ (Với $S=1.5 \implies 	au_{req} = 0.41	ext{ N}\cdot	ext{m}$).
- **Bước 4:** Tốc độ quay & Công suất: $\omega = v/R = 6	ext{ rad/s} pprox 57.3	ext{ RPM}$; $P = 	au \cdot \omega = 1.64	ext{ W}$/động cơ.

---

## CHƯƠNG 02: HỆ THỐNG CẢM BIẾN THU NHẬN MÔI TRƯỜNG
### 1. Phân loại Cảm biến
- **Chủ động (Active) vs Bị động (Passive):** Chủ động tự phát năng lượng (LiDAR, siêu âm); Bị động chỉ thu nhận năng lượng môi trường (Camera, la bàn).
- **Nội tại (Proprioceptive) vs Ngoại tại (Exteroceptive):** Nội tại đo trạng thái robot (Encoder, pin); Ngoại tại đo môi trường bên ngoài (Khoảng cách tường).

### 2. Cảm biến Hồng ngoại PSD (Optical Triangulation)
- Nguyên lý đo bằng góc lệch tam giác đạc thay vì cường độ phản xạ:
  $$D = rac{f \cdot B}{x_p}$$
- Trong đó: $D$ là khoảng cách, $f$ là tiêu cự, $B$ là cự ly đáy cơ sở, $x_p$ là vị trí lệch trên cảm quang PSD.

### 3. Cảm biến Siêu âm Thời gian bay ToF (Time-of-Flight)
- Vận tốc âm thanh theo nhiệt độ $T$ ($^\circ	ext{C}$):
  $$v(T) = 331.3 \cdot \sqrt{1 + rac{T}{273.15}} pprox 331.3 + 0.606 \cdot T \quad (	ext{m/s})$$
- Khoảng cách: $d = rac{v \cdot \Delta t}{2}$.
- *Hạn chế:* Hiện tượng phản xạ gương (Specular reflection) khi góc tới $> 20^\circ$.

### 4. Bộ giải mã Xung quang học (Optical Encoders)
- Đĩa vạch quang kết hợp 2 kênh quang điện lệch pha $90^\circ$ (Quadrature A/B) giải mã chiều quay và số vòng.

---

# TRACK 2: HÀNH VI PHẢN XẠ & MÁY TRẠNG THÁI HỮU HẠN

## CHƯƠNG 03: HÀNH VI PHẢN XẠ & XE BRAITENBERG
### 1. Vòng lặp Nhận thức - Hành động (Perception-Action Loop)
Nối trực tiếp cảm biến đến động cơ không qua biểu diễn thế giới, đạt độ trễ tiệm cận 0.

### 2. Bốn Phương tiện Kinh điển của Braitenberg
- **Xe 2a (Sợ hãi - Fear):** Nối thẳng cùng bên (Ipsilateral Excitatory). Cảm biến phải $	o$ motor phải; Cảm biến trái $	o$ motor trái. Khi gặp ánh sáng bên phải, motor phải quay nhanh hơn $\implies$ rẽ trái trốn chạy.
- **Xe 2b (Hung hăng - Aggression):** Nối chéo (Contralateral Excitatory). Cảm biến phải $	o$ motor trái. Khi gặp ánh sáng bên phải, motor trái quay nhanh hơn $\implies$ quay đầu lao vọt vào ngọn đèn.
- **Xe 3a (Yêu thương - Love):** Nối thẳng ức chế (Ipsilateral Inhibitory). Ánh sáng làm chậm motor cùng bên $\implies$ tiến lại gần và dừng âu yếm trước đèn.
- **Xe 3b (Thám hiểm - Explorer):** Nối chéo ức chế (Contralateral Inhibitory). Lướt qua ngọn đèn và tiếp tục khám phá.

---

## CHƯƠNG 04: MÁY TRẠNG THÁI HỮU HẠN (FSM) & VÙNG TRỄ (HYSTERESIS)
### 1. Mô hình Toán học FSM
Bộ 5 thành phần $(S, I, O, \delta, \lambda)$ điều khiển rời rạc theo sự kiện.

### 2. Hiện tượng Rung giật Chuyển mạch (Chattering)
Khi chỉ dùng một ngưỡng duy nhất $	au$: Nhiễu cảm biến làm trạng thái nhảy qua lại liên tục với tần số cao, gây hao mòn cơ khí và tiêu tốn pin.

### 3. Kỹ thuật Dải Trễ Hysteresis Deadband
Áp dụng hai ngưỡng cách biệt $[	au_{low}, 	au_{high}]$ tạo vùng đệm chết:
- Chuyển sang "Gần tường" chỉ khi $d < 	au_{low}$.
- Chuyển sang "Xa tường" chỉ khi $d > 	au_{high}$.
- Giữa $[	au_{low}, 	au_{high}]$: **Giữ nguyên trạng thái cũ** $\implies$ triệt tiêu hoàn toàn dao động do nhiễu!

---

# TRACK 3: ĐỘNG HỌC ROBOT VI SAI & ĐIỀU KHIỂN VÒNG KÍN PID

## CHƯƠNG 05: ĐỘNG HỌC ROBOT VI SAI & TÂM QUAY TỨC THỜI (ICC)
### 1. Hệ Phương trình Động học Vi sai & ICC
- Vận tốc dài robot: $v = rac{v_r + v_l}{2}$
- Vận tốc góc bẻ lái: $\omega = rac{v_r - v_l}{b}$
- Bán kính quay quanh tâm ICC: $R = rac{b}{2} rac{v_r + v_l}{v_r - v_l}$
- Tọa độ tâm quay tức thời: $	ext{ICC} = [x - R\sin	heta, \; y + R\cos	heta]^T$

### 2. Tích lũy Odometry từ Encoder
$$\Delta s = rac{\Delta s_r + \Delta s_l}{2}, \quad \Delta	heta = rac{\Delta s_r - \Delta s_l}{b}$$
$$x_{t+1} = x_t + \Delta s \cos(	heta_t + rac{\Delta	heta}{2}), \quad y_{t+1} = y_t + \Delta s \sin(	heta_t + rac{\Delta	heta}{2}), \quad 	heta_{t+1} = 	heta_t + \Delta	heta$$

---

## CHƯƠNG 06: ĐIỀU KHIỂN VÒNG KÍN PID & CHỐNG BÃO HÒA TÍCH PHÂN
### 1. Ba Khâu Điều khiển P - I - D
$$u(t) = K_p e(t) + K_i \int_0^t e(	au) d	au + K_d rac{de(t)}{dt}$$
- **Khâu P:** Phản ứng nhanh theo sai lệch tức thời; luôn tồn tại sai số tĩnh $e_{ss} 
e 0$.
- **Khâu I:** Triệt tiêu hoàn toàn sai số tĩnh bằng tích lũy quá khứ.
- **Khâu D:** Dự báo tương lai, cản trở dao động và triệt tiêu vọt lố (Overshoot).

### 2. Hiện tượng Integral Windup & Thuật toán Anti-Windup Clamping
Khi cơ cấu chấp hành chạm trần bão hòa $u_{max}$, khâu tích phân nếu tiếp tục cộng dồn sẽ gây vọt lố thảm họa khi về đích.  
**Giải pháp Clamping:** Đóng ngắt tích lũy khi $u$ bão hòa và $	ext{sign}(e) == 	ext{sign}(u)$.

---

# TRACK 4: DẪN ĐƯỜNG & ĐỊNH VỊ XÁC SUẤT BAYES

## CHƯƠNG 07: ĐỊNH VỊ TRỰC TIẾP & PHƯƠNG PHÁP HÌNH HỌC
### 1. Phương pháp Giao hội Khoảng cách Trilateration
Giải hệ $N \ge 3$ đường tròn từ các trạm phát mốc $B_i(x_i, y_i)$:
$$(x - x_i)^2 + (y - y_i)^2 = d_i^2$$
Tuyến tính hóa bằng cách trừ phương trình thứ nhất để đưa về bài toán bình phương tối thiểu $A\mathbf{x} = \mathbf{b}$.

---

## CHƯƠNG 08: ĐỊNH VỊ XÁC SUẤT & BỘ LỌC BAYES
### 1. Chu trình Đệ quy Hai Bước của Bộ lọc Bayes
1. **Bước Dự đoán (Prediction - Motion Update):**  
   $$\overline{	ext{bel}}(x_t) = \sum_{x_{t-1}} P(x_t \mid x_{t-1}, u_t) \cdot 	ext{bel}(x_{t-1})$$
   *(Làm tản mác entropy, tăng độ bất định do sai số chuyển động).*
2. **Bước Hiệu chỉnh (Correction - Measurement Update):**  
   $$	ext{bel}(x_t) = \eta \cdot P(z_t \mid x_t) \cdot \overline{	ext{bel}}(x_t)$$
   *(Thu hẹp phương sai, hội tụ niềm tin về vị trí đúng).*

---

# TRACK 5: LẬP BẢN ĐỒ & QUY HOẠCH ĐƯỜNG ĐI

## CHƯƠNG 09: LẬP BẢN ĐỒ LƯỚI CHIẾM CHỖ & NGHỊCH LÝ SLAM
### 1. Cập nhật Log-Odds Tránh Tràn số
$$l_t(m_i) = l_{t-1}(m_i) + 	ext{inv\_sensor}(z_t, m_i) - l_0(m_i)$$
$$l(p) = \ln\left(rac{p}{1 - p}ight) \iff p = 1 - rac{1}{1 + e^l}$$

### 2. Nghịch lý SLAM & Đóng Vòng lặp Loop Closure
Đồng thời ước lượng quỹ đạo robot và bản đồ mốc tiêu; khi nhận diện lại cảnh cũ, tối ưu hóa đồ thị Graph-SLAM nắn lại toàn bộ bản đồ.

---

## CHƯƠNG 10: KHÔNG GIAN C-SPACE & THUẬT TOÁN TÌM ĐƯỜNG A*
### 1. C-Space & Phép cộng Minkowski
Thu nhỏ robot thành chất điểm và giãn nở vật cản bằng bán kính robot: $\mathcal{C}_{obs} = \mathcal{W}_{obs} \oplus (-\mathcal{A})$.

### 2. Hàm Đánh giá Chi phí A* Search
$$f(n) = g(n) + h(n)$$
- $g(n)$: Chi phí thực tế đã đi từ Start đến $n$.
- $h(n)$: Chi phí dự đoán từ $n$ đến Goal (Heuristic).
- Đảm bảo tối ưu khi $h(n)$ chấp nhận được (Admissible: $h(n) \le h^*(n)$) và nhất quán (Consistent).

---

# TRACK 6: TRÍ TUỆ NHÂN TẠO & HỌC MÁY CHO ROBOT

## CHƯƠNG 11: MÔI TRƯỜNG PHỨC TẠP & LOGIC MỜ (FUZZY LOGIC)
- Biến ngôn ngữ & hàm thuộc tam giác/hình thang.
- Suy luận mờ Mamdani và Giải mờ tính trọng tâm:
  $$u^* = rac{\sum u_i \cdot \mu_B(u_i)}{\sum \mu_B(u_i)}$$

## CHƯƠNG 12: XỬ LÝ ẢNH SỐ & THỊ GIÁC MÁY TÍNH
- Nhân chập lọc Gauss làm mịn ảnh.
- Toán tử Sobel phát hiện biên cạnh: $|
abla I| = \sqrt{G_x^2 + G_y^2}$.
- Tiêu chuẩn góc Harris Corner: $R = \det(M) - k \cdot (	ext{trace}(M))^2$.

## CHƯƠNG 13: MẠNG NƠ-RON & HỌC MÁY SINH HỌC
- Quy tắc học Hebb: $\Delta w_i = \eta x_i y$.
- Perceptron của Rosenblatt: phân tách siêu phẳng tuyến tính và định lý hội tụ.

## CHƯƠNG 14: PHÂN LOẠI FISHER LDA & HỌC TĂNG CƯỜNG
- Fisher LDA tối đa hóa tỉ số giữa các lớp: $J(w) = rac{w^T S_B w}{w^T S_W w}$.
- Q-Learning theo phương trình Bellman:
  $$Q(s, a) \leftarrow Q(s, a) + lpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$

---

# TRACK 7: ROBOT BẦY ĐÀN & CÁNH TAY THAO TÁC 3D

## CHƯƠNG 15: ROBOT BẦY ĐÀN & THUẬT TOÁN TỤ HỘI BEECLUST
- Ba nguyên lý: Phi tập trung, Co giãn quy mô, Tự phục hồi lỗi.
- Hiện tượng Stigmergy & Mô hình Boids (Separation, Alignment, Cohesion).
- **Thuật toán BeeClust:** Robot di chuyển ngẫu nhiên; khi gặp nhau dừng lại thời gian:
  $$w(T) = rac{w_{\max} \cdot T^2}{T^2 + T_0^2}$$
  Dẫn đến toàn bầy tự động tụ hội tại nguồn nhiệt tối ưu toàn cục.

---

## CHƯƠNG 16: CÁNH TAY THAO TÁC 2-DOF & ĐỘNG HỌC 3D
### 1. Động học Thuận (Forward Kinematics)
$$x = l_1 \cos	heta_1 + l_2 \cos(	heta_1 + 	heta_2), \quad y = l_1 \sin	heta_1 + l_2 \sin(	heta_1 + 	heta_2)$$

### 2. Động học Ngược (Inverse Kinematics)
$$\cos	heta_2 = rac{x^2 + y^2 - l_1^2 - l_2^2}{2 l_1 l_2}$$
$$	heta_2 = 	ext{atan2}(\pm\sqrt{1 - \cos^2	heta_2}, \; \cos	heta_2)$$
$$	heta_1 = 	ext{atan2}(y, x) - 	ext{atan2}(l_2 \sin	heta_2, \; l_1 + l_2 \cos	heta_2)$$
Hai cấu hình nghiệm đối xứng: **Cùi chỏ lên (Elbow-Up)** và **Cùi chỏ xuống (Elbow-Down)**.

### 3. Động học Quay 3D
Tránh hiện tượng Khóa khớp (Gimbal Lock) của góc Euler bằng biểu diễn Quaternions $q = [q_w, q_x, q_y, q_z]^T$ với $\|q\| = 1$.

---

# PHỤ LỤC: CẦU NỐI KIẾN TRÚC SANG HỆ ĐIỀU HÀNH ROS 2
| Tầng Kiến trúc | Package ROS 2 Chuẩn | Topic & Message |
| :--- | :--- | :--- |
| Phần cứng & Motor | `ros2_control` | `/sensor_msgs/msg/LaserScan` |
| Động học Vi sai | `diff_drive_controller` | `/cmd_vel`, `/odom`, TF `odom -> base_link` |
| Bộ điều khiển PID | `control_toolbox::Pid` | Parameters YAML `antiwindup: true` |
| Định vị Xác suất | `nav2_amcl` | Particle filter cloud, `/amcl_pose` |
| Bản đồ & SLAM | `slam_toolbox` | `/map` (`OccupancyGrid`) |
| Quy hoạch A* | `nav2_smac_planner` | `/plan` (`nav_msgs/msg/Path`), Costmap |
| Thị giác Robot | `image_transport`, `cv_bridge` | `/image_raw`, OpenCV Mat |
| Cánh tay Thao tác | `MoveIt 2` | KDL / TRAC-IK, URDF Models |

---
*Bản tài liệu trưng cất được tạo tự động bởi Antigravity Knowledge Distillation System, chuẩn hóa theo toàn bộ nội dung giáo trình Elements of Robotics.*
