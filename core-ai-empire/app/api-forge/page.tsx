"use client";
import React, { useState } from 'react';

export default function APIForge() {
  const [apiKey, setApiKey] = useState("");

  const generateKey = () => {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = 'nc_live_';
    for (let i = 0; i < 32; i++) {
      result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    setApiKey(result);
  };

  return (
    <main className="min-h-screen bg-[#050505] text-white p-6 font-sans">
      <div className="max-w-4xl mx-auto">
        <a href="/" className="text-purple-400 text-xs font-bold uppercase tracking-widest hover:underline mb-8 block">
          ← Back to NeuraCore
        </a>
        
        <h1 className="text-5xl font-black mb-8 bg-gradient-to-r from-purple-400 to-blue-500 bg-clip-text text-transparent italic uppercase tracking-tighter">
          API FORGE
        </h1>

        <div className="p-10 rounded-[40px] border border-white/5 bg-white/[0.02] backdrop-blur-3xl shadow-2xl relative overflow-hidden">
          <div className="absolute top-0 right-0 p-4 opacity-10">
            <svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1"><path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3m-3-3l-2.5-2.5" /></svg>
          </div>

          <div className="mb-10 text-center">
            <div className="w-20 h-20 bg-purple-500/20 rounded-3xl flex items-center justify-center mx-auto mb-6 border border-purple-500/30">
              <span className="text-4xl">🔑</span>
            </div>
            <h2 className="text-2xl font-bold">Forge Your Secret Key</h2>
            <p className="text-gray-500 mt-2 text-sm">Deploy this key to authorize your agents with NeuraCore OS.</p>
          </div>

          {apiKey && (
            <div className="bg-black/80 border border-purple-500/30 p-6 rounded-2xl mb-8 animate-in zoom-in duration-300">
              <p className="text-[10px] text-purple-400 uppercase font-black mb-2 tracking-[0.2em]">Secret Key Generated</p>
              <code className="text-cyan-400 break-all font-mono text-lg select-all cursor-pointer">{apiKey}</code>
            </div>
          )}

          <button 
            onClick={generateKey}
            className="w-full py-5 bg-purple-600 text-white font-black rounded-2xl hover:bg-purple-500 transition-all shadow-[0_0_40px_rgba(168,85,247,0.2)] uppercase tracking-tighter"
          >
            {apiKey ? "FORGE NEW KEY" : "INITIALIZE KEY GENERATION"}
          </button>
        </div>
      </div>
    </main>
  );
}

