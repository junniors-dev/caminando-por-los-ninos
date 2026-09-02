import os
from PIL import Image

# Relativa a la raiz del sitio: asi funciona en cualquier maquina, y no
# publica el nombre de usuario de quien la escribio.
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(RAIZ, "recortes")
DST = os.path.join(RAIZ, "recortes-webp")
os.makedirs(DST, exist_ok=True)

antes = despues = 0
for f in sorted(os.listdir(SRC)):
    nombre, ext = os.path.splitext(f)
    if ext.lower() not in (".jpg", ".jpeg", ".png"):
        continue
    o = os.path.join(SRC, f)
    d = os.path.join(DST, nombre + ".webp")
    with Image.open(o) as im:
        im.convert("RGB").save(d, "WEBP", quality=84, method=6)
    a, b = os.path.getsize(o), os.path.getsize(d)
    antes += a; despues += b
    print(f"{nombre:16s} {a//1024:>4} -> {b//1024:>4} KB  ({100-round(b*100/a)}% menos)")
print(f"\nTOTAL {antes//1024} KB -> {despues//1024} KB  ({100-round(despues*100/antes)}% menos)")
