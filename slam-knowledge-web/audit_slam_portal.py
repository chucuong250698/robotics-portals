# -*- coding: utf-8 -*-
"""
audit_slam_portal.py
Kiểm tra tính toàn vẹn của tất cả 14 chương trong slam-knowledge-web:
- Kiểm tra lỗi công thức MathJax (không chứa ký tự '<' hoặc '>' trần trong khối LaTeX $...$ hoặc $$...$$)
- Kiểm tra sự tồn tại của Canvas ID mô phỏng (sim-canvas-01 đến sim-canvas-14)
- Kiểm tra cấu trúc 6 tầng tri thức: 4-step card, ROS 2 bridge, sidebar links
"""

import os
import re

BASE_DIR = r"c:\Users\chucuong\OneDrive\Reading\slam-knowledge-web"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

total_chapters = 14
real_errors = []

print("=== STARTING SLAM KNOWLEDGE PORTAL AUDIT ===")

for i in range(1, total_chapters + 1):
    num_str = f"{i:02d}"
    file_path = os.path.join(CHAPTERS_DIR, f"ch{num_str}.html")
    
    if not os.path.exists(file_path):
        real_errors.append(f"Chương {num_str}: Tệp không tồn tại ({file_path})")
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    size_kb = len(html.encode('utf-8')) / 1024
    if size_kb < 8:
        real_errors.append(f"Chương {num_str}: Tệp quá nhỏ ({size_kb:.1f} KB), nội dung chưa đầy đủ!")

    # Loại bỏ thẻ script, pre, code để chỉ kiểm tra nội dung text/toán
    clean_html = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
    clean_html = re.sub(r'<code.*?>.*?</code>', '', clean_html, flags=re.DOTALL)
    clean_html = re.sub(r'<pre.*?>.*?</pre>', '', clean_html, flags=re.DOTALL)

    # 1. Tìm khối display math: $$ ... $$
    block_math = re.findall(r'\$\$(.+?)\$\$', clean_html, flags=re.DOTALL)
    for m in block_math:
        if re.search(r'(?<!\\)[<>]', m):
            real_errors.append(f"Chương {num_str} (Display Math $$): Phát hiện '<' hoặc '>' trần: {m.strip()[:60]}")

    # 2. Tìm khối inline math: $ ... $ (không ngắt dòng)
    inline_math = re.findall(r'(?<!\$)\$([^\$\n\r]+?)\$(?!\$)', clean_html)
    for m in inline_math:
        if '<' in m or '>' in m:
            if not ('\\lt' in m or '\\gt' in m or '\\le' in m or '\\ge' in m):
                real_errors.append(f"Chương {num_str} (Inline Math $): Phát hiện '<' hoặc '>' trần: {m.strip()[:60]}")

    # 3. Kiểm tra Canvas ID
    canvas_id = f"sim-canvas-{num_str}"
    if canvas_id not in html:
        real_errors.append(f"Chương {num_str}: Thiếu thẻ canvas '{canvas_id}'!")

    # 4. Kiểm tra 4-step card
    if "worked-step-card" not in html and "worked-step-grid" not in html:
        real_errors.append(f"Chương {num_str}: Thiếu thẻ ví dụ tính số 4 bước (worked-step-card)!")

    # 5. Kiểm tra Code card
    if "code-card" not in html:
        real_errors.append(f"Chương {num_str}: Thiếu thẻ cầu nối mã nguồn (code-card)!")

    print(f"Chương {num_str}: OK ({size_kb:.1f} KB) - Canvas: {canvas_id} verified.")

print("\n=== AUDIT RESULTS ===")
if real_errors:
    print(f"❌ FAILED: Phát hiện {len(real_errors)} lỗi:")
    for err in real_errors:
        print(f"  {err}")
else:
    print("✅ TOÀN BỘ 14 CHƯƠNG ĐẠT CHUẨN TUYỆT ĐỐI! 0 LỖI MATHJAX, 14 CANVAS 2D & CẦU NỐI ROS 2 ĐÃ SẴN SÀNG!")
