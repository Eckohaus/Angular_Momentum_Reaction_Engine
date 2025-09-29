# scripts/convert_xlsx.py
import os
import json
import pandas as pd

# Import your module replica
from amre.lambda_seq.base_equation import base_equation

# Constants
REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
TRANSFORMS_DIR = "transforms"
INDEX_FILE = "docs/in_development_previews.html"

# Ensure folders exist
os.makedirs(PREVIEWS_DIR, exist_ok=True)
os.makedirs(TRANSFORMS_DIR, exist_ok=True)


def convert_xlsx(src_path, rel_path):
    """
    Convert an XLSX into both HTML + JSON.
    Special case: Base_Equation.xlsx → run Python replica instead of parsing spreadsheet.
    """
    try:
        # Detect special case
        if rel_path.endswith("Base_Equation.xlsx"):
            # Run the Python version
            result = base_equation(1.0824, 1.0813)

            # Save HTML preview
            html_dst = os.path.join(PREVIEWS_DIR, rel_path).replace(".xlsx", ".html")
            os.makedirs(os.path.dirname(html_dst), exist_ok=True)
            with open(html_dst, "w", encoding="utf-8") as f:
                f.write("<html><head>")
                f.write('<link rel="stylesheet" type="text/css" href="../docs/style.css">')
                f.write("</head><body>")
                f.write("<h2>Module Preview: Base Equation</h2>")
                f.write("<pre>")
                f.write(json.dumps(result, indent=2))
                f.write("</pre>")
                f.write("</body></html>")

            # Save JSON transform
            json_dst = os.path.join(TRANSFORMS_DIR, rel_path).replace(".xlsx", ".json")
            os.makedirs(os.path.dirname(json_dst), exist_ok=True)
            with open(json_dst, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)

            return html_dst, json_dst

        # Default case: any other XLSX
        xls = pd.ExcelFile(src_path)
        html_parts = []
        json_export = {}

        for sheet in xls.sheet_names:
            df = xls.parse(sheet)
            html_parts.append(f"<h3>Sheet: {sheet}</h3>")
            html_parts.append(df.to_html(index=False, border=0))
            json_export[sheet] = df.to_dict(orient="records")

        # Save HTML
        html_dst = os.path.join(PREVIEWS_DIR, rel_path).replace(".xlsx", ".html")
        os.makedirs(os.path.dirname(html_dst), exist_ok=True)
        with open(html_dst, "w", encoding="utf-8") as f:
            f.write("<html><head>")
            f.write('<link rel="stylesheet" type="text/css" href="../docs/style.css">')
            f.write("</head><body>")
            f.write("\n".join(html_parts))
            f.write("</body></html>")

        # Save JSON
        json_dst = os.path.join(TRANSFORMS_DIR, rel_path).replace(".xlsx", ".json")
        os.makedirs(os.path.dirname(json_dst), exist_ok=True)
        with open(json_dst, "w", encoding="utf-8") as f:
            json.dump(json_export, f, indent=2)

        return html_dst, json_dst

    except Exception as e:
        print(f"❌ Failed to convert {src_path}: {e}")
        return None, None


def build_index(entries):
    """Generate index page."""
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated module/code previews of XLSX files. Expand folders to view contents.</p>\n")

        def recurse(node, indent=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):
                    f.write(" " * indent + f'<details><summary>{name}</summary>\n')
                    recurse(content, indent + 2)
                    f.write(" " * indent + "</details>\n")
                else:
                    xlsx_path, html_path = content
                    f.write(" " * indent + f'<div class="file">{name} '
                            f'[<a href="{html_path}">Module/Code Preview</a>] '
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
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")

            html_dst, json_dst = convert_xlsx(src_path, rel_path)
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
