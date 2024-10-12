def test_index_success(client):
    # Page loads
    response = client.get("/")
    assert response.status_code == 200


def test_index_content(client):
    # Returns welcome text
    response = client.get("/")
    assert b"Welcome to my cookie shop!" in response.data


def test_about_success(client):
    # Page loads
    response = client.get("/about")
    assert response.status_code == 200


def test_about_me_redirect(client):
    # Redirects to /about
    response = client.get("/about-me")
    assert response.status_code == 302
    assert "about" in response.headers["Location"]
    assert "about-me" not in response.headers["Location"]
