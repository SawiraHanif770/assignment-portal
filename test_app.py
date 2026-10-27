import pytest
from app import app, submissions

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    submissions.clear()

def test_valid_submission(client):
    response = client.post('/api/submit', json={
        "name": "Sawira Bibi",
        "reg_no": "SP21-BCS-001",
        "title": "DevOps Lab",
        "url": "https://github.com/example/repo"
    })
    assert response.status_code == 200
    assert response.json["status"] == "saved"

def test_missing_reg_no(client):
    response = client.post('/api/submit', json={
        "name": "Sawira Bibi",
        "reg_no": "",
        "title": "DevOps Lab",
        "url": "https://github.com/example/repo"
    })
    assert response.status_code == 400
    assert "Missing registration number" in response.json["message"]

def test_invalid_url(client):
    response = client.post('/api/submit', json={
        "name": "Sawira Bibi",
        "reg_no": "SP21-BCS-001",
        "title": "DevOps Lab",
        "url": "invalid-url-format"
    })
    assert response.status_code == 400
    assert "Invalid submission URL" in response.json["message"]