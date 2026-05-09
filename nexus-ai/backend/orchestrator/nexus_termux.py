"""
NEXUS AI - TERMUX VERSION
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
import os
import json
import uvicorn

app = FastAPI(title="Nexus AI - Termux")

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

def generate_todo_app():
    return """<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Todo App</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:system-ui;background:linear-gradient(135deg,#667eea,#764ba2);min-height:100vh;padding:20px}
.container{max-width:500px;margin:0 auto;background:white;border-radius:20px;padding:24px;box-shadow:0 20px 60px rgba(0,0,0,0.3)}
h1{text-align:center;color:#667eea;margin-bottom:24px}
.input-group{display:flex;gap:10px;margin-bottom:20px}
input{flex:1;padding:12px;border:2px solid #e0e0e0;border-radius:10px}
button{background:#667eea;color:white;border:none;padding:12px 20px;border-radius:10px;cursor:pointer}
.todo-item{display:flex;align-items:center;padding:12px;margin:8px 0;background:#f7f7f7;border-radius:10px;gap:10px}
.todo-text{flex:1}
.completed{text-decoration:line-through;color:#999}
.delete-btn{background:#ff4757;padding:5px 10px;font-size:12px}
.stats{text-align:center;margin-top:20px;padding-top:20px;border-top:1px solid #eee;color:#666}
</style>
</head>
<body>
<div class="container">
<h1>📝 Todo List</h1>
<div class="input-group"><input type="text" id="todoInput" placeholder="Add a task..."><button onclick="addTodo()">Add</button></div>
<div id="todoList"></div>
<div class="stats" id="stats"></div>
</div>
<script>
let todos=JSON.parse(localStorage.getItem('todos')||'[]');
function saveTodos(){localStorage.setItem('todos',JSON.stringify(todos));renderTodos();}
function addTodo(){const input=document.getElementById('todoInput');const text=input.value.trim();if(text){todos.push({id:Date.now(),text,completed:false});input.value='';saveTodos();}}
function toggleTodo(id){const todo=todos.find(t=>t.id===id);if(todo)todo.completed=!todo.completed;saveTodos();}
function deleteTodo(id){todos=todos.filter(t=>t.id!==id);saveTodos();}
function renderTodos(){const list=document.getElementById('todoList');const stats=document.getElementById('stats');const completed=todos.filter(t=>t.completed).length;list.innerHTML=todos.map(todo=>`<div class="todo-item"><input type="checkbox" ${todo.completed?'checked':''} onclick="toggleTodo(${todo.id})"><div class="todo-text ${todo.completed?'completed':''}">${escapeHtml(todo.text)}</div><button class="delete-btn" onclick="deleteTodo(${todo.id})">Delete</button></div>`).join('');stats.innerHTML=`${completed}/${todos.length} tasks completed`;}
function escapeHtml(text){const div=document.createElement('div');div.textContent=text;return div.innerHTML;}
renderTodos();
</script>
</body>
</html>"""

def generate_general_app(name, features):
    features_html = "".join([f'<div class="feature-card" onclick="alert(\'{f}\')"><div class="feature-icon">✨</div><h3>{f}</h3></div>' for f in features[:4]])
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{name}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:system-ui;background:linear-gradient(135deg,#667eea,#764ba2);min-height:100vh;padding:20px}}
.container{{max-width:600px;margin:0 auto;background:white;border-radius:20px;padding:24px;box-shadow:0 10px 40px rgba(0,0,0,0.1)}}
h1{{color:#667eea;margin-bottom:16px}}
.feature-card{{background:#f7f7f7;padding:16px;margin:12px 0;border-radius:12px;cursor:pointer;transition:transform 0.2s}}
.feature-card:hover{{transform:translateX(5px);background:#667eea;color:white}}
.feature-icon{{font-size:24px;display:inline-block;margin-right:10px}}
</style>
</head>
<body>
<div class="container"><h1>🚀 {name}</h1><p>AI-generated app with:</p>{features_html}<button onclick="alert('Hello from {name}!')" style="margin-top:20px;background:#667eea;color:white;border:none;padding:10px 20px;border-radius:10px">Click Me</button></div>
</body>
</html>"""

@app.post("/api/generate")
async def generate_app(request: PromptRequest):
    prompt_lower = request.prompt.lower()
    session_id = f"nexus_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    if "todo" in prompt_lower:
        html = generate_todo_app()
        name = "Todo App"
        features = ["Add tasks", "Delete tasks"]
    else:
        name = "My App"
        words = prompt_lower.split()
        if "called" in words:
            idx = words.index("called") + 1
            if idx < len(words):
                name = words[idx].title()
        features = ["Dashboard", "Profile", "Settings"] if "login" not in prompt_lower else ["Login", "Profile", "Dashboard"]
        html = generate_general_app(name, features)
    
    os.makedirs("/data/data/com.termux/files/home/tmp", exist_ok=True)
    file_path = f"/data/data/com.termux/files/home/tmp/{session_id}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    return JSONResponse({
        "success": True,
        "session_id": session_id,
        "requirements": {"name": name, "features": features},
        "deployment_urls": {"preview": f"file://{file_path}"},
        "code_preview": html[:300]
    })

@app.get("/")
async def root():
    return {"message": "Nexus AI is running on Termux"}

if __name__ == "__main__":
    print("\n🚀 Nexus AI Backend Started\n📱 http://localhost:8000\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
