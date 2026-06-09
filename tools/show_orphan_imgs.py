#!/usr/bin/env python3
"""Show examples of 163 'orphan' images (saved by MinerU but not referenced in MD)."""
import json
import re
from pathlib import Path

# Find all orphan images (in fig_*.png but not in MD src)
ORPHAN_FILES = [
    ("chapter_02", "fig_0074_1.png"),
    ("chapter_02", "fig_0075_1.png"),
    ("chapter_03", "fig_0092_1.png"),
    ("chapter_03", "fig_0175_1.png"),
    ("chapter_03", "fig_0176_1.png"),
    ("chapter_06", "fig_0310_1.png"),
    ("chapter_07", "fig_0393_1.png"),
    ("chapter_07", "fig_0405_1.png"),
    ("chapter_07", "fig_0407_1.png"),
    ("chapter_07", "fig_0408_1.png"),
    ("chapter_07", "fig_0409_1.png"),
    ("chapter_08", "fig_0556_1.png"),
    ("chapter_08", "fig_0557_1.png"),
    ("chapter_08", "fig_0558_1.png"),
    ("chapter_08", "fig_0559_1.png"),
    ("chapter_08", "fig_0560_1.png"),
    ("chapter_10", "fig_0881_1.png"),
    ("chapter_14", "fig_1194_1.png"),
    ("chapter_14", "fig_1215_1.png"),
]

WORK = Path("/Users/jianmingwang/_work/ch08_fix/mineru_upgrade/output")

# Find which batch each image came from by filename hint
batch_map = {
    "0074": "sub_ch02", "0075": "sub_ch02",
    "0085": "sub_ch03", "0087": "sub_ch03", "0090": "sub_ch03", "0092": "sub_ch03",
    "0175": "sub_ch03", "0176": "sub_ch03", "0177": "sub_ch03", "0178": "sub_ch03",
    "0287": "sub_ch06", "0290": "sub_ch06", "0310": "sub_ch06",
    "0319": "sub_ch07a", "0393": "sub_ch07a", "0405": "sub_ch07a", "0407": "sub_ch07a",
    "0408": "sub_ch07b", "0409": "sub_ch07b",
    "0556": "sub_ch08a", "0557": "sub_ch08a", "0558": "sub_ch08a", "0559": "sub_ch08a",
    "0560": "sub_ch08a", "0561": "sub_ch08a",
    "0881": "sub_ch10",
    "1194": "sub_ch14", "1215": "sub_ch14",
}

# Find the content_list.json for each batch
def get_caption_from_batch(page_str, batch_name):
    """Find the content_list.json that contains this page, return image caption."""
    # The output dir has subdirectories like sub_ch07a_p0319-p0408
    batch_dirs = list(WORK.glob(f"{batch_name}_p*"))
    for bd in batch_dirs:
        # Find content list
        cl_files = list(bd.glob("*_content_list_v2.json"))
        if not cl_files:
            continue
        cl = json.load(open(cl_files[0]))
        # data is list of pages (0-indexed)
        # First page in batch is at page_start
        # Find batch's page range from dir name
        m = re.match(r"sub_ch\d+[a-z]?_p(\d+)-p(\d+)", bd.name)
        if not m:
            continue
        p_start = int(m.group(1))
        # page_str is in 4-digit format
        page_int = int(page_str)
        if page_int < p_start:
            continue
        # Find the next batch boundary
        page_idx = page_int - p_start
        if page_idx >= len(cl):
            continue
        page_blocks = cl[page_idx]
        for block in page_blocks:
            if isinstance(block, dict) and block.get("type") == "image":
                cap_list = block.get("content", {}).get("image_caption", [])
                if cap_list:
                    return cap_list[0].get("content", "")[:100]
    return None

# Now show examples
for ch_dir, fn in ORPHAN_FILES[:20]:
    page_str = fn.split('_')[1]
    batch_name = batch_map.get(page_str, "?")
    fig_path = REPO = Path("figures") / ch_dir / fn
    if not fig_path.exists():
        print(f"\n  [missing] {ch_dir}/{fn}")
        continue
    size_kb = fig_path.stat().st_size / 1024
    caption = get_caption_from_batch(page_str, batch_name)
    print(f"\n  [{ch_dir}/{fn}] {size_kb:.0f}KB")
    if caption:
        print(f"    MinerU 标题: {caption!r}")
    else:
        print(f"    MinerU 标题: (no caption extracted)")
