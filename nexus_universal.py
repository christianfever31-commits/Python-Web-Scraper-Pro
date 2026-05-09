import os
from google import genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

class UniversalNexus:
    def __init__(self):
        print("\n" + "🚀" * 15)
        print("  NEXUS UNIVERSAL BUILDER v3.0  ")
        print("🚀" * 15)
        self.project_name = input("Enter Project Name: ").strip().replace(" ", "_")
        if not os.path.exists(self.project_name): os.makedirs(self.project_name)
        
        # Start a chat session for 'memory'
        self.chat = client.chats.create(model="gemini-2.5-flash")
        self.current_code = ""

    def build_or_edit(self, prompt):
        # System instructions to ensure high-quality code
        instructions = (
            "You are a Senior Full-Stack Developer. Build a professional product. "
            "If it is a mobile app, use PWA standards and Tailwind. "
            "If it is a game, use HTML5 Canvas and modern JavaScript. "
            "If it is a website, ensure it is responsive. "
            "Return ONLY the updated raw HTML/CSS/JS code."
        )
        
        full_prompt = f"{instructions}\n\nUser Request: {prompt}\n\nCurrent Code:\n{self.current_code}"
        
        print(f"\n[Nexus] Processing request for {self.project_name}...")
        
        try:
            response = self.chat.send_message(full_prompt)
            # Clean the code block from the response
            new_code = response.text.strip().replace("```html", "").replace("```", "")
            self.current_code = new_code
            
            with open(f"{self.project_name}/index.html", "w") as f:
                f.write(new_code)
            
            print(f"✅ Build Updated! View at: http://localhost:8080")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    nexus = UniversalNexus()
    while True:
        user_input = input("\n[Chat with AI] What should I build or change? (type 'exit' to quit): ")
        if user_input.lower() == 'exit': break
        nexus.build_or_edit(user_input)

