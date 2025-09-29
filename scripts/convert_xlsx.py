import os
import json
import pandas as pd

REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"
ONEDRIVE_MAP = "onedrive_links.json"

# load optional onedrive map
if os.path.exists(ONEDRIVE_MAP):
    with open(ONEDRIVE_MAP, "r", encoding="utf-8") as f:
        onedrive_links = json.load(f)
else:
    onedrive_links = {}

os.makedirs(PREVIEWS_DIR, exist_ok=True)

def convert_xlsx_to_html(src_path, dst_path):
    """Convert XLSX to a simple HTML table preview with CSS link."""
    try:
        xls = pd.ExcelFile(src_path)
        html_parts = []
        for sheet in xls.sheet_names:
            df = xls.parse(sheet)
            html_parts.append(f"<h3>Sheet: {sheet}</h3>")
            html_parts.append(df.to_html(index=False, border=0))
        html = "\n".join(html_parts)

        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write("<html><head>")
            f.write('<link rel="stylesheet" type="text/css" href="../../docs/style.css">')
            f.write("</head><body>")
            f.write(html)
            f.write("</body></html>")
    except Exception as e:
        print(f"Failed to convert {src_path}: {e}")

def build_index(entries):
    """Build index HTML with source, live (if exists), and preview links."""
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated HTML previews of XLSX files. Expand folders to view contents.</p>\n")

        def recurse(node, indent=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(" " * indent + f"<details><summary>{name}</summary>\n")
                    recurse(content, indent + 2)
                    f.write(" " * indent + "</details>\n")
                else:  # file
                    src_path, html_path, rel_key = content
                    links = [
                        f'[<a href="{src_path}">XLSX source</a>]'
                    ]
                    if rel_key in onedrive_links:
                        links.append(f'[<a href="{onedrive_links[rel_key]}">XLSX live</a>]')
                    links.append(f'[<a href="{html_path}">Code/module preview</a>]')

                    f.write(" " * indent + f'<div class="file">{name} {" ".join(links)}</div>\n')

        recurse(entries)
        f.write("</body></html>\n")

def main():
    entries = {}

    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            if not file.endswith(".xlsx"):
                continue

            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")
            dst_path = os.path.join(PREVIEWS_DIR, rel_path).replace(".xlsx", ".html")

            convert_xlsx_to_html(src_path, dst_path)

            # build tree
            parts = rel_path.split(os.sep)
            node = entries
            for part in parts[:-1]:
                node = node.setdefault(part, {})
            node[parts[-1]] = (
                f"{REPO_URL}/{src_path.replace(os.sep, '/')}",  # source XLSX
                f"../{dst_path}",                              # preview HTML
                rel_path.replace(os.sep, "/")                  # lookup key
            )

    build_index(entries)

if __name__ == "__main__":
    main()
