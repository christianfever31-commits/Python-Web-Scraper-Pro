import { OpenRouter } from "@openrouter/sdk";
import fs from "fs";

const client = new OpenRouter({
  apiKey: "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"
});

async function makeImage(prompt) {
  console.log(`🎨 Faceless AI: Dreaming up "${prompt}"...`);
  
  try {
    const result = await client.chat.send({
      chatRequest: {
        // Riverflow V2 is the top choice for 2026 image generation
        model: "sourceful/riverflow-v2-pro",
        messages: [{ role: "user", content: prompt }]
      }
    });

    // In 2026, image models return a URL or Base64 data
    const imageUrl = result.choices[0].message.content; 
    console.log("\n✅ Image Generated!");
    console.log("🔗 View it here:", imageUrl);

    // Optional: Code to download the image automatically can go here
  } catch (err) {
    console.error("\n❌ Generation Failed:", err.message);
  }
}

makeImage("A futuristic cyberpunk version of Owerri city at night, 8k resolution");

