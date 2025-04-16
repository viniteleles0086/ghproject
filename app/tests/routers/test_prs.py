from fastapi.testclient import TestClient
from ...main import app

client = TestClient(app)



def test_get_prs_without_quantity_query_param() -> None:
    response = client.get("/repos/1/open-prs")
    assert response.status_code == 200

    content = response.json()
    assert content == [{"pr": "prex"}]


def test_get_prs_with_quantity_query_param() -> None:
    response = client.get("/repos/1/open-prs?qty=10")
    assert response.status_code == 200

    content = response.json()
    assert content == [{"pr": "prex"}]


def test_get_prs_with_an_invalid_quantity_query_param() -> None:
    response = client.get("/repos/1/open-prs?qty=some_string")
    assert response.status_code == 400

    content = response.json()
    assert content == {'message': 'Quantity needs to be a number'}
