#!/usr/bin/env python3
"""
clean_orphaned_assets.py — TidyFactor Asset & Folder Structure Hygiene Engine.
Detects and remediates:
1. Binary duplicate image assets using SHA-256 hashing.
2. Unreferenced orphan images in `assets/`.
3. Advises WebP compression for raster assets > 50KB.
"""

import os
import sys
import hashlib
import re
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def compute_sha256(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def scan_assets(root: Path):
    assets_dir = root / "assets"
    if not assets_dir.exists():
        print("[INFO] No assets/ directory found.")
        return 0

    image_extensions = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif"}
    asset_files = [p for p in assets_dir.iterdir() if p.is_file() and p.suffix.lower() in image_extensions]

    # 1. SHA-256 Duplication Check
    hashes = {}
    duplicates = []
    for asset in asset_files:
        digest = compute_sha256(asset)
        if digest in hashes:
            duplicates.append((asset, hashes[digest]))
        else:
            hashes[digest] = asset

    # 2. Markdown Reference Check
    md_files = list(root.rglob("*.md")) + [root / "brand.yaml", root / "brand.json"]
    all_content = ""
    for md in md_files:
        if "dist" in md.parts or ".git" in md.parts or "__pycache__" in md.parts:
            continue
        if md.exists():
            all_content += md.read_text(encoding="utf-8", errors="ignore") + "\n"

    orphans = []
    for asset in asset_files:
        # Match asset name in text
        if asset.name not in all_content:
            orphans.append(asset)

    print("=" * 60)
    print("  TIDYFACTOR MARKETING ASSET HYGIENE AUDIT")
    print("=" * 60)
    print(f"Total assets analyzed: {len(asset_files)}")

    print(f"\n[1] Duplicate Asset Check (SHA-256):")
    if duplicates:
        print(f"  [WARN] Found {len(duplicates)} duplicate asset(s):")
        for dup, orig in duplicates:
            print(f"    - {dup.name} is identical to {orig.name}")
    else:
        print("  [OK] Zero binary duplicates found.")

    print(f"\n[2] Orphan Asset Check:")
    if orphans:
        print(f"  [WARN] Found {len(orphans)} unreferenced orphan asset(s):")
        for orph in orphans:
            print(f"    - {orph.name} ({orph.stat().st_size / 1024:.1f} KB)")
    else:
        print("  [OK] Zero unreferenced orphan assets found.")

    print(f"\n[3] Large Raster File Check (>50KB):")
    large_rasters = [a for a in asset_files if a.suffix.lower() in {".png", ".jpg", ".jpeg"} and a.stat().st_size > 50 * 1024]
    if large_rasters:
        for lr in large_rasters:
            print(f"  [INFO] {lr.name}: {lr.stat().st_size / 1024:.1f} KB. Recommend WebP conversion for ~80% savings.")
    else:
        print("  [OK] All raster assets optimized or under 50KB.")

    print("=" * 60)
    return len(duplicates) + len(orphans)

def main():
    parser = argparse.ArgumentParser(description="TidyFactor Asset Hygiene Engine")
    parser.add_argument("--check", action="store_true", help="Run audit and return non-zero if issues exist")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    issues_count = scan_assets(root)

    if args.check and issues_count > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
