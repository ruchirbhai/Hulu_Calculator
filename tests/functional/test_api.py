from app import app
import pytest


@pytest.fixture
def client():
    app.testing = True

    with app.test_client() as client:
        return client


def test_add(client):
    app.testing = True
    response = client.post('/add',json={
        'number_1': '1', 'number_2': '2'
    })
    data = response.get_json()
    #response.code implement
    #print(data)
    assert data['result'] == 3.0
