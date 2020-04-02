from app import app
import pytest


@pytest.fixture
def client():
    app.testing = True

    with app.test_client() as client:
        return client


def test1_add_positive_int(client):
    app.testing = True
    # test_add #1: check for 2 positive integers
    response = client.post('/add', json={
        'number_1': '1', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == 3.0


def test2_add_mix(client):
    app.testing = True
    # test_add #2: check for 2 negative floats
    response = client.post('/add', json={
        'number_1': '-123000000000000000000000000000', 'number_2': '500.0'
    })
    data = response.get_json()
    assert data['result'] == -1.23e+29


def test3_add_float_out_zero(client):
    app.testing = True
    # test_add #3: check for 1 float 1 integer with final value zero
    response = client.post('/add', json={
        'number_1': '-2.0', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == 0.0


def test1_subtract_positive_int(client):
    app.testing = True
    # test_subtract #1: check for 2 positive integers
    response = client.post('/subtract', json={
        'number_1': '1', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == -1.0


def test2_subtract_negative_floats(client):
    app.testing = True
    # test_subtract #2: check for 2 negative floats with number_1 < number_2
    response = client.post('/subtract', json={
        'number_1': '-1.8', 'number_2': '-2.4'
    })
    data = response.get_json()
    assert data['result'] == 0.5999999999999999


def test3_subtract_negative_mix(client):
    app.testing = True
    # test_subtract #3: check for 1 float 1 integer with final value zero
    response = client.post('/subtract', json={
        'number_1': '2.0', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == 0.0


def test4_subtract_negative_mix(client):
    app.testing = True
    # test_subtract #4: check for negative number_1 and positive number_2
    response = client.post('/subtract', json={
        'number_1': '-2.0', 'number_2': '2'
    })
    data = response.get_json()
    assert data['result'] == -4.0


def test1_multiply_positive_mix(client):
    app.testing = True
    # test_multiply #1: check for 2 positive integers
    response = client.post('/multiply', json={
        'number_1': '10', 'number_2': '15.0'
    })
    data = response.get_json()
    assert data['result'] == 150.0


def test2_multiply_negative_float(client):
    app.testing = True
    # test_multiply #2: check for 2 negative floats
    response = client.post('/multiply', json={
        'number_1': '-10.0', 'number_2': '-25.0'
    })
    data = response.get_json()
    assert data['result'] == 250.0


def test3_multiply_mix(client):
    app.testing = True
    # test_multiply #3: check for 1 float 1 integer
    response = client.post('/multiply', json={
        'number_1': '2.0', 'number_2': '-2'
    })
    data = response.get_json()
    assert data['result'] == -4.0


def test4_multiply_zero(client):
    app.testing = True
    # test_multiply #4: multiplication with 0
    response = client.post('/multiply', json={
        'number_1': '-100.0', 'number_2': '0'
    })
    data = response.get_json()
    assert data['result'] == 0.0


def test1_divide_positive_mix(client):
    app.testing = True
    # test_divide #1: check for 2 positive integers
    response = client.post('/divide', json={
        'number_1': '15', 'number_2': '2.0'
    })
    data = response.get_json()
    assert data['result'] == 7.5


def test2_divide_negative_float(client):
    app.testing = True
    # test_divide #2: check for 2 negative floats
    response = client.post('/divide', json={
        'number_1': '-50.0', 'number_2': '-25.0'
    })
    data = response.get_json()
    assert data['result'] == 2.0


def test3_divide_mix(client):
    app.testing = True
    # test_divide #3: check for 1 float 1 integer number_1 < number_2
    response = client.post('/divide', json={
        'number_1': '5', 'number_2': '-9.0'
    })
    data = response.get_json()
    assert data['result'] == -0.5555555555555556


def test4_divide_negative_float(client):
    app.testing = True
    # test_divide #4: check for negative number_1 and positive number_2
    response = client.post('/divide', json={
        'number_1': '-100.0', 'number_2': '500'
    })
    data = response.get_json()
    assert data['result'] == -0.2
