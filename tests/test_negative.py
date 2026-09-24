def test_nonexistent_post_returns_404(session, base_url):
    resp = session.get(f"{base_url}/posts/99999", timeout=10)
    assert resp.status_code == 404


def test_invalid_id_type_returns_404(session, base_url):
    resp = session.get(f"{base_url}/posts/abc", timeout=10)
    assert resp.status_code == 404


def test_invalid_route_returns_404(session, base_url):
    resp = session.get(f"{base_url}/invalid-route-xyz", timeout=10)
    assert resp.status_code == 404


def test_response_time_is_reasonable(session, base_url):
    resp = session.get(f"{base_url}/posts", timeout=10)
    assert resp.status_code == 200
    assert resp.elapsed.total_seconds() < 2.5


def test_content_type_is_json(session, base_url):
    resp = session.get(f"{base_url}/posts/1", timeout=10)
    assert resp.status_code == 200
    assert "application/json" in resp.headers.get("Content-Type", "")
