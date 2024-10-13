from flask import Blueprint, render_template, request, url_for, redirect, current_app
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from app.users.models import User
from .services.user_services import create_user, validate_new_user

blueprint = Blueprint("users", __name__)


@blueprint.get("/register")
def get_register():
    return render_template("users/register.html")


@blueprint.post("/register")
def post_register():
    try:
        validate_new_user(request.form)
        login_user(create_user(request.form))

        return redirect(url_for("cookies.cookies"))
    except Exception as error_message:
        current_app.logger.info(f"Error creating a user: {error_message}")

        return render_template(
            "users/register.html",
            error=error_message or "An error occurred while creating the user",
        )


@blueprint.get("/login")
def get_login():
    return render_template("users/login.html")


@blueprint.post("/login")
def post_login():
    try:
        user = User.query.filter_by(email=request.form.get("email")).first()
        if not user:
            raise ValueError("User not found")
        elif not check_password_hash(user.password, request.form.get("password")):
            raise ValueError("Password is incorrect")

        login_user(user)
        return redirect(url_for("cookies.cookies"))

    except Exception as error_message:
        error = error_message or "An error occurred while creating the user"
        return render_template("users/login.html", error=error)


@blueprint.get("/logout")
def logout():
    logout_user()
    return redirect(url_for("simple_pages.index"))
