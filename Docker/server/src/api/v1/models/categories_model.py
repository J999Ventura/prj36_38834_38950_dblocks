from api.v1.models import db


class Categories(db.Model):
    __tablename__ = "categories"
    __table_args__ = {'schema': 'capture_adm'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    products = db.relationship('Products', lazy='select', backref=db.backref('category_product'))
