from flask import Blueprint, render_template, request, current_app
from flask_login import login_required
from app.cookies.models import Cookie
from .services.create_order import create_order

blueprint = Blueprint("orders", __name__)


@blueprint.get("/orders/checkout")
@login_required
def get_checkout():
    cookies = Cookie.query.all()
    return render_template("orders/new.html", cookies=cookies)


@blueprint.post("/orders/checkout")
def post_checkout():
    try:
        cookies = Cookie.query.all()

        if not all(
            [
                request.form.get("name"),
                request.form.get("street"),
                request.form.get("city"),
                request.form.get("state"),
                request.form.get("zip"),
                request.form.get("country"),
            ]
        ):
            raise ValueError("Please fill out all address fields.")

        create_order(request.form, cookies)
        return render_template("orders/new.html", cookies=cookies)
    except Exception as error_message:
        error = (
            error_message
            or "An error occurred while processing your order. Please make sure to enter valid data."
        )
        current_app.logger.info(f"Error creating an order: {error}")

        return render_template(
            "orders/new.html",
            cookies=cookies,
            error=error,
        )
