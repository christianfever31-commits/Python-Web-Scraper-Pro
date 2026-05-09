# Create backend folder
mkdir -p backend/orchestrator

# Create the main file
cat > backend/orchestrator/nexus_termux.py << 'EOF'
"""
NEXUS AI - TERMUX OPTIMIZED VERSION
Runs completely on Android phone - No external APIs needed!
"""

import asyncio
import json
import os
import tempfile
import subprocess
from datetime import datetime
from typing import Dict, Any
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import uvicorn
import threading
import webbrowser

# Initialize FastAPI
app = FastAPI(title="Nexus AI - Termux Edition")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str
    platform: str = "auto"

# HTML Templates for different app types
def generate_complete_web_app(app_name: str, features: list, color_scheme: str = "purple") -> str:
    """Generate a complete, beautiful web app"""
    
    colors = {
        "purple": {"primary": "#667eea", "secondary": "#764ba2"},
        "blue": {"primary": "#3b82f6", "secondary": "#1e40af"},
        "green": {"primary": "#10b981", "secondary": "#047857"},
        "orange": {"primary": "#f59e0b", "secondary": "#ea580c"}
    }
    
    c = colors.get(color_scheme, colors["purple"])
    
    features_html = "\n".join([f'''
                <div class="feature-card" onclick="alert('{f} feature coming soon!')">
                    <div class="feature-icon">{chr(127919+i)}</div>
                    <h3>{f}</h3>
                    <p>Click to explore this feature</p>
                </div>
    ''' for i, f in enumerate(features[:6])])
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>{app_name} - Mobile App</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: linear-gradient(135deg, {c["primary"]} 0%, {c["secondary"]} 100%);
            min-height: 100vh;
            color: #333;
            padding-bottom: 70px;
        }}
        
        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        /* Header */
        .header {{
            text-align: center;
            padding: 40px 20px;
            color: white;
        }}
        
        .logo {{
            font-size: 64px;
            margin-bottom: 16px;
            animation: bounce 2s infinite;
        }}
        
        @keyframes bounce {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-10px); }}
        }}
        
        .header h1 {{
            font-size: 32px;
            margin-bottom: 8px;
        }}
        
        .header p {{
            opacity: 0.9;
            font-size: 16px;
        }}
        
        /* Welcome Card */
        .welcome-card {{
            background: white;
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }}
        
        .user-greeting {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }}
        
        .avatar {{
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, {c["primary"]}, {c["secondary"]});
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 20px;
        }}
        
        /* Stats Grid */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-bottom: 20px;
        }}
        
        .stat-card {{
            background: #f7f7f7;
            padding: 16px;
            border-radius: 12px;
            text-align: center;
        }}
        
        .stat-number {{
            font-size: 24px;
            font-weight: bold;
            color: {c["primary"]};
        }}
        
        .stat-label {{
            font-size: 12px;
            color: #666;
            margin-top: 4px;
        }}
        
        /* Features Grid */
        .features-section {{
            margin-top: 20px;
        }}
        
        .section-title {{
            color: white;
            margin-bottom: 16px;
            font-size: 20px;
        }}
        
        .features-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 16px;
        }}
        
        .feature-card {{
            background: white;
            border-radius: 16px;
            padding: 20px;
            text-align: center;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        
        .feature-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        
        .feature-icon {{
            font-size: 36px;
            margin-bottom: 12px;
        }}
        
        .feature-card h3 {{
            font-size: 14px;
            margin-bottom: 4px;
        }}
        
        .feature-card p {{
            font-size: 11px;
            color: #999;
        }}
        
        /* Bottom Navigation */
        .bottom-nav {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            display: flex;
            justify-content: space-around;
            padding: 12px 20px;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
        }}
        
        .nav-item {{
            text-align: center;
            cursor: pointer;
            padding: 8px;
            transition: color 0.3s;
        }}
        
        .nav-item:hover {{
            color: {c["primary"]};
        }}
        
        .nav-icon {{
            font-size: 24px;
            display: block;
        }}
        
        .nav-label {{
            font-size: 11px;
            margin-top: 4px;
        }}
        
        /* Action Button */
        .fab {{
            position: fixed;
            bottom: 80px;
            right: 20px;
            width: 56px;
            height: 56px;
            background: {c["primary"]};
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            transition: transform 0.3s;
        }}
        
        .fab:hover {{
            transform: scale(1.1);
        }}
        
        @media (max-width: 480px) {{
            .container {{
                padding: 16px;
            }}
            .features-grid {{
                grid-template-columns: 1fr 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">🚀</div>
            <h1>{app_name}</h1>
            <p>Your personal AI-generated app</p>
        </div>
        
        <div class="welcome-card">
            <div class="user-greeting">
                <div>
                    <strong>Welcome back!</strong>
                    <div style="font-size: 12px; color: #666;">Ready to {features[0].lower() if features else 'explore'}?</div>
                </div>
                <div class="avatar">👤</div>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">42</div>
                    <div class="stat-label">Tasks Done</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">128</div>
                    <div class="stat-label">Points</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">7</div>
                    <div class="stat-label">Days Streak</div>
                </div>
            </div>
        </div>
        
        <div class="features-section">
            <h2 class="section-title">✨ Features</h2>
            <div class="features-grid">
                {features_html}
            </div>
        </div>
    </div>
    
    <div class="bottom-nav">
        <div class="nav-item" onclick="showToast('Home')">
            <span class="nav-icon">🏠</span>
            <span class="nav-label">Home</span>
        </div>
        <div class="nav-item" onclick="showToast('Explore')">
            <span class="nav-icon">🔍</span>
            <span class="nav-label">Explore</span>
        </div>
        <div class="nav-item" onclick="showToast('Activity')">
            <span class="nav-icon">📊</span>
            <span class="nav-label">Activity</span>
        </div>
        <div class="nav-item" onclick="showToast('Profile')">
            <span class="nav-icon">👤</span>
            <span class="nav-label">Profile</span>
        </div>
    </div>
    
    <div class="fab" onclick="showToast('Quick Action!')">
        +
    </div>
    
    <script>
        function showToast(message) {{
            // Create toast element
            const toast = document.createElement('div');
            toast.textContent = message;
            toast.style.position = 'fixed';
            toast.style.bottom = '140px';
            toast.style.left = '50%';
            toast.style.transform = 'translateX(-50%)';
            toast.style.background = '#333';
            toast.style.color = 'white';
            toast.style.padding = '10px 20px';
            toast.style.borderRadius = '25px';
            toast.style.fontSize = '14px';
            toast.style.zIndex = '1000';
            toast.style.animation = 'fadeInOut 2s';
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 2000);
        }}
        
        // Add animation style
        const style = document.createElement('style');
        style.textContent = `
            @keyframes fadeInOut {{
                0% {{ opacity: 0; transform: translateX(-50%) translateY(20px); }}
                15% {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
                85% {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
                100% {{ opacity: 0; transform: translateX(-50%) translateY(-20px); }}
            }}
        `;
        document.head.appendChild(style);
        
        // Update stats periodically
        let points = 128;
        setInterval(() => {{
            points += Math.floor(Math.random() * 5);
            document.querySelector('.stat-number:nth-child(2)').textContent = points;
        }}, 30000);
    </script>
</body>
</html>'''

def generate_todo_app() -> str:
    """Generate a complete todo list app"""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo App - Nexus AI</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 500px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 24px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        h1 {
            text-align: center;
            color: #667eea;
            margin-bottom: 24px;
        }
        .input-group {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        input {
            flex: 1;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
        }
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 10px;
            cursor: pointer;
        }
        .todo-item {
            display: flex;
            align-items: center;
            padding: 12px;
            margin: 8px 0;
            background: #f7f7f7;
            border-radius: 10px;
            gap: 10px;
        }
        .todo-text {
            flex: 1;
        }
        .completed {
            text-decoration: line-through;
            color: #999;
        }
        .delete-btn {
            background: #ff4757;
            padding: 5px 10px;
            font-size: 12px;
        }
        .stats {
            text-align: center;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 Todo List</h1>
        <div class="input-group">
            <input type="text" id="todoInput" placeholder="Add a new task...">
            <button onclick="addTodo()">Add</button>
        </div>
        <div id="todoList"></div>
        <div class="stats" id="stats"></div>
    </div>
    <script>
        let todos = JSON.parse(localStorage.getItem('todos') || '[]');
        
        function saveTodos() {
            localStorage.setItem('todos', JSON.stringify(todos));
            renderTodos();
        }
        
        function addTodo() {
            const input = document.getElementById('todoInput');
            const text = input.value.trim();
            if (text) {
                todos.push({ id: Date.now(), text, completed: false });
                input.value = '';
                saveTodos();
            }
        }
        
        function toggleTodo(id) {
            const todo = todos.find(t => t.id === id);
            if (todo) todo.completed = !todo.completed;
            saveTodos();
        }
        
        function deleteTodo(id) {
            todos = todos.filter(t => t.id !== id);
            saveTodos();
        }
        
        function renderTodos() {
            const list = document.getElementById('todoList');
            const stats = document.getElementById('stats');
            const completed = todos.filter(t => t.completed).length;
            
            list.innerHTML = todos.map(todo => `
                <div class="todo-item">
                    <input type="checkbox" ${todo.completed ? 'checked' : ''} onclick="toggleTodo(${todo.id})">
                    <div class="todo-text ${todo.completed ? 'completed' : ''}">${escapeHtml(todo.text)}</div>
                    <button class="delete-btn" onclick="deleteTodo(${todo.id})">Delete</button>
                </div>
            `).join('');
            
            stats.innerHTML = `${completed}/${todos.length} tasks completed`;
        }
        
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        renderTodos();
    </script>
</body>
</html>'''

def parse_prompt(prompt: str) -> Dict:
    """Parse user prompt intelligently"""
    prompt_lower = prompt.lower()
    
    # Detect app type
    if "todo" in prompt_lower or "task" in prompt_lower:
        return {"type": "todo", "name": "Todo App", "features": ["Add tasks", "Complete tasks", "Delete tasks", "Local storage"]}
    elif "chat" in prompt_lower or "message" in prompt_lower:
        return {"type": "chat", "name": "Chat App", "features": ["Real-time messaging", "User profiles", "File sharing"]}
    elif "fitness" in prompt_lower or "workout" in prompt_lower:
        return {"type": "fitness", "name": "Fitness Tracker", "features": ["Step counter", "Workout log", "Calorie tracker"]}
    else:
        # Extract name from prompt
        words = prompt_lower.split()
        name = "My App"
        if "called" in words:
            idx = words.index("called") + 1
            if idx < len(words):
                name = words[idx].title()
        
        # Extract features
        features = []
        feature_keywords = {
            "login": "User Login", "signup": "Sign Up", "chat": "Chat", 
            "store": "Store", "payment": "Payments", "map": "Maps",
            "notification": "Notifications", "share": "Social Share"
        }
        for kw, feature in feature_keywords.items():
            if kw in prompt_lower:
                features.append(feature)
        
        if not features:
            features = ["Dashboard", "Profile", "Settings"]
        
        return {"type": "general", "name": name, "features": features}

@app.post("/api/generate")
async def generate_app(request: PromptRequest):
    """Generate app from prompt"""
    
    session_id = f"nexus_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    parsed = parse_prompt(request.prompt)
    
    if parsed["type"] == "todo":
        html_content = generate_todo_app()
    else:
        html_content = generate_complete_web_app(
            parsed["name"], 
            parsed["features"][:6],
            "purple"
        )
    
    # Save to temp file
    temp_file = f"/data/data/com.termux/files/home/tmp/{session_id}.html"
    os.makedirs("/data/data/com.termux/files/home/tmp", exist_ok=True)
    
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return JSONResponse({
        "success": True,
        "session_id": session_id,
        "requirements": parsed,
        "deployment_urls": {
            "preview": f"file://{temp_file}",
            "message": "App generated! Open the file to view."
        },
        "code_preview": html_content[:500]
    })

@app.get("/api/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head><title>Nexus AI - Termux</title></head>
        <body style="font-family: sans-serif; text-align: center; padding: 50px;">
            <h1>🚀 Nexus AI is Running!</h1>
            <p>Your AI app factory is active on Termux.</p>
            <p>Access the web interface at: <a href="http://localhost:3000">http://localhost:3000</a></p>
            <p>API Docs: <a href="/docs">/docs</a></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║     🚀 NEXUS AI - TERMUX EDITION                    ║
    ║     Running on your Android phone!                  ║
    ║                                                      ║
    ║     📱 Server: http://localhost:8000                ║
    ║     📚 API Docs: http://localhost:8000/docs         ║
    ║                                                      ║
    ║     ⚡ Open a NEW Termux session and run:            ║
    ║     cd ~/nexus-ai/frontend && npm start             ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    """)
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF

echo "✅ Backend created!"
