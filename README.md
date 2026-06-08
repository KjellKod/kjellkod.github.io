# kjellkod.github.io

Personal site + blog, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
Publishes to <https://kjellkod.github.io> via GitHub Actions.

Separate from the profile README repo (`KjellKod/KjellKod`) — nothing here affects the
`github.com/KjellKod` profile page.

## Local preview
```bash
pip install -r requirements.txt
mkdocs serve   # http://127.0.0.1:8000
```

## Add a blog post
Create `docs/blog/posts/<slug>.md`:
```markdown
---
date: 2026-06-08
categories:
  - Compliance
slug: my-post-slug
description: One-sentence summary shown in listings and search.
---

# Post Title

Lead paragraph...

<!-- more -->

Rest of the post...
```
The blog index, month archives, category pages, and listing are generated automatically.

## Add / edit a project
Edit `docs/projects.md` — copy a card block and change the icon, title, blurb, and URL.
