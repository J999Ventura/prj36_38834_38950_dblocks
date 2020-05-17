from os import environ

def init_app(app):

    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['PRAETORIAN_CONFIRMATION_SENDER'] = environ.get('PRAETORIAN_CONFIRMATION_SENDER')
    app.config['MAIL_USERNAME'] = environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = environ.get('MAIL_PASSWORD')
    app.config['MAIL_SERVER'] = environ.get('MAIL_SERVER')
    app.config['MAIL_PORT'] = environ.get('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = environ.get('MAIL_USE_TLS')
    app.config['PRAETORIAN_CONFIRMATION_SUBJECT'] = environ.get('PRAETORIAN_CONFIRMATION_SUBJECT')
    app.config['PRAETORIAN_CONFIRMATION_URI'] = environ.get('PRAETORIAN_CONFIRMATION_URI')
    app.config['PRAETORIAN_RESET_SENDER'] = environ.get('PRAETORIAN_RESET_SENDER')
    app.config['PRAETORIAN_RESET_URI'] = environ.get('PRAETORIAN_RESET_URI')
    app.config['JWT_ACCESS_LIFESPAN'] = environ.get('JWT_ACCESS_LIFESPAN')
    app.config['JWT_REFRESH_LIFESPAN'] = environ.get('JWT_REFRESH_LIFESPAN')
    app.config['GOOGLE_APPLICATION_CREDENTIALS'] = environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')