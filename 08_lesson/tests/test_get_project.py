import uuid


def test_get_project_positive(api, project_id):

    response = api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative(api):

    response = api.get_project(str(uuid.uuid4()))

    assert response.status_code == 404
