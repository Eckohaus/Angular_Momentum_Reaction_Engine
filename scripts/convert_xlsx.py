import os
import pandas as pd

REPO_URL = "https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/blob/master"
PREVIEWS_DIR = "previews"
INDEX_FILE = "docs/in_development_previews.html"

# ensure preview folder exists
os.makedirs(PREVIEWS_DIR, exist_ok=True)

def convert_xlsx_to_html(src_path, dst_path, rel_src_link):
    try:
        xls = pd.ExcelFile(src_path)
        html_parts = []

        # add header note
        html_parts.append("<h1>Spreadsheet Preview</h1>")
        html_parts.append(
            f'<p class="note">Depiction only — canonical source: '
            f'<a href="{rel_src_link}">original XLSX</a>.</p>'
        )

        # add sheets
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
    except Exception as e:
        print(f"Failed to convert {src_path}: {e}")

def build_index(entries):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write(
            "<p>These pages are <strong>depictions</strong> of underlying spreadsheet data.<br>"
            "The <em>canonical source</em> is always the original <code>.xlsx</code> file in the repository.<br>"
            "HTML previews are generated automatically for browsing and communication purposes only.</p>\n"
        )

        def recurse(node, level=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(f'<details class="level-{level}"><summary>{name}</summary>\n')
                    recurse(content, level + 1)
                    f.write("</details>\n")
                else:  # file
                    xlsx_path, html_path = content
                    f.write(
                        f'<div class="file level-{level}">{name} '
                        f'[<a href="{html_path}">Preview</a>] '
                        f'[<a href="{xlsx_path}">Source XLSX</a>]</div>\n'
                    )

        recurse(entries)
        f.write("</body></html>\n")

def main():
    entries = {}

    for root, _, files in os.walk("data/spreadsheets/in_development"):
        for file in files:
            if not file.endswith(".xlsx"):
                continue

            src_path = os.path.join(root, file)

            # relative repo + preview paths
            rel_path = os.path.relpath(src_path, "data/spreadsheets/in_development")
            dst_path = os.path.join(PREVIEWS_DIR, rel_path).replace(".xlsx", ".html")
            rel_src_link = f"{REPO_URL}/{src_path.replace(os.sep, '/')}"

            convert_xlsx_to_html(src_path, dst_path, rel_src_link)

            # build tree entry
            parts = rel_path.split(os.sep)
            node = entries
            for part in parts[:-1]:
                node = node.setdefault(part, {})
            node[parts[-1]] = (
                rel_src_link,  # source XLSX link
                f"../{dst_path}"  # preview HTML link
            )

    build_index(entries)

if __name__ == "__main__":
    main()
