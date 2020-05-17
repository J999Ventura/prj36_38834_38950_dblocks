from api.v1.models import db
from api.v1.models.role_model import Roles
from api.v1.models.products_model import Products
import uuid
import datetime


class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = {'schema': 'capture_adm'}

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text)
    email = db.Column(db.String(80), unique=True, nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    birth_date = db.Column(db.DateTime, nullable=False)
    created_date = db.Column(db.DateTime)
    role_id = db.Column(db.Integer, db.ForeignKey('capture_adm.roles.id', ondelete='CASCADE'), nullable=False,
                        default=3)
    product_id = db.relationship('Products', lazy='select', backref=db.backref('user_product'))
    is_active = db.Column(db.Boolean, default=False, server_default='false')

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

    @staticmethod
    def create_user(first_name, last_name, email, password, birth_date):
        try:
            user = Users(public_id=str(uuid.uuid4()),
                         first_name=first_name,
                         last_name=last_name,
                         password=password,
                         email=email,
                         birth_date=birth_date,
                         created_date=datetime.datetime.now()
                         )
            db.session.add(user)
            db.session.commit()
            return user
        except:
            return None

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
            'role': self.rolenames[0]}
        return user_data

    @classmethod
    def get_all_users(cls):
        try:
            return cls.query.all()
        except:
            return None

    @classmethod
    def get_products(cls, public_id):
        user = cls.identify(public_id)
        products = {}
        if user:
            products = Products.query.filter_by(user_id=user.id).all()
        return products
