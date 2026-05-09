import os
from google import genai

# Setup
client = genai.Client(api_key=os.environ.get("AIzaSyBiqYPJa-OFKc2DNJqk7PQ9xEMIj7-eGH0"))

class NexusPro:
    def __init__(self):
        print("💎 NEXUS PRO: MULTI-PLATFORM ARCHITECT 💎")
        self.project = input("Project Name: ").strip().replace(" ", "_")
        if not os.path.exists(self.project): os.makedirs(self.project)
        self.chat = client.chats.create(model="gemini-2.5-flash")
        self.current_state = ""

    def architect(self, prompt):
        # We tell the AI to be a multi-platform expert
        context = (
            "You are a Senior Software Architect. "
            "For WEBSITES: Use Tailwind CSS, Framer Motion, and modern UI. "
            "For MOBILE APPS: Build as a PWA (Progressive Web App) with manifest.json. "
            "For GAMES: Use HTML5 Canvas or Phaser.js for 60fps performance. "
            "Return ONLY the code. Do not explain unless asked."
        )
        
        full_prompt = f"{context}\n\nProject History:\n{self.current_state}\n\nUser Request: {prompt}"
        print(f"🛠️ Working on {self.project}...")

        try:
            response = self.chat.send_message(full_prompt)
            code = response.text.strip().replace("```html", "").replace("```", "")
            self.current_state = code # Update memory
            
            with open(f"{self.project}/index.html", "w") as f:
                f.write(code)
            print("✅ Build Updated.")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    builder = NexusPro()
    while True:
        msg = input("\n[Chat] Describe your app/game or request an edit: ")
        if msg.lower() in ['exit', 'quit']: break
        builder.architect(msg)

