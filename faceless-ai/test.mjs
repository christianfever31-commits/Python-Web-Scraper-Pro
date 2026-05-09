import { GoogleGenAI } from "@google/genai";

// We are putting the key directly in the code to stop the "Expired" errors
const ai = new GoogleGenAI({
  apiKey: "AIzaSyBlVcN1ySc-Ep9GPCp4URa8R4C1-5Zhcxo" 
});

async function run() {
  console.log("📡 Faceless AI: Forcing connection...");
  try {
    const response = await ai.models.generateContent({
      model: "gemini-2.0-flash",
      contents: "System check: Are we finally connected?",
    });

    console.log("\n✅ SUCCESS! Engine Says:", response.text);
    console.log("\n🚀 Now we can start the real building!");
  } catch (err) {
    console.log("\n❌ Status:", err.message);
    if (err.message.includes("400")) {
      console.log("💡 Tip: Go to AI Studio and ensure 'Generative Language API' is ENABLED for this project.");
    }
  }
}

run();

