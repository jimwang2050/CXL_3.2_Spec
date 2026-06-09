#!/usr/bin/env python3
"""Re-scan: check if a proper caption is nearby (blockquote or table cell),
not just inside alt tag.
"""
import re
import sys
from pathlib import Path
from collections import defaultdict

NEW_CHAPTERS = [
    ("chapter_02", "CXL3.2_Spec_ch02_CXL_System_Architecture_CXL系统架构.md"),
    ("chapter_03", "CXL3.2_Spec_ch03_CXL_Transaction_Layer_CXL事务层.md"),
    ("chapter_04", "CXL3.2_Spec_ch04_CXL_Link_Layers_CXL链路层.md"),
    ("chapter_06", "CXL3.2_Spec_ch06_Flex_Bus_Physical_Layer_FlexBus物理层.md"),
    ("chapter_07", "CXL3.2_Spec_ch07_Switching_交换.md"),
    ("chapter_08", "CXL3.2_Spec_ch08_Control_and_Status_Registers_控制与状态寄存器.md"),
    ("chapter_10", "CXL3.2_Spec_ch10_Power_Management_电源管理.md"),
    ("chapter_14", "CXL3.2_Spec_ch14_CXL_Compliance_Testing_Appendix_CXL一致性测试与附录.md"),
]

stats = defaultdict(lambda: {"with_blockquote": 0, "with_table_caption": 0, "no_caption": 0, "not_in_md": 0, "total": 0})
examples = defaultdict(list)

for ch_dir_name, md_name in NEW_CHAPTERS:
    fig_dir = Path("figures") / ch_dir_name
    md_path = Path(md_name)
    if not md_path.exists():
        continue
    md_text = md_path.read_text()
    lines = md_text.splitlines()

    for f in sorted(fig_dir.glob("fig_*_1.png")):
        page = int(f.stem.split('_')[1])
        n = int(f.stem.split('_')[2])
        stats[ch_dir_name]["total"] += 1
        # Find the line with the img src
        line_idx = None
        for i, line in enumerate(lines):
            if f'figures/{ch_dir_name}/fig_{page:04d}_{n}.png' in line and '<img' in line:
                line_idx = i
                break
        if line_idx is None:
            stats[ch_dir_name]["not_in_md"] += 1
            if len(examples[ch_dir_name + "_not"]) < 5:
                examples[ch_dir_name + "_not"].append(f"fig_{page:04d}_{n}.png")
            continue
        # Check 2 lines above for Part A blockquote caption (Figure or Table)
        if line_idx >= 2:
            above = lines[line_idx - 2]
            if re.match(r'^> \*\*(Figure|Table) ', above):
                stats[ch_dir_name]["with_blockquote"] += 1
                continue
        # Check if inside a table cell (look up for | N | title | page | <img>)
        for j in range(max(0, line_idx-3), line_idx):
            if '|' in lines[j] and 'Figure' in lines[j] and '｜' in lines[j]:
                stats[ch_dir_name]["with_table_caption"] += 1
                break
        else:
            stats[ch_dir_name]["no_caption"] += 1
            if len(examples[ch_dir_name + "_nc"]) < 5:
                examples[ch_dir_name + "_nc"].append(f"fig_{page:04d}_{n}.png")

print(f"\n{'Chapter':14} {'Total':>6} {'BlockQ':>7} {'Table':>6} {'NoCap':>6} {'NotInMD':>9}")
print("-" * 60)
total = 0
total_with = 0
total_nocap = 0
total_not = 0
for ch_dir_name, _ in NEW_CHAPTERS:
    s = stats[ch_dir_name]
    with_cap = s["with_blockquote"] + s["with_table_caption"]
    print(f"{ch_dir_name:14} {s['total']:>6} {s['with_blockquote']:>7} {s['with_table_caption']:>6} {s['no_caption']:>6} {s['not_in_md']:>9}")
    total += s["total"]
    total_with += with_cap
    total_nocap += s["no_caption"]
    total_not += s["not_in_md"]
print("-" * 60)
print(f"{'TOTAL':14} {total:>6} {'':>7} {'':>6} {total_nocap:>6} {total_not:>9}")
print(f"\nTotal with caption: {total_with}/{total} ({100*total_with/total:.1f}%)")
print(f"Total need caption:  {total_nocap} (no_caption)")
print(f"Total not in MD:     {total_not}")

print("\n=== no_caption 示例 ===")
for key, exs in list(examples.items())[:10]:
    if 'nc' in key and exs:
        print(f"  {key}: {exs[:5]}")

print("\n=== not_in_md 示例 ===")
for key, exs in list(examples.items())[:10]:
    if 'not' in key and exs:
        print(f"  {key}: {exs[:5]}")
