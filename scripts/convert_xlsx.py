# scripts/convert_xlsx.py
import os
import json
import subprocess
import pandas as pd

REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
TRANSFORMS_DIR = "transforms"
INDEX_FILE = "docs/in_development_previews.html"

os.makedirs(PREVIEWS_DIR, exist_ok=True)
os.makedirs(TRANSFORMS_DIR, exist_ok=True)

def convert_xlsx(src_path, rel_path):
    """Convert XLSX into HTML + JSON."""
    try:
        xls = pd.ExcelFile(src_path)
        html_parts, json_export = [], {}

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
        print(f"❌ Failed XLSX {src_path}: {e}")
        return None


def convert_py(src_path, rel_path):
    """Run a .py module and capture output into HTML preview."""
    html_dst = os.path.join(PREVIEWS_DIR, rel_path).replace(".py", ".html")
    os.makedirs(os.path.dirname(html_dst), exist_ok=True)

    try:
        result = subprocess.run(
            ["python", src_path],
            capture_output=True,
            text=True
        )
        output = result.stdout or result.stderr
    except Exception as e:
        output = f"Error running {src_path}: {e}"

    with open(html_dst, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="../docs/style.css">')
        f.write("</head><body>")
        f.write(f"<h2>Module Preview: {os.path.basename(src_path)}</h2>")
        f.write("<pre>" + output + "</pre>")
        f.write("</body></html>")
    return html_dst


def build_index(entries):
    """Generate the index page with previews."""
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated previews of XLSX + Python modules. Expand folders to view contents.</p>\n")

        def recurse(node, indent=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):
                    f.write(" " * indent + f'<details><summary>{name}</summary>\n')
                    recurse(content, indent + 2)
                    f.write(" " * indent + "</details>\n")
                else:
                    links = []
                    if "xlsx" in content:
                        links.append(f'[<a href="{content["xlsx"][1]}">Spreadsheet Preview</a>]')
                        links.append(f'[<a href="{content["xlsx"][0]}">Source XLSX</a>]')
                    if "py" in content:
                        links.append(f'[<a href="{content["py"][1]}">Module Preview</a>]')
                    f.write(" " * indent + f'<div class="file">{name} {" ".join(links)}</div>\n')

        recurse(entries)
        f.write("</body></html>\n")


def main():
    entries = {}

    # Pass 1: gather XLSX
    xlsx_map = {}
    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            if not file.endswith(".xlsx"):
                continue
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")

            html_dst = convert_xlsx(src_path, rel_path)
            if not html_dst:
                continue

            parts = rel_path.split(os.sep)
            node = entries
            for part in parts[:-1]:
                node = node.setdefault(part, {})
            node[file] = {"xlsx": (
                f"{REPO_URL}/{src_path.replace(os.sep, '/')}",
                f"../{html_dst}"
            )}
            # Map by stem for later .py matching
            xlsx_map[os.path.splitext(file)[0].lower()] = node[file]

    # Pass 2: gather .py
    for root, _, files in os.walk("amre"):
        for file in files:
            if not file.endswith(".py"):
                continue
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, "amre")

            html_dst = convert_py(src_path, rel_path)

            stem = os.path.splitext(file)[0].lower()
            if stem in xlsx_map:
                # attach to matching XLSX entry
                xlsx_map[stem]["py"] = (
                    f"{REPO_URL}/{src_path.replace(os.sep, '/')}",
                    f"../{html_dst}"
                )
            else:
                # place under amre/ tree
                parts = rel_path.split(os.sep)
                node = entries.setdefault("amre", {})
                for part in parts[:-1]:
                    node = node.setdefault(part, {})
                node[file] = {"py": (
                    f"{REPO_URL}/{src_path.replace(os.sep, '/')}",
                    f"../{html_dst}"
                )}

    build_index(entries)


if __name__ == "__main__":
    main()
