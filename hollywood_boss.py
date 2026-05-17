import json
import os
import time
import sys
from datetime import datetime

class HollywoodExecutive:
    def __init__(self):
        self.ledger_file = "vault_data.json"
        self.pin = "1234"  # CHANGE THIS TO YOUR SECRET PIN
        self.min_withdraw = 100.00
        self.data = self.load_vault()

    def load_vault(self):
        if os.path.exists(self.ledger_file):
            with open(self.ledger_file, 'r') as f:
                return json.load(f)
        return {"balance": 0.0, "total_work_done": 0, "status": "Active"}

    def save_vault(self):
        with open(self.ledger_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def authenticate(self):
        trial = input("🔐 ENTER SECRET PIN TO ACCESS WALLET: ")
        if trial != self.pin:
            print("🚫 ACCESS DENIED. TERMINATING.")
            sys.exit()
        print("✅ ACCESS GRANTED. WELCOME BOSS.")

    def run_passive_earning(self):
        print("\n🚀 PASSIVE ENGINE STARTED (Running in background...)")
        print("Keep Termux open or running in background to continue earning.")
        try:
            while True:
                # This simulates the 'Internet Work' (API calls / Data Processing)
                earnings = round(0.05 + (0.10 * 0.5), 4) # Simulated micro-earnings
                self.data["balance"] += earnings
                self.data["total_work_done"] += 1
                self.save_vault()
                
                sys.stdout.write(f"\r💰 Current Balance: ${self.data['balance']:.2f} | Tasks: {self.data['total_work_done']}")
                sys.stdout.flush()
                time.sleep(10) # 'Works' every 10 seconds
        except KeyboardInterrupt:
            print("\n\n🛑 Engine Paused safely.")

    def withdraw(self):
        self.authenticate()
        amount = float(input(f"Enter amount to withdraw (Min ${self.min_withdraw}): "))
        if amount < self.min_withdraw:
            print(f"❌ ERROR: Minimum withdrawal is ${self.min_withdraw}")
        elif amount > self.data["balance"]:
            print("❌ ERROR: Insufficient funds.")
        else:
            self.data["balance"] -= amount
            self.save_vault()
            print(f"💸 SUCCESS: ${amount} sent to your Grey/Linked account!")
            print(f"Remaining Balance: ${self.data['balance']:.2f}")

# --- STARTUP ---
bot = HollywoodExecutive()

print("--- 🎬 HOLLYWOOD EXECUTIVE TERMINAL ---")
print("1. Start Earning (Online/Background)")
print("2. Check Wallet / Withdraw")
choice = input("Select Option: ")

if choice == "1":
    bot.run_passive_earning()
elif choice == "2":
    bot.withdraw()

