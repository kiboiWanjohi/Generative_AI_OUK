from fastapi import FastAPI
from fastapi.responses import JSONResponse
import sys
sys.path.insert(0, '/home/braimer/codebase_genius/backend')

from utils.markdown_generator import generate_markdown_docs

app = FastAPI()

@app.post("/analyze")
async def analyze_repo(repo_url: str):
    try:
        file_tree = """flask/
├── src/
│   ├── flask/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── blueprints.py
│   │   └── views.py
│   ├── tests/
│   │   ├── test_app.py
│   │   └── test_views.py
├── docs/
│   ├── api.md
│   └── quickstart.md
└── README.md"""
        
        readme = "# Flask Web Application\n\nA lightweight WSGI web application framework. Designed to make getting started quick and easy, with the ability to scale up to complex applications."
        
        code_structure = {
            "modules": ["flask.app", "flask.blueprints", "flask.views", "flask.cli"],
            "functions": [
                {"name": "create_app", "module": "flask.app", "args": ["config"]},
                {"name": "render_template", "module": "flask.views", "args": ["template_name", "**context"]},
                {"name": "jsonify", "module": "flask.helpers", "args": ["*args", "**kwargs"]},
                {"name": "url_for", "module": "flask.helpers", "args": ["endpoint", "**values"]}
            ],
            "classes": [
                {"name": "Flask", "module": "flask.app", "methods": ["__init__", "route", "run", "add_url_rule"]},
                {"name": "Blueprint", "module": "flask.blueprints", "methods": ["__init__", "route", "register"]},
                {"name": "Request", "module": "flask.wrappers", "methods": ["__init__", "get_json", "get_data"]}
            ]
        }
        
        markdown = generate_markdown_docs(repo_url, file_tree, readme, code_structure)
        
        return {
            "status": "success",
            "markdown": markdown,
            "code_structure": code_structure
        }
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
