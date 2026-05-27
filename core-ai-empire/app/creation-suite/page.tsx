"use client";
import React, { useState } from 'react';

export default function CreationSuite() {
  const [prompt, setPrompt] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const generate = () => {
    if (!prompt) return;
    setLoading(true);
    // Pollinations AI endpoint
    const url = `https://image.pollinations.ai/prompt/${encodeURIComponent(prompt)}?width=1024&height=1024&nologo=true&seed=${Math.floor(Math.random() * 1000)}`;
    setImageUrl(url);
    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-[#050505] text-white p-6 font-sans">
      <div className="max-w-4xl mx-auto">
        <a href="/" className="text-cyan-400 text-xs font-bold uppercase tracking-widest hover:underline mb-8 block">
          ← Back to NeuralCore
        </a>
        
        <h1 className="text-5xl font-black mb-8 bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text text-transparent italic">
          CREATION SUITE
        </h1>
        
        <div className="p-8 rounded-[30px] border border-white/10 bg-white/5 backdrop-blur-xl mb-10 shadow-2xl">
          <p className="text-xs text-gray-400 mb-3 uppercase font-bold tracking-widest">Input Neural Prompt</p>
          <input 
            type="text" 
            placeholder="A futuristic cyber-city in Nigeria, neon lights, 8k..." 
            className="w-full bg-black/50 border border-white/10 p-5 rounded-2xl mb-6 focus:border-cyan-500 outline-none transition-all text-white font-medium"
            onChange={(e) => setPrompt(e.target.value)}
          />
          <button 
            onClick={generate}
            className="w-full py-5 bg-gradient-to-r from-cyan-500 to-blue-600 text-black font-black rounded-2xl hover:brightness-110 transition-all shadow-[0_0_30px_rgba(6,182,212,0.3)] uppercase tracking-tighter"
          >
            {loading ? "PROCESSING..." : "GENERATE ARTIFICIAL VISION"}
          </button>
        </div>

        {imageUrl && (
          <div className="rounded-[40px] overflow-hidden border border-white/10 shadow-2xl bg-white/5 p-2 animate-in fade-in zoom-in duration-700">
             <img 
              src={imageUrl} 
              alt="AI Generation" 
              className="w-full h-auto rounded-[35px]"
              onLoad={() => setLoading(false)}
            />
          </div>
        )}
      </div>
    </main>
  );
}

