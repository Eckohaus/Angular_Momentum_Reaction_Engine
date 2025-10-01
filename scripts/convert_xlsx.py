def build_index(entries):
    """Generate index page showing Code Preview (py) + Source XLSX + Interactive (if present)."""
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head>")
        f.write('<link rel="stylesheet" type="text/css" href="style.css">')
        f.write("</head><body>\n")
        f.write("<h1>In Development Previews</h1>\n")
        f.write("<p>Browse generated previews. Links: Code Preview (py), Source XLSX, Interactive Calculator (if present).</p>\n")

        def recurse(node, indent=0):
            for name, content in sorted(node.items()):
                if isinstance(content, dict):  # folder
                    f.write(" " * indent + f'<details><summary>{name}</summary>\n')
                    recurse(content, indent + 2)
                    f.write(" " * indent + "</details>\n")
                else:
                    xlsx_path, py_preview, interactive_preview = content
                    f.write(" " * indent + f'<div class="file">{name} ')
                    if py_preview:
                        f.write(f'[<a href="{py_preview}">Code Preview (py)</a>] ')
                    if xlsx_path:
                        f.write(f'[<a href="{xlsx_path}">Source XLSX</a>] ')
                    if interactive_preview:
                        f.write(f'[<a href="{interactive_preview}">Interactive</a>] ')
                    f.write("</div>\n")

        recurse(entries)
        f.write("</body></html>\n")
