"""Genera un HTML por perfil a partir de index.html.
Cada archivo contiene SOLO las guías de su perfil (las demás se quitan del archivo).
Uso:  python3 generar_perfiles.py
"""
import re, pathlib

base = pathlib.Path(__file__).parent
src = (base / "index.html").read_text(encoding="utf-8")
perfiles = re.findall(r'\{ id: "([a-z]+)", nombre:', src)

for perfil in perfiles:
    def quitar(m):
        return m.group(0) if m.group(1) == perfil else ""
    out = re.sub(r'<!-- =+ [^\n]*-->\n<article data-guia="([a-z]+)/[a-z-]+">.*?</article>\n*', quitar, src, flags=re.S)
    out = re.sub(r'<article data-guia="([a-z]+)/[a-z-]+">.*?</article>\n*', quitar, out, flags=re.S)
    out = out.replace("<script>\n", f'<script>\nconst PERFIL_FIJO = "{perfil}";\n', 1)
    (base / f"{perfil}.html").write_text(out, encoding="utf-8")
    n = len(re.findall(r'<article data-guia="[a-z]+/', out))
    print(f"✓ {perfil}.html ({n} guías)")
