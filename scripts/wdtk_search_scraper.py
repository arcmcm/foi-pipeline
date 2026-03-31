#!/usr/bin/env python3
from __future__ import annotations

import requests

URL = "https://www.whatdotheyknow.com/body/glasgow_city_council?page=1"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-GB,en;q=0.9",
}

r = requests.get(URL, headers=HEADERS, timeout=30)
print("status:", r.status_code)

with open("wdtk_page_1.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("saved wdtk_page_1.html")
print("first 500 chars:")
print(r.text[:500])
