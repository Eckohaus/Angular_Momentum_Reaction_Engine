# scripts/convert_xlsx.py
import pandas as pd
import os

def convert_xlsx(file, outfile):
    """Convert one .xlsx file into a read-only HTML preview."""
    xls = pd.ExcelFile(file)
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(f"<h1>{os.path.basename(file)}</h1>")
        for sheet in xls.sheet_names:
            df = pd.read_excel(file, sheet_name=sheet)
            f.write(f"<h2>Sheet: {sheet}</h2>")
            f.write(df.to_html(index=False, escape=False))

if __name__ == "__main__":
    for root, _, files in os.walk("data/spreadsheets"):
        for file in files:
            if file.endswith(".xlsx"):
                infile = os.path.join(root, file)
                base = os.path.splitext(file)[0]
                outfile = f"docs/previews/{base}.html"
                os.makedirs(os.path.dirname(outfile), exist_ok=True)
                print(f"Converting {infile} → {outfile}")
                convert_xlsx(infile, outfile)
