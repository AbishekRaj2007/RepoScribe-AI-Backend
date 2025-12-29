from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.github_service import fetch_repo_structure
from app.services.ai_service import generate_readme


app = FastAPI(title="Reposcribe API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend URL later
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def check():
    return {"status": "Reposcribe API is running 🚀"}



@app.post("/generate-readme")
def generate(repo_url: str):
    owner, repo = repo_url.rstrip("/").split("/")[-2:]
    repo_data = fetch_repo_structure(owner, repo)
    readme = generate_readme(repo_data)
    return {"readme": readme}
