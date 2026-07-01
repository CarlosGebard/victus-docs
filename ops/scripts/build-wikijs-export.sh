#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  ops/scripts/build-wikijs-export.sh SOURCE_DIR EXPORT_DIR

Builds a clean Wiki.js export tree without mutating SOURCE_DIR.

Example:
  ops/scripts/build-wikijs-export.sh . /tmp/wiki-export
USAGE
}

if [[ $# -ne 2 ]]; then
  usage >&2
  exit 2
fi

source_dir=$1
export_dir=$2
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)

python3 "$script_dir/wikijs_export.py" "$source_dir" "$export_dir"
