from os import environ
from flask import Blueprint, jsonify, request
from ..orders.models import Order
from .services.serialize_orders import serialize_orders

blueprint = Blueprint("api", __name__)


@blueprint.get("/api/v1/orders")
def get_orders():
    if environ.get("API_KEY") == request.headers.get("X-API-KEY"):
        orders = Order.query.all()
        return jsonify(serialize_orders(orders))
    else:
        return jsonify({"error": "INvalid API key"}), 401
