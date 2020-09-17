from api.v1.routes import products_bp
from api.v1.models.products_model import Products
from api.v1.models.authentication.user_model import Users
from api.v1.authentication.utilities import current_user
from api.v1.authentication import auth_required
from api.v1.utils import get_products_list
from flask import Response, request
import json
from sqlalchemy import exc


# 4 produtos mais vendidos

# 3 produtos com maior rating
@products_bp.route('/top_rated', methods=['POST'])
def products_top_rated():
    # e um post porque mais tarde se quisermos obter em vez de 3 por exemplo 10 basta enviar como parametro no body
    # e nao pode ser get porque nao se pode dar a oportunidade ao utilizador da app de obter os top rated
    # que ele quiser
    try:
        json_data = request.get_json()
        limit = int(json_data['limit'])
    except (ValueError, KeyError):
        # verificar se o status code e mesmo este
        return Response(json.dumps({'message': 'Invalid parameters'}), status=422, mimetype='application/json')
    try:
        products = Products.get_products_top_rated(limit)
        products_list = get_products_list(products)
        return Response(json.dumps({'products': products_list}), status=201, mimetype='application/json')
    except (ValueError, KeyError ,exc.SQLAlchemyError):
        return Response(json.dumps({'products': []}), status=200, mimetype='application/json')


# 8 produtos premium

# remover produto
@products_bp.route('/remove', methods=['POST'])
@auth_required
def product_remove():
    try:
        json_data = request.get_json()
        product_id = json_data['product_id']
    except (ValueError, KeyError):
        return Response(json.dumps({'message': 'Invalid parameters'}), status=422, mimetype='application/json')
    try:
        user = current_user()
        Products.remove_product(user, product_id)
        return Response(json.dumps(product_info), status=201, mimetype='application/json')
    except (AttributeError, exc.SQLAlchemyError):
        return Response(json.dumps({'message': 'Unable to remove product'}), status=400,
                        mimetype='application/json')

# inserir produto
@products_bp.route('/sell', methods=['POST'])
@auth_required
def product_sell():
    try:
        json_data = request.get_json()
        product_name = json_data['product_name']
        product_description = json_data['product_description']
        product_price = float(json_data['product_price'])
        product_category_id = int(json_data['product_category_id'])
        product_width = json_data['product_width']
        product_height = json_data['product_height']
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


# produtos por pagina
# produtos por categoria
@products_bp.route('/new_arrivals', methods=['GET'])
@products_bp.route('/<int:page>', methods=['GET'])
@products_bp.route('/<string:category>/<int:page>', methods=['GET'])
def products_last_by_page(page=1, category=None):
    per_page = 12
    try:
        products = Products.get_products_by_pagination(page, per_page, category)
        products_list = get_products_list(products)
        return Response(json.dumps({'products': products_list}), status=200, mimetype='application/json')
    except (ValueError, KeyError, exc.SQLAlchemyError):
        return Response(json.dumps({'message': 'Fail to get products'}), status=400,
                        mimetype='application/json')
