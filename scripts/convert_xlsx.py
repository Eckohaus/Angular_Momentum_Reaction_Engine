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
    """Convert an XLSX into both HTML + JSON outputs."""
    try:
        xls = pd.ExcelFile(src_path)
        html_parts = []
        json_export = {}

        for sheet in xls.sheet_names:
            df = xls.parse(sheet)

            # HTML block
            html_parts.append(f"<h3>Sheet: {sheet}</h3>")
            html_parts.append(df.to_html(index=False, border=0))

            # JSON block
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

        # Save JSON transform
        json_dst = os.path.join(TRANSFORMS_DIR, rel_path).replace(".xlsx", ".json")
        os.makedirs(os.path.dirname(json_dst), exist_ok=True)
        with open(json_dst, "w", encoding="utf-8") as f:
            json.dump(json_export, f, indent=2)

        return html_dst, json_dst
    except Exception as e:
        print(f"❌ Failed to convert XLSX {src_path}: {e}")
        return None, None


def convert_py(src_path, rel_path):
    """Run a Python module and capture its output as an HTML preview."""
    preview_html = os.path.join(PREVIEWS_DIR, rel_path).replace(".py", ".html")
    os.makedirs(os.path.dirname(preview_html), exist_ok=True)

    try:
        result = subprocess.run(
            ["python", src_path],
            capture_output=True,
            text=True,
            timeout=5  # avoid hangs
        )
        output = result.stdout or result.stderr
    except Exception as e:
        output = f"⚠️ Error running {src_path}: {e}"

    with open(preview_html, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="../docs/style.css">')
        f.write("</head><body>")
        f.write(f"<h2>Module Preview: {os.path.basename(src_path)}</h2>")
        f.write("<pre>" + output + "</pre>")
        f.write("</body></html>")

    return preview_html


def build_index(entries):
    """Generate index page with links for both XLSX + Python previews."""
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated previews of XLSX spreadsheets and Python modules.</p>\n")

        def recurse(node, indent=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(" " * indent + f'<details><summary>{name}</summary>\n')
                    recurse(content, indent + 2)
                    f.write(" " * indent + "</details>\n")
                else:  # file entry
                    f.write(" " * indent + content + "\n")

        recurse(entries)
        f.write("</body></html>\n")


def main():
    entries = {}

    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")
            parts = rel_path.split(os.sep)
            node = entries
            for part in parts[:-1]:
                node = node.setdefault(part, {})

            if file.endswith(".xlsx"):
                html_dst, _ = convert_xlsx(src_path, rel_path)
                if html_dst:
                    node[file] = (
                        f'<div class="file">{file} '
                        f'[<a href="../{html_dst}">Module/Code Preview</a>] '
                        f'[<a href="{REPO_URL}/{src_path.replace(os.sep, "/")}">Source XLSX</a>]</div>'
                    )
            elif file.endswith(".py"):
                html_dst = convert_py(src_path, rel_path)
                node[file] = (
                    f'<div class="file">{file} '
                    f'[<a href="../{html_dst}">Module Preview</a>]</div>'
                )

    build_index(entries)


if __name__ == "__main__":
    main()
