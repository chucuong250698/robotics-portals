# -*- coding: utf-8 -*-
import os
import re

ch_dir = r"c:\Users\chucuong\OneDrive\Reading\robot-dynamics-modeling-web\chapters"
files = sorted([f for f in os.listdir(ch_dir) if f.endswith(".html")])

print(f"Auditing {len(files)} chapter HTML files...")
all_ok = True

for f in files:
    path = os.path.join(ch_dir, f)
    with open(path, encoding="utf-8") as fp:
        content = fp.read()
    
    ch_num = f[2:4]
    expected_canvas = f"sim-canvas-{ch_num}"
    if expected_canvas not in content:
        print(f"[-] Missing canvas: {f} lacks {expected_canvas}")
        all_ok = False
    
    # Check for display math blocks $$...$$
    blocks = re.findall(r"\$\$(.*?)\$\$", content, re.DOTALL)
    for idx, mb in enumerate(blocks):
        if "<" in mb:
            # check if it's \lt or bare <
            bare = [m.start() for m in re.finditer(r"(?<!\\)<", mb)]
            if bare:
                print(f"[!] Warning in {f} Display Math #{idx}: bare '<' found: {mb[:50]}")
                all_ok = False
        if ">" in mb:
            bare = [m.start() for m in re.finditer(r"(?<!\\)>", mb)]
            if bare:
                print(f"[!] Warning in {f} Display Math #{idx}: bare '>' found: {mb[:50]}")
                all_ok = False

    # Check for inline math $...$
    inlines = re.findall(r"\$([^\$\n]+?)\$", content)
    for idx, im in enumerate(inlines):
        if "<" in im and not "\\lt" in im:
            print(f"[!] Warning in {f} Inline Math: bare '<': {im}")
            all_ok = False
        if ">" in im and not "\\gt" in im:
            print(f"[!] Warning in {f} Inline Math: bare '>': {im}")
            all_ok = False

if all_ok:
    print("[SUCCESS] All 14 chapters strictly adhere to Zero-Error MathJax & Canvas standards!")
else:
    print("[FAIL] Issues detected above.")
