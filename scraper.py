import requests
from bs4 import BeautifulSoup
import time

def scrape_data():
    # Practice site URL
    url = "https://www.scrapethissite.com/pages/forms/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # This checks if the page loaded correctly
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # This looks for the table rows on the practice site
        items = soup.find_all("tr", class_="team")
        
        if items:
            for item in items[:3]: # Just get the first 3 to test
                name = item.find("td", class_="name").get_text().strip()
                print(f"Found Data: {name}")
        else:
            print("⚠️ Tag not found. Check the website source code.")

    except requests.exceptions.ConnectionError:
        print("⚠️ Connection failed. Check your internet or VPN.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

if __name__ == "__main__":
    scrape_data()

