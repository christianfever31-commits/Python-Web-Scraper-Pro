import { GoogleGenAI } from "@google/genai";

// Initialize the client with an explicit configuration object
const client = new GoogleGenAI({
  apiKey: process.env.GEMINI_API_KEY
});

async function start() {
  console.log("🚀 Faceless AI: Sending heartbeat...");
  try {
    // 2.0-flash is the most stable free endpoint right now
    const response = await client.models.generateContent({
      model: "gemini-2.0-flash",
      contents: "System check: Faceless AI engine is live. Awaiting command.",
    });

    console.log("\n✅ ENGINE RESPONSE:\n", response.text);
  } catch (error) {
    // This will tell us EXACTLY why it failed
    console.error("\n❌ ERROR DETAILS:");
    console.error("Message:", error.message);
    if (error.message.includes("400")) console.log("💡 Tip: The key has a typo or extra space.");
    if (error.message.includes("404")) console.log("💡 Tip: Model name changed. Use 'gemini-2.0-flash'.");
  }
}

start();

