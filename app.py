import requests
from bs4 import BeautifulSoup
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Professional UI Template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>SEO Pro Auditor</title>
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow p-4">
            <h1 class="text-primary mb-4">🚀 SEO Pro Auditor</h1>
            
            {% if not results %}
            <form action="/audit" method="get">
                <div class="mb-3">
                    <label class="form-label">Enter Website URL</label>
                    <input type="url" name="url" class="form-control" placeholder="https://example.com" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Analyze Now</button>
            </form>
            {% else %}
            <h3>Analysis for: <small class="text-muted">{{ url }}</small></h3>
            <hr>
            <div class="row text-center mb-4">
                <div class="col"><div class="p-3 border bg-white rounded"><h5>Title Tags</h5><p class="h4">{{ results.title }}</p></div></div>
                <div class="col"><div class="p-3 border bg-white rounded"><h5>H1 Count</h5><p class="h4">{{ results.h1 }}</p></div></div>
                <div class="col"><div class="p-3 border bg-white rounded"><h5>Alt Missing</h5><p class="h4 text-danger">{{ results.missing_alt }}</p></div></div>
            </div>
            <a href="/" class="btn btn-outline-secondary">← Back to Dashboard</a>
            {% endif %}
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, results=None)

@app.route('/audit')
def audit():
    target_url = request.args.get('url')
    try:
        response = requests.get(target_url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        results = {
            "title": "✅ Found" if soup.title else "❌ Missing",
            "h1": len(soup.find_all('h1')),
            "missing_alt": len([img for img in soup.find_all('img') if not img.get('alt')])
        }
        return render_template_string(HTML_TEMPLATE, results=results, url=target_url)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

