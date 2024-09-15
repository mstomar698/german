
import pytest # type: ignore
import httpx # type: ignore
from fastapi.testclient import TestClient # type: ignore
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health-check")  
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_news_by_id():
    valid_id = 123456
    response = client.get(f"/api/get-news/{valid_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data['id'] == valid_id

def test_get_news_by_invalid_id():
    invalid_id = -1
    response = client.get(f"/api/get-news/{invalid_id}")
    assert response.status_code == 404
    expected_detail = f"Story with ID {invalid_id} not found or is unavailable."
    assert response.json()['detail'] == expected_detail

@pytest.mark.asyncio
async def test_health_check_async():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/health-check")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
