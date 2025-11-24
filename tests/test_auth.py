import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_signup():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/auth/signup", json={
            "username": "eya",
            "email": "eya_test@example.com",
            "password": ""
        })
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "eya"
    assert "id" in data
