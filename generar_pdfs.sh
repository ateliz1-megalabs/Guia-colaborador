#!/usr/bin/env bash
# Genera un PDF por cada guía publicada (las que tienen <article data-guia="perfil/slug">).
# Uso:  ./generar_pdfs.sh            (requiere Google Chrome o Chromium)
set -euo pipefail
cd "$(dirname "$0")"

CHROME="${CHROME:-$(command -v google-chrome || command -v chromium || command -v chromium-browser || echo "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")}"
BASE="file://$(pwd)/index.html"
mkdir -p pdf

grep -o 'data-guia="[a-z-]*/[a-z-]*"' index.html | cut -d'"' -f2 | while read -r guia; do
  out="pdf/GGC-${guia/\//-}.pdf"
  "$CHROME" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer \
    --virtual-time-budget=3000 --print-to-pdf="$out" "${BASE}?print#${guia}" >/dev/null 2>&1
  echo "✓ $out"
done
python3 "$(dirname "$0")/generar_perfiles.py"
