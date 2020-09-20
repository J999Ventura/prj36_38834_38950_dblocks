from api.v1.routes import purchases_bp
from api.v1.models.purchases_model import Purchases
from api.v1.models.authentication.user_model import Users
from api.v1.authentication.utilities import current_user
from api.v1.authentication import auth_required
from api.v1.utils import get_products_list
from flask import Response, request
import json
from sqlalchemy import exc


@purchases.route('/buy', methods=['POST'])
@auth_required
def buy_products():
    try:
        json_data = request.get_json()
        products = json_data['products']
        Purchases.buy(products)
    except (ValueError, KeyError):
        # verificar se o status code e mesmo este
        return Response(json.dumps({'message': 'Invalid parameters'}), status=422, mimetype='application/json')

    try:
        user = current_user()
        product = Products.create_product(product_name, product_description, product_price, user.id,
                                          product_category_id, product_width, product_height)
        product_info = product.get_product_info()
        product_info['user_id'] = user.public_id
        return Response(json.dumps(product_info), status=201, mimetype='application/json')
    except (AttributeError, exc.SQLAlchemyError):
        return Response(json.dumps({'message': 'Unable to sell product'}), status=400,
                        mimetype='application/json')
