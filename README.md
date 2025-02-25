# SideHustle Drafts

A tiny solo project to collect, categorize, and iterate on personal project ideas and notes. Think of it as a lightweight “idea garden” with simple CLI tools to add drafts, tag them, and render static HTML previews for sharing.

This repository evolves like a real weekend/night project: small commits, incremental improvements, and a focus on practicality over perfection.

## Goals
- Fast capture of ideas and short notes
- Easy tagging and filtering
- Export to simple static HTML for quick sharing

## Stack
- Language: Python 3.10+
- No external services required

## Quick Start
```
python -m sidehustle add "My idea title" --tags ai,tools --body "A short description"
python -m sidehustle list --tag ai
python -m sidehustle build site
```

Outputs are written under `build/`.

## Notes on Data
- Drafts are stored as JSON files in `data/`.
- Filenames use a prefix counter plus slug (e.g. `0001-idea.json`).
- Timestamps are in UTC.
