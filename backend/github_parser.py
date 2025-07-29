# backend/github_parser.py
import os
import shutil
import tempfile
import subprocess

def clone_repo(owner: str, repo: str) -> str:
    tmp_dir = tempfile.mkdtemp()
    repo_url = f"https://github.com/{owner}/{repo}.git"
    try:
        subprocess.run(["git", "clone", repo_url, tmp_dir], check=True, capture_output=True)
        return tmp_dir
    except subprocess.CalledProcessError as e:
        shutil.rmtree(tmp_dir)
        raise Exception(f"Failed to clone repository: {e.stderr.decode()}")
