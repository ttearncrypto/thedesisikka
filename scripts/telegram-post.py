#!/usr/bin/env python3
"""Post new RSS items to a Telegram channel/group via bot API.

Requires env: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, SITE_RSS
State (last-sent item guids) persists in a JSON file so nothing is
reposted; the GitHub Actions workflow caches that file between runs.

Usage: python scripts/telegram-post.py
"""
import json
import os
import pathlib
import sys
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
CHAT = os.getenv("TELEGRAM_CHAT_ID", "").strip()
RSS_URL = os.getenv("SITE_RSS", "https://ttearncrypto.github.io/thedesisikka/rss.xml").strip()
STATE_FILE = os.getenv("STATE_FILE", "telegram-state.json").strip()

if not TOKEN or not CHAT:
    print("TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID not set; skipping.")
    sys.exit(0)


def load_state():
    try:
        return set(json.loads(pathlib.Path(STATE_FILE).read_text(encoding="utf-8")))
    except Exception:
        return set()


def save_state(guids):
    pathlib.Path(STATE_FILE).write_text(
        json.dumps(sorted(guids), indent=2), encoding="utf-8"
    )


def fetch_rss():
    req = urllib.request.Request(
        RSS_URL, headers={"User-Agent": "DESI-Sikka-TelegramBot/1.0"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def send(guid, title, link, category):
    text = "<b>{}</b>\n\n{}{}".format(
        title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"),
        link,
        f"\n\n#{category.replace(' ', '').replace('-', '')}" if category else "",
    )
    url = "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)
    data = urllib.parse.urlencode(
        {
            "chat_id": CHAT,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": "false",
        }
    ).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    if not body.get("ok"):
        raise RuntimeError("Telegram error: {}".format(body))


def main():
    seen = load_state()
    xml_text = fetch_rss()
    root = ET.fromstring(xml_text)
    items = root.findall(".//item")

    posted = 0
    for item in items:
        guid_el = item.find("guid")
        link_el = item.find("link")
        title_el = item.find("title")
        cat_el = item.find("category")

        guid = (guid_el.text or "").strip() if guid_el is not None else ""
        link = (link_el.text or "").strip() if link_el is not None else ""
        title = (title_el.text or "").strip() if title_el is not None else ""
        category = (cat_el.text or "").strip() if cat_el is not None else ""

        if not guid or guid in seen:
            continue
        if not title or not link:
            seen.add(guid)
            save_state(seen)
            continue
        send(guid, title, link, category)
        seen.add(guid)
        save_state(seen)
        posted += 1
        print("posted:", title)

    print(f"done: {posted} new item(s) posted, {len(seen)} tracked total.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - report and fail so CI surfaces it
        print("telegram-post error: {}".format(e))
        sys.exit(1)