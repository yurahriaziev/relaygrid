from fastapi import FastAPI, status
from app.schemas import AgentCreate, AgentResponse
from uuid import uuid4

app = FastAPI()

@app.get("/health", tags=['Health'])
def health():
    return {
        'status': 'ok'
    }

@app.post("/agents", tags=['Agents'], response_model=AgentResponse, status_code=status.HTTP_201_CREATED)
def create_agent(agent:AgentCreate):
    return AgentResponse(
        id=uuid4(),
        name=agent.name,
        agent_type=agent.agent_type
    )