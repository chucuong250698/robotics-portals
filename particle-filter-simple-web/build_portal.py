# -*- coding: utf-8 -*-
"""
Generator script for Particle Filter Made Simple Knowledge Portal (#12)
Book: Particle Filter Made Simple: A Step-by-Step Beginner-friendly Guide
Author: Sahil Rajesh Dhayalkar (Arizona State University, arXiv:2511.01281)
"""

import os
import re

PORTAL_DIR = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(PORTAL_DIR, "chapters")
os.makedirs(CHAPTERS_DIR, exist_ok=True)

CHAPTER_INFO = [
    {
        "id": "ch01",
        "num": "01",
        "title": "Giới Thiệu & Nhu Cầu Của Bộ Lọc Hạt",
        "title_en": "Introduction & The Need for Particle Filters",
        "track": "Track 1: Cơ Sở Lý Thuyết & Thuật Toán SIR",
        "track_id": "track-1",
        "desc": "Sự thất bại của bộ lọc Kalman trước tính phi tuyến và nhiễu phi Gauss. Triết lý biểu diễn phân bố xác suất tùy ý thông qua đám mây mẫu ngẫu nhiên (particle cloud).",
        "sections": [
            ("sec-1-1", "1.1 Nhu Cầu Cấp Thiết Của Bộ Lọc Hạt (The Need for Particle Filters)"),
            ("sec-1-2", "1.2 Những Giới Hạn Cốt Lõi Của Bộ Lọc Kalman (Limitations of Kalman Filter)"),
            ("sec-1-2-1", "1.2.1 Tính phi tuyến nghiêm trọng (Nonlinearity)"),
            ("sec-1-2-2", "1.2.2 Phân bố xác suất phi Gauss và đa đỉnh (Non-Gaussian distributions)"),
            ("sec-1-2-3", "1.2.3 Nhiễu đo lường có đuôi dày và giá trị ngoại lai (Non-Gaussian noise)"),
            ("sec-1-3", "1.3 Những Ưu Thế Vượt Trội Của Bộ Lọc Hạt (Key Strengths)"),
            ("sec-1-3-1", "1.3.1 Biểu diễn phân bố tùy ý không cần tham số hóa"),
            ("sec-1-3-2", "1.3.2 Dung nạp trực tiếp mọi mô hình hàm phi tuyến f(x) và h(x)"),
            ("sec-1-3-3", "1.3.3 Khả năng chống chịu mất cảm biến và nhiễu cực đoan"),
            ("sec-1-3-4", "1.3.4 Khả năng co giãn tính toán linh hoạt theo số lượng hạt N"),
            ("sec-1-4", "1.4 Phép Ẩn Dụ Trực Quan: Tìm Bạn Trong Đám Đông (Finding a Friend in a Crowd)"),
            ("sec-1-5", "1.5 Lộ Trình Tri Thức Của Toàn Bộ Chuyên Khảo (What Lies Ahead)")
        ],
        "sim_id": "sim-canvas-ch01",
        "prev": None,
        "next": "ch02"
    },
    {
        "id": "ch02",
        "num": "02",
        "title": "Từ Ý Tưởng Đến Biểu Diễn Toán Học",
        "title_en": "From Idea to Mathematical Representation",
        "track": "Track 1: Cơ Sở Lý Thuyết & Thuật Toán SIR",
        "track_id": "track-1",
        "desc": "Bản chất của niềm tin (Belief), mô hình xác suất như một biểu đồ tần suất chuyển động (Histogram in Motion), nguyên lý Monte Carlo, Luật Số Lớn và cấu tạo hạt.",
        "sections": [
            ("sec-2-1", "2.1 Khái Niệm Niềm Tin Xác Suất (The Concept of a Belief)"),
            ("sec-2-1-1", "2.1.1 Niềm tin liên tục đối sánh với niềm tin rời rạc"),
            ("sec-2-1-2", "2.1.2 Biểu diễn xác suất như một Histogram chuyển động (Histogram in Motion)"),
            ("sec-2-2", "2.2 Tại Sao Chọn Phương Pháp Monte Carlo? (Why Monte Carlo?)"),
            ("sec-2-2-1", "2.2.1 Nguyên lý cốt lõi: Chuyển tích phân phức tạp thành trung bình mẫu"),
            ("sec-2-2-2", "2.2.2 Luật Số Lớn (Law of Large Numbers - LLN)"),
            ("sec-2-2-3", "2.2.3 Định lý Giới hạn Trung tâm (Central Limit Theorem - CLT)"),
            ("sec-2-3", "2.3 Giải Phẫu Một Hạt Mẫu (The Anatomy of a Particle)"),
            ("sec-2-3-1", "2.3.1 Biểu diễn trạng thái x^(i)"),
            ("sec-2-3-2", "2.3.2 Trọng số quan trọng w^(i) (Importance weights)"),
            ("sec-2-3-3", "2.3.3 Chuẩn hóa trọng số (Normalization of weights)"),
            ("sec-2-4", "2.4 Ba Giai Đoạn Vận Hành Cốt Lõi (The Three Core Phases)"),
            ("sec-2-4-1", "2.4.1 Giai đoạn Dự đoán (Prediction: Moving particles forward)"),
            ("sec-2-4-2", "2.4.2 Giai đoạn Đánh trọng số (Weighting: Evaluating likelihoods)"),
            ("sec-2-4-3", "2.4.3 Giai đoạn Tái chọn mẫu (Resampling: Survival of the fittest)")
        ],
        "sim_id": "sim-canvas-ch02",
        "prev": "ch01",
        "next": "ch03"
    },
    {
        "id": "ch03",
        "num": "03",
        "title": "Thuật Toán Bộ Lọc Hạt Toàn Diện (SIR Filter)",
        "title_en": "The Complete Particle Filter Algorithm",
        "track": "Track 1: Cơ Sở Lý Thuyết & Thuật Toán SIR",
        "track_id": "track-1",
        "desc": "Giải phẫu toàn diện 6 bước thuật toán SIR (Sampling Importance Resampling), nguồn gốc toán học, hiện tượng thoái hóa mẫu, kích thước hiệu dụng Neff và tái chọn mẫu có hệ thống.",
        "sections": [
            ("sec-3-1", "3.1 Tổng Quan Về Bộ Lọc SIR (Overview of the SIR Filter)"),
            ("sec-3-2", "3.2 Quy Trình 6 Bước Chuẩn Mực Của Thuật Toán SIR (Step-by-Step Algorithm)"),
            ("sec-3-2-1", "3.2.1 Bước 1: Khởi tạo đám mây hạt (Initialization)"),
            ("sec-3-2-2", "3.2.2 Bước 2: Dự đoán trạng thái theo mô hình chuyển động (Prediction)"),
            ("sec-3-2-3", "3.2.3 Bước 3: Cập nhật trọng số theo hợp lý cảm biến (Weighting)"),
            ("sec-3-2-4", "3.2.4 Bước 4: Chuẩn hóa tổng trọng số (Normalization)"),
            ("sec-3-2-5", "3.2.5 Bước 5: Ước lượng trạng thái hệ thống (State Estimation)"),
            ("sec-3-2-6", "3.2.6 Bước 6: Tái chọn mẫu loại bỏ hạt yếu (Resampling)"),
            ("sec-3-3", "3.3 Nền Tảng Toán Học & Nhận Thức Chuyên Sâu (Mathematical Derivation & Insights)"),
            ("sec-3-3-1", "3.3.1 Bản chất của lấy mẫu tầm quan trọng (Importance Sampling)"),
            ("sec-3-3-2", "3.3.2 Vấn đề thoái hóa trọng số (Weight Degeneracy Problem)"),
            ("sec-3-3-3", "3.3.3 Kích thước mẫu hiệu dụng Neff (Effective Sample Size)"),
            ("sec-3-3-4", "3.3.4 Chiến lược tái chọn mẫu thích nghi (When to Resample)")
        ],
        "sim_id": "sim-canvas-ch03",
        "prev": "ch02",
        "next": "ch04"
    },
    {
        "id": "ch04",
        "num": "04",
        "title": "Ví Dụ Số Học: Bám Vết Vật Thể 1D & Code Lab",
        "title_en": "Numerical Example: 1D Object Tracking & Code Lab",
        "track": "Track 2: Thực Hành Số Học & Lọc Đa Chiều",
        "track_id": "track-2",
        "desc": "Từng phép tính số học cụ thể cho các bước thời gian k=1, 2, 3 với Q=1.0, R=4.0; trực quan hóa phân tán và hội tụ hạt; xây dựng bộ lọc 1D hoàn chỉnh bằng Python.",
        "sections": [
            ("sec-4-1", "4.1 Thiết Lập Bài Toán Bám Vết 1D (Problem Setup)"),
            ("sec-4-1-1", "4.1.1 Mô hình chuyển động động học (Motion model)"),
            ("sec-4-1-2", "4.1.2 Mô hình đo lường quan sát (Measurement model)"),
            ("sec-4-1-3", "4.1.3 Tham số mô phỏng thực nghiệm (Simulation parameters)"),
            ("sec-4-2", "4.2 Chi Tiết Các Bước Tính Số Từng Bước Một (Step-by-Step Calculations)"),
            ("sec-4-2-1", "4.2.1 Bước thời gian k = 1 (Chi tiết tính số đầy đủ)"),
            ("sec-4-2-2", "4.2.2 Bước thời gian k = 2 (Cập nhật đo lường thứ hai)"),
            ("sec-4-2-3", "4.2.3 Bước thời gian k = 3 (Xu thế hội tụ và ổn định)"),
            ("sec-4-3", "4.3 Trực Quan Hóa Đám Mây Hạt (Visualizing the Particle Cloud)"),
            ("sec-4-3-1", "4.3.1 Sự phân tán ban đầu và thu hẹp hội tụ về chân giá trị"),
            ("sec-4-3-2", "4.3.2 Động học phân phối trọng số qua các chu kỳ"),
            ("sec-4-4", "4.4 Code Lab 1: Triển Khai Bộ Lọc Hạt 1D Bằng Python (Code Lab 1)"),
            ("sec-4-4-1", "4.4.1 Cấu trúc thiết lập mô phỏng số"),
            ("sec-4-4-2", "4.4.2 Mã nguồn thuật toán bám vết hạt 1D"),
            ("sec-4-4-3", "4.4.3 Chạy thử nghiệm và phân tích đồ thị kết quả")
        ],
        "sim_id": "sim-canvas-ch04",
        "prev": "ch03",
        "next": "ch05"
    },
    {
        "id": "ch05",
        "num": "05",
        "title": "Bộ Lọc Hạt Trong Không Gian Đa Chiều & Code Lab 2D",
        "title_en": "Particle Filter in Higher Dimensions & Code Lab 2D",
        "track": "Track 2: Thực Hành Số Học & Lọc Đa Chiều",
        "track_id": "track-2",
        "desc": "Mở rộng vector trạng thái [x, y, vx, vy]^T; mô hình chuyển động và cảm biến 2D; giải quyết lời nguyền số chiều (Curse of Dimensionality); Code Lab Python 2D và khôi phục sự cố bắt cóc.",
        "sections": [
            ("sec-5-1", "5.1 Thiết Lập Vector Trạng Thái Đa Chiều (State Vector Formulation)"),
            ("sec-5-1-1", "5.1.1 Dạng tổng quát đa biến x_k"),
            ("sec-5-1-2", "5.1.2 Ý nghĩa thực tế trong cấu trúc thuật toán"),
            ("sec-5-1-3", "5.1.3 Lời nguyền số chiều và bài toán co giãn tính toán (Dimensionality scaling)"),
            ("sec-5-2", "5.2 Bám Vết 2D: Mô Hình Chuyển Động & Cảm Biến (Motion & Measurement Models)"),
            ("sec-5-2-1", "5.2.1 Mô hình chuyển động vận tốc không đổi (Constant Velocity Model)"),
            ("sec-5-2-2", "5.2.2 Mô hình quan sát cảm biến radar / landmark phi tuyến"),
            ("sec-5-3", "5.3 Trực Quan Hóa Đám Mây Hạt Không Gian 2D (2D Cloud Visualization)"),
            ("sec-5-4", "5.4 Code Lab 2: Bộ Lọc Hạt Định Vị 2D Trong Python (Code Lab 2)"),
            ("sec-5-4-1", "5.4.1 Thiết lập ma trận hiệp phương sai Q và R"),
            ("sec-5-4-2", "5.4.3 Mã nguồn bộ lọc Monte Carlo 2D hoàn chỉnh"),
            ("sec-5-4-3", "5.4.4 Phân tích hiệu năng, độ trễ và bài học kỹ thuật thực tế")
        ],
        "sim_id": "sim-canvas-ch05",
        "prev": "ch04",
        "next": None
    }
]

print(f"Loaded metadata for {len(CHAPTER_INFO)} chapters.")
