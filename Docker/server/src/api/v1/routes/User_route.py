from api.v1.routes import users_bp
from flask import jsonify
from api.v1.authentication.decorators import auth_required
from api.v1.authentication.utilities import current_user
from api.v1.models.authentication.user_model import Users
import json
from flask import Response


# produtos por utilizador
@users_bp.route('/products/<string:public_id>', methods=['GET'])
@users_bp.route('/products/<string:public_id>/<int:product_id>', methods=['GET'])
def get_user_products(public_id, product_id=0):
    try:
        user = Users.identify(public_id)
        user_data = user.get_user_info()
        products = user_data['products']
        if product_id != 0:
            product = [p for p in products if p["id"] == product_id]
            return Response(json.dumps({'products': product}), status=200, mimetype='application/json')
        return Response(json.dumps({'products': products}), status=200, mimetype='application/json')
    except (AttributeError, ValueError):
        return Response(json.dumps({'products': []}), status=200, mimetype='application/json')

