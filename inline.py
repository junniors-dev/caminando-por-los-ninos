"""Incrusta las fotos de recortes/ dentro del HTML como data URI."""
import base64, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
IMG  = os.path.join(BASE, "recortes-webp")
SRC  = os.path.join(BASE, "pagina.src.html")
OUT  = os.path.join(BASE, "index.html")

MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}

datos = {}
for f in os.listdir(IMG):
    nombre, ext = os.path.splitext(f)
    if ext.lower() in MIME:
        with open(os.path.join(IMG, f), "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode("ascii")
        datos[nombre] = "data:%s;base64,%s" % (MIME[ext.lower()], b64)

html = open(SRC, encoding="utf-8").read()
faltan = []

def sub(m):
    k = m.group(1)
    if k not in datos:
        faltan.append(k)
        return m.group(0)
    return datos[k]

html = re.sub(r"\{\{([a-z0-9\-]+)\}\}", sub, html)

if faltan:
    print("FALTAN estas imagenes en recortes/:", sorted(set(faltan)))
    sys.exit(1)

open(OUT, "w", encoding="utf-8").write(html)
print("index.html ->", round(os.path.getsize(OUT)/1024), "KB")
print("imagenes incrustadas:", len(datos))
