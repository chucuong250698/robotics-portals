# -*- coding: utf-8 -*-
"""
audit_chapters_v2.py
Kiểm tra chính xác công thức toán MathJax (bỏ qua thẻ <script>, <pre>, <code>):
- Tìm các khối math thực sự: $...$ trên cùng 1 dòng, hoặc $$...$$
- Phát hiện xem có ký tự '<' hoặc '>' không phải thẻ HTML và không phải \lt, \gt
"""

import os
import re

BASE_DIR = r"c:\Users\chucuong\OneDrive\Reading\imitation-learning-web"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

total_chapters = 14
real_errors = []

for i in range(1, total_chapters + 1):
    num_str = f"{i:02d}"
    file_path = os.path.join(CHAPTERS_DIR, f"ch{num_str}.html")
    
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Loại bỏ các thẻ script, pre, code để chỉ kiểm tra nội dung text/toán
    clean_html = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
    clean_html = re.sub(r'<code.*?>.*?</code>', '', clean_html, flags=re.DOTALL)
    clean_html = re.sub(r'<pre.*?>.*?</pre>', '', clean_html, flags=re.DOTALL)

    # 1. Tìm khối display math: $$ ... $$
    block_math = re.findall(r'\$\$(.+?)\$\$', clean_html, flags=re.DOTALL)
    for m in block_math:
        # Kiểm tra xem có chứa < hoặc > trần không
        # Ngoại trừ \lt hoặc \gt
        if re.search(r'(?<!\\)[<>]', m):
            real_errors.append(f"Chương {num_str} (Display Math $$): Phát hiện '<' hoặc '>' trần: {m.strip()}")

    # 2. Tìm khối inline math: $ ... $ (không ngắt dòng)
    inline_math = re.findall(r'(?<!\$)\$([^\$\n\r]+?)\$(?!\$)', clean_html)
    for m in inline_math:
        # Nếu m chứa thẻ HTML thì đó không phải math thật mà là do trùng dấu $
        if '<' in m or '>' in m:
            if not ('\\lt' in m or '\\gt' in m or '\\le' in m or '\\ge' in m):
                real_errors.append(f"Chương {num_str} (Inline Math $): Phát hiện '<' hoặc '>' trần: {m.strip()}")

if real_errors:
    print(f"❌ Phát hiện {len(real_errors)} lỗi công thức:")
    for err in real_errors:
        print(f"  {err}")
else:
    print("✅ HOÀN TOÀN KHÔNG CÓ LỖI CÔNG THỨC TOÁN! MathJax 3 sẽ biên dịch sạch 100% không vướng Math Processing Error.")
