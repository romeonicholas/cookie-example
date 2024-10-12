from app.extensions.database import db
from app.cookies.models import Cookie


def test_cookie_update(client):
    # updates cookie's properties
    cookie = Cookie(slug="chocolate-chip", name="Chocolate Chip", price="1.50")
    db.session.add(cookie)
    db.session.commit()

    cookie.name = "Peanut Butter"
    cookie.save()

    updated_cookie = Cookie.query.filter_by(slug="chocolate-chip").first()
    assert updated_cookie.name == "Peanut Butter"


def test_cookie_delete(client):
    # deletes a cookie
    cookie = Cookie(slug="butter", name="Butter", price="1.50")
    db.session.add(cookie)
    db.session.commit()

    cookie.delete()

    deleted_cookie = Cookie.query.filter_by(slug="butter").first()
    assert deleted_cookie is None
