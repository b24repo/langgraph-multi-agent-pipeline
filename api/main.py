from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from graphs.research_graph import build_research_graph
from models.schemas import ResearchRequest

app = FastAPI(title="LangGraph Multi-Agent Pipeline")

@app.post("/research")
async def run_research(request: ResearchRequest):
    graph = build_research_graph()
    return StreamingResponse(
        graph.astream({"topic": request.topic, "depth": request.depth}),
        media_type="text/event-stream"
    )

@app.get("/health")
async def health():
    return {"status": "ok"}
