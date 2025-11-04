import argparse
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import json, os
from pathlib import Path
from datetime import datetime, timezone
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MediumScraper/1.0)"
}

def to_freedium_url(url: str) -> str:
    """Convert Medium URL to Freedium mirror."""
    if "freedium.cfd" in url:
        return url
    if "medium.com" not in url:
        raise ValueError("Please provide a valid Medium URL.")
    return f"https://freedium.cfd/{url}"

def fetch_html(url: str) -> str:
    """Fetch page content."""
    r = requests.get(url, headers=HEADERS, timeout=25)
    r.raise_for_status()
    return r.text

def sanitize_filename(name: str) -> str:
    """Remove invalid Windows filename characters."""
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip()

def parse_article(html: str, url: str) -> dict:
    """Parse Freedium HTML page."""
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.select_one("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Untitled"

    author_tag = soup.select_one("a[href*='@']")
    author = author_tag.get_text(strip=True) if author_tag else "Unknown"

    date_tag = soup.find("time")
    date = date_tag.get("datetime") or date_tag.get_text(strip=True) if date_tag else ""

    canonical = soup.find("link", rel="canonical")
    canonical = canonical["href"] if canonical and canonical.get("href") else url

    main = soup.select_one(".main-content")
    if not main:
        raise ValueError("Could not find .main-content container — Freedium layout may have changed.")

    markdown = md(str(main))
    images = [
        {"src": img.get("src"), "alt": img.get("alt", "")}
        for img in main.find_all("img") if img.get("src")
    ]

    return {
        "url": url,
        "title": title,
        "author": author,
        "date": date,
        "canonical": canonical,
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "images": images,
        "markdown": markdown.strip(),
    }

def save_article(article: dict, output_dir: str):
    """Save scraped article as .json and .md"""
    outdir = Path(output_dir)
    outdir.mkdir(exist_ok=True)
    
    # Sanitize filename to avoid Windows invalid chars
    safe_title = sanitize_filename(article["title"])[:80]

    json_path = outdir / f"{safe_title}.json"
    md_path = outdir / f"{safe_title}.md"

    json_path.write_text(json.dumps(article, indent=2, ensure_ascii=False), encoding="utf-8")
    md_path.write_text(
        f"# {article['title']}\n\n_By {article['author']}_  \n_Published: {article['date']}_\n\n{article['markdown']}",
        encoding="utf-8"
    )
    current_pwd = os.popen('cd').read()
    print("Directory : ",current_pwd)
    print(f"✅ Saved Markdown: {md_path}")
    print(f"✅ Saved JSON: {json_path}")

def main():
    parser = argparse.ArgumentParser(description="Medium Scraper (via Freedium)")
    parser.add_argument("url", help="Medium article URL (normal or Freedium link)")
    parser.add_argument("-o", "--output", default="scraped_articles", help="Output folder")
    args = parser.parse_args()

    freedium_url = to_freedium_url(args.url)
    print(f"🔗 Fetching from Freedium mirror:\n{freedium_url}\n")

    html = fetch_html(freedium_url)
    article = parse_article(html, freedium_url)
    save_article(article, args.output)

if __name__ == "__main__":
    main()
