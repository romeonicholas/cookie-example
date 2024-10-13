from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from app.users.models import User

blueprint = Blueprint("users", __name__)


@blueprint.get("/register")
def get_register():
    return render_template("users/register.html")


@blueprint.post("/register")
def post_register():
    try:
        if request.form.get("password") != request.form.get("password_confirmation"):
            raise ValueError("Passwords do not match")
        elif User.query.filter_by(email=request.form.get("email")).first():
            raise ValueError("User already exists")

        user = User(
            email=request.form.get("email"),
            password=generate_password_hash(request.form.get("password")),
        )
        user.save()

        return redirect(url_for("cookies.cookies"))
    except Exception as error_message:
        error = error_message or "An error occurred while creating the user"
        return render_template("users/register.html", error=error)


@blueprint.get("/login")
def get_login():
    return render_template("users/login.html")


@blueprint.post("/login")
def post_login():
    return "User logged in"


@blueprint.get("/logout")
def get_logout():
    return "User logged out"
