# scripts/convert_xlsx.py
import os
import json
import pandas as pd
import traceback
from pathlib import Path
import inspect

# Constants
REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
TRANSFORMS_DIR = "transforms"
INDEX_FILE = "docs/in_development_previews.html"

# Ensure folders exist
os.makedirs(PREVIEWS_DIR, exist_ok=True)
os.makedirs(TRANSFORMS_DIR, exist_ok=True)


# -------------------------------
# XLSX → HTML + JSON
# -------------------------------
def convert_xlsx(src_path, rel_path):
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

        json_dst = os.path.join(TRANSFORMS_DIR, rel_path).replace(".xlsx", ".json")
        os.makedirs(os.path.dirname(json_dst), exist_ok=True)
        with open(json_dst, "w", encoding="utf-8") as f:
            json.dump(json_export, f, indent=2)

        return html_dst
    except Exception as e:
        print(f"❌ XLSX conversion failed for {src_path}: {e}")
        traceback.print_exc()
        return None


# -------------------------------
# PYTHON → HTML Preview
# -------------------------------
def convert_py(src_path, rel_path):
    try:
        # Only special-case base_equation for now
        if "base_equation.py" not in src_path:
            return None

        import importlib.util

        spec = importlib.util.spec_from_file_location("base_equation", src_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Run with example values
        if hasattr(module, "base_equation"):
            result = module.base_equation(1.0824, 1.0813)
        else:
            result = {"error": "No base_equation() found"}

        # Render source code
        with open(src_path, "r", encoding="utf-8") as f:
            source_code = f.read()

        html_content = (
            "<html><head>"
            '<link rel="stylesheet" type="text/css" href="../docs/style.css">'
            "</head><body>"
            "<h2>Code Preview</h2>"
            "<pre style='background:#f4f4f4;padding:1em;border:1px solid #ddd;'>"
            f"{source_code}"
            "</pre>"
            "<h2>Example Output</h2>"
            f"<pre>{json.dumps(result, indent=2)}</pre>"
            "</body></html>"
        )

        html_dst = os.path.join(PREVIEWS_DIR, rel_path).replace(".py", ".html")
        os.makedirs(os.path.dirname(html_dst), exist_ok=True)
        with open(html_dst, "w", encoding="utf-8") as f:
            f.write(html_content)

        return html_dst
    except Exception as e:
        print(f"❌ Python conversion failed for {src_path}: {e}")
        traceback.print_exc()
        return None


# -------------------------------
# INDEX BUILDER
# -------------------------------
def build_index(entries):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated previews of XLSX and Python modules. Expand folders to view contents.</p>\n")

        def recurse(node, indent=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):
                    f.write(" " * indent + f'<details><summary>{name}</summary>\n')
                    recurse(content, indent + 2)
                    f.write(" " * indent + "</details>\n")
                else:
                    src_link, html_link = content
                    f.write(" " * indent + f'<div class="file">{name} '
                            f'[<a href="{html_link}">Preview</a>] '
                            f'[<a href="{src_link}">Source</a>]</div>\n')

        recurse(entries)
        f.write("</body></html>\n")


# -------------------------------
# MAIN
# -------------------------------
def main():
    entries = {}

    # Pipeline A: XLSX files
    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            if file.endswith(".xlsx"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")
                html_dst = convert_xlsx(src_path, rel_path)
                if html_dst:
                    parts = rel_path.split(os.sep)
                    node = entries
                    for part in parts[:-1]:
                        node = node.setdefault(part, {})
                    node[parts[-1]] = (
                        f"{REPO_URL}/{src_path.replace(os.sep, '/')}",
                        f"../{html_dst}"
                    )

    # Pipeline B: Python files
    for root, _, files in os.walk("amre"):
        for file in files:
            if file.endswith(".py"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, "amre")
                html_dst = convert_py(src_path, rel_path)
                if html_dst:
                    parts = rel_path.split(os.sep)
                    node = entries
                    for part in parts[:-1]:
                        node = node.setdefault(part, {})
                    node[parts[-1]] = (
                        f"{REPO_URL}/{src_path.replace(os.sep, '/')}",
                        f"../{html_dst}"
                    )

    build_index(entries)


if __name__ == "__main__":
    main()
