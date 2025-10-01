#!/usr/bin/env python3
import os
from pathlib import Path
import pandas as pd

# Paths
DATA_DIR = Path("data/spreadsheets/in_development")
PREVIEW_DIR = Path("docs/previews")
INDEX_FILE = Path("docs/in_development_previews.html")

def convert_xlsx_to_html(src: Path, dst: Path):
    """Convert an Excel file into HTML table preview."""
    try:
        df = pd.read_excel(src, sheet_name=None, engine="openpyxl")
        dst.parent.mkdir(parents=True, exist_ok=True)
        with open(dst, "w", encoding="utf-8") as f:
            f.write("<html><head><meta charset='UTF-8'></head><body>")
            f.write(f"<h1>{src.name}</h1>")
            for sheet, frame in df.items():
                f.write(f"<h2>Sheet: {sheet}</h2>")
                f.write(frame.to_html(border=1, index=False))
            f.write("</body></html>")
        print(f"✔ Converted {src} → {dst}")
    except Exception as e:
        print(f"⚠️ Failed to convert {src}: {e}")

def build_index(previews_root=PREVIEW_DIR, index_file=INDEX_FILE):
    """Generate index of all previews, code, and interactive HTML files."""
    index_lines = [
        "<!DOCTYPE html>",
        "<html><head><meta charset='UTF-8'><title>In Development Previews</title></head><body>",
        "<h1>In Development Previews</h1>",
        "<p>Browse generated previews. Links: Source XLSX · Code Preview (py) · Interactive.</p>"
    ]

    for root, _, files in os.walk(previews_root):
        rel_root = Path(root).relative_to(previews_root)
        if not files:
            continue

        section = "/".join(rel_root.parts)
        index_lines.append(f"<details><summary>{section}</summary><ul>")

        for f in sorted(files):
            rel_path = rel_root / f
            label = f

            # Labeling by type
            if f.endswith(".xlsx"):
                label = f"{f} [Source XLSX]"
            elif f.endswith(".py"):
                label = f"{f} [Code Preview]"
            elif f.endswith("_interactive.html"):
                label = f"{f} [Interactive]"
            elif f.endswith(".html"):
                label = f"{f} [Preview]"

            index_lines.append(f"<li><a href='previews/{rel_path.as_posix()}'>{label}</a></li>")

        index_lines.append("</ul></details>")

    index_lines.append("</body></html>")

    index_file.parent.mkdir(parents=True, exist_ok=True)
    with open(index_file, "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines))

    print(f"✅ Index rebuilt at {index_file}")

def main():
    # Step 1: convert all .xlsx in DATA_DIR
    for src in DATA_DIR.rglob("*.xlsx"):
        dst = PREVIEW_DIR / src.relative_to(DATA_DIR)
        dst = dst.with_suffix(".html")
        convert_xlsx_to_html(src, dst)

    # Step 2: regenerate index (this also pulls in .py + _interactive.html if placed under docs/previews)
    build_index()

if __name__ == "__main__":
    main()
