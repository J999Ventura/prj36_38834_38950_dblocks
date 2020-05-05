from api.v1.models import db

class Products(db.Model):
 
    __tablename__ = "products"
    __table_args__ = {'schema':'capture_adm'}

    id = db.Column(db.Integer,primary_key=True)
    product_name = db.Column(db.String(100),unique=True, nullable = False)
    product_price = db.Column(db.Integer)