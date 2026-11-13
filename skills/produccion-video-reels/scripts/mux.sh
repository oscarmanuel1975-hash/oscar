#!/usr/bin/env bash
# Monta MP4 compatible con Instagram, TikTok y WhatsApp a partir de fotogramas y un audio.
# Uso: mux.sh carpeta_frames audio.wav salida.mp4 [fps=30]
set -euo pipefail
FR="$1"; AU="$2"; OUT="$3"; FPS="${4:-30}"
ffmpeg -y -loglevel error -framerate "$FPS" -i "$FR/f_%05d.jpg" -i "$AU" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r "$FPS" \
  -c:a aac -b:a 192k -ar 44100 -movflags +faststart -shortest "$OUT"
echo "creado $OUT"
