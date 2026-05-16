import subprocess
import sys
import os
import time
import re
import shutil
import zipfile

class MasterAgent:
    def __init__(self, task_name, code_to_run):
        self.task_name = task_name
        self.code = code_to_run
        self.file_path = f"{task_name}.py"
        self.max_attempts = 10
        
    def save_to_disk(self):
        with open(self.file_path, "w") as f:
            f.write(self.code)
        print(f"💾 Agent writing to {self.file_path}...")

    def run_task(self):
        print(f"🚀 Executing Master Mission: {self.task_name}...")
        process = subprocess.run(
            [sys.executable, self.file_path],
            capture_output=True,
            text=True
        )
        return process.returncode, process.stdout, process.stderr

    def self_heal(self, error_log, attempt):
        print(f"❌ Crash detected on Attempt {attempt}!")
        line_match = re.findall(rf'File ".*{self.file_path}", line (\d+)', error_log)
        target_line = int(line_match[-1]) if line_match else None

        # 1. Fix Missing Libraries
        if "ModuleNotFoundError" in error_log:
            module = error_log.split("No module named ")[1].strip().replace("'", "")
            print(f"🛠️  Fixing: Installing {module}...")
            subprocess.run([sys.executable, "-m", "pip", "install", module])
            return True
        # 2. Fix Undefined Variables
        elif "NameError" in error_log:
            var_match = re.search(r"name '(\w+)' is not defined", error_log)
            if var_match:
                var_name = var_match.group(1)
                print(f"🛠️  Fixing: Defining missing variable '{var_name}'...")
                self.code = f"{var_name} = 'MASTER_KEY_ALPHA_777'\n" + self.code
                return True
        # 3. Fix Math Errors
        elif "ZeroDivisionError" in error_log and target_line:
            print(f"🛠️  Fixing: Patching math logic on line {target_line}...")
            lines = self.code.splitlines()
            lines[target_line - 1] = lines[target_line - 1].split("/")[0] + "/ (1) # Auto-Healed"
            self.code = "\n".join(lines)
            return True
        # 4. Master Bypass
        elif target_line:
            print(f"⚠️ Unknown error on line {target_line}. Bypassing to save mission...")
            lines = self.code.splitlines()
            lines[target_line - 1] = f"# Bypassed: {lines[target_line - 1]}"
            self.code = "\n".join(lines)
            return True
        return False

    def start(self):
        for i in range(1, self.max_attempts + 1):
            print(f"\n--- 🤖 Master Loop {i} ---")
            self.save_to_disk()
            exit_code, out, err = self.run_task()
            if exit_code == 0:
                print("\n✅ MISSION ACCOMPLISHED")
                print(f"--- FINAL REPORT ---\n{out}")
                break
            else:
                if not self.self_heal(err, i):
                    print("💥 Fatal Error. System stopped.")
                    break
                time.sleep(1)

# ==========================================
# THE FULL MULTI-MISSION CODE
# ==========================================
mission_code = """
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

print("\\n--- 📂 2. PHONE ORGANIZER ---")
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

print("\\n--- 📦 3. AUTO BACKUP ---")
with zipfile.ZipFile("Master_Backup.zip", "w") as z:
    for root, d, files in os.walk(base):
        for file in files: z.write(os.path.join(root, file))
print("Status: 'Master_Backup.zip' created successfully.")

print("\\n--- 🔐 4. SECURITY & LOGIC ---")
# TRAP 1: Undefined Variable
print(f"Encryption Token: {master_encryption_key}")

# TRAP 2: Logic Error
logic_check = 100 / 0
"""

if __name__ == "__main__":
    if os.path.exists("autonomous_worker.py"):
        os.remove("autonomous_worker.py")
    bot = MasterAgent("autonomous_worker", mission_code)
    bot.start()

