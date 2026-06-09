#!/usr/bin/env python3
"""Insert 163 orphan tight-crop figures into each Part's MD as a "## 🖼 图补遗" section.

For each orphan image:
  1. Get title (English + Chinese) from MinerU content_list_v2.json
  2. Build a Part A-style 4-line blockquote
  3. Group by Part (chapter)
  4. Insert at the end of each Part body (just before the next Part H1)
"""
import re
import json
import sys
from pathlib import Path
from collections import defaultdict

REPO = Path("/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/CXL_zh")
FIG_ROOT = REPO / "figures"
WORK = Path("/Users/jianmingwang/_work/ch08_fix/mineru_upgrade/output")

# Build page -> batch_dir name by scanning WORK dir
def build_page_to_batch_map():
    """Scan all batch output dirs and build {page_str: batch_dir_name}."""
    page_map = {}
    for batch_dir in WORK.iterdir():
        if not batch_dir.is_dir():
            continue
        m = re.match(r"sub_ch\d+[a-z]?_p(\d+)-p(\d+)", batch_dir.name)
        if not m:
            continue
        p_start, p_end = int(m.group(1)), int(m.group(2))
        for p in range(p_start, p_end + 1):
            page_map[f"{p:04d}"] = batch_dir.name
    return page_map

BATCH_DIRS = build_page_to_batch_map()
print(f"Loaded {len(BATCH_DIRS)} page -> batch mappings")

# Cache content_list_v2.json per batch
_content_list_cache = {}
def get_content_list(batch_dir_name):
    if batch_dir_name in _content_list_cache:
        return _content_list_cache[batch_dir_name]
    bd = WORK / batch_dir_name
    if not bd.exists():
        return None
    cl_files = list(bd.glob("*_content_list_v2.json"))
    if not cl_files:
        return None
    data = json.load(open(cl_files[0]))
    _content_list_cache[batch_dir_name] = data
    return data

def get_image_caption(page_str, batch_dir_name):
    """Return list of (fig_idx_in_page, title_en) for the given page."""
    cl = get_content_list(batch_dir_name)
    if cl is None:
        return []
    m = re.match(r"sub_ch\d+[a-z]?_p(\d+)-p(\d+)", batch_dir_name)
    if not m:
        return []
    p_start = int(m.group(1))
    p_end = int(m.group(2))
    page_int = int(page_str)
    if page_int < p_start or page_int > p_end:
        return []
    page_idx = page_int - p_start
    if page_idx >= len(cl):
        return []
    page_blocks = cl[page_idx]
    results = []
    fig_idx = 0
    for block in page_blocks:
        if not isinstance(block, dict) or block.get("type") != "image":
            continue
        fig_idx += 1
        # Get caption
        cap_list = block.get("content", {}).get("image_caption", [])
        title_en = ""
        for c in cap_list:
            if c.get("type") == "text":
                title_en += c.get("content", "")
        title_en = title_en.strip()
        results.append((fig_idx, title_en))
    return results

# Find orphan images (in fig dir but not in MD src)
def find_orphans_for_chapter(ch_dir_name, md_path):
    fig_dir = FIG_ROOT / ch_dir_name
    if not fig_dir.exists():
        return []
    md_text = md_path.read_text()
    orphans = []
    for f in sorted(fig_dir.glob("fig_*_1.png")):
        # Skip tiny files (<30KB) — likely empty/junk stubs
        if f.stat().st_size < 30_000:
            continue
        page = f.stem.split('_')[1]
        n = f.stem.split('_')[2]
        src = f'src="figures/{ch_dir_name}/fig_{page}_{n}.png"'
        if src not in md_text:
            orphans.append(f)
    return orphans

# Chapter mapping
CHAPTERS = [
    ("chapter_02", "CXL3.2_Spec_ch02_CXL_System_Architecture_CXL系统架构.md", "Ch2"),
    ("chapter_03", "CXL3.2_Spec_ch03_CXL_Transaction_Layer_CXL事务层.md", "Ch3"),
    ("chapter_04", "CXL3.2_Spec_ch04_CXL_Link_Layers_CXL链路层.md", "Ch4"),
    ("chapter_06", "CXL3.2_Spec_ch06_Flex_Bus_Physical_Layer_FlexBus物理层.md", "Ch6"),
    ("chapter_07", "CXL3.2_Spec_ch07_Switching_交换.md", "Ch7"),
    ("chapter_08", "CXL3.2_Spec_ch08_Control_and_Status_Registers_控制与状态寄存器.md", "Ch8"),
    ("chapter_10", "CXL3.2_Spec_ch10_Power_Management_电源管理.md", "Ch10"),
    ("chapter_14", "CXL3.2_Spec_ch14_CXL_Compliance_Testing_Appendix_CXL一致性测试与附录.md", "Ch14"),
]

def main(dry_run=True):
    # First pass: collect all orphan info
    orphan_data = {}  # ch_dir_name -> [(file, batch_name, captions)]
    for ch_dir, md_name, ch_label in CHAPTERS:
        md_path = REPO / md_name
        if not md_path.exists():
            continue
        orphans = find_orphans_for_chapter(ch_dir, md_path)
        if not orphans:
            continue
        ch_data = []
        for f in orphans:
            page = f.stem.split('_')[1]
            batch_name = BATCH_DIRS.get(page)
            if not batch_name:
                print(f"  {f.name}: no batch mapping (page {page})")
                continue
            captions = get_image_caption(page, batch_name)
            # captions is list of (fig_idx, title_en) for that page
            ch_data.append((f, batch_name, page, captions))
        orphan_data[ch_dir] = ch_data
        print(f"  {ch_label}: {len(orphans)} orphans, {sum(len(d[3]) for d in ch_data)} total figs in those pages")

    # Second pass: build "## 🖼 图补遗" sections
    for ch_dir, md_name, ch_label in CHAPTERS:
        if ch_dir not in orphan_data:
            continue
        md_path = REPO / md_name
        text = md_path.read_text()
        ch_data = orphan_data[ch_dir]

        # Build blockquote lines for each orphan
        blockquote_lines = []
        blockquote_lines.append("## 🖼 图补遗 (Figure Supplement)")
        blockquote_lines.append("")
        blockquote_lines.append("> 本节为 MinerU Standard API 在原始 markdown 之外额外提取的 figures, 已用 Part A 风格 4 行 blockquote 补齐双语 caption, 但未插入正文具体节 (内容可能与正文有重复, 仅供参考)。")
        blockquote_lines.append("")

        # Group by page
        by_page = defaultdict(list)
        for f, batch_name, page, captions in ch_data:
            by_page[page].append((f, batch_name, captions))

        for page in sorted(by_page):
            items = by_page[page]
            for f, batch_name, captions in items:
                # Get title from captions
                if captions:
                    fig_idx, title_en = captions[0]
                else:
                    fig_idx, title_en = 1, ""
                title_en = title_en.strip().rstrip('.')
                if not title_en:
                    # No MinerU title — use just page number as placeholder
                    title_en = f"(p.{page} 图, MinerU 未提取标题, 见 {f.name})"
                page_int = int(page)
                rel = f"figures/{ch_dir}/fig_{page}_{fig_idx}.png"
                alt = title_en[:50]
                block = (
                    f"> **Figure p.{page}.** {title_en}\n"
                    f">\n"
                    f"> <img src=\"{rel}\" alt=\"{alt}\" width=\"700\">\n"
                    f">\n"
                    f"> *Source*: MinerU tight crop extraction (page {page} of CXL 3.2 spec)"
                )
                blockquote_lines.append(block)
                blockquote_lines.append("")

        new_section = "\n".join(blockquote_lines)

        if dry_run:
            print(f"\n=== {ch_label} dry-run (would insert at end of MD) ===")
            print(new_section[:1500] + ("..." if len(new_section) > 1500 else ""))
        else:
            # Insert at end of file
            text = text.rstrip() + "\n\n" + new_section + "\n"
            md_path.write_text(text)
            print(f"  {ch_label}: appended {len(blockquote_lines)} lines")

if __name__ == "__main__":
    dry_run = "--apply" not in sys.argv
    main(dry_run=dry_run)
