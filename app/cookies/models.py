from app.extensions.database import db, CRUDMixin


class Cookie(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Numeric(10, 2))
    picture_url = db.Column(db.String(255))
    cookie_orders = db.relationship("CookieOrder", backref="cookie", lazy=True)
