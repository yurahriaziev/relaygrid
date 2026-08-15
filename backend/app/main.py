from fastapi import FastAPI, status, Depends
from app.schemas import AgentCreate, AgentResponse
from uuid import uuid4

from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Agent
from app.database import get_db

app = FastAPI()

@app.get("/health", tags=['Health'])
def health():
    return {
        'status': 'ok'
    }

@app.post("/agents", tags=['Agents'], response_model=AgentResponse, status_code=status.HTTP_201_CREATED)
async def create_agent(agent: AgentCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    db_agent = Agent(
        name=agent.name,
        agent_type=agent.agent_type
    )

    db.add(db_agent)
    await db.commit()

    return AgentResponse(
        id=db_agent.id,
        name=db_agent.name,
        agent_type=db_agent.agent_type
    )