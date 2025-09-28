import os
import pandas as pd

PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"

# Utility: make relative path label
def rel_label(path):
    return os.path.basename(path)

# Build index with collapsible folders
def build_index():
    sections = []

    for root, _, files in os.walk(PREVIEWS_DIR):
        if not files:
            continue

        # Relative folder (skip previews/ root itself)
        rel_folder = os.path.relpath(root, PREVIEWS_DIR)
        if rel_folder == ".":
            folder_name = "Root Previews"
        else:
            folder_name = rel_folder

        # Start collapsible block
        section_html = [f'<details><summary>📂 {folder_name}</summary><ul>']

        for f in sorted(files):
            if not f.endswith(".html"):
                continue

            file_path = os.path.join(root, f)
            label = rel_label(f)
            preview_url = f"/{file_path}"

            # Try to reconstruct XLSX source path
            source_xlsx = f.replace(".html", ".xlsx")

            section_html.append(
                f'<li>{label} '
                f'[<a href="{preview_url}">Preview</a>] '
                f'[<a href="../data/spreadsheets/in_development/{source_xlsx}">Source XLSX</a>]'
                '</li>'
            )

        section_html.append("</ul></details>")
        sections.append("\n".join(section_html))

    # Write final index
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>In Development Previews</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>📊 In Development Previews</h1>
  <p>Browse generated HTML previews of XLSX files. Expand folders to view contents.</p>
  {}
</body>
</html>""".format("\n\n".join(sections))
    )

if __name__ == "__main__":
    build_index()
