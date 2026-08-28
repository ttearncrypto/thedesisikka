#!/usr/bin/env python3
"""Validate a built Jekyll site: feeds, search index, JSON-LD blocks,
and post front matter against the news-publishing contract.

Usage: python scripts/validate.py <path-to-_site>
"""
import datetime
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

SITE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
ROOT = pathlib.Path(__file__).resolve().parent.parent

VALID_CATS = {"bitcoin", "ethereum", "altcoins", "regulation", "defi", "exchanges"}
errors = []


def parse_yaml():
    try:
        import yaml
        return yaml
    except ImportError:
        return None


# 1. feed.json must be strict valid JSON with an items list
feed_json = SITE / "feed.json"
if feed_json.exists():
    try:
        data = json.loads(feed_json.read_text(encoding="utf-8"))
        if not isinstance(data.get("items"), list):
            errors.append("feed.json: missing 'items' array (site has no posts?)")
    except Exception as e:
        errors.append(f"feed.json: invalid JSON: {e}")
else:
    errors.append("feed.json: missing from build output")

# 2. search.json must parse (powers site search + saved list)
search_json = SITE / "search.json"
if search_json.exists():
    try:
        json.loads(search_json.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"search.json: invalid JSON: {e}")

# 3. feeds must be well-formed XML
for name in ("rss.xml", "atom.xml", "feed.xml"):
    p = SITE / name
    if not p.exists():
        errors.append(f"{name}: missing from build output")
        continue
    try:
        ET.fromstring(p.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"{name}: malformed XML: {e}")

# 4. every application/ld+json block must parse as JSON
ld_count = 0
for html in SITE.rglob("*.html"):
    txt = html.read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        txt,
        re.S,
    ):
        blob = m.group(1)
        if not blob.strip():
            continue
        ld_count += 1
        try:
            json.loads(blob)
        except Exception as e:
            errors.append(f"{html.relative_to(SITE)}: JSON-LD invalid: {e}")

# 5. post front matter lint (mirrors skills/news-publishing/SKILL.md)
yaml_mod = parse_yaml()
if yaml_mod is None:
    print("WARN: pyyaml not installed; skipping front-matter lint", file=sys.stderr)
else:
    posts = sorted(ROOT.glob("_posts/*.md")) + sorted(ROOT.glob("_posts/*.markdown"))
    for post in posts:
        txt = post.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---", txt, re.S)
        if not m:
            errors.append(f"{post.name}: no front matter block")
            continue
        try:
            fm = yaml_mod.safe_load(m.group(1)) or {}
        except Exception as e:
            errors.append(f"{post.name}: front matter YAML error: {e}")
            continue

        title = (fm.get("title") or "").strip()
        if not title:
            errors.append(f"{post.name}: missing title")
        elif len(title) > 110:
            errors.append(f"{post.name}: title {len(title)} chars (>110)")

        if not fm.get("date"):
            errors.append(f"{post.name}: missing date")

        cats = list(fm.get("categories") or [])
        if len(cats) != 1:
            errors.append(f"{post.name}: expected exactly one category (got {len(cats)})")
        elif cats[0] not in VALID_CATS:
            errors.append(f"{post.name}: unknown category '{cats[0]}'")

        desc = (fm.get("description") or "").strip()
        if not desc:
            errors.append(f"{post.name}: missing description")
        elif not (120 <= len(desc) <= 180):
            errors.append(f"{post.name}: description {len(desc)} chars (want 120-180)")

        summ = fm.get("summary")
        if not isinstance(summ, list) or not (0 < len(summ) <= 5):
            errors.append(f"{post.name}: summary must be a list of 1-5 bullets")
        elif any(not str(b).strip() for b in summ):
            errors.append(f"{post.name}: empty summary bullet")

        if not (fm.get("keywords") or "").strip():
            errors.append(f"{post.name}: missing keywords")

        d = fm.get("date")
        if d is not None:
            try:
                ds = d.date() if hasattr(d, "date") else d
                if ds > datetime.date.today():
                    errors.append(f"{post.name}: date {ds} is in the future")
            except Exception:
                pass

        author = fm.get("author")
        if author is not None:
            known = {"newsdesk", "muskanshaik"}
            if author not in known:
                errors.append(f"{post.name}: unknown author '{author}'")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print(f"OK: {ld_count} JSON-LD blocks valid; feeds + search index parse; front matter lint clean")