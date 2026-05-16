import time
import requests

def mobile_monitor():
    url = "https://example.com"
    print(f"Monitoring {url} from Android...")
    
    while True:
        try:
            status = requests.get(url).status_code
            print(f"[{time.ctime()}] Status: {status}")
        except Exception as e:
            print(f"Error: {e}")
            
        # Wait 10 minutes before checking again
        time.sleep(600)

if __name__ == "__main__":
    mobile_monitor()

