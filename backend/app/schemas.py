from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID

class AgentCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=1)
    agent_type: str = Field(min_length=1)

class AgentResponse(BaseModel):
    id: UUID
    name: str
    agent_type: str