import { OpenRouter } from "@openrouter/sdk";
import fs from "fs";

const client = new OpenRouter({
  apiKey: "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"
});

async function analyzeImage(imagePath) {
  console.log(`📸 Faceless AI: Processing ${imagePath}...`);
  
  try {
    // Read the local image file from your phone
    const imageData = fs.readFileSync(imagePath).toString("base64");

    const result = await client.chat.send({
      chatRequest: {
        model: "google/gemma-4-26b-a4b-it:free",
        messages: [
          {
            role: "user",
            content: [
              { type: "text", text: "Describe this image in detail for the Faceless AI project logs." },
              {
                type: "image_url",
                image_url: {
                  url: `data:image/jpeg;base64,${imageData}`
                }
              }
            ]
          }
        ]
      }
    });

    console.log("\n👁️ VISION LOGS:");
    console.log(result.choices[0].message.content);

  } catch (err) {
    console.error("\n❌ VISION ERROR:", err.message);
  }
}

// Replace 'test.jpg' with the name of an actual photo in your folder
analyzeImage("test.jpg");

