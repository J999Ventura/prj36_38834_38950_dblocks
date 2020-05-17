from api.v1.routes import v1_bp
from api.v1.models.products_model import Products
from api.v1.routes.utils import get_products_list
from flask import Response
import json


@v1_bp.route('/products/<int:page>', methods=['GET'])
def view(page=1):
    per_page = 12
    products = Products.get_products_by_pagination(page, per_page)
    products_list = {}
    if products:
        products_list = get_products_list(products)

    return Response(json.dumps(products_list), status=201, mimetype='application/json')
