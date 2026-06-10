#!/usr/bin/env python3
"""Fix ch10 Figure 10-1: replace .jpx (15KB mostly-blank) with .png (300KB MinerU tight crop).

Steps:
  1. Verify .png file exists with reasonable size
  2. Update main body line 373 <img src=...>
  3. Update main body line 375 Full size link
  4. Remove duplicate from orphan section (line 1025-1029)
"""
import re
from pathlib import Path

MD = Path("/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/CXL_zh/CXL3.2_Spec_ch10_Power_Management_电源管理.md")
JPX = MD.parent / "figures" / "chapter_10" / "fig_0881_1.jpx"
PNG = MD.parent / "figures" / "chapter_10" / "fig_0881_1.png"

# Verify PNG exists and is reasonable
assert PNG.exists(), f"PNG not found: {PNG}"
png_size = PNG.stat().st_size
print(f"PNG: {PNG.name} = {png_size:,} bytes")
assert png_size > 50_000, f"PNG too small: {png_size}"
print(f"JPX: {JPX.name} = {JPX.stat().st_size:,} bytes (old, will be kept as backup)")

text = MD.read_text()
orig = text

# 1) Replace .jpx with .png in main body (specific line range 370-380)
lines = text.splitlines(keepends=True)
n_main = 0
for i in range(370, min(380, len(lines))):
    if 'fig_0881_1.jpx' in lines[i]:
        lines[i] = lines[i].replace('fig_0881_1.jpx', 'fig_0881_1.png')
        n_main += 1
        print(f"  line {i+1}: replaced jpx → png")

# 2) Remove duplicate from orphan section (lines 1025-1029)
n_orphan = 0
for i in range(1023, min(1032, len(lines))):
    if 'fig_0881_1' in lines[i]:
        # Mark for removal by replacing with empty line
        lines[i] = ''
        n_orphan += 1
        print(f"  cleared orphan line {i+1}")

text = ''.join(lines)

if n_main + n_orphan > 0:
    MD.write_text(text)
    print(f"\nWROTE: {n_main} main + {n_orphan} orphan cleared")
else:
    print("\nNo changes")

# Verify
text = MD.read_text()
print("\n=== 最终 fig_0881_1 引用 ===")
for m in re.finditer(r'<img src="figures/chapter_10/fig_0881_1\.(\w+)"', text):
    print(f"  {m.group(0)}")
print("\n=== Full size 链接 ===")
for m in re.finditer(r'\[📄 Full size\]\(([^)]+fig_0881_1[^)]+)\)', text):
    print(f"  {m.group(0)}")
