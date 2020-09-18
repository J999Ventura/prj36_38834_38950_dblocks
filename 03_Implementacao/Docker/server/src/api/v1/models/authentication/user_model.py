from api.v1.models import db
from api.v1.models.authentication.role_model import Roles
import uuid
from datetime import datetime
from api.v1.utils import get_products_list


class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = {'schema': 'capture_adm'}

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    birth_date = db.Column(db.DateTime, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now())
    role_id = db.Column(db.Integer, db.ForeignKey('capture_adm.roles.id', ondelete='CASCADE'), nullable=False,
                        default=3)
    product_id = db.relationship('Products', lazy='select', backref=db.backref('user_product'))
    is_active = db.Column(db.Boolean, default=False, server_default='false')

    purchase = db.relationship('Purchases', lazy='select', backref=db.backref('user_purchase'))
    favorite = db.relationship('Favorites', lazy='select', backref=db.backref('user_favorite'))


    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email).one_or_none()

    @classmethod
    def identify(cls, public_id):
        return cls.query.filter_by(public_id=public_id).one_or_none()

    @property
    def rolenames(self):
        return Roles.query.filter_by(id=self.role_id).with_entities(Roles.name).first()

    @property
    def identity(self):
        return self.public_id

    def is_valid(self):
        return self.is_active

    @staticmethod
    def create_user(first_name, last_name, email, password, birth_date,is_active=False):
        user = Users(public_id=str(uuid.uuid4()),
                     first_name=first_name,
                     last_name=last_name,
                     password=password,
                     email=email,
                     birth_date=birth_date,
                     is_active=is_active
                     )
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def remove_user(cls, user):
        if user:
            user = cls.lookup(user.email)
            db.session.delete(user)
            db.session.commit()

    def active_user(self):
        self.is_active = True
        db.session.commit()

    def get_user_info(self):
        user_data = {
            'id': self.public_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'profile_image': self.profile_image,
            'email': self.email,
            'birth_date': str(self.birth_date),
            'role': self.rolenames[0],
            'products': get_products_list(self.product_id)
        }
        return user_data

    @classmethod
    def get_all_users(cls):
        return cls.query.all()
