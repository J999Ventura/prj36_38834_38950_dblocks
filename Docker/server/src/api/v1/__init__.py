from flask import Flask
from . import models,routes
from v1.models import db,migrate
from .commands import create_tables,create_users,create_roles
from .extensions import guard, mail
from os import environ

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #obter o nome do ambiente (dev, prod)
    environment = environ.get('FLASK_ENV') #carregar o ficheiro .env na maquina de prod antes de tudo set -a; source ~/my-project-dir/.env; set +a
    app.config.from_pyfile(environment + '.cfg') 
    app.config.from_pyfile('..\mail_config.cfg')

    #routes and models
    from .routes import User_route, Api_route
    routes.init_app(app)
    models.init_app(app)

    #praetorian and email
    from .models.User_model import Users
    guard.init_app(app,Users)
    mail.init_app(app)

    #commands
    app.cli.add_command(create_tables)
    app.cli.add_command(create_users)
    app.cli.add_command(create_roles)
    return app