#!/usr/bin/env bash
# Instala las 11 skills de réplica en tu carpeta de usuario de Claude Code,
# para poder usarlas en cualquier proyecto.
set -euo pipefail
origen="$(cd "$(dirname "$0")" && pwd)/.claude/skills"
destino="${HOME}/.claude/skills"
mkdir -p "$destino"
for d in "$origen"/replica-*/; do
  n="$(basename "$d")"
  rm -rf "$destino/$n"
  cp -r "$d" "$destino/$n"
  echo "Instalada: /$n"
done
echo "Listo. Reinicia Claude Code y empieza con /replica-recon"
