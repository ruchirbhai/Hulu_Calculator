from app import app
import pytest


@pytest.fixture
def client():
    app.testing = True

    with app.test_client() as client:
        return client


def test_add(client):
    app.testing = True
    # test_add #1: check for 2 positive integers
    response = client.post('/add', json={
        'number_1': '1', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == 3.0

    # test_add #2: check for 2 negative floats
    response = client.post('/add', json={
        'number_1': '-1.3', 'number_2': '-2.5'
    })
    data = response.get_json()
    assert data['result'] == -3.8

    # test_add #3: check for 1 float 1 integer with final value zero
    response = client.post('/add', json={
        'number_1': '-2.0', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == 0.0


def test_subtract(client):
    app.testing = True
    # test_subtract #1: check for 2 positive integers
    response = client.post('/subtract', json={
        'number_1': '1', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == -1.0

    # test_subtract #2: check for 2 negative floats with number_1 < number_2
    response = client.post('/subtract', json={
        'number_1': '-1.8', 'number_2': '-2.4'
    })
    data = response.get_json()
    assert data['result'] == 0.5999999999999999

    # test_subtract #3: check for 1 float 1 integer with final value zero
    response = client.post('/subtract', json={
        'number_1': '2.0', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == 0.0

    # test_subtract #4: check for negative number_1 and positive number_2
    response = client.post('/subtract', json={
        'number_1': '-2.0', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == -4.0


def test_multiply(client):
    app.testing = True
    # test_multiply #1: check for 2 positive integers
    response = client.post('/multiply', json={
        'number_1': '10', 'number_2': '15'
    })
    data = response.get_json()
    assert data['result'] == 150.0

    # test_multiply #2: check for 2 negative floats
    response = client.post('/multiply', json={
        'number_1': '-10.0', 'number_2': '-25.0'
    })
    data = response.get_json()
    assert data['result'] == 250.0

    # test_multiply #3: check for 1 float 1 integer
    response = client.post('/multiply', json={
        'number_1': '2.0', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == 4.0

    # test_multiply #4: check for negative number_1 and positive number_2
    response = client.post('/multiply', json={
        'number_1': '-100.0', 'number_2': '500'
    })
    data = response.get_json()
    assert data['result'] == -50000.0

    # test_multiply #5: multiplication with 0
    response = client.post('/multiply', json={
        'number_1': '-100.0', 'number_2': '0'
    })
    data = response.get_json()
    assert data['result'] == 0.0


def test_divide(client):
    app.testing = True
    # test_divide #1: check for 2 positive integers
    response = client.post('/divide', json={
        'number_1': '15', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == 7.5

    # test_divide #2: check for 2 negative floats
    response = client.post('/divide', json={
        'number_1': '-50.0', 'number_2': '-25.0'
    })
    data = response.get_json()
    assert data['result'] == 2.0

    # test_divide #3: check for 1 float 1 integer number_1 < number_2
    response = client.post('/divide', json={
        'number_1': '5', 'number_2': '-9.0'
    })
    data = response.get_json()
    assert data['result'] == -0.5555555555555556

    # test_divide #4: check for negative number_1 and positive number_2
    response = client.post('/divide', json={
        'number_1': '-100.0', 'number_2': '500'
    })
    data = response.get_json()
    assert data['result'] == -0.2
