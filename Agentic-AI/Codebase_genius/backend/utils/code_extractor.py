"""Extract code structure (functions, classes, relationships)"""
import os
import ast
from pathlib import Path

def extract_code_structure(repo_path: str, max_files: int = 20) -> dict:
    """Extract functions, classes, and modules from repo"""
    structure = {
        "modules": [],
        "functions": [],
        "classes": [],
        "relationships": []
    }
    
    try:
        files_processed = 0
        for root, dirs, files in os.walk(repo_path):
            # Skip hidden and common non-code directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules', '.git']]
            
            for file in files:
                if files_processed >= max_files:
                    break
                    
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    relative_path = filepath.replace(repo_path, '').lstrip('/')
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            tree = ast.parse(content)
                            
                            module_name = relative_path.replace('/', '.').replace('.py', '')
                            structure["modules"].append(module_name)
                            
                            for node in ast.walk(tree):
                                if isinstance(node, ast.FunctionDef):
                                    structure["functions"].append({
                                        "name": node.name,
                                        "module": module_name,
                                        "args": [arg.arg for arg in node.args.args]
                                    })
                                elif isinstance(node, ast.ClassDef):
                                    structure["classes"].append({
                                        "name": node.name,
                                        "module": module_name,
                                        "methods": [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                                    })
                        
                        files_processed += 1
                    except Exception as e:
                        print(f"Error parsing {filepath}: {e}")
    except Exception as e:
        print(f"Error extracting structure: {e}")
    
    return structure
