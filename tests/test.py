from fastapi.testclient import TestClient
from app.main import app
from typing import Final


class Settings:
    JIRA_CORE_URL: Final[
        str] = "https://raw.githubusercontent.com/ganievs/atlasian-release-tracking/feature/tests/data/jira-core.json"
    JIRA_CORE_REVOKED_URL: Final[
        str] = "https://raw.githubusercontent.com/ganievs/atlasian-release-tracking/feature/tests/data/jira-core-revoked.json"
    JIRA_SOFTWARE_URL: Final[
        str] = "https://raw.githubusercontent.com/ganievs/atlasian-release-tracking/main/data/jira-software.json"


client = TestClient(app)


def test_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_new_app():
    response = client.post("/",
                           json={
                               "product": "jira-core",
                               "url": Settings.JIRA_CORE_URL
                           })
    assert response.status_code == 201
    assert response.json() == {"status": "The new version 7.4.0 is available!"}


def test_same_app():
    response = client.post("/",
                           json={
                               "product": "jira-core",
                               "url": Settings.JIRA_CORE_URL
                           })
    assert response.status_code == 201
    assert response.json() == {
        "status": "Nothing changed current version is 7.4.0"
    }


def test_revoked_app():
    response = client.post("/",
                           json={
                               "product": "jira-core",
                               "url": Settings.JIRA_CORE_REVOKED_URL
                           })
    assert response.status_code == 201
    assert response.json() == {
        "status": "The release 7.4.0 is revoked! Current version is 7.3.8"
    }


def test_new_different_app():
    response = client.post("/",
                           json={
                               "product": "jira-software",
                               "url": Settings.JIRA_SOFTWARE_URL
                           })
    assert response.status_code == 201
    assert response.json() == {"status": "The new version 7.4.0 is available!"}
