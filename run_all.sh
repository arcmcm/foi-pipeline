#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_ROOT"

# 1) Build PDFs + CSVs
python "$PROJECT_ROOT/src/foi_research_prototype.py"

# 2) Serve the folder
echo "Serving on http://100.109.150.79:8000/"
python -m http.server 8000
