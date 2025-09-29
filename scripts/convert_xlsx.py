import os
import pandas as pd

# Repo + paths
REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"
CSS_URL = "https://eckohaus.github.io/Angular_Momentum_Reaction_Engine_v2/docs/style.css"

# Ensure preview folder exists
os.makedirs(PREVIEWS_DIR, exist_ok=True)

def convert_xlsx_to_html(src_path, dst_path):
    """Convert a single XLSX to styled HTML preview"""
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
            f.write(f'<link rel="stylesheet" type="text/css" href="{CSS_URL}">')
            f.write("</head><body>\n")
            f.write(f"<h1>Preview: {os.path.basename(src_path)}</h1>\n")
            f.write(html)
            f.write("</body></html>")
        print(f"✔ Converted {src_path} → {dst_path}")
    except Exception as e:
        print(f"✘ Failed to convert {src_path}: {e}")

def build_index(entries):
    """Build the main previews index page"""
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write(f'<link rel="stylesheet" type="text/css" href="{CSS_URL}">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated HTML previews of XLSX files. Expand folders to view contents.</p>\n")

        def recurse(node, indent=0, level=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(" " * indent + f'<details class="level-{level}"><summary>{name}</summary>\n')
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

    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            if not file.endswith(".xlsx"):
                continue

            src_path = os.path.join(root, file)

            # preview path mirrors repo structure
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")
            dst_path = os.path.join(PREVIEWS_DIR, rel_path).replace(".xlsx", ".html")

            convert_xlsx_to_html(src_path, dst_path)

            # build tree entry
            parts = rel_path.split(os.sep)
            node = entries
            for part in parts[:-1]:
                node = node.setdefault(part, {})
            node[parts[-1]] = (
                f"{REPO_URL}/{src_path.replace(os.sep, '/')}",   # source XLSX link
                f"/{dst_path}"                                 # preview HTML link (served by Pages)
            )

    build_index(entries)

if __name__ == "__main__":
    main()
