# run_agent.py

from fastapi import FastAPI, HTTPException
from core.orchestrator import Orchestrator

app = FastAPI(title="Web Research Agent")

@app.on_event("startup")
async def startup_event():
    # instantiate our orchestrator once
    app.state.orch = Orchestrator()

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Web Research Agent is live!"}

@app.get("/demo")
async def demo_search(query: str):
    """
    Demo endpoint: /demo?query=your+search+term
    """
    try:
        return app.state.orch.run(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

