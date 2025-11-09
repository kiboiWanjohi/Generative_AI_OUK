"""Bridge between Jac and Python utilities"""
from utils.repo_cloner import clone_repository, get_file_tree, get_readme_content

def process_repository(repo_url: str) -> dict:
    """Process a repository and return all data"""
    try:
        # Clone repo
        repo_path = clone_repository(repo_url)
        
        if not repo_path:
            return {
                "success": False,
                "error": "Failed to clone repository"
            }
        
        # Get file tree
        file_tree = get_file_tree(repo_path, max_depth=3)
        
        # Get README
        readme = get_readme_content(repo_path)
        
        return {
            "success": True,
            "repo_path": repo_path,
            "file_tree": file_tree,
            "readme": readme
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
