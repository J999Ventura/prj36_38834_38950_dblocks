from flask import Blueprint
from flask_cors import CORS, cross_origin

v1_bp = Blueprint('v1', __name__)

def init_app(app):
    app.register_blueprint(v1_bp,url_prefix='/api/v1')
    CORS(app)
    