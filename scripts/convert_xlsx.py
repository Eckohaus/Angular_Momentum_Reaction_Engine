import os
import pandas as pd

REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"

# Ensure preview folder exists
os.makedirs(PREVIEWS_DIR, exist_ok=True)

def convert_xlsx_to_html(src_path, dst_path):
    """Convert one XLSX file into HTML preview"""
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
            # look for style.css in previews/, fallback to docs/
            f.write('<link rel="stylesheet" type="text/css" href="style.css">')
            f.write("</head><body>")
            f.write(html)
            f.write("</body></html>")
    except Exception as e:
        print(f"Failed to convert {src_path}: {e}")

def build_index(entries):
    """Build the index HTML page with collapsible folder structure"""
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated HTML previews of XLSX files. Expand folders to view contents.</p>\n")

        def recurse(node, indent=0, level=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(" " * indent + f'<details><summary class="folder level-{level}">{name}</summary>\n')
                    recurse(content, indent + 2, level + 1)
                    f.write(" " * indent + "</details>\n")
                else:  # file
                    xlsx_path, html_path = content
                    f.write(" " * indent + f'<div class="file level-{level}">{name} '
                            f'[<a href="{html_path}">Preview</a>] '
                            f'[<a href="{xlsx_path}">Source XLSX</a>]</div>\n')

        recurse(entries)
        f.write("</body></html>\n")

def main():
    entries = {}
    seen_previews = set()  # track previews actually generated this run

    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            if not file.endswith(".xlsx"):
                continue

            src_path = os.path.join(root, file)

            # preview path mirrors repo structure
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")
            dst_path = os.path.join(PREVIEWS_DIR, rel_path).replace(".xlsx", ".html")
            dst_path = dst_path.replace(" ", "_")  # normalize spaces

            convert_xlsx_to_html(src_path, dst_path)
            seen_previews.add(os.path.normpath(dst_path))

            # build tree entry
            parts = rel_path.split(os.sep)
            node = entries
            for part in parts[:-1]:
                node = node.setdefault(part, {})
            node[parts[-1]] = (
                f"{REPO_URL}/{src_path.replace(os.sep, '/')}",   # source XLSX link
                f"../{dst_path}"                                # preview HTML link
            )

    # 🧹 cleanup: remove previews without a matching XLSX
    for root, _, files in os.walk(PREVIEWS_DIR):
        for file in files:
            if not file.endswith(".html"):
                continue
            full_path = os.path.normpath(os.path.join(root, file))
            if full_path not in seen_previews:
                print(f"Removing stale preview: {full_path}")
                os.remove(full_path)

    build_index(entries)

if __name__ == "__main__":
    main()
