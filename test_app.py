from main import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"This is a secure app demo!" in response.data
