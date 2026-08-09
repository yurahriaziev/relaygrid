from fastapi.testclient import TestClient
from app.main import app

test_client = TestClient(app)

def test_agent_create():
    response = test_client.post('/agents', json={'name': 'robot2', 'agent_type': 'robot'})

    assert response.status_code == 201
    assert response.json().get('name') == 'robot2'
    assert response.json().get('agent_type') == 'robot'
    assert response.json().get('id')