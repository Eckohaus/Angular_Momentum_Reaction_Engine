import os
import json
import pandas as pd

# Import your Python module(s)
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
        print(f"❌ Failed to convert {src_path}: {e}")
        return None, None


def convert_python_module(name, func, args, rel_path):
    """Run a Python module, capture output as pretty JSON wrapped in <pre>."""
    try:
        result = func(*args)
        pretty_json = json.dumps(result, indent=2)

        html_dst = os.path.join(PREVIEWS_DIR, rel_path).replace(".py", ".html")
        os.makedirs(os.path.dirname(html_dst), exist_ok=True)
        with open(html_dst, "w", encoding="utf-8") as f:
            f.write("<html><head>")
            f.write('<link rel="stylesheet" type="text/css" href="../docs/style.css">')
            f.write("</head><body>")
            f.write(f"<h2>Module Preview: {name}</h2>")
            f.write(f"<pre>{pretty_json}</pre>")
            f.write("</body></html>")

        return html_dst
    except Exception as e:
        print(f"❌ Failed to run {name}: {e}")
        return None


def build_index(entries):
    """Generate index page linking to previews."""
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated previews of XLSX and Python modules. Expand folders to view contents.</p>\n")

        def recurse(node, indent=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(" " * indent + f'<details><summary>{name}</summary>\n')
                    recurse(content, indent + 2)
                    f.write(" " * indent + "</details>\n")
                else:  # file
                    links = " ".join([f'[<a href="{link}">{label}</a>]' for label, link in content])
                    f.write(" " * indent + f'<div class="file">{name} {links}</div>\n')

        recurse(entries)
        f.write("</body></html>\n")


def main():
    entries = {}

    # Pass 1 – XLSX files
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
                node[parts[-1]] = [
                    ("Source XLSX", f"{REPO_URL}/{src_path.replace(os.sep, '/')}"),
                    ("Module/Code Preview", f"../{html_dst}")
                ]

    # Pass 2 – Python modules
    py_rel_path = "Electrical_resistance/lambda_sequencer/Base_Equation.py"
    py_html = convert_python_module("Base Equation", base_equation, (1.0824, 1.0813), py_rel_path)
    if py_html:
        parts = py_rel_path.split(os.sep)
        node = entries
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = [("Module/Code Preview", f"../{py_html}")]

    build_index(entries)


if __name__ == "__main__":
    main()
