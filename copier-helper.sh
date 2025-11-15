#!/usr/bin/env bash
set -euo pipefail

TEMPLATE_DIR="$(cd "$(dirname "$0")" && pwd)"
OUT_DIR="${1:-$TEMPLATE_DIR/tmp/generated}"

# Clean up existing output directory
rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

uvx copier copy --defaults --force --trust \
  --data author="Switchbox" \
  --data email="hello@switch.box" \
  --data author_github_handle="switchbox-data" \
  --data project_description="Example" \
  --data project_features="[python_data_science, python_package]" \
  --data use_github=true \
  --data open_source_license="MIT license" \
  --data aws=false \
  "$TEMPLATE_DIR" "$OUT_DIR"

echo "Generated at: $OUT_DIR"
