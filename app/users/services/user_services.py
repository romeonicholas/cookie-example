from werkzeug.security import generate_password_hash
from app.users.models import User


def validate_new_user(form_data) -> None:
    if form_data.get("password") != form_data.get("password_confirmation"):
        raise ValueError("Passwords do not match")
    if User.query.filter_by(email=form_data.get("email")).first():
        raise ValueError("User already exists")


def create_user(form_data) -> User:
    user = User(
        email=form_data.get("email"),
        password=generate_password_hash(form_data.get("password")),
    )
    user.save()

    return user
