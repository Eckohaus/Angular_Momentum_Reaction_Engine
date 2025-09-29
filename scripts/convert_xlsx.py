import os
import pandas as pd
from datetime import datetime

REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"
LOG_FILE = "cleanup_log.txt"
LOGS_DIR = "logs"

# ensure folders exist
os.makedirs(PREVIEWS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# reset log each run
with open(LOG_FILE, "w", encoding="utf-8") as log:
    log.write(f"Log for run at {datetime.utcnow().isoformat()} UTC\n\n")

def log_event(message: str):
    """Write message to cleanup_log.txt"""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(message + "\n")
    print(message)

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

        log_event(f"✔ Converted {src_path} → {dst_path}")
    except Exception as e:
        log_event(f"✘ Failed {src_path}: {e}")

def build_index(entries):
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
                    xlsx_path, html_path = content
                    f.write(" " * indent + f'<div class="file level-{indent//2}">{name} '
                            f'[<a href="{html_path}">Preview</a>] '
                            f'[<a href="{xlsx_path}">Source XLSX</a>]</div>\n')

        recurse(entries)
        f.write("</body></html>\n")

def main():
    entries = {}
    generated = set()

    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            if not file.endswith(".xlsx"):
                continue

            src_path = os.path.join(root, file)

            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")
            dst_path = os.path.join(PREVIEWS_DIR, rel_path).replace(".xlsx", ".html")

            convert_xlsx_to_html(src_path, dst_path)

            generated.add(os.path.normpath(dst_path))

            # build tree entry
            parts = rel_path.split(os.sep)
            node = entries
            for part in parts[:-1]:
                node = node.setdefault(part, {})
            node[parts[-1]] = (
                f"{REPO_URL}/{src_path.replace(os.sep, '/')}",   # source XLSX link
                f"../{dst_path}"                                # preview HTML link
            )

    # cleanup stale previews
    for root, _, files in os.walk(PREVIEWS_DIR):
        for file in files:
            if not file.endswith(".html"):
                continue
            path = os.path.normpath(os.path.join(root, file))
            if path not in generated and not path.endswith("index.html"):
                os.remove(path)
                log_event(f"🗑 Deleted stale preview: {path}")

    build_index(entries)

    # Weekly archive snapshot on Sundays (UTC)
    today = datetime.utcnow()
    if today.weekday() == 6:  # Sunday = 6
        archive_name = today.strftime("%Y-%m-%d_cleanup_log.txt")
        archive_path = os.path.join(LOGS_DIR, archive_name)
        os.replace(LOG_FILE, archive_path)
        print(f"📦 Archived log to {archive_path}")
    else:
        print("✔ Run complete – log kept as cleanup_log.txt")

if __name__ == "__main__":
    main()
