from api.v1.models import db
from api.v1.models.categories_model import Categories


class Products(db.Model):
    __tablename__ = "products"
    __table_args__ = {'schema': 'capture_adm'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    price = db.Column(db.Numeric)
    user_id = db.Column(db.Integer, db.ForeignKey('capture_adm.users.id', ondelete='CASCADE'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('capture_adm.categories.id', ondelete='CASCADE'), nullable=False)
    exclusivity = db.Column(db.Boolean, default=False, nullable=False)
    rating = db.Column(db.Numeric)
    created_date = db.Column(db.DateTime)

    @classmethod
    def get_products_by_pagination(cls, page, per_page):
        try:
            return cls.query.order_by(cls.created_date.desc()).paginate(page, per_page, error_out=False).items
        except:
            return None

    def get_product_info(self):
        product_data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            'user_id': self.user_id,
            'category_id': self.category_id,
            'exclusivity': self.exclusivity,
            'rating': str(self.rating)
        }
        return product_data




