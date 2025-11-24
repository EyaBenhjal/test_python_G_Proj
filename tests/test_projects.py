from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_project():
    # On crée un projet
    response = client.post("/projects/", json={
        "title": "Projet Test",
        "description": "Description Test",
        "owner_id": 1
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Projet Test"
    assert data["description"] == "Description Test"

def test_get_projects():
    response = client.get("/projects/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
