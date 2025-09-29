# scripts/convert_xlsx.py
import os
import json
import pandas as pd
import subprocess

# Constants
REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
TRANSFORMS_DIR = "transforms"
INDEX_FILE = "docs/in_development_previews.html"

# Ensure folders exist
os.makedirs(PREVIEWS_DIR, exist_ok=True)
os.makedirs(TRANSFORMS_DIR, exist_ok=True)

def convert_xlsx(src_path, rel_path):
    """Convert an XLSX into HTML + JSON for pipeline use (not shown in index)."""
    try:
        xls = pd.ExcelFile(src_path)
        html_parts, json_export = [], {}

        for sheet in xls.sheet_names:
            df = xls.parse(sheet)
            html_parts.append(f"<h3>Sheet: {sheet}</h3>")
            html_parts.append(df.to_html(index=False, border=0))
            json_export[sheet] = df.to_dict(orient="records")

        # Save HTML preview (hidden from index, but stored)
        html_dst = os.path.join(PREVIEWS_DIR, rel_path).replace(".xlsx", ".html")
        os.makedirs(os.path.dirname(html_dst), exist_ok=True)
        with open(html_dst, "w", encoding="utf-8") as f:
            f.write("<html><head>")
            f.write('<link rel="stylesheet" type="text/css" href="../docs/style.css">')
            f.write("</head><body>")
            f.write("\n".join(html_parts))
            f.write("</body></html>")

        # Save JSON transform
        json_dst = os.path.join(TRANSFORMS_DIR, rel_path).replace(".xlsx", ".json")
        os.makedirs(os.path.dirname(json_dst), exist_ok=True)
        with open(json_dst, "w", encoding="utf-8") as f:
            json.dump(json_export, f, indent=2)

        return html_dst, json_dst
    except Exception as e:
        print(f"❌ Failed to convert {src_path}: {e}")
        return None, None


def convert_py(src_path, rel_path):
    """Run a Python module and capture its output into an HTML preview."""
    preview_html = os.path.join(PREVIEWS_DIR, rel_path).replace(".py", ".html")
    os.makedirs(os.path.dirname(preview_html), exist_ok=True)

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

    with open(preview_html, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="../docs/style.css">')
        f.write("</head><body>")
        f.write(f"<h2>Module Preview: {os.path.basename(src_path)}</h2>")
        f.write("<pre>" + output + "</pre>")
        f.write("</body></html>")

    return preview_html


def build_index(entries):
    """Generate index page showing only Code Preview + Source XLSX."""
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated previews. Only key links shown: Code Preview (py) + Source XLSX.</p>\n")

        def recurse(node, indent=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(" " * indent + f'<details><summary>{name}</summary>\n')
                    recurse(content, indent + 2)
                    f.write(" " * indent + "</details>\n")
                else:
                    xlsx_path, py_preview = content
                    f.write(" " * indent + f'<div class="file">{name} ')
                    if py_preview:
                        f.write(f'[<a href="{py_preview}">Code Preview (py)</a>] ')
                    if xlsx_path:
                        f.write(f'[<a href="{xlsx_path}">Source XLSX</a>]')
                    f.write("</div>\n")

        recurse(entries)
        f.write("</body></html>\n")


def main():
    entries = {}

    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")

            if file.endswith(".xlsx"):
                convert_xlsx(src_path, rel_path)  # still runs for pipeline use
                # add XLSX link
                parts = rel_path.split(os.sep)
                node = entries
                for part in parts[:-1]:
                    node = node.setdefault(part, {})
                node[file] = (
                    f"{REPO_URL}/{src_path.replace(os.sep, '/')}",  # Source XLSX
                    None  # no direct preview in index
                )

            elif file.endswith(".py"):
                preview_html = convert_py(src_path, rel_path)
                # add Python preview
                parts = rel_path.split(os.sep)
                node = entries
                for part in parts[:-1]:
                    node = node.setdefault(part, {})
                node[file] = (
                    None,  # no XLSX link
                    f"../{preview_html}"  # Code Preview (py)
                )

    build_index(entries)


if __name__ == "__main__":
    main()
