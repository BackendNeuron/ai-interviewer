# backend/utils.py

import os

def get_meaningful_code_files(repo_path):
    files = []
    for root, _, filenames in os.walk(repo_path):
        for name in filenames:
            path = os.path.join(root, name)
            if name.endswith(('.py', '.ipynb', '.js', '.ts', '.html', '.css', '.java', '.cpp', '.c', '.go', '.rs')) or is_code_file(path):
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        if len(content.strip()) > 20:
                            files.append({"path": path, "content": content})
                except:
                    pass
    return files

def is_code_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            sample = f.read(500)
            return any(c in sample for c in ["def ", "class ", "import ", "#", "{", "}", "function "])
    except:
        return False
