import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client

def test_login_page_renders(client):
    rv = client.get('/login')
    assert rv.status_code == 200
    assert b'HR Executive Login' in rv.data

def test_unauthorized_access(client):
    rv = client.get('/')
    assert rv.status_code == 302
    assert b'/login' in rv.data
