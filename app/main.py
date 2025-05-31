from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .services.complexity import analyze_complexity
from .services.linting import run_linting
from .services.ast_analysis import analyze_ast
from .services.ai_review import generate_ai_review

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html") as f:
        return f.read()

@app.post("/upload/")
async def upload_files(files: list[UploadFile] = File(...)):
    results = {}
    for file in files:
        content = await file.read()
        code = content.decode("utf-8")
        
        complexity = analyze_complexity(code)
        linting_issues = run_linting(code)
        ast_info = analyze_ast(code)
        ai_feedback = generate_ai_review(code)

        results[file.filename] = {
            "complexity": complexity,
            "linting_issues": linting_issues,
            "ast_info": ast_info,
            "ai_feedback": ai_feedback
        }
    
    return results
