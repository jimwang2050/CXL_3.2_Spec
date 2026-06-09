#!/usr/bin/env python3
"""Scan all 808 newly-upgraded images and check their MD references."""
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

stats = defaultdict(lambda: {"with_caption": 0, "placeholder_alt": 0, "not_in_md": 0, "total": 0})
examples = defaultdict(list)

for ch_dir_name, md_name in NEW_CHAPTERS:
    fig_dir = Path("figures") / ch_dir_name
    md_path = Path(md_name)
    if not md_path.exists():
        print(f"  {ch_dir_name}: MD missing")
        continue
    md_text = md_path.read_text()

    for f in sorted(fig_dir.glob("fig_*_1.png")):
        page = int(f.stem.split('_')[1])
        n = int(f.stem.split('_')[2])
        src_pat = re.compile(rf'src="figures/{ch_dir_name}/fig_{page:04d}_{n}\.png"')
        src_match = src_pat.search(md_text)
        stats[ch_dir_name]["total"] += 1
        if not src_match:
            stats[ch_dir_name]["not_in_md"] += 1
            if len(examples[ch_dir_name + "_not"]) < 3:
                examples[ch_dir_name + "_not"].append(f"fig_{page:04d}_{n}.png")
        else:
            alt_pat = re.compile(rf'<img src="figures/{ch_dir_name}/fig_{page:04d}_{n}\.png" alt="([^"]*)"')
            alt_match = alt_pat.search(md_text)
            if alt_match:
                alt = alt_match.group(1)
                # Placeholder alt = starts with Page/page, or no | separator, or short
                if re.match(r'^(Page|page|图|table)[\s_-]?\d', alt) or ('|' not in alt and len(alt) < 30):
                    stats[ch_dir_name]["placeholder_alt"] += 1
                    if len(examples[ch_dir_name + "_ph"]) < 3:
                        examples[ch_dir_name + "_ph"].append((f"fig_{page:04d}_{n}.png", alt))
                else:
                    stats[ch_dir_name]["with_caption"] += 1

print(f"\n{'Chapter':14} {'Total':>6} {'WithCap':>8} {'PlaceAlt':>9} {'NotInMD':>9}")
print("-" * 56)
total_all = 0
total_with = 0
total_ph = 0
total_not = 0
for ch_dir_name, _ in NEW_CHAPTERS:
    s = stats[ch_dir_name]
    print(f"{ch_dir_name:14} {s['total']:>6} {s['with_caption']:>8} {s['placeholder_alt']:>9} {s['not_in_md']:>9}")
    total_all += s["total"]
    total_with += s["with_caption"]
    total_ph += s["placeholder_alt"]
    total_not += s["not_in_md"]
print("-" * 56)
print(f"{'TOTAL':14} {total_all:>6} {total_with:>8} {total_ph:>9} {total_not:>9}")

print("\n=== 占位 alt 示例 (前 10) ===")
for key, exs in list(examples.items())[:10]:
    if exs:
        print(f"  {key}: {exs[:3]}")

print("\n=== 未引用示例 (前 5) ===")
for key, exs in list(examples.items())[:5]:
    if 'not' in key and exs:
        print(f"  {key}: {exs}")
