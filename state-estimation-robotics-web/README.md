# State Estimation for Robotics — Explorable Knowledge Portal

> **Tác phẩm nguồn:** *State Estimation for Robotics* (Second Edition 2026, 580 trang)  
> **Tác giả:** Giáo sư **Timothy D. Barfoot** (University of Toronto / Cambridge University Press)  
> **Tiêu chuẩn chuyển hóa:** Chưng cất tri thức học thuật sâu **Deep Reading Distiller** (Kiến trúc 6 tầng, 2 cột thích ứng, 14 mô phỏng tương tác 60 FPS, MathJax 3 sạch 100%, code kỹ thuật sản xuất C++/GTSAM/ROS 2).

---

## 🧭 Cấu Trúc Khóa Học & 5 Master Tracks

| Track | Phạm Vi Chương | Trọng Tâm Học Thuật |
| :--- | :--- | :--- |
| **Track 1** | Chương 01 – 04 | **Cơ Sở Xác Suất & Tuyến Tính Gauss:** Cramér-Rao Lower Bound, Fisher Information, Dạng thông tin (Information Form), Khoảng cách Mahalanobis & Chi-squared Gating, Batch MAP & RTS Smoother, Ba con đường suy dẫn Kalman Filter, Kalman-Bucy Riccati SDE, Gaussian Process Regression. |
| **Track 2** | Chương 05 – 06 | **Ước Lượng Phi Tuyến & Biến Phân:** EKF, IEKF (tương đương Gauss-Newton MAP), Unscented Kalman Filter (UKF Sigmapoints), Particle Filter, Độ nhất quán NEES/NIS, Ước lượng vững Robust M-Estimation (Huber/Cauchy IRLS), **Variational Inference** (*Mục đột phá mới trong Tái bản 2*: ELBO, CAVI, Laplace). |
| **Track 3** | Chương 07 – 09 | **Hình Học 3D & Nhóm Lie Ma Trận:** Khóa góc Gimbal Lock, Unit Quaternions, $SO(3)$, $SE(3)$, Đại số Lie tiếp tuyến $\mathfrak{so}(3)/\mathfrak{se}(3)$, Ánh xạ mũ Rodrigues, Toán tử liên hợp Adjoint, Công thức BCH, Jacobian vi phân trái/phải ($J_l, J_r$), Phân phối Gauss tập trung trên nhóm Lie (Concentrated Gaussians), Lan truyền bất định qua Adjoint. |
| **Track 4** | Chương 10 – 12 | **Ứng Dụng Tư Thế Thực Chiến:** Đăng ký mây điểm dạng đóng SVD của Arun & Horn, Thuật toán lặp ICP Point-to-Point & Point-to-Plane, Tối ưu hóa đồ thị tư thế Pose-Graph SLAM với Loop Closure và Hessian thưa, **Tiền tích phân IMU trên nhóm Lie (On-Manifold IMU Pre-integration)** với Jacobian bù trôi Bias không cần tích phân lại. |
| **Track 5** | Chương 13 – 14 | **Bundle Adjustment & STEAM Liên Tục:** Cân bằng bó Bundle Adjustment, Sai số chiếu lại phối cảnh pinhole camera, Ma trận mũi tên Arrowhead, Kỹ thuật triệt tiêu mốc Schur Complement Marginalization, **STEAM (Simultaneous Trajectory Estimation and Mapping)**, Nghiệm giải tích đóng GP Spline Interpolation cho cảm biến bất đồng bộ (LiDAR quét, Rolling shutter). |

---

## 🚀 Khởi Chạy Nhanh Trực Tiếp (Local Preview)

Cổng thông tin được xây dựng 100% Client-Side thuần túy, không yêu cầu Node.js, Webpack hay bất kỳ trình biên dịch nào.

1. Mở PowerShell hoặc Terminal tại thư mục này:
   ```powershell
   python -m http.server 8769
   ```
2. Truy cập trình duyệt:
   ```
   http://localhost:8769/index.html
   ```

---

## 📂 Tổ Chức Tệp Tin

```
state-estimation-robotics-web/
├── index.html                   # Cổng thông tin Portal Hub (14 thẻ chương, 5 tracks, live search < 10ms)
├── README.md                    # Tài liệu kiến trúc và hướng dẫn sử dụng
├── assets/
│   ├── css/
│   │   └── style.css            # Hệ thống CSS 2 cột thích ứng (Sidebar 320px + Fit Web)
│   └── js/
│       ├── app.js               # Quản lý tìm kiếm tức thì, lọc pills, ScrollSpy & tiến độ đọc
│       └── simulators.js        # 14 phòng lab mô phỏng Canvas 2D 60 FPS thuần Vanilla JS
└── chapters/
    ├── ch01.html                # Cơ Sở Xác Suất, Cramér-Rao & Fisher Information
    ├── ch02.html                # Biến Ngẫu Nhiên Gauss & Khoảng Cách Mahalanobis
    ├── ch03.html                # Ước Lượng Tuyến Tính Gauss, Batch MAP & RTS Smoother
    ├── ch04.html                # Bộ Lọc Kalman Rời Rạc/Liên Tục & Gaussian Process
    ├── ch05.html                # Ước Lượng Phi Tuyến: EKF, IEKF, UKF & Particle Filter
    ├── ch06.html                # Xử Lý Ngoại Lai, NEES/NIS & Variational Inference
    ├── ch07.html                # Hình Học 3D: Ma Trận Quay, Quaternions & SE(3)
    ├── ch08.html                # Nhóm Lie Ma Trận: SO(3), SE(3) & Đại Số Lie
    ├── ch09.html                # Giải Tích Trên Nhóm Lie, BCH & Gauss Tập Trung
    ├── ch10.html                # Căn Chỉnh Đám Mây Điểm: SVD Arun, Horn & ICP
    ├── ch11.html                # Tối Ưu Hóa Đồ Thị Tư Thế Pose-Graph SLAM
    ├── ch12.html                # Tiền Tích Phân IMU Trên Nhóm Lie Cho VIO
    ├── ch13.html                # Bundle Adjustment & Triệt Tiêu Schur Complement
    └── ch14.html                # Continuous-Time STEAM Quỹ Đạo Gaussian Process
```

---

## 🛡️ Đảm Bảo Chất Lượng Kỹ Thuật (QA Audit)

- **Chuẩn hiển thị công thức:** MathJax 3 được cấu hình `\lt` và `\gt`, sạch 100% không dính lỗi `Math Processing Error`.
- **Giao diện 2 cột:** Cột trái Sticky Sidebar 320px định vị mục lục và thanh tiến độ đọc mượt mà; cột phải tự động giãn theo màn hình.
- **Mô phỏng Canvas 2D:** 14/14 chương đều tích hợp phòng lab thời gian thực 60 FPS tương tác độc lập.
- **Code mẫu:** Sử dụng C++20, Eigen 3, Sophus, Google Ceres Solver và GTSAM chuẩn công nghiệp.
