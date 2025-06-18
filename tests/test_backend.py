import os
import pytest
from backend.app import app, init_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Login Method' in response.data

def test_login_vuln_fail(client):
    response = client.post('/login-vuln', data={'username': 'fake', 'password': 'fake'})
    assert b'Login failed (vulnerable)' in response.data

def test_login_safe_fail(client):
    response = client.post('/login-safe', data={'username': 'fake', 'password': 'fake'})
    assert b'Login failed (secure)' in response.data

def test_login_vuln_sql_injection(client):
    response = client.post('/login-vuln', data={
        'username': "' OR '1'='1' --",
        'password': 'x'
    }, follow_redirects=False)
    assert response.status_code == 302
    assert response.headers['Location'].endswith('/dashboard')
