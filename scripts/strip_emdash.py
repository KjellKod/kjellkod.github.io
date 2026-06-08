#!/usr/bin/env python3
"""Strip em-dashes from Markdown prose.

The spaced em-dash (``—``, U+2014) reads as an "AI tell," so this tool rewrites
it into a comma-based construction. Design rules:

* **Em-dash only.** The en-dash (``–``, U+2013) is left untouched, because it is
  the *correct* character for numeric ranges like ``$20k–50k`` or ``$52–98``.
  Rewriting those would introduce errors, so we never do.
* **Code is sacred.** Fenced code blocks (```` ``` ````/``~~~``) and inline code
  spans (`` `like this` ``) are preserved verbatim, so ASCII diagrams and
  snippets survive intact.

Usage::

    python scripts/strip_emdash.py --check            # exit 1 if any em-dash found
    python scripts/strip_emdash.py --fix              # rewrite files in place
    python scripts/strip_emdash.py --check docs README.md   # specific targets

With no paths, it scans ``docs/`` and ``README.md`` relative to the repo root.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

EMDASH = "—"  # —
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"(`+)(?:.*?)\1")
# Any whitespace surrounding an em-dash collapses to a single ", ".
EMDASH_RE = re.compile(r"\s*" + EMDASH + r"\s*")

DEFAULT_TARGETS = ("docs", "README.md")


def _transform_prose(text: str) -> str:
    return EMDASH_RE.sub(", ", text)


def _transform_line(line: str) -> str:
    """Rewrite prose on a line, leaving inline-code spans verbatim."""
    out: list[str] = []
    pos = 0
    for m in INLINE_CODE_RE.finditer(line):
        out.append(_transform_prose(line[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(_transform_prose(line[pos:]))
    return "".join(out)


def transform_markdown(src: str) -> str:
    """Return ``src`` with em-dashes rewritten outside of code.

    When an em-dash opened a soft-wrapped line, a naive replacement would strand
    the comma at the start of the next line (rendering as ``word , next``). We
    reattach that comma to the end of the previous prose line so it reads
    ``word, next``. Trailing ``", "`` left by an end-of-line em-dash is also
    tidied to ``","`` (Markdown re-inserts the wrap space).
    """
    leading_comma = re.compile(r"^([ \t]*), (\S.*)$")
    prose_tail = re.compile(r"[\w)\]\"'’]$")
    in_fence = False
    result: list[str] = []
    for line in src.split("\n"):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            result.append(line)
            continue
        if in_fence:
            result.append(line)
            continue
        t = re.sub(r",[ \t]+$", ",", _transform_line(line))
        m = leading_comma.match(t)
        if m and result and result[-1].strip() and prose_tail.search(result[-1]):
            result[-1] += ","
            t = m.group(1) + m.group(2)
        result.append(t)
    return "\n".join(result)


def iter_markdown_files(targets: list[str]) -> list[Path]:
    files: list[Path] = []
    for t in targets:
        p = Path(t)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.suffix == ".md" and p.is_file():
            files.append(p)
    return files


def _offenders(src: str) -> list[tuple[int, str]]:
    """Line number + text for em-dashes that live in prose (not code)."""
    hits: list[tuple[int, str]] = []
    in_fence = False
    for n, line in enumerate(src.split("\n"), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if EMDASH in _strip_inline_code(line):
            hits.append((n, line.strip()))
    return hits


def _strip_inline_code(line: str) -> str:
    return INLINE_CODE_RE.sub("", line)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Strip em-dashes from Markdown prose.")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true",
                      help="report offenders and exit 1 if any (default)")
    mode.add_argument("--fix", action="store_true",
                      help="rewrite files in place")
    ap.add_argument("paths", nargs="*", default=list(DEFAULT_TARGETS),
                    help="files or directories (default: docs/ and README.md)")
    args = ap.parse_args(argv)

    files = iter_markdown_files(args.paths or list(DEFAULT_TARGETS))
    if not files:
        print("strip_emdash: no Markdown files found", file=sys.stderr)
        return 0

    total = 0
    changed = 0
    for f in files:
        src = f.read_text(encoding="utf-8")
        hits = _offenders(src)
        if not hits:
            continue
        total += len(hits)
        if args.fix:
            f.write_text(transform_markdown(src), encoding="utf-8")
            changed += 1
            print(f"fixed {len(hits):>3} in {f}")
        else:
            for n, text in hits:
                print(f"{f}:{n}: {text}")

    if args.fix:
        print(f"\nstrip_emdash: rewrote {total} em-dash(es) across {changed} file(s)")
        return 0

    if total:
        print(f"\nstrip_emdash: found {total} em-dash(es). Run with --fix to rewrite.",
              file=sys.stderr)
        return 1
    print("strip_emdash: clean, no em-dashes in prose.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
