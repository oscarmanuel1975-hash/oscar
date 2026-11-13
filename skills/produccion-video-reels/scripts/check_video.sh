#!/usr/bin/env bash
# Comprueba el MP4 final y genera una hoja de contacto para revisarlo a ojo.
# Uso: check_video.sh video.mp4 [carpeta_salida] [segundos_entre_miniaturas=3]
set -euo pipefail
V="$1"; OUT="${2:-$(dirname "$V")/check}"; STEP="${3:-3}"; mkdir -p "$OUT"
read -r VC W H PF FPS < <(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,pix_fmt,r_frame_rate -of csv=p=0 "$V" | tr ',' ' ')
AC=$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of csv=p=0 "$V" || true)
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
SIZE=$(du -h "$V" | cut -f1)
echo "vídeo: $VC ${W}x${H} $PF $FPS fps | audio: ${AC:-SIN AUDIO} | duración: ${DUR}s | tamaño: $SIZE"
WARN=0
[ "$VC" = h264 ] || { echo "AVISO: el códec de vídeo no es h264"; WARN=1; }
[ "$PF" = yuv420p ] || { echo "AVISO: pix_fmt no es yuv420p (algunos móviles no lo reproducen)"; WARN=1; }
[ "$AC" = aac ] || { echo "AVISO: falta audio aac"; WARN=1; }
[ "$W" -lt "$H" ] && echo "formato vertical" || echo "AVISO: no es vertical"
N=$(awk -v d="$DUR" -v s="$STEP" 'BEGIN{n=int(d/s)+1; print n}')
ROWS=$(( (N + 5) / 6 )); [ "$ROWS" -ge 1 ] || ROWS=1
ffmpeg -y -loglevel error -i "$V" -vf "fps=1/$STEP,scale=270:-1,tile=6x$ROWS" -frames:v 1 "$OUT/hoja_contacto.png"
ffmpeg -y -nostats -i "$V" -af volumedetect -vn -f null - 2>&1 | grep -E "mean_volume|max_volume" || true
echo "hoja de contacto: $OUT/hoja_contacto.png"
exit $WARN
