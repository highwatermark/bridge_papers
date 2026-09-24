#!/usr/bin/env bash
# Build PDFs. Requires a local TeX install (e.g. MacTeX / BasicTeX).
set -euo pipefail
cd "$(dirname "$0")"
for f in bridge2_paperA_translation bridge2_paperB_method bridge2_paperC_position; do
  echo "=== $f ==="
  pdflatex -interaction=nonstopmode "$f.tex" >/dev/null
  bibtex   "$f" >/dev/null || true
  pdflatex -interaction=nonstopmode "$f.tex" >/dev/null
  pdflatex -interaction=nonstopmode "$f.tex" >/dev/null
  [ -f "$f.pdf" ] && echo "  built $f.pdf" || echo "  FAILED — see $f.log"
done
