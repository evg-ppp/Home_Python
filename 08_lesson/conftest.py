import pytest
import requests

from project_api import ProjectAPI
from secret import LOGIN, PASSWORD


BASE_URL = "https://ru.yougile.com/api-v2"


def get_company_id():


def get_company_id():
    response = requests.post(
        f"{BASE_URL}/auth/companies",
        json={
            "login": LOGIN,
            "password": PASSWORD,
            "name": ""
        }
    )
    response.raise_for_status()
    return response.json()["content"][0]["id"]


def get_api_key():
    company_id = get_company_id()

    response = requests.post(
        f"{BASE_URL}/auth/keys",
        json={
            "login": LOGIN,
            "password": PASSWORD,
            "companyId": company_id
        }
    )
    response.raise_for_status()
    return response.json()["key"]


@pytest.fixture(scope="session")
def headers():
    token = get_api_key()

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="session")
def api():
    token = get_api_key()
    return ProjectAPI(token)


@pytest.fixture
def project_id(headers):
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=headers,
        json={
            "title": "Project for test"
        }
    )

    return response.json()["id"]
