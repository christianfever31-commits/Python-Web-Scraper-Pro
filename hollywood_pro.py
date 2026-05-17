import json
import os
import time
from datetime import datetime

class HollywoodPro:
    def __init__(self):
        self.ledger_file = "hollywood_ledger.json"
        self.goal = 100.00
        self.tax_rate = 0.20  # 20% Tax Reserve
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.ledger_file):
            with open(self.ledger_file, 'r') as f:
                return json.load(f)
        return {
            "wallet_usd": 0.0,
            "tax_reserve_usd": 0.0,
            "total_earned_gross": 0.0,
            "tasks_completed": 0,
            "history": []
        }

    def save_data(self):
        with open(self.ledger_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def log_work(self, task_name, amount):
        tax = amount * self.tax_rate
        net = amount - tax
        
        # Update finances
        self.data["wallet_usd"] += net
        self.data["tax_reserve_usd"] += tax
        self.data["total_earned_gross"] += amount
        self.data["tasks_completed"] += 1
        
        # Add to history
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "task": task_name,
            "earned": f"${amount:.2f}",
            "net": f"${net:.2f}"
        }
        self.data["history"].append(entry)
        self.save_data()

        print(f"✅ TASK COMPLETED: {task_name}")
        print(f"💵 Added to Wallet: ${net:.2f}")
        print(f"🏦 Reserved for Tax: ${tax:.2f}")

    def show_dashboard(self):
        percent_to_goal = (self.data["wallet_usd"] / self.goal) * 100
        print("\n" + "="*30)
        print("🎬 HOLLYWOOD WORKER DASHBOARD")
        print("="*30)
        print(f"💰 Spendable (Net):   ${self.data['wallet_usd']:.2f}")
        print(f"🏛️  Tax Pot:           ${self.data['tax_reserve_usd']:.2f}")
        print(f"📊 Tasks Done:        {self.data['tasks_completed']}")
        print(f"🎯 Goal ($100):       {percent_to_goal:.1f}% Complete")
        print("="*30)
        
        if percent_to_goal >= 100:
            print("🚀 GOAL REACHED! Time to withdraw to Grey!")
        else:
            remaining = self.goal - self.data["wallet_usd"]
            print(f"🔥 Need ${remaining:.2f} more for the payout.")

# --- EXECUTION ---
bot = HollywoodPro()

# Simulate a fresh work cycle
print("🌐 Bot is 'twerking' the internet work-stream...")
time.sleep(2)

# You can change these numbers based on what you actually earn
bot.log_work("Ad-Revenue Optimization", 12.50)
bot.log_work("Data Scraping Task", 8.00)

# Show the results
bot.show_dashboard()

