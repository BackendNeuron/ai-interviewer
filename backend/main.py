# backend/main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.responses import JSONResponse
from backend.github_parser import clone_repo
from backend.llm_engine import analyze_code_with_llm
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("interview.html", {"request": request})






# backend/main.py 

from backend.github_parser import clone_repo  
from backend.llm_engine import analyze_code_with_llm

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, repo_url: str = Form(...)):
    try:
        parts = repo_url.rstrip("/").split("/")
        owner, repo = parts[-2], parts[-1]

        repo_path = clone_repo(owner, repo)
        questions = analyze_code_with_llm(repo_path)  

        return templates.TemplateResponse("interview.html", {
            "request": request,
            "questions": questions,
            "repo_url": repo_url
        })
    except Exception as e:
        return templates.TemplateResponse("interview.html", {
            "request": request,
            "error": str(e)
        })
