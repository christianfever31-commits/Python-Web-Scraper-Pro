import time
import random

class HollywoodBot:
    def __init__(self):
        self.wallet = 0.0
        self.tax_vault = 0.0
        self.tax_rate = 0.20 # 20% Tax
        self.work_rate = 5.50 # $5.50 earned per "task"

    def perform_internet_work(self):
        print("🌐 Connecting to internet work-stream...")
        time.sleep(2) # Simulating work
        print("✅ Task Complete: Data verified.")
        self.process_payment(self.work_rate)

    def process_payment(self, amount):
        tax = amount * self.tax_rate
        net_income = amount - tax
        
        self.wallet += net_income
        self.tax_vault += tax
        
        print(f"💰 Earned: ${amount}")
        print(f"📉 Tax deducted: ${tax}")
        print(f"💵 Net to Wallet: ${net_income}")

    def check_finances(self):
        print("\n--- 🏦 HOLLYWOOD WALLET STATUS ---")
        print(f"Available Balance: ${self.wallet:.2f}")
        print(f"Tax Reserves: ${self.tax_vault:.2f}")

# Start the bot
bot = HollywoodBot()
for i in range(3): # Run 3 work cycles
    print(f"\n--- Cycle {i+1} ---")
    bot.perform_internet_work()

bot.check_finances()

