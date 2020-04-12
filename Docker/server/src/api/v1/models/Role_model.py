from . import db

class Roles(db.Model):

    __tablename__ = "roles"
    __table_args__ = {'schema':'capture_adm'}

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True, nullable = False)
    description = db.Column(db.String(100))

    users = db.relationship('Users', lazy='select',backref=db.backref('user'))
    #backref=db.backref('user', lazy='joined'))