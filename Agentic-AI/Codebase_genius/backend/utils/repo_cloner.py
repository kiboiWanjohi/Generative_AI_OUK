import os
import tempfile
from pathlib import Path
from git import Repo

def clone_repository(repo_url: str, depth: int = 1) -> str:
    """Clone a repository and return the local path"""
    try:
        temp_dir = tempfile.mkdtemp(prefix="repo_")
        Repo.clone_from(repo_url, temp_dir, depth=depth)
        return temp_dir
    except Exception as e:
        print(f"Error cloning repo: {e}")
        return ""

def get_file_tree(repo_path: str, max_depth: int = 3, prefix: str = "") -> str:
    """Generate a file tree from a directory"""
    if not os.path.exists(repo_path):
        return ""
    
    tree = ""
    try:
        for i, item in enumerate(os.listdir(repo_path)):
            if item.startswith('.'):
                continue
            path = os.path.join(repo_path, item)
            is_last = i == len(os.listdir(repo_path)) - 1
            
            if os.path.isdir(path) and max_depth > 0:
                tree += f"{prefix}├── {item}/\n"
                tree += get_file_tree(path, max_depth - 1, prefix + "│   ")
            else:
                tree += f"{prefix}├── {item}\n"
    except Exception as e:
        print(f"Error reading directory: {e}")
    
    return tree

def get_readme_content(repo_path: str) -> str:
    """Extract README content"""
    readme_files = ["README.md", "README.txt", "README", "readme.md"]
    
    for readme in readme_files:
        path = os.path.join(repo_path, readme)
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    return f.read()[:500]
            except Exception as e:
                print(f"Error reading {readme}: {e}")
    
    return "No README found"
