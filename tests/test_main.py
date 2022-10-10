from app.main import app

client = TestClient(app)


def test_new_app():
    response = client.post(
        "/",
        json={"url": ""}
    )
    assert response.status_code == 201
    assert response.json() == {
        "status": "The new version 7.4.0 is available!"
    }

def test_same_app():
    response = client.post(
        "/",
        json={"url": ""}
    )
    )
    assert response.status_code == 201
    assert response.json() == {
        "status": "Nothing changed current version is 7.4.0"
    }


def test_revoked_app():
    response = client.post(
        "/",
                json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},

        json={"url": ""}
    )
    assert response.status_code == 201
    assert response.json() == {
        "status": "The release 7.4.0 is revoked! Current version version is 7.3.0!"
    }

def test_new_app():
    response = client.post(
        "/",
        json={"url": ""}
    )
    assert response.status_code == 201
    assert response.json() == {
        "status": "The new version 7.4.0 is available!"
    }

def test_new_different_app():
    response = client.post(
        "/",
        json={"url": ""}
    )
    assert response.status_code == 201
    assert response.json() == {
        "status": "The new version 7.4.0 is available!"
    }

