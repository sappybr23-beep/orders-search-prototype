#!/usr/bin/env python3
"""Inline assets/*.svg as data URIs -> dist/prototype.html (standalone) and dist/artifact.html (fragment for publishing) + docs/index.html (GitHub Pages)."""
import base64, pathlib, re
root = pathlib.Path(__file__).parent
src = (root / "index.html").read_text(encoding="utf-8")
def data_uri(m):
    p = root / m.group(0)
    return "data:image/svg+xml;base64," + base64.b64encode(p.read_bytes()).decode()
out = re.sub(r"assets/[\w\-]+\.svg", data_uri, src)
assert "assets/" not in out
d = root / "dist"; d.mkdir(exist_ok=True)
(d / "artifact.html").write_text(out, encoding="utf-8")
(d / "prototype.html").write_text('<!doctype html>\n<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><style>[hidden]{display:none!important}body{margin:0}</style>\n' + out.replace("<div class=\"app\"", "</head><body>\n<div class=\"app\"", 1) + "\n</body></html>\n", encoding="utf-8")
docs = root / "docs"; docs.mkdir(exist_ok=True)
(docs / "index.html").write_text((d / "prototype.html").read_text(encoding="utf-8"), encoding="utf-8")
(docs / ".nojekyll").write_text("")
print("ok", len(out))
