from api.v1.models import db
from datetime import datetime


class Purchases(db.Model):
    __tablename__ = "purchases"
    __table_args__ = {'schema': 'capture_adm'}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('capture_adm.users.id', ondelete='CASCADE'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('capture_adm.products.id', ondelete='CASCADE'), primary_key=True)
    price = db.Column(db.Numeric, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now())

    @staticmethod
    def buy(products):
        for product in products:
            purchase = Purchases(user_id=product.user_id, product_id=product.id,price=product.price)
            db.session.add(purchase)
            db.session.commit()
