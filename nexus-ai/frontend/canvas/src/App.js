import React, { useState } from 'react';

function App() {
  const [prompt, setPrompt] = useState('');
  const [generating, setGenerating] = useState(false);
  const [result, setResult] = useState(null);
  const [logs, setLogs] = useState([]);

  const addLog = (msg, type = 'info') => setLogs(prev => [...prev, { msg, type, time: new Date().toLocaleTimeString() }]);

  const generate = async () => {
    if (!prompt.trim()) return addLog('Enter a prompt', 'error');
    setGenerating(true);
    addLog('Generating...', 'info');
    try {
      const res = await fetch('http://localhost:8000/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
      });
      const data = await res.json();
      if (data.success) {
        setResult(data);
        addLog(`Success: ${data.requirements.name}`, 'success');
      } else addLog(`Error: ${data.error}`, 'error');
    } catch(e) { addLog(`Connection error: ${e.message}`, 'error'); }
    setGenerating(false);
  };

  return (
    <div style={{ background: '#0a0a0a', minHeight: '100vh', color: 'white', padding: 20, fontFamily: 'system-ui' }}>
      <div style={{ maxWidth: 800, margin: '0 auto' }}>
        <h1 style={{ background: 'linear-gradient(135deg,#667eea,#764ba2)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>🚀 Nexus AI on Termux</h1>
        <textarea rows={4} style={{ width: '100%', padding: 16, background: '#1a1a1a', border: '1px solid #333', borderRadius: 12, color: 'white', marginBottom: 16 }} placeholder='Example: "Build me a todo list app"' value={prompt} onChange={e => setPrompt(e.target.value)} />
        <button onClick={generate} disabled={generating} style={{ width: '100%', padding: 14, background: 'linear-gradient(135deg,#667eea,#764ba2)', border: 'none', borderRadius: 12, color: 'white', fontWeight: 'bold', cursor: generating ? 'not-allowed' : 'pointer', opacity: generating ? 0.5 : 1 }}>{generating ? 'Generating...' : 'Generate App'}</button>
        <div style={{ marginTop: 24 }}><h3>Logs</h3><div style={{ background: '#111', borderRadius: 12, padding: 16, maxHeight: 300, overflow: 'auto', fontSize: 12 }}>{logs.map((log,i) => <div key={i} style={{ color: log.type==='error'?'#ef4444':log.type==='success'?'#10b981':'#888' }}>[{log.time}] {log.msg}</div>)}</div></div>
        {result && <div style={{ marginTop: 24, background: '#111', borderRadius: 12, padding: 16 }}><p><strong>App:</strong> {result.requirements.name}</p><p><strong>File:</strong> {result.deployment_urls.preview}</p><p style={{ color: '#10b981' }}>Check ~/tmp/ folder</p></div>}
      </div>
    </div>
  );
}
export default App;
