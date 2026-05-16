# Create the Python script
cat <<EOF > audit.py
import requests
from bs4 import BeautifulSoup
import json

def run_audit(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        report = {
            "target": url,
            "title": soup.title.string.strip() if soup.title else "Missing Title",
            "h1_count": len(soup.find_all('h1')),
            "images_without_alt": len([img for img in soup.find_all('img') if not img.get('alt')])
        }
        with open('latest_audit.json', 'w') as f:
            json.dump(report, f, indent=4)
        print("[+] Audit complete.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    site = input("Enter URL: ")
    run_audit(site)
EOF

# Create the Sync script
cat <<EOF > sync.sh
#!/bin/bash
python audit.py
git add .
git commit -m "SEO Audit Update: \$(date +%Y-%m-%d)"
git push origin main
EOF

chmod +x sync.sh

