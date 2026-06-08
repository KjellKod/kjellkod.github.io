---
name: no-emdash
description: Keep em-dashes out of published Markdown prose (the "AI tell"), rewriting them to comma/period/colon/parentheses. Use when writing or reviewing site content, or before committing anything under docs/.
---

# no-emdash

The spaced em-dash (`—`) is a giveaway of machine-written prose. This site does
not use it. This skill is the convention plus the deterministic guard that
enforces it.

## Rule

- Replace `—` with a comma, period, colon, or parentheses, whichever reads best.
  In headings, a colon usually beats a comma.
- Keep the en-dash (`–`) **only** for numeric ranges (`$20k–50k`). Never as
  sentence punctuation.
- Never touch code: fenced blocks and inline code spans stay verbatim, so ASCII
  diagrams and snippets survive.

## Tooling

Deterministic guard at `scripts/strip_emdash.py` (standard library only):

```bash
python scripts/strip_emdash.py --check        # list offenders, exit 1 if any
python scripts/strip_emdash.py --fix          # rewrite docs/ and README.md in place
python scripts/strip_emdash.py --check FILE…   # target specific files/dirs
```

Workflow: run `--check` before publishing. If it flags anything, run `--fix`,
then **review the diff** — comma substitution is mechanical, so a heading or a
list-introducing dash may read better re-cast by hand.
