import pandas as pd
import os

INPUT_DIR = "data/spreadsheets/in_development"
OUTPUT_DIR = "previews"
STYLE_FILE = os.path.join(OUTPUT_DIR, "style.css")

STYLE_CONTENT = """
body {
  font-family: Arial, sans-serif;
  margin: 2em;
  background: #fafafa;
  color: #333;
}

h1, h2, h3 {
  font-family: "Segoe UI", Tahoma, sans-serif;
  color: #222;
  margin-top: 1em;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin-bottom: 2em;
  font-size: 14px;
}

th, td {
  border: 1px solid #ddd;
  padding: 6px 10px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

tr:hover {
  background-color: #f1f7ff;
}

details {
  margin-bottom: 1em;
}

summary {
  font-weight: bold;
  cursor: pointer;
  padding: 4px 0;
}
"""

def ensure_output_dir():
    """Ensure previews directory and stylesheet exist."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(STYLE_FILE, "w", encoding="utf-8") as f:
        f.write(STYLE_CONTENT)

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
        f"<html><head><meta charset='utf-8'>",
        f"<link rel='stylesheet' type='text/css' href='style.css'>",
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
    return outpath

def main():
    ensure_output_dir()
    for root, _, files in os.walk(INPUT_DIR):
        for file in files:
            if file.endswith(".xlsx"):
                filepath = os.path.join(root, file)
                convert_xlsx_to_html(filepath)

if __name__ == "__main__":
    main()
