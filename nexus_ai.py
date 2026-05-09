import os
from google import genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

class NexusAI:
    def __init__(self):
        print("\n" + "="*45)
        print("      NEXUS AI: ARCHITECT v2.5 (2026)      ")
        print("="*45)
        self.p_name = input("App Name: ").strip().replace(" ", "_")
        if not os.path.exists(self.p_name):
            os.makedirs(self.p_name)

    def generate(self, user_goal):
        print(f"\n[Nexus] Brain: Gemini 2.5 Flash")
        print(f"[Nexus] Status: Architecting '{self.p_name}'...")
        
        sys_prompt = (
            f"Build a professional, mobile-responsive web app for: {user_goal}. "
            "Use Tailwind CSS for a modern aesthetic. Return ONLY raw HTML code."
        )

        try:
            # UPDATED to Gemini 2.5 Flash for 2026 compatibility
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=sys_prompt
            )
            
            # Clean and save
            clean_html = response.text.strip().replace("```html", "").replace("```", "")
            file_path = f"{self.p_name}/index.html"
            
            with open(file_path, "w") as f:
                f.write(clean_html)
            
            print(f"\n✅ SUCCESS! Build Complete.")
            print(f"👉 Run: cd {self.p_name} && python -m http.server 8080")
            
        except Exception as e:
            print(f"\n❌ BUILD FAILED: {e}")

if __name__ == "__main__":
    nexus = NexusAI()
    idea = input("\nWhat should Nexus build today? ")
    nexus.generate(idea)

