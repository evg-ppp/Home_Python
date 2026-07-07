import uuid


def test_update_project_positive(api, project_id):

    new_title = f"Updated_{uuid.uuid4()}"

    response = api.update_project(project_id, new_title)

    assert response.status_code == 200

    response = api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["title"] == new_title


def test_update_project_negative(api):

    response = api.update_project(
        str(uuid.uuid4()),
        "Test Project"
    )

    assert response.status_code == 404
