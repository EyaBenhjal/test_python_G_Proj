from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

TEST_TASK_ID = 1
TEST_AUTHOR_ID = 1

def test_create_comment():
    response = client.post("/comments/", json={
        "content": "Commentaire Test",
        "task_id": TEST_TASK_ID,
        "author_id": TEST_AUTHOR_ID
    })
    assert response.status_code == 201
    data = response.json()
    assert data["content"] == "Commentaire Test"

def test_get_comments():
    response = client.get("/comments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_comment():
    response = client.put("/comments/1", json={
        "content": "Commentaire modifié"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["content"] == "Commentaire modifié"

def test_delete_comment():
    # On suppose que l'id 1 existe
    response = client.delete("/comments/1")
    assert response.status_code == 204  # pas de contenu
