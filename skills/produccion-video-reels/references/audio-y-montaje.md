# Audio, sincronía y solución de problemas

## Música sintetizada

`scripts/synth_lib.py` ofrece timbres de caja de música y campana, acordes de fondo, cascabeles, whoosh y reverberación sencilla. El reel del club usó esa técnica: una melodía de caja de música sobre acordes, cascabeles en cada pulso, un whoosh en cada cambio de escena y un arpegio de campanas al final.

Pautas:

- Define el tempo y calcula los tiempos en pulsos; coloca los efectos en los segundos del guion, no a ojo.
- Deja la mezcla con margen (la librería normaliza a 0,89) y un fundido final de un segundo.
- La duración del audio es la del vídeo. Si cambias la duración de la pieza, cambia también la mezcla y comprueba que `check_video.sh` marca el mismo tiempo para audio y vídeo.
- Prueba la melodía a volumen bajo: en el móvil, muchos reels se ven sin sonido, así que el mensaje tiene que entenderse solo con los textos.

## Derechos de autor

Usa melodías de dominio público o compuestas para la pieza. Antes de usar una canción tradicional, comprueba que lo es y que no usas un arreglo protegido. Esta skill no incluye ninguna pista comercial, y no debe añadirse ninguna aunque sea breve.

## Sincronía de vídeo y audio

- El vídeo se renderiza a los fps que marca `window.REEL.fps` (30 por defecto) y el audio va a 44 100 Hz.
- `mux.sh` usa `-shortest`: si el audio es más corto, el vídeo se corta; si es más largo, se ignora el sobrante. Comprueba las duraciones antes de dar por bueno el MP4.
- Si notas que un efecto llega tarde, el fallo está casi siempre en los segundos que pusiste en el guion, no en el montaje.

## Rendimiento

- `render_frames.js` usa cuatro procesos en paralelo. Con una pieza de 33 s a 30 fps son unos mil fotogramas; el tiempo depende de la máquina. Si va lento, baja `--quality` a 88 o los `--workers`, y revisa que no haya efectos pesados (muchas sombras o desenfoques) en el HTML.
- Para pruebas rápidas renderiza con `--fps 15`: el resultado se ve a trompicones pero basta para revisar la secuencia. El renderizado final siempre a 30.
- Los fotogramas ocupan mucho. No los subas al repositorio.

## Problemas frecuentes

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| Imagen o fuente que falta en los fotogramas | La imagen no es un `<img>` o no se esperó a cargar | Pon las imágenes como `<img>` en el HTML y usa `window.ready` |
| Los fotogramas salen distintos entre ejecuciones | Hay animaciones CSS o temporizadores que dependen del reloj | Calcula todo desde `t` dentro de `render(t)` |
| El vídeo no se reproduce en el móvil | Formato de píxel distinto de yuv420p | Usa `mux.sh`; `check_video.sh` avisa de este caso |
| Texto cortado por la interfaz de la red | Está fuera de la zona segura | Muévelo hacia el centro y vuelve a revisar con imágenes fijas |
| Logo borroso | Imagen pequeña ampliada | Pide al usuario una versión de más resolución, no la reescales |
| Audio más corto o más largo que el vídeo | La mezcla no coincide con la duración | Ajusta `Mix(duracion=...)` a la del vídeo |
| `playwright` no se encuentra | Se ejecuta desde un entorno distinto | En este entorno ya está instalado; no lo reinstales |
