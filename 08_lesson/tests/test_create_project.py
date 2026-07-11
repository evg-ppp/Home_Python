import uuid
import requests


BASE_URL = "https://ru.yougile.com/api-v2"


def test_create_project_positive(headers):

    title = f"Project_{uuid.uuid4()}"

    response = requests.post(
        f"{BASE_URL}/projects",
        headers=headers,
        json={
            "title": title
        }
    )

    assert response.status_code == 201

    body = response.json()

    assert "id" in body


def test_create_project_negative(headers):

    response = requests.post(
        f"{BASE_URL}/projects",
        headers=headers,
        json={
            "title": ""
        }
    )

    print(response.status_code)
    print(response.text)

    assert response.status_code == 400
