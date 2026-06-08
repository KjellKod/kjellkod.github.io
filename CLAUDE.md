# Repository guide for AI agents

Personal site + blog built with MkDocs Material, deployed to
<https://kjellkod.github.io/> via GitHub Actions. See `README.md` for build,
preview, and authoring steps.

## Writing style

- **No em-dashes.** Never use the em-dash (`—`, U+2014) in prose. Use a comma,
  period, colon, or parentheses, whichever reads best. The spaced em-dash reads
  as an "AI tell" and is not this site's voice.
- The en-dash (`–`, U+2013) is allowed **only** for numeric ranges, e.g.
  `$20k–50k`. Never use it as sentence punctuation.
- Before committing content, run the guard:
  `python scripts/strip_emdash.py --check` (add `--fix` to auto-rewrite). It
  skips fenced code blocks and inline code.

The convention and tooling live in `.claude/skills/no-emdash/SKILL.md`.
