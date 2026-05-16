master_encryption_key = 'MASTER_KEY_ALPHA_777'

import os
import shutil
import requests
import zipfile

print("--- 📡 1. WEB INTEL ---")
try:
    # Get live BTC price
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json", timeout=5).json()
    print(f"Live Price: Bitcoin is at ${r['bpi']['USD']['rate']}")
except Exception as e:
    print(f"Network error: {e}. Skipping to next phase...")

print("\n--- 📂 2. PHONE ORGANIZER ---")
base = "Phone_Work"
for sub in ["Docs", "Media"]:
    os.makedirs(f"{base}/{sub}", exist_ok=True)

# Generate dummy work to organize
with open(f"{base}/report.txt", "w") as f: f.write("Mission successful.")
with open(f"{base}/photo_log.jpg", "w") as f: f.write("Dummy data")

for f in os.listdir(base):
    if f.endswith(".txt"): shutil.move(f"{base}/{f}", f"{base}/Docs/{f}")
    elif f.endswith(".jpg"): shutil.move(f"{base}/{f}", f"{base}/Media/{f}")
print("Status: Files sorted into 'Docs' and 'Media'.")

print("\n--- 📦 3. AUTO BACKUP ---")
with zipfile.ZipFile("Master_Backup.zip", "w") as z:
    for root, d, files in os.walk(base):
        for file in files: z.write(os.path.join(root, file))
print("Status: 'Master_Backup.zip' created successfully.")

print("\n--- 🔐 4. SECURITY & LOGIC ---")
# TRAP 1: Undefined Variable
print(f"Encryption Token: {master_encryption_key}")

# TRAP 2: Logic Error
logic_check = 100 / (1) # Auto-Healed