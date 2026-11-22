# Động Lực Học & Modeling Robot - Explorable Knowledge Portal
## Hệ Thống Chưng Cất Tri Thức Học Thuật Toàn Diện (Brian Fabien, Olav Egeland & J. Tommy Gravdahl)

Trang web chưng cất tri thức chuẩn học thuật và kỹ thuật số, được tự động hóa bởi skill **Deep Reading Distiller**.

### 🌟 Tính Năng Nổi Bật:
- **14 Chương Toàn Diện**: Bao quát 100% mục lục và nội dung khoa học từ 3 tác phẩm kinh điển về Động lực học & Modeling Robot.
- **6 Master Tracks**: Lộ trình tri thức phân cấp từ nền tảng mô hình hóa, cơ cấu chấp hành, cơ học giải tích, dao động đàn hồi, giải tích số đến triển khai ROS 2 thời gian thực.
- **Bố Cục 2 Cột Chống Tràn**: Thanh tag mục lục 320px cố định bên trái + khung nội dung fit web công thái học bên phải.
- **Chuẩn MathJax 3 Tuyệt Đối Không Lỗi**: Hiển thị hoàn hảo mọi công thức toán tensor, ký hiệu Christoffel, Quaternions và ma trận Lie $SO(3)$.
- **14 Bộ Mô Phỏng Tương Tác Canvas 2D 60 FPS**: Tự động giả lập chuyển động vật lý, đồ thị thời gian thực với thanh trượt tham số.
- **14 Ví Dụ Tính Số Kỹ Thuật 4 Bước**: Trình bày theo layout grid `repeat(auto-fit, minmax(320px, 1fr))` không tràn mép.
- **Cầu Nối Thực Tế ROS 2 / C++**: Code mẫu chuẩn `ros2_control`, Pinocchio C++, URDF/XACRO và Gazebo Sim.

---

## 🗺️ Danh Mục 6 Master Tracks & 14 Chương Chuyên Sâu

| Track | Chương | Tên Chuyên Đề Học Thuật | Mô Phỏng Canvas 2D 60 FPS |
| :--- | :--- | :--- | :--- |
| **Track 1** | **Chương 01** | Biểu Diễn Hệ Thống Hợp Nhất & Không Gian Trạng Thái | Dòng Năng Lượng Ghép Nối Cơ - Điện |
| **Track 1** | **Chương 02** | Động Học Vật Rắn 3D & Biến Đổi Tọa Độ Robot | 3D Quaternions vs Khóa Khớp Gimbal Lock |
| **Track 2** | **Chương 03** | Động Lực Học Động Cơ & Khớp Đàn Hồi | Dao Động Khớp Đàn Hồi Robot (Spong) |
| **Track 2** | **Chương 04** | Ma Sát Động LuGre & Hệ Truyền Động Thủy Lực | Hiện Tượng Dính - Trượt (Stick-Slip) |
| **Track 3** | **Chương 05** | Động Lực Học Newton-Euler & Thuật Toán RNEA $\mathcal{O}(n)$ | Con Lắc Ngược Quay Furuta Dynamics |
| **Track 3** | **Chương 06** | Cơ Học Lagrange & Động Lực Học Robot Cánh Tay | Robot 2-DOF & Đẳng Thức $\dot{M}-2C=0$ |
| **Track 3** | **Chương 07** | Động Lực Học Hệ Ràng Buộc & Phương Pháp Kane | Robot Bánh Xe Vi Sai Nonholonomic |
| **Track 3** | **Chương 08** | Cơ Học Hamilton & Hệ Port-Hamiltonian Trong Robot | Suy Giảm Năng Lượng Ổn Định IDA-PBC |
| **Track 4** | **Chương 09** | Dao Động Cơ Học, Dầm Đàn Hồi & Phân Tích FEM | 3 Mode Dao Động Dầm Euler-Bernoulli |
| **Track 5** | **Chương 10** | Thuật Toán Tích Phân Số ODEs Cho Động Lực Học | So Sánh Sai Số Euler vs Midpoint vs RK4 |
| **Track 5** | **Chương 11** | Hệ Cứng, Tích Phân Symplectic & Phương Pháp Đa Bước | Symplectic Verlet vs Cổ Điển RK4 (Bảo toàn) |
| **Track 5** | **Chương 12** | Giải Hệ Phương Trình DAEs & Động Lực Học Va Chạm | Trôi DAEs & Ổn Định Hóa Baumgarte |
| **Track 6** | **Chương 13** | Phân Tích Ổn Định Lyapunov & Điều Khiển Mô-Men CTC | Bám Quỹ Đạo CTC Với Tải Trọng Nhiễu |
| **Track 6** | **Chương 14** | Kiến Trúc Thực Tế: URDF, Pinocchio, ros2_control & Gazebo | Giám Sát Vòng Lặp Real-Time Jitter 1000 Hz |

---

## 🚀 Chạy Thử Cục Bộ (Local Preview)

Khởi chạy web server đơn giản với Python:
```bash
cd c:\Users\chucuong\OneDrive\Reading\robot-dynamics-modeling-web
python -m http.server 8000
```
Mở trình duyệt truy cập: `http://localhost:8000`

---

## 🌐 Xuất Bản Miễn Phí Lên GitHub Pages (`github.io`)

1. Tạo một repository mới trên GitHub (ví dụ: `robot-dynamics-modeling-web`).
2. Mở terminal và đẩy toàn bộ thư mục lên branch `main`:
   ```bash
   git init
   git add .
   git commit -m "feat: complete 14-chapter robot dynamics knowledge portal"
   git branch -M main
   git remote add origin https://github.com/<your-username>/robot-dynamics-modeling-web.git
   git push -u origin main
   ```
3. Vào **Settings -> Pages** trên repository, chọn source là branch `main` (thư mục root `/`).
4. Trang web sẽ trực tiếp hoạt động toàn cầu tại: `https://<your-username>.github.io/robot-dynamics-modeling-web/`.
