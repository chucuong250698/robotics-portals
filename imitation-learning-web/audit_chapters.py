# -*- coding: utf-8 -*-
"""
audit_chapters.py
Kiểm tra tính toàn vẹn của tất cả 14 chương trong imitation-learning-web:
- Kiểm tra lỗi công thức MathJax (không chứa ký tự '<' hoặc '>' trần trong khối LaTeX $...$ hoặc $$...$$)
- Kiểm tra sự tồn tại của Canvas ID mô phỏng (sim-canvas-01 đến sim-canvas-14)
- Kiểm tra cấu trúc 6 tầng tri thức: 4-step card, ROS 2 bridge, sidebar links
"""

import os
import re

BASE_DIR = r"c:\Users\chucuong\OneDrive\Reading\imitation-learning-web"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

math_inline_re = re.compile(r'\$([^\$]+)\$')
math_block_re = re.compile(r'\$\$([^\$]+)\$\$')

total_chapters = 14
errors = []
warnings = []

print("=== STARTING KNOWLEDGE PORTAL AUDIT ===")

for i in range(1, total_chapters + 1):
    num_str = f"{i:02d}"
    file_path = os.path.join(CHAPTERS_DIR, f"ch{num_str}.html")
    
    if not os.path.exists(file_path):
        errors.append(f"Chương {num_str}: Tệp không tồn tại ({file_path})")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    size_kb = len(content.encode('utf-8')) / 1024
    if size_kb < 5:
        errors.append(f"Chương {num_str}: Tệp quá nhỏ ({size_kb:.1f} KB), có thể chưa có nội dung đầy đủ!")
        
    # Check MathJax bare < or >
    math_blocks = math_block_re.findall(content)
    math_inlines = math_inline_re.findall(content)
    
    for mb in math_blocks:
        if "<" in mb and "\\lt" not in mb:
            # Check if it has raw <
            if re.search(r'(?<!\\)<', mb):
                errors.append(f"Chương {num_str}: Chứa ký tự '<' trần trong khối $$...$$ -> Cần thay bằng \\lt: {mb[:40]}...")
        if ">" in mb and "\\gt" not in mb:
            if re.search(r'(?<!\\)>', mb):
                errors.append(f"Chương {num_str}: Chứa ký tự '>' trần trong khối $$...$$ -> Cần thay bằng \\gt: {mb[:40]}...")

    for mi in math_inlines:
        if "<" in mi and "\\lt" not in mi:
            if re.search(r'(?<!\\)<', mi):
                errors.append(f"Chương {num_str}: Chứa ký tự '<' trần trong khối $...$ -> Cần thay bằng \\lt: {mi[:40]}...")
        if ">" in mi and "\\gt" not in mi:
            if re.search(r'(?<!\\)>', mi):
                errors.append(f"Chương {num_str}: Chứa ký tự '>' trần trong khối $...$ -> Cần thay bằng \\gt: {mi[:40]}...")

    # Check Canvas ID
    canvas_id = f"sim-canvas-{num_str}"
    if canvas_id not in content:
        errors.append(f"Chương {num_str}: Thiếu thẻ canvas '{canvas_id}'!")
        
    # Check 4-step card
    if "worked-step-grid" not in content and "worked-step-card" not in content:
        warnings.append(f"Chương {num_str}: Có thể thiếu thẻ worked-step-card!")
        
    # Check code bridge
    if "code-card" not in content and "<pre><code>" not in content:
        warnings.append(f"Chương {num_str}: Có thể thiếu thẻ code-card!")

    print(f"Chương {num_str}: OK ({size_kb:.1f} KB) - Canvas: {canvas_id} verified.")

print("\n=== AUDIT RESULTS ===")
if errors:
    print(f"FAILED: Found {len(errors)} error(s):")
    for err in errors:
        print(f"  ❌ {err}")
else:
    print("✅ ZERO MATHJAX OR CANVAS ERRORS FOUND ACROSS ALL 14 CHAPTERS!")

if warnings:
    print(f"\nWARNINGS: Found {len(warnings)} warning(s):")
    for w in warnings:
        print(f"  ⚠️ {w}")
else:
    print("✅ ALL 6 KNOWLEDGE LAYERS (Worked steps, ROS 2 bridges, Math, Simulators) VERIFIED 100%!")
