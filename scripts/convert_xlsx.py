import os
import pandas as pd

REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"
LOG_FILE = "docs/cleanup_log.txt"

# Ensure required dirs
os.makedirs(PREVIEWS_DIR, exist_ok=True)
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# --- Logging ---
def log_message(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

# --- Convert XLSX → HTML ---
def convert_xlsx_to_html(src_path, dst_path):
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
            f.write('<link rel="stylesheet" type="text/css" href="../docs/style.css">')
            f.write("</head><body>")
            f.write(html)
            f.write("</body></html>")

        log_message(f"Converted {src_path} → {dst_path}")
        return True
    except Exception as e:
        log_message(f"Failed {src_path}: {e}")
        return False

# --- Build Index HTML ---
def build_index(entries):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated HTML previews of XLSX files. Expand folders to view contents.</p>\n")

        def recurse(node, level=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(f'<details class="folder level-{level}"><summary>{name}</summary>\n')
                    recurse(content, level + 1)
                    f.write("</details>\n")
                else:  # file
                    xlsx_path, html_path = content
                    f.write(f'<div class="file level-{level}">{name} '
                            f'[<a href="{html_path}">Preview</a>] '
                            f'[<a href="{xlsx_path}">Source XLSX</a>]</div>\n')

        recurse(entries)
        f.write("</body></html>\n")

# --- Cleanup Stale Previews ---
def clean_previews(preview_dir, valid_html_paths):
    removed_files = []
    for root, _, files in os.walk(preview_dir):
        for file in files:
            if file.endswith(".html"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, preview_dir)
                if rel_path not in valid_html_paths:
                    os.remove(full_path)
                    removed_files.append(rel_path)
                    log_message(f"Removed stale preview: {rel_path}")
    if removed_files:
        print(f"Cleanup complete: {len(removed_files)} stale previews removed.")
    else:
        print("Cleanup complete: no stale previews found.")

# --- Main ---
def main():
    entries = {}
    valid_html_paths = set()

    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            if not file.endswith(".xlsx"):
                continue

            src_path = os.path.join(root, file)

            # preview path mirrors repo structure
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")
            dst_path = os.path.join(PREVIEWS_DIR, rel_path).replace(".xlsx", ".html")

            if convert_xlsx_to_html(src_path, dst_path):
                valid_html_paths.add(os.path.relpath(dst_path, PREVIEWS_DIR))

            # build tree entry
            parts = rel_path.split(os.sep)
            node = entries
            for part in parts[:-1]:
                node = node.setdefault(part, {})
            node[parts[-1]] = (
                f"{REPO_URL}/{src_path.replace(os.sep, '/')}",   # source XLSX link
                f"../{dst_path}"                                # preview HTML link
            )

    # cleanup unused previews
    clean_previews(PREVIEWS_DIR, valid_html_paths)

    # rebuild index
    build_index(entries)

    print("Index regenerated and previews updated.")

if __name__ == "__main__":
    main()
