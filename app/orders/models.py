from datetime import datetime, timezone
from app.extensions.database import db, CRUDMixin


class CookieOrder(db.Model, CRUDMixin):
    cookie_id = db.Column(db.Integer, db.ForeignKey("cookie.id"), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), primary_key=True)
    number_of_cookies = db.Column(db.Integer)


class Order(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    address = db.relationship("Address", backref="order", uselist=False, lazy=True)
    cookie_orders = db.relationship("CookieOrder", backref="order", lazy=True)


class Address(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    street = db.Column(db.String(80))
    city = db.Column(db.String(80))
    state = db.Column(db.String(80))
    zip = db.Column(db.String(80))
    country = db.Column(db.String(80))
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
