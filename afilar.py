"""Reprocesa los recortes: contraresta la doble compresion de Instagram
con una mascara de enfoque suave y guarda a calidad alta."""
import os
from PIL import Image, ImageFilter, ImageEnhance

DST = r"C:\Users\junni\Downloads\proyectos jun\caminando-web\recortes"

for f in sorted(os.listdir(DST)):
    nombre, ext = os.path.splitext(f)
    if ext.lower() not in (".jpg", ".jpeg"):
        continue
    p = os.path.join(DST, f)
    antes = os.path.getsize(p)
    with Image.open(p) as im:
        im = im.convert("RGB")
        im = im.filter(ImageFilter.UnsharpMask(radius=1.1, percent=85, threshold=3))
        im = ImageEnhance.Color(im).enhance(1.06)
        im.save(p, quality=93, optimize=True, subsampling=0)
    print(f"{nombre:16s} {im.size[0]}x{im.size[1]:<5} {antes//1024} -> {os.path.getsize(p)//1024} KB")
