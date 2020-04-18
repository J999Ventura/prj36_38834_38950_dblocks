import os
from os import environ

def init_app(app):

    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['PRAETORIAN_CONFIRMATION_SENDER'] = environ.get('PRAETORIAN_CONFIRMATION_SENDER')
    app.config['MAIL_USERNAME'] = environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = environ.get('MAIL_PASSWORD')

