---
name: produccion-video-reels
description: Producción de reels y vídeos verticales 9:16 para redes (Instagram, TikTok, WhatsApp) hechos con HTML animado, fotogramas renderizados con Playwright, música sintetizada sin derechos y montaje con ffmpeg. Úsala para piezas del club (C.A.R. Marisqueiro, lotería de Navidad, patrocinadores, convocatorias, resultados), de la gestoría (avisos de plazos, novedades normativas, campañas) o de cualquier cliente. Cubre guion por escenas, uso correcto de escudos, logos y fotos reales, zona segura, revisión con imágenes fijas antes de renderizar, audio, montaje y comprobación final. Actívala SIEMPRE que se pida un reel, vídeo corto, vídeo para redes, animación de logo, anuncio vertical o vídeo con música, aunque no se mencione HTML ni ffmpeg. Si el contenido incluye datos jurídicos, fiscales o de juego, apóyate en verificacion-normativa, y si salen personas, en rgpd-proteccion-datos.
---

# Producción de reels y vídeo vertical

El reel de la lotería del club salió en seis versiones. Casi todo lo que se corrigió entre una y otra no eran fallos técnicos: eran decisiones de contenido que se podían haber fijado al principio (el logo del patrocinador pequeño, el escudo recreado en vez del oficial, la imagen del presidente con un disfraz que no se quería, objetos de más en el trineo). Esta skill sirve para acertar antes: fijar el contenido con el usuario, revisar con imágenes fijas y dejar el renderizado final para cuando ya está aprobado, porque renderizar y montar es lo que más tarda.

## Cómo funciona el método

La pieza es una **página HTML** de 1080 por 1920 píxeles con una función `render(t)` que la deja exactamente como estaría en el segundo `t`. Un script saca un fotograma por cada instante, un segundo script sintetiza el audio y ffmpeg une todo en un MP4. Como cada fotograma se calcula de forma determinista, se puede revisar cualquier segundo en una imagen fija y repetir el vídeo sin sorpresas.

Todo está en la carpeta de esta skill:

| Archivo | Para qué sirve |
|---|---|
| `assets/reel-template.html` | Plantilla mínima con tres escenas, zona segura y funciones de animación |
| `scripts/still.js` | Imágenes fijas en los segundos que indiques, para revisar escenas |
| `scripts/render_frames.js` | Fotogramas JPEG en paralelo (lee fps y duración de `window.REEL`) |
| `scripts/synth_lib.py` | Música y efectos sintetizados con numpy, sin derechos de autor |
| `scripts/mux.sh` | MP4 h264, yuv420p y aac, listo para móvil |
| `scripts/check_video.sh` | Comprobación técnica y hoja de contacto para revisar a ojo |
| `references/guion-y-contenido.md` | Cómo preparar el guion, los activos y las reglas de contenido |
| `references/audio-y-montaje.md` | Detalles de audio, sincronía y solución de problemas |

## Flujo de trabajo

### 1. Fija el encargo antes de tocar código

Pregunta solo lo que falte de esto, y deja las respuestas escritas en un `brief.md` dentro del proyecto:

- Objetivo y público (vender décimos, anunciar un plazo, dar la bienvenida a un patrocinador).
- Duración (entre 15 y 35 segundos funciona bien en un reel) y dónde se publicará.
- **Textos exactos** que deben salir, con números, precios, fechas y nombres. Nunca inventes un número de lotería, un precio, una fecha de sorteo ni un importe de premio: los da el usuario o se comprueba en su fuente oficial.
- Material real disponible: escudo, logos, fotos, fuentes de letra, colores del club.
- Tono (festivo, serio, institucional).

### 2. Escribe el guion por escenas

Una tabla con segundo de inicio y fin, qué se ve, qué texto aparece y qué suena. Una idea por escena, y el primer segundo tiene que enganchar. Enséñasela al usuario y espera su visto bueno: cambiar una escena en el guion cuesta un minuto, cambiarla después de renderizar y montar cuesta mucho más. Más detalle en `references/guion-y-contenido.md`.

### 3. Prepara los activos

Guarda cada archivo original sin tocar con el sufijo `_original` y trabaja con una copia. Para el escudo y los logos, usa siempre el archivo oficial que dé el usuario; si hay que quitar el fondo o recortar, hazlo sobre la copia y comprueba que no se deforma ni se desdibuja. No redibujes ni "recrees" un escudo: la versión recreada fue una de las correcciones del reel del club.

### 4. Construye el HTML y revisa con imágenes fijas

Parte de `assets/reel-template.html`. Reglas que evitan los problemas más comunes:

- `render(t)` no depende del reloj, de temporizadores ni de animaciones CSS. Todo se calcula desde `t`.
- Las imágenes van como `<img>` en el HTML, para que `window.ready` espere a que carguen.
- Escribe fuera de las franjas que tapan las aplicaciones: como regla práctica, deja libres unos 250 px arriba y unos 450 px abajo en un lienzo de 1080 por 1920, y deja unos 90 px a los lados. Son márgenes de uso habitual, no una norma oficial; si la pieza es importante, compruébala en la propia app.
- Los logos de patrocinadores y el escudo tienen que verse a simple vista en un móvil. Si dudas, hazlos más grandes.
- Texto grande (a partir de unos 54 px) y pocas palabras por escena.

Para revisar: `node scripts/still.js reel.html stills 1 5 9 14` genera una imagen por segundo indicado. Mira las imágenes, corrige y repite hasta que cada escena esté bien. Enseña al usuario las imágenes clave antes de seguir.

### 5. Audio

Genera la música con `scripts/synth_lib.py` y haz que dure **exactamente** lo mismo que el vídeo. Usa solo melodías de dominio público o compuestas para la ocasión, y sonidos sintetizados; no incluyas pistas comerciales aunque sean "cortas", porque las redes las pueden silenciar o retirar el vídeo. Alinea los efectos con los momentos del guion (un sonido en cada entrada importante). Si la melodía es una canción conocida, comprueba que es de dominio público antes de usarla. Detalles en `references/audio-y-montaje.md`.

### 6. Renderiza, monta y comprueba

```bash
node scripts/render_frames.js --html reel.html --out frames
bash scripts/mux.sh frames assets/music.wav salida.mp4 30
bash scripts/check_video.sh salida.mp4 check 3
```

`check_video.sh` avisa si el códec, el formato de píxel o el audio no son compatibles con los móviles, y genera `hoja_contacto.png`. Mira esa hoja: es la forma de ver todo el vídeo de un vistazo. Después, abre un par de fotogramas a tamaño completo para revisar textos y logos. Si hay algo que corregir, vuelve al paso 4 con imágenes fijas, no renderices otra vez a ciegas.

### 7. Entrega

- Deja el MP4 final con un nombre claro (`reel_<tema>_<club>.mp4`).
- Guarda en el repositorio el HTML, los activos, los scripts de audio y el comando exacto de montaje, para poder rehacer la pieza. No guardes la carpeta de fotogramas, que pesa mucho y se regenera.
- Termina con un resumen en lenguaje natural: qué contiene el vídeo escena por escena, qué datos aportó el usuario, qué se comprobó y qué debe revisar él antes de publicar. Si se publica a nombre de una entidad, que lo apruebe la persona responsable.

## Contenido que exige cuidado

- **Personas.** Una foto es dato personal. Usa solo imágenes que el usuario aporte, con permiso de las personas que salen, y con más cuidado si hay menores. No alteres la imagen de una persona real (disfraces, cambios de rostro o de contexto) sin que lo pida expresamente esa persona o el usuario. Para el tratamiento de datos, consulta `rgpd-proteccion-datos`.
- **Lotería y juego.** Las condiciones de venta, el mensaje de edad y los límites de la publicidad de juego están regulados. Esta skill no los fija de memoria: antes de afirmar un requisito, compruébalo con `verificacion-normativa` y deja el dato como pendiente de contrastar si no puedes abrir la fuente.
- **Música y marcas.** Música sintetizada o de dominio público; logos y escudos solo con autorización de su titular.
- **Contenido normativo de la gestoría.** Plazos, tipos o novedades legales se citan con su fuente oficial y fecha, como en `verificacion-normativa`.

## Límites

El resultado es un vídeo hecho con herramientas gratuitas y reproducibles. No sustituye la edición con grabaciones reales ni la animación avanzada. Si el usuario necesita vídeo grabado con personas o animación compleja, dilo claramente en vez de forzar este método.
