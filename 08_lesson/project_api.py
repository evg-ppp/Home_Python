import requests
from config import BASE_URL


class ProjectAPI:

    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        return requests.post(
            f"{BASE_URL}/projects",
            headers=self.headers,
            json={
                "title": title
            }
        )

    def update_project(self, project_id, title):
        return requests.put(
            f"{BASE_URL}/projects/{project_id}",
            headers=self.headers,
            json={
                "title": title
            }
        )

    def get_project(self, project_id):
        return requests.get(
            f"{BASE_URL}/projects/{project_id}",
            headers=self.headers
        )