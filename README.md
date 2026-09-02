# Caminando por los Niños

Sitio del grupo solidario **Caminando por los Niños**, del Gran Rosario, Santa Fe.
Viandas los sábados para personas en situación de calle, módulos alimentarios,
colectas de abrigo y encuentros de barrio.

Instagram: [@caminandopor_losninos](https://www.instagram.com/caminandopor_losninos/)

## Cómo está armado

Una sola página, sin frameworks ni build tools. HTML, CSS y JavaScript a mano.

| Archivo | Qué es |
|---|---|
| `index.html` | **La página publicada.** Es un solo archivo: las fotos y el logo van incrustados en base64, así que no depende de ninguna carpeta de imágenes. |
| `pagina.src.html` | El código fuente, con marcadores `{{nombre-foto}}` donde después entran las imágenes. **Editar acá, no en `index.html`.** |
| `recortes-webp/` | Las fotos ya recortadas y optimizadas en WebP. |
| `herramientas/` | Los tres scripts de Python que preparan la página. No hacen falta para publicarla, solo para regenerarla. |

### Los scripts

| Script | Qué hace |
|---|---|
| `herramientas/inline.py` | Toma `pagina.src.html`, reemplaza cada `{{nombre}}` por la foto correspondiente y escribe `index.html`. **Es el único que hace falta para publicar.** |
| `herramientas/webp.py` | Convierte los JPG de `recortes/` a WebP en `recortes-webp/`. |
| `herramientas/afilar.py` | Reprocesa los JPG de `recortes/` para contrarrestar la doble compresión de Instagram. Se corre antes de `webp.py`. |

`recortes/` no se versiona: son los intermedios. Los que se publican son los `.webp`.

## Para cambiar algo

1. Editar `pagina.src.html`.
2. Correr:

   ```
   python herramientas/inline.py
   ```

3. Commit y push. GitHub Pages publica solo.

Para agregar una foto nueva: dejarla en `recortes-webp/` y usar `{{nombre-del-archivo}}`
en el HTML, sin la extensión.

## Cosas pendientes

- Poner el correo del grupo en la variable `CORREO` del script, al final de
  `pagina.src.html`. Mientras esté vacía, el formulario copia el mensaje y abre
  el mensaje directo de Instagram.
- Confirmar si Juan Pablo II 9896 es la dirección fija del espacio.

## Licencia

El código del sitio está bajo licencia [MIT](LICENSE): HTML, CSS, JavaScript y los
scripts de Python.

No cubre el contenido del grupo — su nombre, su logo, sus fotografías y los textos
sobre su actividad pertenecen a Caminando por los Niños y no se licencian aquí.
