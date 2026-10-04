#!/usr/bin/env python3
"""Offline checks for the production output. Run after hugo --gc --minify."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import re
import sys
import tomllib
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "public"
CONFIG = tomllib.loads((ROOT / "config.toml").read_text())
BASE = CONFIG["baseURL"]

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def attrs(self, tag):
        return [attrs for name, attrs in self.tags if name == tag]

    def meta(self, key):
        return [attrs.get("content", "") for attrs in self.attrs("meta")
                if attrs.get("name", attrs.get("property")) == key]

    def canonical(self):
        return [attrs.get("href") for attrs in self.attrs("link")
                if "canonical" in attrs.get("rel", "").split()]


def local_exists(url, page_url=BASE):
    parsed = urlsplit(urljoin(page_url, url))
    if parsed.scheme not in ("http", "https") or parsed.netloc != urlsplit(BASE).netloc:
        return True  # Network-dependent links are outside this offline smoke check.
    path = PUBLIC / unquote(parsed.path).lstrip("/")
    return path.is_file() or (path / "index.html").is_file()

assert PUBLIC.is_dir(), f"Build directory missing: {PUBLIC}"
html_files = list(PUBLIC.rglob("*.html"))
assert html_files, "No HTML output"
for path in html_files:
    text = path.read_text()
    doc = Document(text)
    page_url = urljoin(BASE, path.relative_to(PUBLIC).as_posix())
    for tag, attrs in doc.tags:
        # Check generated internal navigation, CSS, images, scripts and feed links.
        attr = "src" if tag in ("img", "script", "source") else "href" if tag in ("a", "link") else None
        if attr and attrs.get(attr):
            assert local_exists(attrs[attr], page_url), f"{path}: missing {attrs[attr]}"

home_text = (PUBLIC / "index.html").read_text()
home = Document(home_text)
assert home.canonical() == [BASE], home.canonical()
assert home.attrs("html")[0].get("lang", "").startswith("en")
assert home.meta("viewport") and "width=device-width" in home.meta("viewport")[0]
assert any("charset" in attrs for attrs in home.attrs("meta"))

items = []
for filename in ("index.xml", "rss.xml"):
    feed = ET.parse(PUBLIC / filename).getroot()
    assert feed.tag == "rss"
    channel = feed.find("channel")
    assert channel is not None
    entries = channel.findall("item")
    assert len(entries) == CONFIG["services"]["rss"]["limit"] == 1
    self_link = channel.find("{http://www.w3.org/2005/Atom}link")
    assert self_link is not None and self_link.attrib["href"] == BASE + filename
    assert entries[0].findtext("link", "").startswith(BASE)
    items.append(ET.tostring(entries[0]))
assert items[0] == items[1], "Both feed URLs must publish the same item"
draft = ROOT / "content/post/2026-07-19-ai-will-not-fix-the-way-actuaries-work.md"
assert re.search(r"(?m)^draft:\s*true\s*$", draft.read_text()), "Do not publish the existing draft"
assert not any("ai-will-not-fix" in str(path) for path in html_files), "Draft leaked into production"
assert "ai-will-not-fix" not in home_text and "ai-will-not-fix" not in (PUBLIC / "index.xml").read_text()
redirects = (PUBLIC / "_redirects").read_text()
assert "https://blog.houstonperrett.com/* https://blog.houstonp.com/:splat 301!" in redirects
assert "/subscribe / 301!" in redirects
print(f"PASS: {len(html_files)} HTML files, local links/assets, metadata, two one-item feeds, draft exclusion, redirects")
