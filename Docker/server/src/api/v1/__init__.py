from flask import Flask
from . import models,routes
from v1.models import db,migrate
from .commands import create_tables,create_users,create_roles
from os import environ

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #obter o nome do ambiente (dev, prod)
    environment = environ.get('FLASK_ENV')
    app.config.from_pyfile(environment + '.cfg') #alterar para ir buscar ao dicionario de acordo com a variavel em .env
    from .routes import User_route, Api_route
    routes.init_app(app)
    models.init_app(app)

    app.cli.add_command(create_tables)
    app.cli.add_command(create_users)
    app.cli.add_command(create_roles)
    return app