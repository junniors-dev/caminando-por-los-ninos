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
| `inline.py` | Toma `pagina.src.html`, reemplaza cada `{{nombre}}` por la foto correspondiente y escribe `index.html`. |

## Para cambiar algo

1. Editar `pagina.src.html`.
2. Correr:

   ```
   python inline.py
   ```

3. Commit y push. GitHub Pages publica solo.

Para agregar una foto nueva: dejarla en `recortes-webp/` y usar `{{nombre-del-archivo}}`
en el HTML, sin la extensión.

## Cosas pendientes

- Poner el correo del grupo en la variable `CORREO` del script, al final de
  `pagina.src.html`. Mientras esté vacía, el formulario copia el mensaje y abre
  el mensaje directo de Instagram.
- Confirmar si Juan Pablo II 9896 es la dirección fija del espacio.
