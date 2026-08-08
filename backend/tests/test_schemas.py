from app.schemas import AgentCreate

import pytest
from pydantic import ValidationError

def test_schemas():
    agent1 = AgentCreate(name='  drone-01   ', agent_type=' drone    ')
    
    assert agent1.name == 'drone-01'
    assert agent1.agent_type == 'drone'

def test_agent_name_cannot_be_blank():
    with pytest.raises(ValidationError):
        AgentCreate(name="    ", agent_type='robot')