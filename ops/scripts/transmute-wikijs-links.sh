#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  transmute-wikijs-links.sh TARGET_DIR

Converts internal Markdown links for Wiki.js:
  - removes .md from Markdown link targets
  - makes relative internal link targets absolute from the Wiki.js root
  - collapses accidental leading double slashes

External URLs and same-page anchors are left unchanged.
USAGE
}

if [[ $# -ne 1 ]]; then
  usage >&2
  exit 2
fi

target_dir=$1

if [[ ! -d "$target_dir" ]]; then
  printf 'error: TARGET_DIR does not exist or is not a directory: %s\n' "$target_dir" >&2
  exit 1
fi

export LC_ALL=C

find "$target_dir" -type f -name '*.md' -print0 |
  while IFS= read -r -d '' file; do
    tmp_file=$(mktemp)

    perl -0777 -pe '
      sub wikijs_target {
        my ($target) = @_;
        my $wrapped = 0;

        if ($target =~ /^<(.*)>$/s) {
          $target = $1;
          $wrapped = 1;
        }

        return $wrapped ? "<$target>" : $target
          if $target =~ m{^(?:https?://|#)}i;

        $target =~ s{\.md(?=([?#]|$))}{}gi;

        if ($target !~ m{^/}) {
          $target = "/" . $target;
        }

        $target =~ s{^//+}{/};

        return $wrapped ? "<$target>" : $target;
      }

      s{
        (?<!\!)
        (\[[^\]\n]+\]\()
        (
          <[^>\n]+>
          |
          [^)\s]+
        )
        ([^)]*\))
      }{
        $1 . wikijs_target($2) . $3
      }gex;
    ' "$file" > "$tmp_file"

    if ! cmp -s "$file" "$tmp_file"; then
      cat "$tmp_file" > "$file"
      printf 'updated %s\n' "$file"
    fi

    rm -f "$tmp_file"
  done
