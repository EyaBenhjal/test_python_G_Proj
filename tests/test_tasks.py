from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ID de test, à adapter selon ta base
TEST_PROJECT_ID = 1
TEST_USER_ID = 1

def test_create_task():
    response = client.post("/tasks/", json={
        "title": "Tâche Test",
        "description": "Description de la tâche",
        "status": "todo",
        "project_id": TEST_PROJECT_ID,
        "assigned_to_id": TEST_USER_ID
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Tâche Test"
    assert data["status"] == "todo"

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    # On suppose que l'id 1 existe
    response = client.put("/tasks/1", json={
        "title": "Tâche Modifiée",
        "description": "Nouvelle description",
        "status": "done",
        "assigned_to_id": TEST_USER_ID
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "done"

def test_delete_task():
    # On suppose que l'id 1 existe
    response = client.delete("/tasks/1")
    assert response.status_code == 204  # pas de contenu
