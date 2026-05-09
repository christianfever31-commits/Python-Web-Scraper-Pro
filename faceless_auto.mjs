import fetch from "node-fetch";
import { InferenceClient } from "@huggingface/inference";
import { client } from "@gradio/client";
import fs from "fs";
import path from "path";

// ✅ HF Token
const HF_TOKEN = process.env.HF_TOKEN || "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";

if (!HF_TOKEN) {
    console.error("❌ Missing HF_TOKEN.");
    console.log("💡 Run: export HF_TOKEN=your_token_here");
    process.exit(1);
}

const inference = new InferenceClient(HF_TOKEN);

// ✅ Auto-detect Android or PC
const isAndroid = fs.existsSync("/sdcard");
const PICTURES_DIR = isAndroid ? "/sdcard/Pictures" : ".";
const IMAGE_PATH = path.join(PICTURES_DIR, "faceless_input.jpg");
const OUTPUT_PATH = path.join(PICTURES_DIR, "FacelessAI_Final.mp4");

// ✅ Ensure Pictures folder exists
if (!fs.existsSync(PICTURES_DIR)) {
    fs.mkdirSync(PICTURES_DIR, { recursive: true });
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function generateImage(prompt, retries = 3) {
    for (let i = 0; i < retries; i++) {
        try {
            console.log(`\n🎨 Generating image... (attempt ${i + 1}/${retries})`);

            const imageBlob = await inference.textToImage({
                model: "black-forest-labs/FLUX.1-schnell",
                inputs: prompt,
            });

            if (!imageBlob) throw new Error("Empty image response.");

            const imgBuffer = Buffer.from(await imageBlob.arrayBuffer());
            if (imgBuffer.length < 1000) throw new Error("Image too small.");

            fs.writeFileSync(IMAGE_PATH, imgBuffer);
            console.log(`✅ Image saved to: ${IMAGE_PATH}`);
            return imgBuffer;

        } catch (err) {
            console.error(`❌ Image attempt ${i + 1} failed: ${err.message}`);
            if (i < retries - 1) {
                console.log("⏳ Retrying in 10 seconds...");
                await sleep(10000);
            } else {
                throw new Error("Image generation failed after all retries.");
            }
        }
    }
}

async function generateVideo(imgBuffer, retries = 3) {
    for (let i = 0; i < retries; i++) {
        try {
            console.log(`\n🎬 Generating video... (attempt ${i + 1}/${retries})`);

            const base64Image = imgBuffer.toString("base64");
            const dataURL = `data:image/jpeg;base64,${base64Image}`;

            // ✅ Try multiple working SVD spaces
            const spaces = [
                "multimodalart/stable-video-diffusion",
                "fffiloni/stable-video-diffusion",
                "wangfuyun/AnimateLCM-SVD",
            ];

            let result = null;
            let connectedApp = null;

            for (const space of spaces) {
                try {
                    console.log(`🔗 Trying space: ${space}`);
                    const app = await client(space, {
                        hf_token: HF_TOKEN,
                    });

                    // ✅ Use fn_index 0 (first function) instead of named endpoint
                    result = await app.predict(0, [
                        dataURL,  // Image
                        25,       // Frames
                        6,        // FPS  
                        127,      // Motion bucket
                        0,        // Noise aug strength
                        true,     // Decode chunk size
                    ]);

                    connectedApp = space;
                    console.log(`✅ Connected and got result from: ${space}`);
                    break;

                } catch (spaceErr) {
                    console.log(`⚠️ Space ${space} failed: ${spaceErr.message}`);
                    await sleep(3000);
                }
            }

            if (!result) {
                throw new Error("All SVD spaces failed. Servers may be busy.");
            }

            // ✅ Extract video URL safely
            const videoInfo = result?.data?.[0];
            const videoUrl = videoInfo?.url || videoInfo?.path || videoInfo;

            if (!videoUrl || typeof videoUrl !== "string") {
                console.log("🔍 Raw result data:", JSON.stringify(result?.data));
                throw new Error("No valid video URL in response.");
            }

            console.log(`🔗 Video URL: ${videoUrl}`);

            // ✅ Download video
            console.log("📥 Downloading video...");
            const videoResponse = await fetch(videoUrl);
            if (!videoResponse.ok) {
                throw new Error(`Download failed. HTTP: ${videoResponse.status}`);
            }

            const videoData = await videoResponse.arrayBuffer();
            const videoBuffer = Buffer.from(videoData);

            if (videoBuffer.length < 1000) {
                throw new Error("Downloaded video too small. Likely corrupt.");
            }

            fs.writeFileSync(OUTPUT_PATH, videoBuffer);
            console.log(`✅ Video saved: ${OUTPUT_PATH}`);
            return true;

        } catch (err) {
            console.error(`❌ Video attempt ${i + 1} failed: ${err.message}`);

            if (err.message.includes("busy") || err.message.includes("Queue")) {
                console.log("⏳ Server busy. Waiting 60 seconds...");
                await sleep(60000);
            } else if (i < retries - 1) {
                console.log("⏳ Retrying in 15 seconds...");
                await sleep(15000);
            } else {
                throw new Error("Video generation failed after all retries.");
            }
        }
    }
}

async function runFacelessAI(prompt) {
    console.log("\n╔══════════════════════════════════════╗");
    console.log("║       🤖 FacelessAI Starting...      ║");
    console.log("╚══════════════════════════════════════╝");
    console.log(`📝 Prompt: "${prompt}"`);
    console.log(`📱 Platform: ${isAndroid ? "Android" : "PC/Linux"}`);
    console.log(`📁 Output: ${OUTPUT_PATH}`);

    try {
        // ── STEP 1: Generate Image ──
        const imgBuffer = await generateImage(prompt);

        // ── STEP 2: Generate Video ──
        await generateVideo(imgBuffer);

        console.log("\n╔══════════════════════════════════════╗");
        console.log("║   🔥 SUCCESS! Video Generated! 🔥    ║");
        console.log("╚══════════════════════════════════════╝");
        console.log(`📁 Saved: ${OUTPUT_PATH}`);
        console.log(isAndroid
            ? "📱 Open Gallery app to view your video!"
            : "💻 Open FacelessAI_Final.mp4 in your folder.");

    } catch (err) {
        console.error("\n╔══════════════════════════════════════╗");
        console.error("║         ❌ PROCESS FAILED             ║");
        console.error("╚══════════════════════════════════════╝");
        console.error(`Error: ${err.message}`);

        if (err.message.includes("401") || err.message.includes("unauthorized")) {
            console.log("\n💡 Fix: HF token invalid or expired.");
            console.log("   → https://huggingface.co/settings/tokens");
            console.log("   → export HF_TOKEN=your_new_token");
        } else if (err.message.includes("EACCES") || err.message.includes("permission")) {
            console.log("\n💡 Fix: Run: termux-setup-storage");
        } else if (err.message.includes("busy") || err.message.includes("spaces")) {
            console.log("\n💡 Fix: All servers busy. Wait 5 mins and retry.");
        } else {
            console.log("\n💡 Fix: Check internet and try again.");
        }

        process.exit(1);
    }
}

// ══════════════════════════════════════
// 🚀 START
// ══════════════════════════════════════
runFacelessAI("A gritty, cinematic 8k shot of a faceless hacker in a neon Owerri street");
