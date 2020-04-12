from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_praetorian import Praetorian


db = SQLAlchemy()
migrate = Migrate()
guard = Praetorian()

def init_app(app):
    db.init_app(app)
    from .User_model import Users
    migrate.init_app(app, db)
    guard.init_app(app,Users)
    