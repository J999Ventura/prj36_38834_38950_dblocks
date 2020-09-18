from api.v1.models import db
from api.v1.models.categories_model import Categories
from api.v1.models.purchases_model import Purchases
from api.v1.models.favorites_model import Favorites
from datetime import datetime


class Products(db.Model):
    __tablename__ = "products"
    __table_args__ = {'schema': 'capture_adm'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    price = db.Column(db.Numeric, nullable =False)
    user_id = db.Column(db.Integer, db.ForeignKey('capture_adm.users.id', ondelete='CASCADE'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('capture_adm.categories.id', ondelete='CASCADE'), nullable=False)
    exclusivity = db.Column(db.Boolean, default=False, nullable=False)
    rating = db.Column(db.Numeric, default=0.0)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now())
    purchase = db.relationship('Purchases', lazy='select', backref=db.backref('product_purchase'))
    favorite = db.relationship('Favorites', lazy='select', backref=db.backref('product_favorite'))

    @classmethod
    def get_products_by_pagination(cls, page, per_page, category):
        if category:
            products_by_category = cls.query.join(Categories, cls.category_id == Categories.id) \
                .filter(Categories.name == category) \
                .order_by(cls.created_date.desc()).paginate(page, per_page, error_out=False).items
            return products_by_category

        return cls.query.order_by(cls.created_date.desc()).paginate(page, per_page, error_out=False).items

    @classmethod
    def get_products_top_rated(cls, limit=3):
        return cls.query.order_by(cls.rating.desc()).limit(limit)

    @staticmethod
    def create_product(product_name, product_description, product_price, product_user_id, product_category_id,
                       product_width, product_height):
        product = Products(name=product_name,
                           description=product_description,
                           price=product_price,
                           user_id=product_user_id,
                           category_id=product_category_id,
                           width=product_width,
                           height=product_height
                           )
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def remove_product(product_id, product_user_id):
        product = Products(id=product_id,
                           user_id=product_user_id
                           )
        db.session.delete(product)
        db.session.commit()

    def get_product_info(self):
        product_data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            'user_id': self.user_id,
            'category_id': self.category_id,
            'exclusivity': self.exclusivity,
            'rating': str(self.rating),
            'width': self.width,
            'height': self.height
        }
        return product_data
