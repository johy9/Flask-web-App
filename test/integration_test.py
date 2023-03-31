import requests

def test_integration():
    url = 'http://localhost:5000/'
    response = requests.get(url)
    assert response.status_code == 200
    assert 'Hello, World!' in response.text

