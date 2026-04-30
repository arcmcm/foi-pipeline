#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import requests
from pathlib import Path

# Load .env
load_dotenv('/home/arcmcm/jobbot/.env')
host = os.getenv("HOST", "arcmcm.local")
port = os.getenv("FOI_PORT", "8000")

DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

def download_file(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        filename = url.split("/")[-1].split("?")[0]
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
        urls = []
        for line in f:
            path = line.strip()
            if not path:
                continue
            if path.startswith("http"):
                urls.append(path)
            else:
                urls.append(f"http://{host}:{port}/{path.lstrip('/')}")

    print(f"Using FOI server: http://{host}:{port}")

    for url in urls:
        download_file(url)

if __name__ == "__main__":
    main()
