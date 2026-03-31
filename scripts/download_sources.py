#!/usr/bin/env python3
import requests
from pathlib import Path

DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

def download_file(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        filename = url.split("/")[-1]
        filename = filename.split("?")[0]

        if not filename:
            print(f"Skipped (no filename): {url}")
            return

        filepath = DOWNLOAD_DIR / filename

        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"Downloaded: {filename}")

    except Exception as e:
        print(f"Failed: {url} ({e})")

def main():
    with open("sources_to_fetch.txt") as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        download_file(url)

if __name__ == "__main__":
    main()
