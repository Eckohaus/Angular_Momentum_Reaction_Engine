import os
import pandas as pd

# Config
DATA_DIR = "data/spreadsheets/in_development"
PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"
STYLE_PATH = "style.css"
REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"

os.makedirs(PREVIEWS_DIR, exist_ok=True)

def sanitize_filename(path):
    """Make a unique but simple filename for previews."""
    return path.replace("/", "_").replace(" ", "_").replace(".xlsx", ".html")

def convert_xlsx_to_html(xlsx_path, html_path):
    try:
        df = pd.read_excel(xlsx_path, sheet_name=None)  # all sheets
        with open(html_path, "w", encoding="utf-8") as f:
            f.write("<html><head>")
            f.write(f'<link rel="stylesheet" href="../{STYLE_PATH}">')
            f.write("</head><body>\n")
            f.write(f"<h2>{xlsx_path}</h2>\n")
            for sheet_name, sheet in df.items():
                f.write(f"<h3>Sheet: {sheet_name}</h3>\n")
                f.write(sheet.fillna("").to_html(index=False, border=0))
                f.write("<hr>\n")
            f.write("</body></html>")
        print(f"✔ Converted {xlsx_path} → {html_path}")
    except Exception as e:
        print(f"✘ Failed to convert {xlsx_path}: {e}")

def build_index(entries):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write(f'<link rel="stylesheet" href="../{STYLE_PATH}">')
        f.write("</head><body>\n")
        f.write("<h1>In Development XLSX Previews</h1>\n")
        f.write("<p>Browse generated HTML previews of XLSX files. Expand folders to view contents.</p>\n")

        def recurse(tree, indent=0):
            for name, node in sorted(tree.items()):
                if isinstance(node, dict):
                    f.write("  " * indent + f"<details><summary>📂 {name}</summary>\n")
                    recurse(node, indent + 1)
                    f.write("  " * indent + "</details>\n")
                else:
                    src_link = f"{REPO_URL}/{node['src']}"
                    prev_link = f"https://eckohaus.github.io/Angular_Momentum_Reaction_Engine_v2/{node['preview']}"
                    f.write("  " * indent + f"• {name} [<a href='{prev_link}'>Preview</a>] [<a href='{src_link}'>Source XLSX</a>]<br>\n")

        recurse(entries, 0)
        f.write("</body></html>")

def main():
    entries = {}

    for root, _, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith(".xlsx"):
                xlsx_path = os.path.join(root, file)
                rel_path = os.path.relpath(xlsx_path, ".")
                html_name = sanitize_filename(rel_path)
                html_path = os.path.join(PREVIEWS_DIR, html_name)

                convert_xlsx_to_html(xlsx_path, html_path)

                # Build nested tree
                parts = rel_path.split(os.sep)
                current = entries
                for p in parts[:-1]:
                    current = current.setdefault(p, {})
                current[file] = {"src": rel_path, "preview": f"{PREVIEWS_DIR}/{html_name}"}

    build_index(entries)

if __name__ == "__main__":
    main()
