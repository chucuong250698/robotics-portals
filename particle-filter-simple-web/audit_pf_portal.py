# -*- coding: utf-8 -*-
"""
Audit script for Particle Filter Made Simple Knowledge Portal (#12)
"""

import os
import re

PORTAL_DIR = r"c:\Users\chucuong\OneDrive\Reading\web-content\particle-filter-simple-web"
CHAPTERS_DIR = os.path.join(PORTAL_DIR, "chapters")

errors = []
warnings = []

# 1. Check files
expected_files = ["index.html", "README.md", "assets/css/style.css", "assets/js/app.js", "assets/js/simulators.js"]
for i in range(1, 6):
    expected_files.append(f"chapters/ch{i:02d}.html")

for rel in expected_files:
    full = os.path.join(PORTAL_DIR, rel)
    if not os.path.exists(full):
        errors.append(f"Missing file: {rel}")
    else:
        size = os.path.getsize(full)
        if size < 500:
            errors.append(f"File too small ({size} bytes): {rel}")

# 2. Check MathJax & Anchors in chapter pages
for i in range(1, 6):
    ch_file = os.path.join(CHAPTERS_DIR, f"ch{i:02d}.html")
    if not os.path.exists(ch_file):
        continue
    with open(ch_file, "r", encoding="utf-8") as f:
        html = f.read()

    # Check unescaped < or > inside math delimiters
    # First extract display math $$...$$
    display_math = re.findall(r'\$\$(.*?)\$\$', html, re.DOTALL)
    for dm in display_math:
        if '<' in dm and not '\\lt' in dm:
            errors.append(f"ch{i:02d}: Raw '<' in display math: {dm[:40]}...")
        if '>' in dm and not '\\gt' in dm:
            errors.append(f"ch{i:02d}: Raw '>' in display math: {dm[:40]}...")

    # Extract inline math $...$
    # Be careful not to match across code blocks or pre tags
    # Remove <pre><code>...</code></pre> first
    cleaned = re.sub(r'<pre.*?</pre>', '', html, flags=re.DOTALL)
    inline_math = re.findall(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', cleaned)
    for im in inline_math:
        if '<' in im and '\\lt' not in im:
            errors.append(f"ch{i:02d}: Raw '<' in inline math: {im}")
        if '>' in im and '\\gt' not in im:
            errors.append(f"ch{i:02d}: Raw '>' in inline math: {im}")

    # Count total $ signs in cleaned text (should be even)
    dollar_count = cleaned.count('$')
    if dollar_count % 2 != 0:
        errors.append(f"ch{i:02d}: Odd dollar count ({dollar_count}) indicates unclosed math delimiter!")

    # Check anchor consistency
    # All href="#sec-..." in sidebar must exist as id="sec-..."
    sidebar_links = re.findall(r'<a href="#(sec-[^"]+)"', html)
    declared_ids = set(re.findall(r'id="(sec-[^"]+)"', html))
    for sl in sidebar_links:
        if sl not in declared_ids:
            errors.append(f"ch{i:02d}: Sidebar anchor '#{sl}' has no matching id='{sl}' in document!")

    # Check canvas simulator ID
    canvas_id = f"sim-canvas-ch{i:02d}"
    if canvas_id not in html:
        errors.append(f"ch{i:02d}: Missing simulator canvas id '{canvas_id}'!")

# 3. Check simulator button IDs
sim_controls = {
    1: ['btn-measure-ch01', 'btn-move-ch01', 'btn-reset-ch01'],
    2: ['btn-step-ch02', 'btn-toggle-ch02', 'btn-reset-ch02', 'slider-n-ch02', 'label-n-ch02'],
    3: ['btn-update-w-ch03', 'btn-resample-ch03', 'btn-reset-ch03'],
    4: ['btn-step-ch04', 'btn-reset-ch04', 'slider-r-ch04', 'label-r-ch04'],
    5: ['btn-patrol-ch05', 'btn-kidnap-ch05', 'btn-reset-ch05']
}

for ch_num, ctrl_ids in sim_controls.items():
    ch_file = os.path.join(CHAPTERS_DIR, f"ch{ch_num:02d}.html")
    with open(ch_file, "r", encoding="utf-8") as f:
        html = f.read()
    for cid in ctrl_ids:
        if f'id="{cid}"' not in html:
            errors.append(f"ch{ch_num:02d}: Missing expected control element id='{cid}'!")

print("=== AUDIT SUMMARY ===")
print(f"Total Errors Found: {len(errors)}")
print(f"Total Warnings:     {len(warnings)}")
if errors:
    print("\n--- DETAILED ERRORS ---")
    for e in errors:
        print(f"❌ {e}")
else:
    print("✅ ALL AUDIT CHECKS PASSED PERFECTLY (0 errors, 0 warnings)!")
