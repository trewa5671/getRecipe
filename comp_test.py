import pytest
import requests
from main import app
import asyncio

def test_root_get():
    response = requests.get("http://localhost/")
    assert response.status_code == 200
    data = response.json()
    assert 'title' in data.keys()
    assert isinstance(data['title'], str)

def test_list_get():
    response = requests.get("http://localhost/list/?q=1208")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['title'] == 'Beer Braised BBQ Pork Butt'