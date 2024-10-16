from flask import Flask
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager
from . import cookies, simple_pages, orders, api, users


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("app.config")

    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(cookies.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(orders.routes.blueprint)
    app.register_blueprint(api.routes.blueprint)
    app.register_blueprint(users.routes.blueprint)


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.init_app(app)
