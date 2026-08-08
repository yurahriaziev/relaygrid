from pydantic import BaseModel, Field

class AgentCreate(BaseModel):
    name: str = Field(min_length=1)
    agent_type: str = Field(min_length=1)