import json
import pytest
from app import app, db
from models import Comment

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_comment(client):
    res = client.post('/comments', json={"task_id": 1, "text": "Test comment"})
    assert res.status_code == 201
    data = res.get_json()
    assert data['text'] == "Test comment"

def test_update_comment(client):
    res = client.post('/comments', json={"task_id": 1, "text": "Old text"})
    comment_id = res.get_json()['id']
    res2 = client.put(f'/comments/{comment_id}', json={"text": "New text"})
    assert res2.status_code == 200
    assert res2.get_json()['text'] == "New text"

def test_delete_comment(client):
    res = client.post('/comments', json={"task_id": 1, "text": "Delete me"})
    comment_id = res.get_json()['id']
    res2 = client.delete(f'/comments/{comment_id}')
    assert res2.status_code == 200
    assert res2.get_json()['message'] == "Deleted successfully"