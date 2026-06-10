#!/usr/bin/env python3
"""Build ch08 page→figure_title map from raw texts (handles multi-line captions).

Output: /tmp/ch08_figs.json
"""
import re
import json
from pathlib import Path

REPO = Path("/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/CXL_zh")
OUT = Path("/tmp/ch08_figs.json")

all_figs = {}

for raw_file in ["chapter_08a_raw.txt", "chapter_08b_raw.txt", "chapter_08c_raw.txt", "chapter_08d_raw.txt"]:
    text = (REPO / raw_file).read_text()
    pages = re.split(r"^=+\s*PAGE\s+(\d+)\s*=+\s*$", text, flags=re.MULTILINE)
    for i in range(1, len(pages), 2):
        page_num = int(pages[i])
        content = pages[i+1] if i+1 < len(pages) else ""
        for m in re.finditer(r"^Figure 8-(\d+)\.\s*$", content, re.MULTILINE):
            fig_num = int(m.group(1))
            pos = m.end()
            rest = content[pos:].lstrip('\n')
            title_lines = []
            for line in rest.split('\n')[:3]:
                line = line.strip()
                if not line:
                    break
                if line.startswith('Figure ') or line.startswith('Table ') or line.startswith('====='):
                    break
                title_lines.append(line)
                if len(title_lines) >= 1 and not line.endswith('.'):
                    break
            title = ' '.join(title_lines[:2]).strip().rstrip('.')
            all_figs.setdefault(page_num, []).append((fig_num, title))

OUT.write_text(json.dumps({str(k): v for k, v in all_figs.items()}, ensure_ascii=False, indent=2))

print(f"Total pages: {len(all_figs)}, total entries: {sum(len(v) for v in all_figs.values())}")
print(f"Saved to {OUT}")
print()
for p in sorted(all_figs.keys()):
    if 556 <= p <= 620:
        print(f"  p.{p}: {all_figs[p]}")
print()
for p in sorted(all_figs.keys()):
    if 621 <= p <= 700:
        print(f"  p.{p}: {all_figs[p]}")
print()
for p in sorted(all_figs.keys()):
    if 701 <= p <= 798:
        print(f"  p.{p}: {all_figs[p]}")
