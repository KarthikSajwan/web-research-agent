# run_agent.py
from fastapi import FastAPI

app = FastAPI(title="Web Research Agent")

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Web Research Agent is live!"}

# here’s where you’ll later mount routers, etc.
