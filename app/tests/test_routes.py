import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_upload_file(client):
    data = {'file': (open('test_file.txt', 'rb'), 'test_file.txt')}
    response = client.post('/upload', content_type='multipart/form-data', data=data)
    assert response.status_code == 200

def test_view_scans(client):
    response = client.get('/scans')
    assert response.status_code == 200
