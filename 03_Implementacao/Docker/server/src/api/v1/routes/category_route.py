from api.v1.routes import v1_bp
from api.v1.models.categories_model import Categories
from flask import Response
import json
from sqlalchemy import exc
from api.v1.utils import get_categories_list


@v1_bp.route("/categories", methods=['GET'])
def get_categories():
    try:
        categories = Categories.get_all_categories()
        categories_list = get_categories_list(categories)
        return Response(json.dumps(categories_list), status=201, mimetype='application/json')
    except (ValueError, KeyError, exc.SQLAlchemyError):
        return Response(json.dumps({'message': 'Fail to get categories'}), status=400,
                        mimetype='application/json')
