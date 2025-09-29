# scripts/convert_xlsx.py
import os
import json
import pandas as pd
import subprocess

# Constants
REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"

# Ensure folders exist
os.makedirs(PREVIEWS_DIR, exist_ok=True)


def convert_xlsx(src_path, rel_path):
    """Convert XLSX into HTML preview + JSON export."""
    try:
        xls = pd.ExcelFile(src_path)
        html_parts = []
        json_export = {}

        for sheet in xls.sheet_names:
            df = xls.parse(sheet)
            html_parts.append(f"<h3>Sheet: {sheet}</h3>")
            html_parts.append(df.to_html(index=False, border=0))
            json_export[sheet] = df.to_dict(orient="records")

        # Save HTML preview
        html_dst = os.path.join(PREVIEWS_DIR, rel_path).replace(".xlsx", ".html")
        os.makedirs(os.path.dirname(html_dst), exist_ok=True)
        with open(html_dst, "w", encoding="utf-8") as f:
            f.write("<html><head>")
            f.write('<link rel="stylesheet" type="text/css" href="../docs/style.css">')
            f.write("</head><body>")
            f.write("\n".join(html_parts))
            f.write("</body></html>")

        return html_dst
    except Exception as e:
        print(f"❌ Failed to convert {src_path}: {e}")
        return None


def convert_py(src_path, rel_path):
    """Run a .py file and capture its stdout for HTML preview."""
    try:
        result = subprocess.run(
            ["python", src_path],
            capture_output=True,
            text=True,
            check=False
        )
        output = result.stdout or result.stderr
    except Exception as e:
        output = f"Error running {src_path}: {e}"

    # Save preview HTML
    html_dst = os.path.join(PREVIEWS_DIR, rel_path).replace(".py", ".html")
    os.makedirs(os.path.dirname(html_dst), exist_ok=True)
    with open(html_dst, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="../docs/style.css">')
        f.write("</head><body>")
        f.write(f"<h2>Module Preview: {os.path.basename(src_path)}</h2>")
        f.write("<pre>" + output + "</pre>")
        f.write("</body></html>")

    return html_dst


def build_index(entries):
    """Generate index page with combined XLSX + .py previews where available."""
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated previews. Expand folders to view contents.</p>\n")

        def recurse(node, level=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(f'<details class="level-{level}"><summary>{name}</summary>\n')
                    recurse(content, level + 1)
                    f.write("</details>\n")
                else:  # file entry (may contain xlsx + py)
                    row = f'<div class="file level-{level}">{name} '
                    if "xlsx" in content:
                        src, html = content["xlsx"]
                        row += f'[<a href="{html}">Spreadsheet Preview</a>] '
                        row += f'[<a href="{src}">Source XLSX</a>] '
                    if "py" in content:
                        src, html = content["py"]
                        row += f'[<a href="{html}">Module Preview</a>] '
                        row += f'[<a href="{src}">Source .py</a>] '
                    row += "</div>\n"
                    f.write(row)

        recurse(entries)
        f.write("</body></html>\n")


def main():
    entries = {}

    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")
            parts = rel_path.split(os.sep)

            # build nested dict for index
            node = entries
            for part in parts[:-1]:
                node = node.setdefault(part, {})

            base, ext = os.path.splitext(file)
            if base not in node:
                node[base] = {}

            if ext == ".xlsx":
                html_dst = convert_xlsx(src_path, rel_path)
                if html_dst:
                    node[base]["xlsx"] = (
                        f"{REPO_URL}/{src_path.replace(os.sep, '/')}",
                        f"../{html_dst}"
                    )
            elif ext == ".py":
                html_dst = convert_py(src_path, rel_path)
                if html_dst:
                    node[base]["py"] = (
                        f"{REPO_URL}/{src_path.replace(os.sep, '/')}",
                        f"../{html_dst}"
                    )

    build_index(entries)


if __name__ == "__main__":
    main()
