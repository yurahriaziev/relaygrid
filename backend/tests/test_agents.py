from fastapi.testclient import TestClient
from app.main import app
from uuid import UUID

test_client = TestClient(app)

def test_agent_create():
    response = test_client.post('/agents', json={'name': 'robot2', 'agent_type': 'robot'})

    body = response.json()

    assert response.status_code == 201
    assert body['name'] == 'robot2'
    assert body['agent_type'] == 'robot'
    assert body['id']

    UUID(body['id'])

def test_invalid_name():
    response = test_client.post('/agents', json={'name': '   ', 'agent_type': 'robot'})

    body = response.json()

    assert response.status_code == 422
    