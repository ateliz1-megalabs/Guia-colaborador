# Guías de usuario GGC

Un solo `index.html` con todas las guías y el menú por perfil, y un PDF por guía generado desde el mismo contenido.

```
guias-ggc/
├── index.html          ← sitio completo (menú + guías)
├── img/                ← capturas: PC04-03.png, PC05-03.png, …
├── pdf/                ← un PDF por guía (se genera con el script)
└── generar_pdfs.sh     ← regenera los PDF después de cambiar texto o capturas
```

## Capturas para "Completar un gasto"

Ya están todas. Las nuevas se guardan en `img/` con **exactamente** este nombre, en PNG. Cuando existe el archivo, la página lo muestra en lugar del recuadro.

| Archivo | Qué tiene que mostrar |
|---|---|
| `PC02-01.png` | Correo "Merlin Gestión de Gastos Corporativos" de liquidación de tarjeta generada (período, cantidad de gastos, enlace) |
| `PC03-01.png` | Liquidación de tarjeta abierta (pestañas Detalle / Gastos) |
| `PC04-01.png` | Formulario de un gasto de tarjeta tal como llega (campos precargados visibles) |
| `PC04-03.png` | Campo **Concepto de gasto** completado |
| `PC04-04.png` | Campo **Canal** con la lista desplegada |
| `PC04-05.png` | Campo **Cuenta contable** con la lista desplegada |
| `PC04-07.png` | **Comprobante adjunto** ya cargado |
| `PC04-09.png` | Barra de acciones del gasto con el **tick** visible |
| `PC05-03.png` | Mensaje que aparece al apretar el tick con un campo sin completar |
| `PC04-10.png` | Gasto con estado **Completado** |

Recomendaciones:
- Solo ambiente de prueba y datos ficticios.
- Navegador al 100 % de zoom y ventana de unos 1366 px de ancho. Recortá a la zona del formulario, sin escritorio ni pestañas del navegador.
- Mandalas **sin marcas**: las flechas y los recuadros se agregan después, todos con el mismo estilo.

## Un archivo por perfil

| Archivo | Quién lo ve | Contenido |
|---|---|---|
| `colaborador.html` | Colaboradores | Solo las guías del colaborador |
| `aprobador.html` | Aprobadores | Solo las guías del aprobador |
| `administracion.html` | Administración | Solo las guías de Administración |
| `index.html` | Vos (edición) | Todas las guías. **No se embebe en Merlin.** |

Los tres archivos de perfil se generan a partir de `index.html` con `generar_perfiles.py`, que también corre al final de `./generar_pdfs.sh`. Cada archivo **no contiene** las guías de los otros perfiles, y si alguien escribe a mano el enlace de una guía de otro perfil, vuelve al inicio.

## Publicar (GitHub Pages)

1. Creá un repositorio (por ejemplo `guias-ggc`) y subí **todo el contenido** de esta carpeta: los `.html`, `img/` y `pdf/`.
2. En el repositorio: **Settings → Pages → Deploy from a branch → main / (root) → Save**.
3. En 1 o 2 minutos queda en `https://<usuario>.github.io/guias-ggc/`.

**Importante:** el sitio queda **público** (también desde un repositorio privado). Solo capturas de prueba y nombres difuminados.

## Embeber en Merlin (iframe)

Una entrada de menú por perfil. Los permisos de cada perfil en Merlin deciden quién ve cada entrada.

| Entrada de menú | URL del iframe |
|---|---|
| Ayuda GGC (Colaborador) | `https://<usuario>.github.io/guias-ggc/colaborador.html?embed` |
| Ayuda GGC (Aprobador) | `https://<usuario>.github.io/guias-ggc/aprobador.html?embed` |
| Ayuda GGC (Administración) | `https://<usuario>.github.io/guias-ggc/administracion.html?embed` |

```html
<iframe src="https://<usuario>.github.io/guias-ggc/colaborador.html?embed"
        style="width:100%;height:100%;border:0" title="Guías GGC"></iframe>
```

- `?embed` oculta la barra superior (Merlin ya tiene la suya).
- Para abrir una guía puntual: `colaborador.html?embed#colaborador/presentar-liquidacion`.
- Para una guía sola, sin menú: `colaborador.html?solo#colaborador/presentar-liquidacion`.
- Si el iframe es angosto (menos de 820 px), el menú se esconde y aparece el botón "☰ Guías".

## Agregar una guía nueva

1. Copiar un bloque `<article data-guia="perfil/slug">` en `index.html` y cambiar el contenido.
2. En el catálogo `PERFILES` (al final del archivo), poner `lista: true` en esa guía.
3. Correr `./generar_pdfs.sh` para crear su PDF en `pdf/`.

## Regenerar los PDF

```bash
./generar_pdfs.sh
```
Necesita Google Chrome o Chromium. Genera `pdf/GGC-<perfil>-<guia>.pdf` por cada guía publicada.

## Capturas pendientes

Ninguna por ahora.

Los nombres de colaboradores y aprobadores **nunca** pueden quedar visibles: se difuminan antes de publicar.
