#!/usr/bin/env python3
"""Optimize ch08 placeholder captions: replace 3 with real titles, 275 with better text.

Reads:
  - /tmp/ch08_figs.json (from extract_ch08_figs.py)
  - CXL3.2_Spec_ch08_Control_and_Status_Registers_控制与状态寄存器.md

Strategy:
  1. For each placeholder "(p.NNNN 图, MinerU 未提取标题, 见 fig_NNNN.png)":
     a. If page NNNN has a Figure 8-NN. title in JSON map, use it
     b. Else, replace with: "(spec 内容为 Table 或 sequence diagram, MinerU 未提取 Figure 8-NN 标题, 见 fig_NNNN.png)"
     c. The "**Figure p.NNNN.**" prefix also updates to "**Figure 8-NN.**" if title found, or "**Figure p.NNNN.**" otherwise

Also updates the alt tag in the <img> line.
"""
import re
import json
from pathlib import Path

MD = Path("/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/CXL_zh/CXL3.2_Spec_ch08_Control_and_Status_Registers_控制与状态寄存器.md")
FIGS = json.load(open("/tmp/ch08_figs.json"))

text = MD.read_text()
orig = text

# Build page -> (fig_num, title) map
page_to_fig = {int(k): v[0] for k, v in FIGS.items()}  # only first title per page

# Find each placeholder and replace
# Pattern: "**Figure p.NNNN.** (p.NNNN 图, MinerU 未提取标题, 见 fig_NNNN.png)"
n_real_title = 0
n_better_placeholder = 0

def replace_placeholder(match):
    global n_real_title, n_better_placeholder
    page = int(match.group(1))
    page_str = f"{page:04d}"
    fig_file = f"fig_{page_str}_1.png"
    full_placeholder = match.group(0)

    if page in page_to_fig:
        # Use real title
        fig_num, title = page_to_fig[page]
        n_real_title += 1
        return f"**Figure 8-{fig_num}.** {title} (extracted from p.{page_str} via MinerU)"
    else:
        # Better placeholder
        n_better_placeholder += 1
        return f"**Figure p.{page_str}.** (spec 内容为 Table 或 sequence diagram, MinerU 未提取 Figure 8-NN 标题, 见 {fig_file})"

# Pattern 1: **Figure p.NNNN.** (p.NNNN 图, MinerU 未提取标题, 见 fig_NNNN.png)
pat1 = re.compile(r"\*\*Figure p\.(\d{4})\.\*\* \(p\.\1 图, MinerU 未提取标题, 见 fig_\1_1\.png\)")
text, _ = pat1.subn(replace_placeholder, text)

# Pattern 2: alt="(p.NNNN 图, MinerU 未提取标题, 见 fig_NNNN.png)"
def replace_alt(match):
    page = int(match.group(1))
    page_str = f"{page:04d}"
    fig_file = f"fig_{page_str}_1.png"
    if page in page_to_fig:
        fig_num, title = page_to_fig[page]
        return f'alt="Figure 8-{fig_num}: {title} (p.{page_str} via MinerU)"'
    else:
        return f'alt="(spec Table/sequence diagram, see {fig_file})"'

pat2 = re.compile(r'alt="\(p\.(\d{4}) 图, MinerU 未提取标题, 见 fig_\1_1\.png\)"')
text, _ = pat2.subn(replace_alt, text)

# Also handle "> **Figure p.NNNN.** (... 见 fig_NNNN.png)" pattern (alt at top of blockquote)
# This is the caption line itself
# Already handled in pat1

if text != orig:
    MD.write_text(text)
    print(f"WROTE {MD}")
    print(f"  real titles: {n_real_title}")
    print(f"  better placeholders: {n_better_placeholder}")
else:
    print("No changes")
