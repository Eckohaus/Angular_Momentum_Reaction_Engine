import os
import json
import pandas as pd
import subprocess

# Constants
REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"

os.makedirs(PREVIEWS_DIR, exist_ok=True)

def convert_xlsx(src_path, rel_path):
    """Convert .xlsx into stripped HTML preview + JSON."""
    try:
        xls = pd.ExcelFile(src_path)
        html_parts = []
        json_export = {}

        for sheet in xls.sheet_names:
            df = xls.parse(sheet)
            html_parts.append(f"<h3>Sheet: {sheet}</h3>")
            html_parts.append(df.to_html(index=False, border=0))
            json_export[sheet] = df.to_dict(orient="records")

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
        print(f"❌ Failed XLSX conversion {src_path}: {e}")
        return None


def convert_py(src_path, rel_path):
    """Run .py module and capture output into HTML preview."""
    preview_html = os.path.join(PREVIEWS_DIR, rel_path).replace(".py", ".html")
    os.makedirs(os.path.dirname(preview_html), exist_ok=True)

    try:
        result = subprocess.run(["python", src_path], capture_output=True, text=True)
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
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated previews. Expand folders to view contents.</p>\n")

        def recurse(node, indent=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(" " * indent + f"<details><summary>{name}</summary>\n")
                    recurse(content, indent + 2)
                    f.write(" " * indent + "</details>\n")
                else:
                    link_type, path = content
                    if link_type == "xlsx":
                        f.write(" " * indent + f'<div class="file">{name} '
                                f'[<a href="{path}">Spreadsheet Preview</a>] '
                                f'[<a href="{REPO_URL}/{name}">Source XLSX</a>]</div>\n')
                    elif link_type == "py":
                        f.write(" " * indent + f'<div class="file">{name} '
                                f'[<a href="{path}">Module Preview</a>]</div>\n')

        recurse(entries)
        f.write("</body></html>")


def main():
    entries = {}

    # Walk spreadsheets
    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            if not file.endswith(".xlsx"):
                continue
            if file == "Base_Equation.xlsx":
                # Skip XLSX version of Base Equation
                continue

            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")
            html_dst = convert_xlsx(src_path, rel_path)

            if html_dst:
                parts = rel_path.split(os.sep)
                node = entries
                for part in parts[:-1]:
                    node = node.setdefault(part, {})
                node[file] = ("xlsx", f"../{html_dst}")

    # Walk Python modules (only Base_Equation.py for now)
    for root, _, files in os.walk("amre/lambda_seq"):
        for file in files:
            if file == "base_equation.py":
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, "amre/lambda_seq")
                html_dst = convert_py(src_path, rel_path)

                parts = ["Electrical_resistance", "lambda_sequencer"]
                node = entries
                for part in parts:
                    node = node.setdefault(part, {})
                node[file] = ("py", f"../{html_dst}")

    build_index(entries)


if __name__ == "__main__":
    main()
