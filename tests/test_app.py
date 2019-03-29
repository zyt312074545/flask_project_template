from app.extensions import db


def test_create(client, app):
    response = client.post("/", json={"username": "a", "password": "a"})
    assert "_id" in response.get_json()

    with app.app_context():
        assert (
            db.engine.execute(
                "select * from test_model where username = 'a'"
            ).fetchone()
            is not None
        )


def test_update(client, app):
    response = client.put("/1", json={"username": "a"})
    assert response.get_json()["status"] is True

    with app.app_context():
        assert (
            db.engine.execute(
                "select * from test_model where username = 'a'"
            ).fetchone()
            is not None
        )


def test_get(client, app):
    response = client.get("/1")
    assert "test" == response.get_json()["username"]


def test_delete(client, app):
    response = client.delete("/1")
    assert response.get_json()["status"] is True

    with app.app_context():
        assert (
            db.engine.execute(
                "select * from test_model where username = 'test'"
            ).fetchone()
            is None
        )
