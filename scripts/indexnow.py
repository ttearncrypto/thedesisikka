#!/usr/bin/env python3
"""Submit one or more URLs to IndexNow.

Usage:
    python scripts/indexnow.py <url> [<url> ...]
    python scripts/indexnow.py --key-file d6628032fa1e4b2ea31ba81441024687.txt <url>

The script reads `url` and `baseurl` from _config.yml, finds the 32-char hex
IndexNow key file in the repo root, and posts the URLs to api.indexnow.org,
Bing, and Yandex. A 200 or 202 response means the submission was accepted.

Exit code is 0 when at least one endpoint accepts the payload, 1 otherwise.
"""
import argparse
import json
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEY_RE = re.compile(r"^[0-9a-f]{32}$", re.I)
DEFAULT_ENDPOINTS = [
    "https://api.indexnow.org/IndexNow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow",
]


def read_config():
    text = (ROOT / "_config.yml").read_text(encoding="utf-8")

    def grab(name):
        match = re.search(rf"(?m)^{name}:\s*[\"']?([^\"'\n#]+)", text)
        return match.group(1).strip() if match else ""

    return grab("url").rstrip("/"), grab("baseurl").strip("/")


def find_key_file(explicit=None):
    if explicit:
        path = pathlib.Path(explicit)
        return path if path.is_absolute() else ROOT / path
    for path in ROOT.glob("*.txt"):
        if KEY_RE.match(path.stem):
            return path
    raise SystemExit("No IndexNow key file found (32-char hex .txt in repo root).")


def normalize(url, site_url, baseurl):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    if url.startswith("/"):
        return f"{site_url}/{baseurl}{url}" if baseurl else f"{site_url}{url}"
    return f"{site_url}/{baseurl}/{url.lstrip('/')}" if baseurl else f"{site_url}/{url.lstrip('/')}"


def main():
    parser = argparse.ArgumentParser(description="Submit URLs to IndexNow.")
    parser.add_argument("urls", nargs="+", help="URLs or site-relative paths to submit")
    parser.add_argument("--key-file", help="Path to the IndexNow key file")
    parser.add_argument(
        "--endpoint",
        action="append",
        help="Override the IndexNow endpoint (repeatable)",
    )
    args = parser.parse_args()

    site_url, baseurl = read_config()
    if not site_url:
        raise SystemExit("Could not read `url` from _config.yml.")

    key_file = find_key_file(args.key_file)
    key = key_file.read_text(encoding="utf-8").strip()
    if not KEY_RE.match(key):
        raise SystemExit(f"{key_file} does not contain a 32-char hex key.")
    if key.lower() != key_file.stem.lower():
        raise SystemExit("Key file name and contents do not match.")

    host = urllib.parse.urlsplit(site_url).netloc
    if baseurl:
        key_location = f"{site_url}/{baseurl}/{key_file.name}"
    else:
        key_location = f"{site_url}/{key_file.name}"

    urls = [normalize(url, site_url, baseurl) for url in args.urls]
    payload = {
        "host": host,
        "key": key,
        "keyLocation": key_location,
        "urlList": urls,
    }
    body = json.dumps(payload).encode("utf-8")
    endpoints = args.endpoint or DEFAULT_ENDPOINTS

    accepted = False
    for endpoint in endpoints:
        request = urllib.request.Request(
            endpoint,
            data=body,
            method="POST",
            headers={"Content-Type": "application/json; charset=utf-8"},
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                print(f"{endpoint} -> {response.status}")
                accepted = accepted or 200 <= response.status < 300
        except urllib.error.HTTPError as error:
            print(f"{endpoint} -> {error.code} {error.reason}")
        except Exception as error:
            print(f"{endpoint} -> error: {error}")

    if not accepted:
        print("No endpoint accepted the submission.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
