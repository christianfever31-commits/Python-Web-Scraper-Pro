import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Function to extract data
def scrape_market():
    # 1. The target URL (This is a safe site for testing scraping)
    url = "https://www.scrapethissite.com/pages/forms/"
    
    # 2. Set the Headers (Makes your Termux look like a real mobile browser)
    headers = {
        "User-Agent": "Mozilla/5.0 (Android 10; Mobile; rv:115.0) Gecko/115.0 Firefox/115.0"
    }

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Connecting to server...")
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if the connection was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            data_list = []

            # 3. Finding the data rows (The logic)
            # This looks for table rows labeled 'team'
            rows = soup.find_all('tr', class_='team')

            for row in rows:
                name = row.find('td', class_='name').text.strip()
                price_proxy = row.find('td', class_='wins').text.strip() # We use 'wins' as a stand-in for price

                data_list.append({
                    "Scrape_Date": datetime.now().strftime("%Y-%m-%d"),
                    "Property_Name": name,
                    "Estimated_Value": price_proxy
                })

            # 4. Save the results to a CSV file on your phone
            df = pd.DataFrame(data_list)
            df.to_csv('market_leads.csv', index=False)
            
            print("------------------------------------")
            print(f"SUCCESS: {len(data_list)} properties captured.")
            print("File saved as: market_leads.csv")
            print("------------------------------------")
        else:
            print(f"Failed. Server returned code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_market()

