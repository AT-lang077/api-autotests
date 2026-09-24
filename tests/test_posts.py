def test_get_posts_returns_list(session, base_url):
    resp = session.get(f"{base_url}/posts", timeout=10)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) == 100


def test_get_post_by_id_structure(session, base_url):
    resp = session.get(f"{base_url}/posts/1", timeout=10)
    assert resp.status_code == 200
    data = resp.json()
    assert set(data.keys()) == {"userId", "id", "title", "body"}
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str) and len(data["title"]) > 0
    assert isinstance(data["body"], str) and len(data["body"]) > 0


def test_create_post(session, base_url):
    payload = {"title": "autotest", "body": "hello", "userId": 1}
    resp = session.post(f"{base_url}/posts", json=payload, timeout=10)
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert "id" in data


def test_update_post_put(session, base_url):
    payload = {"id": 1, "title": "updated", "body": "updated body", "userId": 1}
    resp = session.put(f"{base_url}/posts/1", json=payload, timeout=10)
    assert resp.status_code == 200
    assert resp.json()["title"] == "updated"


def test_patch_post(session, base_url):
    resp = session.patch(f"{base_url}/posts/1", json={"title": "patched"}, timeout=10)
    assert resp.status_code == 200
    assert resp.json()["title"] == "patched"


def test_delete_post(session, base_url):
    resp = session.delete(f"{base_url}/posts/1", timeout=10)
    assert resp.status_code == 200
