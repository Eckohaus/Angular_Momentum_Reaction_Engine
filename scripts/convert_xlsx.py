import pandas as pd
import os
from collections import defaultdict

INPUT_DIR = "data/spreadsheets/in_development"
OUTPUT_DIR = "docs/previews"
INDEX_FILE = "docs/in_development_previews.html"


def convert_xlsx_to_html(filepath):
    """Convert one XLSX file to styled HTML with collapsible sheets."""
    try:
        xls = pd.ExcelFile(filepath)
    except Exception as e:
        print(f"❌ Could not read {filepath}: {e}")
        return None

    filename = os.path.splitext(os.path.basename(filepath))[0]
    outpath = os.path.join(OUTPUT_DIR, f"{filename}.html")

    html_parts = [
        "<html><head><meta charset='utf-8'>",
        "<link rel='stylesheet' type='text/css' href='style.css'>",
        f"</head><body><h1>{filename}</h1>"
    ]

    for sheet in xls.sheet_names:
        try:
            df = pd.read_excel(filepath, sheet_name=sheet)
            table_html = df.to_html(index=False, border=0, escape=False)
            html_parts.append(
                f"<details><summary>Sheet: {sheet}</summary>{table_html}</details>"
            )
        except Exception as e:
            html_parts.append(
                f"<p style='color:red;'>⚠️ Could not render sheet '{sheet}': {e}</p>"
            )

    html_parts.append("</body></html>")

    with open(outpath, "w", encoding="utf-8") as f:
        f.write("\n".join(html_parts))

    print(f"✅ Converted {filepath} → {outpath}")
    return filename, filepath


def build_index(entries):
    """Generate hierarchical index HTML grouped by folder structure."""
    # Build a nested dict tree
    tree = defaultdict(dict)
    for name, src in entries:
        rel_path = os.path.relpath(src, start=INPUT_DIR)
        parts = rel_path.split(os.sep)
        cursor = tree
        for part in parts[:-1]:  # folders
            cursor = cursor.setdefault(part, {})
        cursor[parts[-1]] = (name, src)  # file

    # Recursive function to render HTML
    def render_node(node, depth=2):
        html = []
        for key, value in sorted(node.items()):
            if isinstance(value, dict):
                # Folder
                html.append(f"<h{depth}>{key}</h{depth}>")
                html.append("<ul>")
                html.extend(render_node(value, depth + 1))
                html.append("</ul>")
            else:
                # File
                name, src = value
                rel_src = os.path.relpath(src, start=".")
                html.append("<li>")
                html.append(f"{name}.xlsx<br>")
                html.append(f"↳ <a href='previews/{name}.html'>Preview (HTML)</a><br>")
                html.append(f"↳ <a href='{rel_src}'>Source XLSX</a>")
                html.append("</li>")
        return html

    html = [
        "<html><head><meta charset='utf-8'>",
        "<title>In Development Previews</title>",
        "<link rel='stylesheet' type='text/css' href='previews/style.css'>",
        "</head><body>",
        "<h1>In Development Previews</h1>"
    ]

    html.extend(render_node(tree))
    html.extend(["</body></html>"])

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print(f"📑 Index updated → {INDEX_FILE}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    entries = []
    for root, _, files in os.walk(INPUT_DIR):
        for file in files:
            if file.endswith(".xlsx"):
                filepath = os.path.join(root, file)
                result = convert_xlsx_to_html(filepath)
                if result:
                    name, src = result
                    entries.append((name, src))

    if entries:
        build_index(entries)


if __name__ == "__main__":
    main()
