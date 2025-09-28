#!/usr/bin/env python3
import os
import pandas as pd

# Paths
DATA_DIR = "data/spreadsheets/in_development"
PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"
STYLE_PATH = "docs/style.css"

# Repo URL for source links
REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"

def convert_xlsx_to_html(xlsx_path, html_path):
    try:
        df = pd.read_excel(xlsx_path, sheet_name=None)  # all sheets
        with open(html_path, "w", encoding="utf-8") as f:
            f.write("<html><head>\n")
            f.write(f'<link rel="stylesheet" type="text/css" href="../{STYLE_PATH}">\n')
            f.write("</head><body>\n")
            f.write(f"<h2>{os.path.basename(xlsx_path)}</h2>\n")

            for sheet, data in df.items():
                f.write(f"<h3>Sheet: {sheet}</h3>\n")
                f.write(data.to_html(index=False, na_rep=""))

            f.write("</body></html>")
        print(f"✔ Converted {xlsx_path} → {html_path}")
    except Exception as e:
        print(f"✘ Failed to convert {xlsx_path}: {e}")

def ensure_previews_dir():
    if not os.path.exists(PREVIEWS_DIR):
        os.makedirs(PREVIEWS_DIR)

def sanitize_filename(path):
    return path.replace("/", "_").replace("(", "").replace(")", "").replace(" ", "_")

def build_index(entries):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>\n")
        f.write(f'<link rel="stylesheet" type="text/css" href="style.css">\n')
        f.write("</head><body>\n")
        f.write("<h1>In-Development Previews</h1>\n")
        f.write("<p>Browse generated HTML previews of XLSX files. Expand folders to view contents.</p>\n")

        def recurse(node, depth=0):
            indent = "  " * depth
            if isinstance(node, dict):
                for k, v in sorted(node.items()):
                    if isinstance(v, dict):
                        f.write(f'{indent}<details open><summary class="folder">{k}</summary>\n')
                        recurse(v, depth + 1)
                        f.write(f"{indent}</details>\n")
                    else:
                        name, src, preview = v
                        f.write(
                            f'{indent}<span class="file">• {name} '
                            f'[<a href="{preview}">Preview</a>] '
                            f'[<a href="{REPO_URL}/{src}">Source XLSX</a>]</span><br>\n'
                        )

        recurse(entries)
        f.write("</body></html>")

def build_tree():
    tree = {}
    for root, _, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith(".xlsx"):
                src_path = os.path.join(root, file)
                rel_src = os.path.relpath(src_path, ".")
                preview_name = sanitize_filename(rel_src)[:-5] + ".html"
                preview_path = os.path.join(PREVIEWS_DIR, preview_name)
                convert_xlsx_to_html(src_path, preview_path)

                parts = rel_src.split(os.sep)
                node = tree
                for part in parts[:-1]:
                    node = node.setdefault(part, {})
                node[parts[-1]] = (file, rel_src, preview_path)
    return tree

def main():
    ensure_previews_dir()
    entries = build_tree()
    build_index(entries)

if __name__ == "__main__":
    main()
