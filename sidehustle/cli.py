from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from . import storage
from .render import render_index


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return s or "untitled"


def cmd_add(args: argparse.Namespace) -> int:
    title = args.title
    tags = (args.tags or "").split(",") if args.tags else []
    body = args.body or ""
    did = f"{storage.list_by_tag().__len__()+1:04d}-{slugify(title)}"
    draft = storage.Draft.new(did, title, tags, body)
    storage.save(draft)
    print(did)
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    drafts = storage.list_by_tag(args.tag)
    for d in drafts:
        print(f"{d.id}\t{','.join(d.tags)}\t{d.title}")
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    out = Path("build")
    out.mkdir(parents=True, exist_ok=True)
    drafts = storage.list_by_tag(args.tag)
    items = render_index(args.tag)
    html = f"""
    <html>
    <head><meta charset=\"utf-8\"><title>SideHustle Drafts</title></head>
    <body>
    <h1>SideHustle Drafts</h1>
    {items}
    </body>
    </html>
    """
    (out / "index.html").write_text(html)
    print(str(out / "index.html"))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="sidehustle", description="SideHustle drafts helper")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="add a new draft")
    a.add_argument("title")
    a.add_argument("--tags")
    a.add_argument("--body")
    a.set_defaults(func=cmd_add)

    l = sub.add_parser("list", help="list drafts")
    l.add_argument("--tag")
    l.set_defaults(func=cmd_list)

    b = sub.add_parser("build", help="build static site")
    b.add_argument("site", nargs="?")
    b.add_argument("--tag")
    b.set_defaults(func=cmd_build)
    return p


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
