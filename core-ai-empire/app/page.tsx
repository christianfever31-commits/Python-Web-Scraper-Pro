import React from 'react';

export default function Home() {
  return (
    <div className="min-h-screen bg-[#020203] text-slate-200 font-sans selection:bg-cyan-500/30">
      {/* High-End Background Gradient */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-[10%] -left-[10%] w-[70%] h-[70%] bg-cyan-900/20 rounded-full blur-[120px] animate-pulse" />
        <div className="absolute -bottom-[10%] -right-[10%] w-[70%] h-[70%] bg-purple-900/10 rounded-full blur-[120px]" />
      </div>

      {/* Professional Top Bar */}
      <nav className="sticky top-0 z-50 flex justify-between items-center px-6 py-4 border-b border-white/5 backdrop-blur-2xl bg-black/40">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 bg-gradient-to-tr from-cyan-500 to-blue-600 rounded-xl shadow-[0_0_20px_rgba(6,182,212,0.3)] flex items-center justify-center">
            <span className="text-black font-black text-xs">N</span>
          </div>
          <div>
            <h1 className="text-sm font-bold tracking-tight text-white uppercase">NeuraCore <span className="text-cyan-400">Control</span></h1>
            <p className="text-[10px] text-slate-500 font-mono">v1.0.4-stable</p>
          </div>
        </div>
        
        <div className="flex items-center gap-4">
          <div className="hidden md:flex items-center gap-2 px-3 py-1 rounded-md bg-white/5 border border-white/10">
            <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Mainnet</span>
          </div>
          <button className="p-2 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 transition-colors">
            <span className="text-lg">🔔</span>
          </button>
        </div>
      </nav>

      {/* Dashboard Grid */}
      <main className="relative z-10 container mx-auto px-6 py-12">
        <header className="mb-12">
          <h2 className="text-3xl font-black text-white tracking-tight mb-2 uppercase">Systems Overview</h2>
          <p className="text-slate-400 text-sm">Welcome back, Developer. Your neural modules are online.</p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          
          {/* Creation Suite Card */}
          <a href="/creation-suite" className="group relative overflow-hidden p-8 rounded-[32px] bg-white/[0.03] border border-white/10 hover:border-cyan-500/50 hover:bg-white/[0.05] transition-all duration-500">
            <div className="absolute top-0 right-0 w-32 h-32 bg-cyan-500/10 blur-3xl group-hover:bg-cyan-500/20 transition-all" />
            <div className="w-12 h-12 bg-cyan-500/20 rounded-2xl flex items-center justify-center mb-6 border border-cyan-500/30 group-hover:scale-110 transition-transform">
              <span className="text-2xl">🎨</span>
            </div>
            <h3 className="text-xl font-bold text-white mb-2">Creation Suite</h3>
            <p className="text-slate-400 text-xs leading-relaxed mb-6">Deploy high-fidelity multimodal generative engines for vision and art.</p>
            <div className="flex items-center justify-between">
              <span className="text-[10px] font-bold text-cyan-400 uppercase tracking-widest">Launch Tool →</span>
              <span className="text-[10px] text-slate-600 font-mono">LATENCY: 24ms</span>
            </div>
          </a>

          {/* API Forge Card */}
          <a href="/api-forge" className="group relative overflow-hidden p-8 rounded-[32px] bg-white/[0.03] border border-white/10 hover:border-purple-500/50 hover:bg-white/[0.05] transition-all duration-500">
            <div className="absolute top-0 right-0 w-32 h-32 bg-purple-500/10 blur-3xl group-hover:bg-purple-500/20 transition-all" />
            <div className="w-12 h-12 bg-purple-500/20 rounded-2xl flex items-center justify-center mb-6 border border-purple-500/30 group-hover:scale-110 transition-transform">
              <span className="text-2xl">⚡</span>
            </div>
            <h3 className="text-xl font-bold text-white mb-2">API Forge</h3>
            <p className="text-slate-400 text-xs leading-relaxed mb-6">Generate and manage secure, monetizable neural keys for production.</p>
            <div className="flex items-center justify-between">
              <span className="text-[10px] font-bold text-purple-400 uppercase tracking-widest">Forge Keys →</span>
              <span className="text-[10px] text-slate-600 font-mono">ACTIVE: 12</span>
            </div>
          </a>

          {/* God Mode Card (Locked) */}
          <div className="relative overflow-hidden p-8 rounded-[32px] bg-black/40 border border-white/5 opacity-40 grayscale">
            <div className="w-12 h-12 bg-white/5 rounded-2xl flex items-center justify-center mb-6 border border-white/10">
              <span className="text-2xl">🛡️</span>
            </div>
            <h3 className="text-xl font-bold text-white mb-2">God Mode</h3>
            <p className="text-slate-500 text-xs leading-relaxed mb-6">Centralized governance and global traffic analytics dashboard.</p>
            <div className="px-3 py-1 rounded-full bg-white/5 border border-white/10 inline-block">
              <span className="text-[9px] font-black text-slate-400 uppercase tracking-widest italic">Encrypted</span>
            </div>
          </div>

        </div>

        {/* Global Analytics Preview */}
        <section className="mt-12 p-8 rounded-[40px] bg-white/[0.02] border border-white/5">
          <div className="flex justify-between items-end mb-8">
            <div>
              <p className="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em] mb-1">Global Network Traffic</p>
              <h4 className="text-2xl font-bold text-white tracking-tighter">Real-time Analytics</h4>
            </div>
            <div className="text-right">
              <span className="text-3xl font-black text-cyan-400 tracking-tighter">842.1k</span>
              <p className="text-[10px] text-slate-500 uppercase">Requests / hr</p>
            </div>
          </div>
          <div className="h-2 w-full bg-white/5 rounded-full overflow-hidden">
             <div className="h-full bg-gradient-to-r from-cyan-500 to-purple-600 w-[65%] rounded-full shadow-[0_0_15px_rgba(6,182,212,0.5)]" />
          </div>
        </section>
      </main>
    </div>
  );
}

