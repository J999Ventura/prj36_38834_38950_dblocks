from flask import Blueprint
from flask_cors import CORS

v1_bp = Blueprint('v1', __name__)
auth_bp = Blueprint('auth', __name__)
users_bp = Blueprint('users', __name__)
products_bp = Blueprint('products', __name__)
admin_bp = Blueprint('admin', __name__)
purchases_bp = Blueprint('purchases', __name__)

def init_app(app):
    from api.v1.routes import user_route, product_route, admin_route, category_route
    from api.v1.routes.authentication_routes import user_auth_route
    url_prefix = '/api/v1'
    app.register_blueprint(v1_bp, url_prefix=url_prefix)
    app.register_blueprint(auth_bp, url_prefix=url_prefix + '/auth')
    app.register_blueprint(users_bp, url_prefix=url_prefix + '/users')
    app.register_blueprint(products_bp, url_prefix=url_prefix + '/products')
    app.register_blueprint(admin_bp, url_prefix=url_prefix + '/admin')
    app.register_blueprint(purchases_bp, url_prefix=url_prefix + '/purchases')
    CORS(app)
