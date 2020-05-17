from flask import Flask
from api.v1 import models, routes
from api.v1.routes.authentication_routes import guard, mail
from api import config


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    models.init_app(app)
    routes.init_app(app)

    # praetorian and email
    from api.v1.models.user_model import Users
    guard.init_app(app, Users)
    mail.init_app(app)

    return app
