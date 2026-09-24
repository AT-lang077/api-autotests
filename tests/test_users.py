def test_get_users_structure(session, base_url):
    resp = session.get(f"{base_url}/users", timeout=10)
    assert resp.status_code == 200
    users = resp.json()
    assert isinstance(users, list) and len(users) > 0
    user = users[0]
    for field in ("id", "name", "username", "email", "address", "company"):
        assert field in user
    assert "@" in user["email"]
    assert "geo" in user["address"]


def test_get_comments_for_post(session, base_url):
    resp = session.get(f"{base_url}/posts/1/comments", timeout=10)
    assert resp.status_code == 200
    comments = resp.json()
    assert isinstance(comments, list) and len(comments) > 0
    for c in comments:
        assert c["postId"] == 1
        assert set(c.keys()) >= {"postId", "id", "name", "email", "body"}
        assert "@" in c["email"]


def test_get_todos_structure(session, base_url):
    resp = session.get(f"{base_url}/todos/1", timeout=10)
    assert resp.status_code == 200
    todo = resp.json()
    assert set(todo.keys()) == {"userId", "id", "title", "completed"}
    assert isinstance(todo["completed"], bool)
