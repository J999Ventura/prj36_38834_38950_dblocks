from . import db
from ..extensions import guard
from .Role_model import Roles

class Users(db.Model):
 
    __tablename__ = "users"
    __table_args__ = {'schema':'capture_adm'}

    id = db.Column(db.Integer,primary_key=True)
    public_id = db.Column(db.String(50), unique = True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text)
    email = db.Column(db.String(80), unique = True, nullable = False)
    profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    birth_date = db.Column(db.DateTime, nullable = False)
    created_date = db.Column(db.DateTime)
    role_id = db.Column(db.Integer, db.ForeignKey('capture_adm.roles.id', ondelete='CASCADE'), nullable=False, default=3)
    is_active = db.Column(db.Boolean, default=False, server_default='false')
 
    @classmethod
    def lookup(cls,email):
        return cls.query.filter_by(email=email).one_or_none()

    @classmethod
    def identify(cls,public_id):
        return cls.query.filter_by(public_id=public_id).one_or_none()

    @property
    def rolenames(self):
        return Roles.query.filter_by(id=self.role_id).with_entities(Roles.name).first()
    
    @property
    def identity(self):
        return self.public_id

    def is_valid(self):
        return self.is_active
