"""Move ideas through the pipeline in ideas/.

Usage:
    python tools/idea.py new "Shift-swap app for the team"
    python tools/idea.py list
    python tools/idea.py move shift-swap-app active
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

IDEAS = Path(__file__).resolve().parent.parent / "ideas"
STAGES = ["inbox", "active", "done", "parked"]


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def find(slug):
    for stage in STAGES:
        path = IDEAS / stage / f"{slug}.md"
        if path.exists():
            return path
    return None


def cmd_new(args):
    slug = slugify(args.title)
    if find(slug):
        sys.exit(f"An idea called '{slug}' already exists.")
    template = (IDEAS / "TEMPLATE.md").read_text()
    text = template.replace("{title}", args.title).replace("{date}", date.today().isoformat())
    path = IDEAS / "inbox" / f"{slug}.md"
    path.write_text(text)
    print(f"Created {path.relative_to(IDEAS.parent)}")


def cmd_list(args):
    for stage in STAGES:
        files = sorted((IDEAS / stage).glob("*.md"))
        print(f"{stage} ({len(files)})")
        for f in files:
            print(f"  {f.stem}")


def cmd_move(args):
    path = find(args.slug)
    if not path:
        sys.exit(f"No idea called '{args.slug}'. Try: python tools/idea.py list")
    target = IDEAS / args.stage / path.name
    # Keep the status line in the front matter in step with the folder.
    text = re.sub(r"^status: \w+$", f"status: {args.stage}", path.read_text(), count=1, flags=re.M)
    target.write_text(text)
    if target != path:
        path.unlink()
    print(f"{args.slug}: {path.parent.name} -> {args.stage}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("new", help="capture a new idea in the inbox")
    p.add_argument("title")
    p.set_defaults(func=cmd_new)

    p = sub.add_parser("list", help="show ideas by stage")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("move", help="move an idea to another stage")
    p.add_argument("slug")
    p.add_argument("stage", choices=STAGES)
    p.set_defaults(func=cmd_move)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
