#!/usr/bin/env python3
"""Build a Wiki.js export tree for victus-docs."""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit, urlunsplit


DOC_EXTENSIONS = {".md"}
ASSET_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf"}
EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "node_modules",
    "ops",
}
URL_SCHEMES = {
    "http",
    "https",
    "mailto",
    "tel",
    "ftp",
    "ftps",
    "data",
}
PROBLEM_SEGMENT_RE = re.compile(r"[\s\\:*?\"<>|]")
LINK_RE = re.compile(r"(!?)\[([^\]\n]*)\]\(([^)\n]+)\)")
REF_LINK_RE = re.compile(r"(?<!\!)\[([^\]\n]+)\]:\s*(\S+)")


@dataclass(frozen=True)
class ManifestEntry:
    export_path: str
    wikijs_path: str


@dataclass
class Stats:
    copied_docs: int = 0
    copied_assets: int = 0
    frontmatter_tags_rewritten: int = 0
    rewritten_links: int = 0


def usage() -> None:
    print("Usage: wikijs_export.py SOURCE_DIR EXPORT_DIR", file=sys.stderr)


def to_posix(path: Path) -> str:
    return path.as_posix()


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.parts)


def wikijs_path(export_path: str) -> str:
    path = PurePosixPath(export_path)
    without_suffix = path.with_suffix("") if path.suffix.lower() == ".md" else path
    return "/" + without_suffix.as_posix().strip("/")


def discover_files(source_dir: Path) -> list[Path]:
    files: list[Path] = []
    for path in source_dir.rglob("*"):
        rel = path.relative_to(source_dir)
        if is_excluded(rel) or not path.is_file():
            continue
        if path.suffix.lower() in DOC_EXTENSIONS | ASSET_EXTENSIONS:
            files.append(rel)
    return sorted(files, key=to_posix)


def build_manifest(source_dir: Path, files: list[Path], stats: Stats) -> dict[str, ManifestEntry]:
    manifest: dict[str, ManifestEntry] = {}
    export_to_source: dict[str, str] = {}

    for rel in files:
        source = to_posix(rel)
        export_path = source
        if export_path in export_to_source:
            other = export_to_source[export_path]
            raise SystemExit(
                f"Wiki.js export path collision: {other} and {source} both map to {export_path}"
            )
        export_to_source[export_path] = source
        manifest[source] = ManifestEntry(export_path=export_path, wikijs_path=wikijs_path(export_path))

    return manifest


def split_target(raw_target: str) -> tuple[str, str, str, bool]:
    wrapped = raw_target.startswith("<") and raw_target.endswith(">")
    target = raw_target[1:-1] if wrapped else raw_target
    parsed = urlsplit(target)
    base = urlunsplit(("", "", parsed.path, "", ""))
    suffix = ""
    if parsed.query:
        suffix += "?" + parsed.query
    if parsed.fragment:
        suffix += "#" + parsed.fragment
    return unquote(base), suffix, parsed.scheme.lower(), wrapped


def join_target(path: str, suffix: str, wrapped: bool) -> str:
    target = path + suffix
    return f"<{target}>" if wrapped else target


def resolve_source_target(current_source: str, target_path: str) -> str:
    current_dir = PurePosixPath(current_source).parent
    if target_path.startswith("/"):
        candidate = PurePosixPath(target_path.lstrip("/"))
    else:
        candidate = current_dir / target_path
    normalized = PurePosixPath(os.path.normpath(candidate.as_posix()))
    return "" if normalized.as_posix() == "." else normalized.as_posix()


def alias_source_target(
    current_source: str,
    source_target: str,
    manifest: dict[str, ManifestEntry],
) -> str | None:
    workspace_prefix = "01-Projects/victus/victus-docs/"
    if workspace_prefix in source_target:
        stripped = source_target.split(workspace_prefix, 1)[1]
        if stripped in manifest:
            return stripped

    target_name = PurePosixPath(source_target).name
    if not target_name.lower().endswith(".md"):
        return None

    target_file = target_name
    target_stem = re.sub(r"^\d+-", "", PurePosixPath(target_file).stem).lower()
    current_parts = PurePosixPath(current_source).parts
    scopes: list[str] = []
    if len(current_parts) >= 2 and current_parts[0] == "repos":
        scopes.append("/".join(current_parts[:2]))
    scopes.append("")

    for scope in scopes:
        exact_matches = [
            source
            for source in manifest
            if source.endswith(".md")
            and (not scope or source.startswith(scope + "/"))
            and PurePosixPath(source).name == target_file
        ]
        if len(exact_matches) == 1:
            return exact_matches[0]
        operations_match = [
            source
            for source in exact_matches
            if f"/operations/{target_file}" in source.lower()
        ]
        if len(operations_match) == 1:
            return operations_match[0]

        matches: list[str] = []
        for source in manifest:
            if not source.endswith(".md"):
                continue
            if scope and not source.startswith(scope + "/"):
                continue
            source_stem = re.sub(
                r"^\d+-",
                "",
                PurePosixPath(source).stem,
            ).lower()
            if source_stem == target_stem:
                matches.append(source)
        if len(matches) == 1:
            return matches[0]

    return None


def rewrite_target(
    current_source: str,
    raw_target: str,
    manifest: dict[str, ManifestEntry],
    asset_sources: set[str],
    broken_links: list[str],
    *,
    image: bool,
) -> tuple[str, bool]:
    path_part, suffix, scheme, wrapped = split_target(raw_target)

    if scheme in URL_SCHEMES or raw_target.startswith("#") or not path_part:
        return raw_target, False

    resolved = resolve_source_target(current_source, path_part)
    source_target = resolved
    if source_target not in manifest:
        alias = alias_source_target(current_source, source_target, manifest)
        if alias:
            source_target = alias

    if source_target in manifest and source_target.endswith(".md"):
        if image:
            return raw_target, False
        return join_target(manifest[source_target].wikijs_path, suffix, wrapped), True

    if source_target in asset_sources:
        export_path = manifest[source_target].export_path
        return join_target("/" + export_path, suffix, wrapped), export_path != path_part

    if Path(source_target).suffix.lower() == ".md":
        broken_links.append(f"{current_source}: missing Markdown target {raw_target} -> {source_target}")

    return raw_target, False


def rewrite_markdown(
    source_path: str,
    text: str,
    manifest: dict[str, ManifestEntry],
    asset_sources: set[str],
    broken_links: list[str],
    stats: Stats,
) -> str:
    def replace_inline(match: re.Match[str]) -> str:
        image = bool(match.group(1))
        label = match.group(2)
        target = match.group(3).strip()
        replacement, changed = rewrite_target(
            source_path, target, manifest, asset_sources, broken_links, image=image
        )
        if changed:
            stats.rewritten_links += 1
        return f"{match.group(1)}[{label}]({replacement})"

    def replace_reference(match: re.Match[str]) -> str:
        target = match.group(2)
        replacement, changed = rewrite_target(
            source_path, target, manifest, asset_sources, broken_links, image=False
        )
        if changed:
            stats.rewritten_links += 1
        return f"[{match.group(1)}]: {replacement}"

    text = LINK_RE.sub(replace_inline, text)
    return REF_LINK_RE.sub(replace_reference, text)


def rewrite_wikijs_frontmatter_tags(source_path: str, text: str, stats: Stats) -> str:
    if not text.startswith("---\n"):
        return text

    end = text.find("\n---", 4)
    if end == -1:
        return text

    frontmatter = text[4:end]
    rest = text[end:]
    lines = frontmatter.splitlines()
    output: list[str] = []
    changed = False
    index = 0

    while index < len(lines):
        line = lines[index]
        if line == "tags:":
            tag_index = index + 1
            tags: list[str] = []
            while tag_index < len(lines):
                tag_line = lines[tag_index]
                match = re.fullmatch(r"\s{2}-\s+(.+)", tag_line)
                if not match:
                    break
                tags.append(match.group(1).strip().strip('"\''))
                tag_index += 1

            if tags:
                # Wiki.js imports expect frontmatter tags as a scalar string;
                # YAML lists trigger "split is not a function" during import.
                output.append(f"tags: {', '.join(tags)}")
                stats.frontmatter_tags_rewritten += 1
                changed = True
                index = tag_index
                continue

        output.append(line)
        index += 1

    if not changed:
        return text

    return "---\n" + "\n".join(output) + rest


def validate_wikijs_frontmatter_tags(source_path: str, text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []

    end = text.find("\n---", 4)
    if end == -1:
        return []

    frontmatter = text[4:end]
    lines = frontmatter.splitlines()
    problems: list[str] = []
    for index, line in enumerate(lines):
        if line == "tags:" and index + 1 < len(lines) and re.fullmatch(r"\s{2}-\s+.+", lines[index + 1]):
            problems.append(f"{source_path}: frontmatter tags remained a YAML list")
    return problems


def validate_problem_paths(manifest: dict[str, ManifestEntry]) -> list[str]:
    problems: list[str] = []
    seen_wiki: dict[str, str] = {}
    for source, entry in manifest.items():
        export = PurePosixPath(entry.export_path)
        for segment in export.parts:
            if segment in {".", ".."} or PROBLEM_SEGMENT_RE.search(segment):
                problems.append(f"{source}: problematic Wiki.js path segment in {entry.export_path}")
        previous = seen_wiki.get(entry.wikijs_path)
        if previous:
            problems.append(
                f"Wiki.js path collision: {previous} and {source} both map to {entry.wikijs_path}"
            )
        seen_wiki[entry.wikijs_path] = source
    return problems


def copy_export(
    source_dir: Path,
    export_dir: Path,
    manifest: dict[str, ManifestEntry],
    stats: Stats,
) -> tuple[list[str], list[str]]:
    broken_links: list[str] = []
    frontmatter_problems: list[str] = []
    asset_sources = {
        source for source in manifest if Path(source).suffix.lower() in ASSET_EXTENSIONS
    }

    if export_dir.exists():
        shutil.rmtree(export_dir)
    export_dir.mkdir(parents=True, exist_ok=True)

    for source, entry in sorted(manifest.items()):
        src = source_dir / source
        dst = export_dir / entry.export_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix.lower() == ".md":
            text = src.read_text(encoding="utf-8")
            rewritten = rewrite_markdown(source, text, manifest, asset_sources, broken_links, stats)
            rewritten = rewrite_wikijs_frontmatter_tags(source, rewritten, stats)
            frontmatter_problems.extend(validate_wikijs_frontmatter_tags(source, rewritten))
            dst.write_text(rewritten, encoding="utf-8")
            stats.copied_docs += 1
        else:
            shutil.copy2(src, dst)
            stats.copied_assets += 1

    return broken_links, frontmatter_problems


def write_manifest(export_dir: Path, manifest: dict[str, ManifestEntry]) -> None:
    # The manifest makes the export reversible and lets link rewriting use exact
    # source-to-Wiki.js mappings instead of guessing from strings.
    payload = {
        source: {
            "export_path": entry.export_path,
            "wikijs_path": entry.wikijs_path,
        }
        for source, entry in sorted(manifest.items())
    }
    (export_dir / ".wikijs-path-map.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        usage()
        return 2

    source_dir = Path(argv[1]).resolve()
    export_dir = Path(argv[2]).resolve()
    if not source_dir.is_dir():
        print(f"error: SOURCE_DIR does not exist: {source_dir}", file=sys.stderr)
        return 1

    stats = Stats()
    files = discover_files(source_dir)
    manifest = build_manifest(source_dir, files, stats)
    path_problems = validate_problem_paths(manifest)

    # Path and link validation happens before import so a bad export never
    # replaces the currently rendered Wiki.js tree.
    if path_problems:
        print("Wiki.js path validation failed:", file=sys.stderr)
        for problem in path_problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1

    # A clean export directory keeps the source branch untouched and makes
    # repeated runs idempotent.
    broken_links, frontmatter_problems = copy_export(source_dir, export_dir, manifest, stats)
    write_manifest(export_dir, manifest)

    print("Wiki.js export build complete")
    print(f"  Markdown files copied: {stats.copied_docs}")
    print(f"  Assets copied: {stats.copied_assets}")
    print(f"  Frontmatter tag lists rewritten: {stats.frontmatter_tags_rewritten}")
    print(f"  Links rewritten: {stats.rewritten_links}")
    print(f"  Broken internal links found: {len(broken_links)}")
    print(f"  Frontmatter tag validation errors: {len(frontmatter_problems)}")
    print("  Collisions found: 0")
    print(f"  Export directory: {export_dir}")

    if broken_links:
        print("Broken internal Markdown links:", file=sys.stderr)
        for broken in broken_links:
            print(f"  - {broken}", file=sys.stderr)
        return 1

    if frontmatter_problems:
        print("Wiki.js frontmatter validation failed:", file=sys.stderr)
        for problem in frontmatter_problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
