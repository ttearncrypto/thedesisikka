#!/usr/bin/env python3
"""Binance WOTD daily autopilot runner for The DESI Sikka.

Fetch tracker pages for a target date, cross-check the theme and 3-8 letter word
lists, render the daily post in the established repository template, and (in ship
mode) build-check, commit, and push to main.

True to the editorial rule on this site, this script never fabricates data. If
tracker extraction does not clear the consensus gates, it aborts instead of
publishing, and raises an alert (GitHub issue + optional Telegram message).

Usage:
  python scripts/wotd-daily.py                 # today, IST; write + commit + push when WOTD_SHIP=1
  python scripts/wotd-daily.py --date 2026-09-25
  python scripts/wotd-daily.py --dry-run       # print the rendered post, write nothing
  python scripts/wotd-daily.py --json          # print the extracted data model only

A hand-verified data file at scripts/wotd-data/<date>.json always wins over
scraping. See the SKILL.md docs for the schema.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POSTS = REPO / "_posts"
DATA_DIR = REPO / "scripts" / "wotd-data"
IST = timezone(timedelta(hours=5, minutes=30))

MONTH_ABBR = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "June",
    7: "July", 8: "Aug", 9: "Sept", 10: "Oct", 11: "Nov", 12: "Dec",
}
MONTH_FULL = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
    6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
    11: "November", 12: "December",
}
MONTH_SLUG = {
    1: "january", 2: "february", 3: "march", 4: "april", 5: "may",
    6: "june", 7: "july", 8: "august", 9: "september", 10: "october",
    11: "november", 12: "december",
}

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
     "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"

NOISE_WORDS = {
    "THE", "AND", "WITH", "FROM", "WORD", "WORDS", "LETTER", "LETTERS",
    "ANSWERS", "ANSWER", "TODAY", "DATE", "THEME", "BINANCE", "ALSO",
    "FOR", "THIS", "THAT", "MORE", "IN", "OUR", "YOUR", "EACH", "WHEN",
    "USDC", "BNB", "POOL", "REWARD", "REWARDS", "SHARE", "SPLIT",
    "WILL", "YOU", "CAN", "FULL", "LIST", "FIVE", "SIX", "SEVEN", "EIGHT",
}


def log(*args):
    print("[wotd]", *args, file=sys.stderr)


# --------------------------------------------------------------------------- #
# Agent-side notes in the data block (for the skill / humans).
# --------------------------------------------------------------------------- #
def today_ist() -> date:
    return datetime.now(IST).date()


def existing_post_for(day: date) -> bool:
    prefix = day.isoformat()
    for p in POSTS.glob("*.md"):
        if p.name.startswith(prefix) and "binance-wotd" in p.name:
            return True
    return False


def fetch(url: str, timeout: int = 20) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", "ignore")
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, TimeoutError) as exc:
        log("fetch failed", url, "->", exc)
        return None


def strip_tags(html: str) -> str:
    html = re.sub(r"<script.*?</script>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<style.*?</style>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<[^>]+>", "\n", html)
    return re.sub(r"[ \t]+", " ", html)


def extract_words(text: str) -> list[str]:
    words: list[str] = []
    for m in re.finditer(r"[A-Z][A-Z]{2,7}", text):
        w = m.group(0)
        if len(w) < 3 or len(w) > 8 or w in NOISE_WORDS:
            continue
        if w not in words:
            words.append(w)
    return words


def extract_lengths(text: str) -> dict[str, list[str]]:
    text = "\n".join(l.strip() for l in text.splitlines() if l.strip())
    labels = list(re.finditer(r"(?i)([3-8])\s*(?:-|to)?\s*letters?\s*:", text))
    out: dict[str, list[str]] = {}
    for i, m in enumerate(labels):
        start = m.end()
        end = labels[i + 1].start() if i + 1 < len(labels) else min(start + 500, len(text))
        chunk = text[start:end]
        words = extract_words(chunk)
        if words:
            out.setdefault(m.group(1), []).extend(words)
    # hard fallback: "3 letters LOG RUN KEY" without a trailing colon
    if not out:
        for m in re.finditer(
            r"(?i)([3-8])\s*letters?\s+([A-Z][A-Z\s,·|/]{2,120})", text
        ):
            words = extract_words(m.group(2))
            if words:
                out.setdefault(m.group(1), []).extend(words)
    for key in out:
        out[key] = list(dict.fromkeys(out[key]))
    return out


def extract_theme(text: str) -> str | None:
    m = re.search(r"(?i)theme\s*[:—\-]?\s*([A-Z][A-Za-z0-9 ,&'.()+-]{3,70})", text)
    if m:
        t = m.group(1).strip().strip(":.\n")
        if len(t) <= 70:
            return t
    return None


def extract_reward(text: str) -> str | None:
    for m in re.finditer(r"\b([\d,]+)\s*(USDC|BNB)\b", text):
        n = int(m.group(1).replace(",", ""))
        if n in (3, 15, 10000, 7000):
            return f"{m.group(1)} {m.group(2)}"
    m = re.search(r"reward\s*pools?\s*(?:of|:)?\s*([\d,]+)\s*(USDC|BNB)", text, re.I)
    if m:
        return f"{m.group(1)} {m.group(2)}"
    return None


def parse_tracker(html: str) -> dict:
    text = strip_tags(html)
    words = extract_lengths(text)
    return {
        "theme": extract_theme(text),
        "words": {k: v for k, v in words.items()},
        "reward": extract_reward(text),
    }


def tracker_urls(day: date) -> list[str]:
    d, mon, y = day.day, MONTH_SLUG[day.month], day.year
    return [
        f"https://www.quiknotes.in/binance-word-of-the-day-answer-today-{d}-{mon}-{y}/",
        f"https://www.coingabbar.com/en/binance-word-of-the-day-answer-{d}-{mon}-{y}-full-wotd-list",
        f"https://www.bittime.com/en/blog/binance-word-of-the-day-{d}-{mon}-{y}",
    ]


# --------------------------------------------------------------------------- #
# Consensus.
# --------------------------------------------------------------------------- #
def build_consensus(parsed: list[dict]) -> tuple[dict, list[str]]:
    files: list[dict] = [p for p in parsed if p["words"]]
    notes: list[str] = []
    themes = Counter(p["theme"] for p in parsed if p.get("theme"))
    rewards = Counter(p["reward"] for p in parsed if p.get("reward"))

    theme, theme_sources = ("", 0)
    if themes:
        theme, theme_sources = themes.most_common(1)[0]

    final_words: dict[str, list[str]] = {}
    for length in range(3, 9):
        counts: Counter = Counter()
        for p in files:
            for w in p["words"].get(str(length), []):
                counts[w] += 1
        strong = [w for w in sorted(counts, key=lambda x: -counts[x]) if counts[w] >= 2]
        singles = [w for w in sorted(counts, key=lambda x: -counts[x]) if counts[w] == 1]
        final_words[str(length)] = strong + singles

    strong_lengths = 0
    for length in range(3, 9):
        counts: Counter = Counter()
        for p in files:
            for w in p["words"].get(str(length), []):
                counts[w] += 1
        if any(c >= 2 for c in counts.values()):
            strong_lengths += 1

    reward, reward_sources = ("", 0)
    if rewards:
        reward, reward_sources = rewards.most_common(1)[0]

    gate_ok = (
        theme_sources >= 2
        and len(files) >= 2
        and all(final_words[str(length)] for length in range(3, 9))
        and strong_lengths >= 3
    )
    return {
        "theme": theme,
        "theme_sources": theme_sources,
        "reward": reward,
        "reward_sources": reward_sources,
        "words": final_words,
        "tracker_files": len(files),
        "strong_lengths": strong_lengths,
        "gate_ok": gate_ok,
        "sources": sum(1 for p in parsed if p["words"]),
    }, notes


# --------------------------------------------------------------------------- #
# Data file overrides (hand-verified wins over scraping).
# --------------------------------------------------------------------------- #
def load_data_file(day: date) -> dict | None:
    path = DATA_DIR / f"{day.isoformat()}.json"
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    return data if data.get("words") and data.get("theme") else None


# --------------------------------------------------------------------------- #
# Rendering.
# --------------------------------------------------------------------------- #
def build_description(day: date, theme: str, reward: str) -> str:
    m = MONTH_FULL[day.month]
    variants = [
        f"Binance WOTD answers for {m} {day.day}, {day.year}: get the full 3 to 8 "
        f"letter word list for the {theme} theme, plus how to play and {reward} in rewards.",
        f"Binance WOTD answers for {m} {day.day}, {day.year}: get the full 3 to 8 "
        f"letter word list for the {theme} theme, plus how to play.",
        f"Binance WOTD answers for {m} {day.day}, {day.year}: the full 3 to 8 letter "
        f"word list for the {theme} theme, plus how to play for {reward} in rewards.",
        f"Binance WOTD answers for {m} {day.day}, {day.year}: the full 3 to 8 letter "
        f"word list for the {theme} theme, plus how to play.",
    ]
    best = None
    for v in variants:
        n = len(v)
        if 150 <= n <= 160:
            return v
        if best is None or abs(n - 155) < abs(len(best) - 155):
            best = v
    return best if best else variants[0]


def render_post(day: date, theme: str, words: dict[str, list[str]], reward: str,
                campaign_end: date | None, confirmed: str | None, reward_detail: str | None,
                two_games: bool = False) -> str:
    m = MONTH_ABBR[day.month]
    mfull = MONTH_FULL[day.month]
    d, y, ymd = day.day, day.year, day.isoformat()
    end_str = f"{MONTH_ABBR[campaign_end.month]} {campaign_end.day}" if campaign_end else "the end of the cycle"

    w3 = ", ".join(words["3"])
    w4 = ", ".join(words["4"])
    w5 = ", ".join(words["5"])
    w6 = ", ".join(words["6"])
    w7 = ", ".join(words["7"])
    w8 = ", ".join(words["8"])
    first_pair = f"{words['3'][0]} and {words['4'][0]}" if len(words["3"]) and len(words["4"]) else "3 letters"
    last_pair = f"{words['8'][0]} and {words['7'][0]}" if len(words["8"]) and len(words["7"]) else "8 letters"

    if confirmed:
        bullet4 = f"Community trackers logged {confirmed} ({len(confirmed)} letters) as today's answer, with more candidates below."
        faq1 = (f"Community trackers logged {confirmed} ({len(confirmed)} letters) as today's answer. Other "
                f"candidates for the {theme} theme: {w3} (3 letters); {w4} (4); {w5} (5); {w6} (6); "
                f"{w7} (7); {w8} (8). Match the list to the number of tiles in your grid.")
        lead2 = (f"Today's confirmed word is {confirmed} ({len(confirmed)} letters), per community trackers. "
                 f"Even so, count your tiles and check the candidates below before you guess.")
    else:
        bullet4 = "No single confirmed answer is public yet, so use the candidate list with your tile count."
        faq1 = (f"No single confirmed answer is public yet. Possible words for the {theme} theme: {w3} "
                f"(3 letters); {w4} (4); {w5} (5); {w6} (6); {w7} (7); {w8} (8). Match the list to "
                f"the number of tiles in your grid.")
        lead2 = "No confirmed single-word answer is public yet for today. Work from the candidate list below and match it to your tile count."

    if reward_detail:
        earn_para = reward_detail
    elif reward:
        earn_para = (
            f"Rewards change by round, so treat any number you read elsewhere with suspicion. For this "
            f"{theme} cycle, the pool is listed at {reward}, shared among users who bank the campaign's "
            f"required wins, per community trackers that quote the campaign terms."
        )
    else:
        earn_para = (
            "Rewards change by round, so treat any number you read elsewhere with suspicion. Check the "
            "campaign page inside the app for the current pool and eligibility before you put time in."
        )

    play_extra = (
        "Binance lets you play up to two games a day in this cycle. The second one unlocks when you hit "
        "**Get A New WOTD**, share the link, and get a logged-in user to click it. It is a small referral "
        "bump, but it doubles your daily attempts."
        if two_games else
        "You can earn extra attempts by sharing the official campaign link. When someone else opens it, "
        "you typically get one more guess. It is a small referral bump, but it can save a stuck puzzle."
    )

    desc = build_description(day, theme, reward or "USDC")

    summary = [
        f"Binance's Word of the Day for {mfull} {d}, {y} runs under the {theme} theme, live through {end_str}.",
        f"Possible answers span 3 to 8 letters, from {first_pair} up to {last_pair}.",
        "Different accounts get different word lengths, so match the list to your grid before guessing.",
        bullet4,
        "Rules and rewards are set in-app and can change without notice; check the campaign page for the current prize pool.",
    ]

    kw = (f"binance wotd, word of the day answers, binance word of the day {MONTH_SLUG[day.month]} {d} {y}, "
          f"binance wotd {' '.join(theme.lower().split())} answers, how to play binance word of the day")

    rel_img = "{{ '/assets/articles-images/binance-wotd-app-grid.webp' | relative_url }}"
    rel_learn = "{{ '/pages/learn/' | relative_url }}"

    post = f"""---
title: "Binance WOTD Answers {m} {d}, {y}: Full List"
seo_title: "Binance WOTD Answers {m} {d}, {y}"
date: {ymd}
categories: [todays-combo, news]
tags: [combo]
author: muskanshaik
large_text: true
description: "{desc}"
summary:
  - "{summary[0]}"
  - "{summary[1]}"
  - "{summary[2]}"
  - "{summary[3]}"
  - "{summary[4]}"
keywords: "{kw}"
cover_image: /assets/articles-images/binance-wotd-answers-hero.webp
image_alt: "Binance Word of the Day puzzle answers for {mfull} {d}, {y}, theme {theme}"
cover_caption: "The Binance Word of the Day puzzle for {mfull} {d}, {y} runs on the {theme} theme."
faq:
  - q: "What are today's Binance WOTD answers for {mfull} {d}, {y}?"
    a: "{faq1}"
  - q: "How do you play Binance Word of the Day?"
    a: "Open the Binance app, tap More, then Gifts and Campaigns, then Word of the Day. Guess a hidden crypto word; green means the letter is right, yellow means it is in the word but misplaced, and grey means it is not in the word."
  - q: "How much can you earn from Binance WOTD today?"
    a: "{earn_para}"
---

Binance's Word of the Day for {mfull} {d}, {y} is live, and the answer list depends on how many tiles your grid shows. The current round runs under the theme **{theme}** and stays open through {end_str}. Get the right word and you earn points toward this cycle's campaign pool.

{lead2}

The catch is that Binance does not give every player the same puzzle. One account might see a 5-letter word while another stares at 8 empty tiles. Match the list below to the number of letters in your own grid, then try each option until one lands.

![Binance WOTD word grid in the mobile app]({rel_img} "Binance WOTD color-coded guessing grid")

## What are the Binance WOTD answers for {mfull} {d}, {y}?

Possible words for the {theme} theme, organized by word length:

**3 letters:** {w3}

**4 letters:** {w4}

**5 letters:** {w5}

**6 letters:** {w6}

**7 letters:** {w7}

**8 letters:** {w8}

| Word length | Possible answers |
| ----------- | ---------------- |
| 3 letters   | {w3} |
| 4 letters   | {w4} |
| 5 letters   | {w5} |
| 6 letters   | {w6} |
| 7 letters   | {w7} |
| 8 letters   | {w8} |

Count the blank tiles first. If the first word in your length group comes back wrong, move to the next one. You have six guesses, so a wasted guess costs you real progress.

## What is Binance Word of the Day?

Binance Word of the Day, shortened to WOTD, is a daily word game inside the Binance app under Gifts and Campaigns. It plays like Wordle: guess a hidden crypto-related word, and after each try the app colors the tiles so you know which letters are right.

The color system is simple. Green means the letter is correct and in the right spot. Yellow means the letter is in the word but in the wrong position. Black or grey means the letter is not in the word at all. Use that feedback to shrink the options instead of guessing blind.

## How do I play Binance Word of the Day?

Open the official Binance app, not a third-party site. From the bottom menu tap **More**, then open **Gifts and Campaigns**, then pick **Word of the Day**. You can also jump straight to the Word of the Day page on the [official Binance site](https://www.binance.com). Enter your guesses and read the colors after each attempt. Most players finish a day's puzzle in under two minutes.

{play_extra}

## How much can you earn from Binance WOTD?

{earn_para}

Binance can change the pool, the eligibility rules, or the prize vouchers at any time without notice. Binance has its own reporting rules for some regions, and crypto rewards are taxable in many places. Check the campaign page inside the app for today's real numbers before you put time in. The safest habit is to treat every third-party word list, including this one, as a starting point, and verify in-app.

## Why do some users see different Binance WOTD answers?

Binance hands out different word lengths, and sometimes different words, to different accounts even under the same daily theme. That is deliberate. If everyone got one shared answer, the challenge would collapse on day one. Count your tiles, pick the matching group, and ignore anyone who claims a single universal answer.

If the answers here look like a mismatch, log in, open the puzzle, and read your actual grid. Themes change weekly and words rotate, so yesterday's list will not save you tomorrow.

## Bottom line

The {mfull} {d}, {y} Binance WOTD runs on the {theme} theme{' until ' + end_str if campaign_end else ''}. Use the 3 to 8 letter lists above, play straight from the official app, and confirm the live prize pool in-app rather than trusting a number you saw on social. Binance reserves the right to change terms with no notice. If this is your first time on the desk, we explain crypto basics without the jargon in our [learn guides]({rel_learn}).
"""
    return post


# --------------------------------------------------------------------------- #
# Ship: write, build-check, commit, push.
# --------------------------------------------------------------------------- #
def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=REPO)


def commit_and_push(filename: Path, day: date) -> bool:
    msg = f"news: Binance WOTD answers {MONTH_ABBR[day.month]} {day.day} {day.year}"
    add = git("add", "--", str(filename.relative_to(REPO)))
    if add.returncode != 0:
        log("git add failed:", add.stderr)
        return False
    commit = git(
        "-c", "user.name=F9XR News Desk", "-c", "user.email=hello@f9xr.org",
        "commit", "-m", msg, "--", str(filename.relative_to(REPO)),
    )
    if commit.returncode != 0:
        log("git commit failed:", commit.stderr)
        return False
    push = git("push", "origin", "HEAD:main")
    if push.returncode != 0:
        log("git push failed:", push.stderr)
        return False
    log("shipped", filename.name, "->", msg)
    return True


def build_check() -> bool:
    try:
        probe = ["cmd", "/c", "where", "jekyll"] if os.name == "nt" else ["which", "jekyll"]
        which = subprocess.run(probe, capture_output=True, text=True)
        if which.returncode != 0:
            log("jekyll not on PATH; skipping local build check")
            return True
        cmd = (["cmd", "/c", "jekyll", "build"] if os.name == "nt"
               else ["jekyll", "build"])
        run = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO)
    except FileNotFoundError:
        log("jekyll executable not launchable; skipping local build check")
        return True
    if run.returncode != 0:
        log("jekyll build failed:", run.stdout[-2000:], run.stderr[-2000:])
        return False
    return True


def alert(title: str, body: str) -> None:
    try:
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if token:
            env = dict(os.environ)
            env["GH_TOKEN"] = token
            subprocess.run(["gh", "issue", "create", "--title", title, "--body", body],
                           capture_output=True, text=True, env=env, timeout=60)
    except Exception as exc:  # noqa: BLE001
        log("issue alert failed:", exc)
    try:
        tok = os.environ.get("TELEGRAM_BOT_TOKEN")
        chat = os.environ.get("TELEGRAM_CHAT_ID")
        if tok and chat:
            url = f"https://api.telegram.org/bot{tok}/sendMessage"
            data = urllib.parse.urlencode({"chat_id": chat, "text": f"{title}\n{body}"}).encode()
            urllib.request.urlopen(url, data=data, timeout=30)
    except Exception as exc:  # noqa: BLE001
        log("telegram alert failed:", exc)


# --------------------------------------------------------------------------- #
# Main.
# --------------------------------------------------------------------------- #
def main(argv: list[str]) -> int:
    day = today_ist()
    dry_run = False
    show_json = False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--date" and i + 1 < len(argv):
            day = date.fromisoformat(argv[i + 1])
            i += 1
        elif a == "--dry-run":
            dry_run = True
        elif a == "--json":
            show_json = True
        i += 1

    if not dry_run and not show_json and existing_post_for(day):
        log(f"{day.isoformat()} already has a post; nothing to do")
        return 0

    data = load_data_file(day)
    parsed: list[dict] = []
    if data:
        consensus = {
            "theme": data["theme"],
            "theme_sources": 1,
            "reward": data.get("reward", ""),
            "reward_sources": 1,
            "words": {str(k): list(v) for k, v in data["words"].items()},
            "tracker_files": 1,
            "strong_lengths": 6,
            "gate_ok": True,
            "sources": 1,
        }
        log("using hand-verified data file:", DATA_DIR / f"{day.isoformat()}.json")
    else:
        urls = tracker_urls(day)
        for url in urls:
            html = fetch(url)
            if html:
                parsed.append(parse_tracker(html))
        consensus, _notes = build_consensus(parsed)

        if show_json:
            print(json.dumps({"date": day.isoformat(),
                              "fetched": [u for _u, u in zip(range(len(urls)), urls)],
                              "parsed": parsed,
                              "consensus": {k: v for k, v in consensus.items()
                                            if k != "words"},
                              "words": consensus["words"]}, indent=2))
            return 0

        if not consensus["gate_ok"]:
            log("WOTD data did not clear consensus gates; aborting without publishing")
            log("theme_sources:", consensus["theme_sources"],
                "tracker_files:", consensus["tracker_files"],
                "strong_lengths:", consensus["strong_lengths"],
                "coverage:", {str(n): bool(consensus["words"].get(str(n)))
                              for n in range(3, 9)})
            alert(
                f"Binance WOTD run aborted for {day.isoformat()}",
                "The scheduled runner could not cross-check the daily word lists (weak or zero "
                "tracker agreement). No post was published. Run the binance-wotd-autopilot skill "
                "to publish manually, or drop a verified data file at "
                f"scripts/wotd-data/{day.isoformat()}.json.",
            )
            return 2

    words = {str(k): list(v) for k, v in consensus["words"].items()}
    if not all(words.get(str(n)) for n in range(3, 9)):
        log("incomplete word coverage; aborting without publishing")
        return 2

    theme = consensus["theme"]
    reward = consensus.get("reward", "") or ""
    confirmed = (data or {}).get("confirmed") or None
    detail = (data or {}).get("reward_detail") or None
    two_games = bool((data or {}).get("two_games", False))
    if not two_games and detail:
        two_games = "two games" in detail.lower()
    end_raw = (data or {}).get("campaign_end")
    campaign_end = date.fromisoformat(end_raw) if end_raw else None

    post = render_post(day, theme, words, reward, campaign_end, confirmed, detail, two_games=two_games)

    if dry_run:
        print(post)
        return 0

    filename = POSTS / f"{day.isoformat()}-binance-wotd-{MONTH_SLUG[day.month]}-{day.day}-{day.year}.md"
    filename.write_text(post, encoding="utf-8")
    log("wrote", filename.name)

    if not build_check():
        log("build check failed; not committing")
        return 3

    if os.environ.get("WOTD_SHIP") == "1" or "--ship" in argv:
        if not commit_and_push(filename, day):
            return 4
    else:
        log("staged build only; WOTD_SHIP=1 or --ship to commit and push")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))