#!/usr/bin/env python3
"""Step 6: Map MinerU images to fig_PPPP_N.png naming + replace de-watermarked.

For each completed batch:
  1. Read content_list_v2.json
  2. Find image blocks per page
  3. Map page_in_batch -> PDF page (1-indexed) using batch's chunk PDF
  4. Name images as fig_PPPP_N.png where N = figure index on page
  5. Copy/save to figures/chapter_XX/ directory
  6. Backup de-watermarked version to .dewatermarked.bak before overwriting

Usage:
  python3 image_mapper.py <mineru_output_dir> [--chapter ch01:62-67] ...

Example:
  python3 image_mapper.py /Users/jianmingwang/_work/ch08_fix/mineru_upgrade/output
"""
import json
import re
import shutil
import sys
import argparse
from pathlib import Path
from collections import defaultdict
from PIL import Image

REPO = Path("/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/CXL_zh")
FIG_ROOT = REPO / "figures"

# Mapping: (chapter_name, page_start, page_end) for each batch
# This mirrors the chunk_pdf name → PDF page range
def parse_chunk_filename(name):
    """Parse 'sub_ch01_p0062-p0067' or 'sub_ch01b_p0068' -> ('chapter_01', pmin, pmax)"""
    # Match either range (62-67) or single page (68)
    m = re.match(r"(?:sub_)?(ch\d+)[a-z]?_(?:p)?(\d+)(?:-p?(\d+))?", name)
    if not m:
        return None
    ch_short = m.group(1)
    pmin = int(m.group(2))
    pmax = int(m.group(3)) if m.group(3) else pmin  # single page
    chapter = f"chapter_{ch_short[2:]}"
    return (chapter, pmin, pmax)

def find_batch_outputs(output_dir):
    """Find all completed batch output directories."""
    batches = []
    if not output_dir.exists():
        return batches
    for d in sorted(output_dir.iterdir()):
        if not d.is_dir():
            continue
        parsed = parse_chunk_filename(d.name)
        if not parsed:
            continue
        chapter, pmin, pmax = parsed
        # Check if it has expected content
        has_content = any(d.glob("*_content_list*.json"))
        if has_content:
            batches.append((d, chapter, pmin, pmax))
    return batches

def extract_images_from_batch(batch_dir, page_start):
    """Extract all images from a batch with their page mapping.

    Returns: list of (pdf_page, fig_index_on_page, image_path, caption)
    """
    cl = next(batch_dir.glob("*_content_list_v2.json"), None)
    if not cl:
        cl = next(batch_dir.glob("*_content_list.json"), None)
    if not cl:
        return []

    with open(cl) as f:
        data = json.load(f)

    results = []
    for page_idx, page_blocks in enumerate(data):
        pdf_page = page_start + page_idx
        fig_idx = 0
        for block in page_blocks:
            if not isinstance(block, dict) or block.get("type") != "image":
                continue
            fig_idx += 1
            content = block.get("content", {})
            image_source = content.get("image_source", {})
            img_rel_path = image_source.get("path", "")
            if not img_rel_path:
                continue
            img_path = batch_dir / img_rel_path
            if not img_path.exists():
                continue
            # Extract caption
            caption = ""
            cap_list = content.get("image_caption", [])
            for c in cap_list:
                if c.get("type") == "text":
                    caption += c.get("content", "")
            results.append((pdf_page, fig_idx, img_path, caption.strip()))
    return results

def save_tight_crop(img_path, fig_target, caption=None, dry_run=False):
    """Save image to fig_target path, converting JPG -> PNG if needed."""
    if dry_run:
        return True
    try:
        img = Image.open(img_path).convert("RGB")
        fig_target.parent.mkdir(parents=True, exist_ok=True)
        # Backup existing de-watermarked version
        if fig_target.exists():
            bak = fig_target.with_suffix(fig_target.suffix + ".dewatermarked.bak")
            if not bak.exists():
                shutil.copy2(fig_target, bak)
        img.save(fig_target, "PNG", optimize=True)
        return True
    except Exception as e:
        print(f"  ERROR saving {fig_target}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path, help="MinerU output dir")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--chapter", action="append", help="Filter: ch01 or ch01:62-67")
    args = parser.parse_args()

    batches = find_batch_outputs(args.output_dir)
    if not batches:
        print(f"No completed batches in {args.output_dir}")
        sys.exit(1)

    print(f"Found {len(batches)} completed batches")
    print()

    total_imgs = 0
    for batch_dir, chapter, pmin, pmax in batches:
        print(f"=== {batch_dir.name} ===")
        print(f"  chapter: {chapter}, pages: {pmin}-{pmax}")
        imgs = extract_images_from_batch(batch_dir, pmin)
        print(f"  extracted: {len(imgs)} images")

        # Group by pdf_page
        by_page = defaultdict(list)
        for pdf_page, fig_idx, img_path, caption in imgs:
            by_page[pdf_page].append((fig_idx, img_path, caption))

        for pdf_page in sorted(by_page):
            for fig_idx, img_path, caption in by_page[pdf_page]:
                target = FIG_ROOT / chapter / f"fig_{pdf_page:04d}_{fig_idx}.png"
                caption_short = caption[:60] + "..." if len(caption) > 60 else caption
                status = "WOULD SAVE" if args.dry_run else "saved"
                if save_tight_crop(img_path, target, caption, args.dry_run):
                    print(f"  p.{pdf_page}.{fig_idx}  {img_path.suffix} -> {target.name}  ({caption_short})  [{status}]")
                    total_imgs += 1
        print()

    print(f"Total: {total_imgs} images {'would be saved' if args.dry_run else 'saved'}")

if __name__ == "__main__":
    main()
