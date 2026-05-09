import http.server
import socketserver
from urllib.parse import unquote_plus
import os

PORT = 8080

class SmartHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Secret Admin Path: http://localhost:8080/admin
        if self.path == '/admin':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            content = "<h2>No messages yet.</h2>"
            if os.path.exists("messages.txt"):
                with open("messages.txt", "r") as f:
                    # Convert text file lines to a basic HTML list
                    messages = f.read().replace("\n", "<br>")
                    content = f"<div style='background:#1e293b;padding:20px;border-radius:10px;'>{messages}</div>"

            admin_html = f"""
            <html>
            <body style='background:#0f172a;color:white;font-family:sans-serif;padding:40px;'>
                <h1 style='color:#38bdf8;'>🛡️ Nexus Admin Dashboard</h1>
                <hr style='border:0.5px solid #334155;margin-bottom:20px;'>
                {content}
                <br><a href='/' style='color:#94a3b8;'>← Back to Site</a>
            </body>
            </html>
            """
            self.wfile.write(admin_html.encode('utf-8'))
        else:
            # Serve the regular website files
            super().do_GET()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        readable_data = unquote_plus(post_data)

        # Save with a timestamp or simple separator
        with open("messages.txt", "a") as f:
            f.write(f"ENTRY: {readable_data}\n")

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        success_page = """
        <html>
        <body style='background:#0f172a;color:white;text-align:center;padding-top:50px;font-family:sans-serif;'>
            <h1>🚀 Data Archived!</h1>
            <p>Nexus AI has saved your message.</p>
            <a href='/' style='color:#38bdf8;'>Return to App</a> | <a href='/admin' style='color:#38bdf8;'>View Admin</a>
        </body>
        </html>
        """
        self.wfile.write(success_page.encode('utf-8'))

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), SmartHandler) as httpd:
    print(f"🚀 Nexus Admin Server LIVE at http://localhost:{PORT}")
    httpd.serve_forever()

