from fastapi.testclient import TestClient
from ...main import app

client = TestClient(app)


def test_get_repos() -> None:
    response = client.get("repos/")
    assert response.status_code == 200

    content = response.json()
    assert content == [{"repo": "ex"}]


def test_get_no_repos() -> None:
    response = client.get("repos/")
    assert response.status_code == 200

    content = response.json()
    assert content == []


def test_create_repo() -> None:
    response = client.post("repos/")
    assert response.status_code == 201

    content = response.json()
    assert content == None


def test_unable_create_repo() -> None:
    response = client.post("repos/")
    assert response.status_code == 400

    content = response.json()
    assert content == None


def test_delete_repo() -> None:
    response = client.delete("repos/1")
    assert response.status_code == 204

    content = response.json()
    assert content == None


def test_unable_to_delete_repo() -> None:
    response = client.delete("repos/1")
    assert response.status_code == 400

    content = response.json()
    assert content == None
