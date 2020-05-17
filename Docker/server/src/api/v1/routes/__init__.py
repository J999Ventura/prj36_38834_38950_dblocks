from flask import Blueprint
from flask_cors import CORS

v1_bp = Blueprint('v1', __name__)
auth_bp = Blueprint('auth', __name__)
admin_bp = Blueprint('admin', __name__)

def init_app(app):
    from api.v1.routes import user_route, api_route, product_route, admin_route
    from api.v1.routes.authentication_routes import user_auth_route
    url_prefix = '/api/v1'
    app.register_blueprint(v1_bp, url_prefix=url_prefix)
    app.register_blueprint(auth_bp, url_prefix=url_prefix + '/auth')
    app.register_blueprint(admin_bp, url_prefix=url_prefix + '/admin')
    CORS(app)
    