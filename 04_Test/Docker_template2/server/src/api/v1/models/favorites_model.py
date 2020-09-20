from api.v1.models import db
from datetime import datetime


class Favorites(db.Model):
    __tablename__ = "favorites"
    __table_args__ = {'schema': 'capture_adm'}

    user_id = db.Column(db.Integer, db.ForeignKey('capture_adm.users.id', ondelete='CASCADE'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('capture_adm.products.id', ondelete='CASCADE'), primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.now())
