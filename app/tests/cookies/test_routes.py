from app.cookies.models import Cookie


def test_cookies_renders_cookies(client):
    # page loads and renders cookies
    new_cookie = Cookie(slug="chocolate-chip", name="Chocolate Chip", price="1.50")
    new_cookie.save()

    response = client.get("/cookies")

    assert b"Chocolate Chip" in response.data


def test_cookies_slug_renders_cookie(client):
    # page loads and renders correct cookie
    new_cookie = Cookie(slug="peanut-butter", name="Peanut Butter", price="1.50")
    new_cookie.save()

    response = client.get("/cookies/peanut-butter")

    assert b"Peanut Butter" in response.data
