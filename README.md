# 📰 Medium Scraper (Freedium-backed)

A simple but powerful **Python CLI tool** that scrapes Medium articles — including **member-only** posts — by automatically routing them through **[Freedium](https://freedium.cfd)**.

It extracts:
- Title  
- Author  
- Publish date  
- Canonical URL  
- Images (URLs + alt text)  
- Full article body in clean **Markdown**

and saves everything locally as both `.json` and `.md` files.

---

## 🚀 Features
✅ Works on **member-only Medium articles**  
✅ Converts the article to **Markdown**  
✅ Saves metadata + images list in JSON  
✅ Lightweight — no login or API key needed  
✅ Works via **command-line arguments**

---

## 📦 Installation

Clone or download this repository, then install dependencies:

```bash
pip install requests beautifulsoup4 markdownify
```

---

## 🧠 Usage

### 1️⃣ Basic command
```bash
python medium_scraper.py "https://medium.com/bugbountywriteup/how-i-used-sequential-ids-to-download-an-entire-companys-user-database-and-the-joker-helped-2a8dd23127e6"
```

The script will automatically convert the Medium URL into a Freedium mirror and scrape it.

Example output:
```
🔗 Fetching from Freedium mirror:
https://freedium.cfd/https://medium.com/bugbountywriteup/how-i-used-sequential-ids-to-download-an-entire-companys-user-database-and-the-joker-helped-2a8dd23127e6

✅ Saved Markdown: scraped_articles/How I Used Sequential IDs to Download an Entire Company’s User Database.md
✅ Saved JSON: scraped_articles/How I Used Sequential IDs to Download an Entire Company’s User Database.json
```

---

### 2️⃣ Specify output folder
```bash
python medium_scraper.py "https://medium.com/@iski/some-article" -o output_folder
```

This saves files into your chosen folder instead of the default `scraped_articles/`.

---

### 3️⃣ Command help
```bash
python medium_scraper.py -h
```

Output:
```
usage: medium_scraper.py [-h] [-o OUTPUT] url

Scrape a Medium article (via Freedium)

positional arguments:
  url                   Medium article URL (normal or Freedium link)

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output folder (default: scraped_articles)
```

---

## 🧾 Output Format

### 🗂️ JSON (`.json`)
```json
{
  "url": "https://freedium.cfd/https://medium.com/...article...",
  "title": "How I Used Sequential IDs to Download an Entire Company’s User Database",
  "author": "Iski",
  "date": "October 21, 2025",
  "canonical": "https://medium.com/...original...",
  "scraped_at": "2025-11-04T09:10:00Z",
  "images": [
    {"src": "https://miro.medium.com/v2/resize:fit:1100/1*xyz.jpg", "alt": ""}
  ],
  "markdown": "# How I Used Sequential IDs to Download an Entire Company’s User Database\n\n[Article content here...]"
}
```

### 📝 Markdown (`.md`)
```markdown
# How I Used Sequential IDs to Download an Entire Company’s User Database

_By Iski_  
_Published: October 21, 2025_

[Full article body here...]
```

---

## ⚙️ How It Works
1. Takes your Medium URL.  
2. Converts it to a Freedium mirror (`https://freedium.cfd/<medium-url>`).  
3. Fetches the Freedium HTML.  
4. Extracts metadata + main `.main-content`.  
5. Converts HTML → Markdown using `markdownify`.  
6. Saves `.json` and `.md` locally.  

---

## 🧩 Tech Stack
- **Python 3.8+**
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [Markdownify](https://pypi.org/project/markdownify/)

---

## ⚠️ Disclaimer
This tool is for **educational and personal research** purposes only.  
Respect Medium’s [Terms of Service](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f) and authors’ copyrights.  
Do **not** use it for commercial redistribution or automated mass scraping.

---

## 🧪 Example Use Cases
- Summarizing or analyzing Medium writeups programmatically  
- Backing up your own Medium posts  
- Extracting Markdown for static-site migration  
- Research dataset creation (ethical use only)

---

## 🧱 Folder structure
```
medium_scraper.py
README.md
scraped_articles/
 ├─ Some Article.md
 └─ Some Article.json
```

---

## ❤️ Author
Built by **Dimuth De Zoysa**  
Inspired by the need to make Medium content more accessible for researchers and learners.

---

## 📜 License
MIT License — free to modify and use with attribution.
