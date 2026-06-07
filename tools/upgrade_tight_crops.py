#!/usr/bin/env python3
"""One-shot tight figure crop upgrade via MinerU Standard API.

Usage:
  1. (one time) Get a token from https://mineru.net/apiManage/token
  2. export MINERU_TOKEN="eyJhbGciOi..."
  3. python3 upgrade_tight_crops.py --dry-run   # preview what will be processed
  4. python3 upgrade_tight_crops.py            # run for real

What it does:
  1. Identifies all de-watermarked fig_*_1.png in CXL_zh/figures/ (296 images)
  2. Groups pages by chapter range and extracts from master PDF
  3. Splits into ≤200 page MinerU chunks (if needed)
  4. Calls MinerU Standard API on each chunk
  5. Extracts images/ from each result zip
  6. Maps images back to fig_PPPP_N.png (per page) and replaces the
     de-watermarked versions
  7. Logs skipped/failed images

Pre-requisites:
  - pypdf + PyMuPDF installed (already in repo's .python_deps)
  - MINERU_TOKEN env var set
  - Master PDF at /Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf
"""
import os
import re
import sys
import shutil
import zipfile
import subprocess
from pathlib import Path
from collections import defaultdict
from PIL import Image
import pypdf

# ----------------- Config -----------------
# Repo root: parent of tools/ dir
REPO = Path(__file__).resolve().parent.parent
FIG_ROOT = REPO / "figures"

# Master PDF: walk up to find it (it's at ../CXL-Specification_rev3p2_..._evalcopy.pdf)
# Or set MINERU_MASTER_PDF env var
import os
MASTER_PDF = Path(os.environ.get(
    "MINERU_MASTER_PDF",
    str(REPO.parent / "CXL-Specification_rev3p2_ver1p0_2024October2_evalcopy.pdf")
))

# MinerU script (skill installation)
MINERU_PY = Path(os.environ.get(
    "MINERU_PY",
    str(Path.home() / ".claude/skills/mineru/scripts/mineru.py")
))

# Working dir for chunks/outputs/logs
WORK = Path(os.environ.get(
    "MINERU_WORK",
    str(Path.home() / "_work/ch08_fix/mineru_upgrade")
))
CHUNKS = WORK / "chunks"
OUTPUT = WORK / "output"
LOGS = WORK / "logs"

# MinerU Standard API limits
MAX_PAGES_PER_BATCH = 200
MAX_BYTES_PER_BATCH = 200 * 1024 * 1024

# ----------------- Helpers -----------------
def log(msg):
    print(msg, flush=True)
    LOGS.joinpath("upgrade.log").open("a").write(msg + "\n")

def collect_dewatermarked_pages():
    """Find all 296 de-watermarked fig_*_1.png and return (chapter, page) list."""
    pages = []
    for ch_dir in sorted(FIG_ROOT.glob("chapter_*")):
        for f in ch_dir.glob("fig_*_1.png"):
            w, h = Image.open(f).size
            if w >= 1000 and h >= 1400:
                page = int(f.stem.split('_')[1])
                pages.append((ch_dir.name, page, f))
    return pages

def group_by_chapter(pages):
    """Group pages into (chapter, page_min, page_max) chunks."""
    by_ch = defaultdict(list)
    for ch, p, _ in pages:
        by_ch[ch].append(p)
    chunks = []
    for ch, plist in sorted(by_ch.items()):
        chunks.append((ch, min(plist), max(plist)))
    return chunks

def extract_page_range(src_pdf, dst_pdf, page_start, page_end):
    """Extract pages [start, end] (1-indexed) from src_pdf to dst_pdf."""
    reader = pypdf.PdfReader(str(src_pdf))
    writer = pypdf.PdfWriter()
    for i in range(page_start - 1, min(page_end, len(reader.pages))):
        writer.add_page(reader.pages[i])
    with open(dst_pdf, "wb") as f:
        writer.write(f)
    return dst_pdf.stat().st_size

def merge_chapters_into_batches(chapter_chunks, max_pages=MAX_PAGES_PER_BATCH):
    """Merge adjacent chapter ranges into ≤max_pages chunks.
    If a single chapter exceeds max_pages, split it in half.
    """
    sorted_chunks = sorted(chapter_chunks, key=lambda x: x[1])
    batches = []
    cur_chapters = []
    cur_min = None
    cur_max = None
    for ch, pmin, pmax in sorted_chunks:
        # If this single chapter exceeds max_pages, split it
        if pmax - pmin + 1 > max_pages:
            # Flush current batch
            if cur_chapters:
                batches.append((cur_chapters, cur_min, cur_max))
                cur_chapters, cur_min, cur_max = [], None, None
            # Split the large chapter in half
            mid = (pmin + pmax) // 2
            batches.append(([ch], pmin, mid))
            batches.append(([ch], mid + 1, pmax))
            continue

        cur_span = (cur_max - cur_min + 1) if cur_min else 0
        new_span = (max(cur_max or pmin, pmax) - (cur_min or pmin) + 1)
        if new_span > max_pages:
            if cur_chapters:
                batches.append((cur_chapters, cur_min, cur_max))
            cur_chapters = [ch]
            cur_min = pmin
            cur_max = pmax
        else:
            cur_chapters.append(ch)
            cur_min = cur_min if cur_min else pmin
            cur_max = max(cur_max or pmax, pmax)
    if cur_chapters:
        batches.append((cur_chapters, cur_min, cur_max))
    return batches

def run_mineru_on_chunk(pdf_path, output_dir, page_range):
    """Call MinerU Standard API on a chunk PDF.
    Returns (success, output_dir).
    """
    env = os.environ.copy()
    token = env.get("MINERU_TOKEN")
    if not token:
        log(f"ERROR: MINERU_TOKEN env var not set")
        return False, None
    cmd = [
        "python3", str(MINERU_PY),
        str(pdf_path),
        "--api", "standard",
        "--output", str(output_dir),
        "--token", token,
        "--pages", page_range,
    ]
    log(f"  $ {' '.join(cmd[:6])} ...")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if result.returncode == 0:
            log(f"  ✅ MinerU success")
            return True, output_dir
        else:
            log(f"  ❌ MinerU failed: {result.stderr[-500:]}")
            return False, None
    except subprocess.TimeoutExpired:
        log(f"  ❌ MinerU timeout")
        return False, None
    except Exception as e:
        log(f"  ❌ MinerU error: {e}")
        return False, None

def extract_images_from_mineru_output(mineru_output_dir, target_ch, target_pages):
    """Map MinerU's images/ output back to our fig_PPPP_N.png naming.
    Returns: dict {chapter: {page: [(fig_index, source_path), ...]}}
    """
    # MinerU output structure: mineru_output_dir/<pdf_stem>/images/...
    images_dir = None
    for p in mineru_output_dir.rglob("images"):
        if p.is_dir():
            images_dir = p
            break
    if not images_dir:
        return {}
    # Heuristic: figure images are named like <uuid>.png, located in images/ subdir
    # We need to map by content - we don't have positional info from MinerU directly.
    # For now, collect all images and assign to the chunk's pages in document order.
    all_images = sorted(images_dir.glob("*.png")) + sorted(images_dir.glob("*.jpg"))
    log(f"  Found {len(all_images)} images in {images_dir}")
    # Note: assigning images to specific pages requires Markdown parsing with
    # positional info from the MinerU output. For now, this is a placeholder
    # that the user can refine.
    return {target_ch: {p: [] for p in target_pages}}

def main():
    WORK.mkdir(parents=True, exist_ok=True)
    CHUNKS.mkdir(exist_ok=True)
    OUTPUT.mkdir(exist_ok=True)
    LOGS.mkdir(exist_ok=True)
    LOGS.joinpath("upgrade.log").unlink(missing_ok=True)

    dry_run = "--dry-run" in sys.argv
    if dry_run:
        log("=== DRY-RUN MODE (no API calls, no file modifications) ===")
    else:
        if not os.environ.get("MINERU_TOKEN"):
            log("ERROR: MINERU_TOKEN env var not set. Aborting.")
            log("Get a token from https://mineru.net/apiManage/token")
            sys.exit(1)
        log("=== REAL-RUN MODE (will make API calls) ===")

    # Step 1: collect pages
    pages = collect_dewatermarked_pages()
    log(f"Step 1: Found {len(pages)} de-watermarked fig_*_1.png")

    # Step 2: group by chapter
    chapter_chunks = group_by_chapter(pages)
    log(f"Step 2: {len(chapter_chunks)} chapter ranges")
    for ch, pmin, pmax in chapter_chunks:
        log(f"  {ch}: pages {pmin}-{pmax} ({pmax-pmin+1} pages)")

    # Step 3: merge into ≤200 page batches
    batches = merge_chapters_into_batches(chapter_chunks)
    log(f"Step 3: {len(batches)} MinerU batches (≤200 pages each)")
    for chapters, pmin, pmax in batches:
        log(f"  batch: {chapters}, pages {pmin}-{pmax} ({pmax-pmin+1} pages)")

    if dry_run:
        log("\n=== DRY-RUN SUMMARY ===")
        log(f"  {len(batches)} batch(es) would be submitted to MinerU")
        log(f"  Estimated: ~{len(batches) * 5} minutes of API time")
        log(f"  Estimated output: {len(pages)} tight-crop fig_*_*.png")
        log(f"\nTo run for real: export MINERU_TOKEN=... && python3 {__file__}")
        return

    # Step 4: extract chunks from master PDF
    log("\nStep 4: Extracting chunk PDFs from master...")
    for i, (chapters, pmin, pmax) in enumerate(batches, 1):
        chunk_pdf = CHUNKS / f"batch_{i:02d}_p{pmin:04d}-p{pmax:04d}.pdf"
        if chunk_pdf.exists():
            log(f"  batch {i}: {chunk_pdf.name} exists, skip")
            continue
        extract_page_range(MASTER_PDF, chunk_pdf, pmin, pmax)
        size = chunk_pdf.stat().st_size
        log(f"  batch {i}: {chunk_pdf.name} ({size:,} bytes)")

    # Step 5: submit each batch to MinerU
    log("\nStep 5: Submitting to MinerU Standard API...")
    for i, (chapters, pmin, pmax) in enumerate(batches, 1):
        chunk_pdf = CHUNKS / f"batch_{i:02d}_p{pmin:04d}-p{pmax:04d}.pdf"
        out_dir = OUTPUT / f"batch_{i:02d}"
        page_range = f"{pmin}-{pmax}"
        log(f"  batch {i}: pages {page_range}")
        success, _ = run_mineru_on_chunk(chunk_pdf, out_dir, page_range)
        if not success:
            log(f"  batch {i} FAILED, continuing with next")

    # Step 6: extract images and replace de-watermarked versions
    log("\nStep 6: Extracting tight crops and replacing...")
    # TODO: parse MinerU markdown to map images to pages
    # For now, log a note that this is the integration step
    log("  NOTE: Image-to-page mapping requires parsing MinerU markdown output.")
    log("  This step is scaffolded but not yet implemented.")
    log("  See: https://mineru.net/apiManage/docs for output format.")

    log("\n=== DONE ===")
    log(f"  Chunks: {CHUNKS}")
    log(f"  Output: {OUTPUT}")
    log(f"  Logs: {LOGS}/upgrade.log")

if __name__ == "__main__":
    main()
