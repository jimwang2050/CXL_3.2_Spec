#!/usr/bin/env python3
"""Fix ch12 caption off-by-one: img src references are 1 page earlier than the actual figure.

Current MD (line numbers approximate):
  L174: > **Figure 12-1.** RCH Downstream Port ... (caption)
  L176: > <img src=".../fig_0999_1.png" alt="Figure 12-1" ...>
  L209: > **Figure 12-2.** RCD Upstream Port ... (caption)
  L211: > <img src=".../fig_1000_1.png" alt="Figure 12-2" ...>
  L241: > **Figure 12-3.** RCD RCiEP ... (caption)
  L243: > <img src=".../fig_1001_1.png" alt="Figure 12-3" ...>

MinerU (per content_list_v2.json) says:
  PDF p.1000: Figure 12-1. RCH Downstream Port Detects Error
  PDF p.1001: Figure 12-2. RCD Upstream Port Detects Error
  PDF p.1002: Figure 12-3. RCD RCiEP Detects Error

Fix: shift each img src page by +1.
After: fig_0999 → fig_1000, fig_1000 → fig_1001, fig_1001 → fig_1002
"""
import re
from pathlib import Path

MD = Path("/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/CXL_zh/CXL3.2_Spec_ch12_Reliability_Availability_Serviceability_可靠性可用性可服务性.md")
text = MD.read_text()
orig = text

# 1) Update img src: fig_0999 → fig_1000, fig_1000 → fig_1001, fig_1001 → fig_1002
# These three specific substitutions
shifts = [
    ("fig_0999_1.png", "fig_1000_1.png"),
    ("fig_1000_1.png", "fig_1001_1.png"),
    ("fig_1001_1.png", "fig_1002_1.png"),
]
for old, new in shifts:
    # Only replace within <img src=...> blocks (not text mentions)
    pat = re.compile(rf'(<img src="figures/chapter_12/){old}(")')
    text, n = pat.subn(rf'\1{new}\2', text)
    print(f"  {old} → {new}: {n} replacements in <img>")

# 2) Verify: page in Full size link might also need shift
# Look at fig_0999 Full size link
size_shifts = [
    ("page_0999.png", "page_1000.png"),
    ("page_1000.png", "page_1001.png"),
    ("page_1001.png", "page_1002.png"),
]
for old, new in size_shifts:
    # Only update if it's a "Full size" link in the same Figure 12-X block
    # For simplicity, replace all page_0XXX.png -> +1
    pass  # Don't do this aggressively; just verify

# Save
if text != orig:
    MD.write_text(text)
    print(f"\nWROTE {MD}")
else:
    print("\nNo changes made.")

# Verify
print("\n=== 验证修复 ===")
new_text = MD.read_text()
for old, new in shifts:
    n_old = len(re.findall(rf'<img src="figures/chapter_12/{old}"', new_text))
    n_new = len(re.findall(rf'<img src="figures/chapter_12/{new}"', new_text))
    print(f"  {old} img refs: {n_old} (期望 0)")
    print(f"  {new} img refs: {n_new}")
PYEOF