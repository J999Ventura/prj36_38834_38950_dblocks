from api.v1.routes import v1_bp
from api.v1.models.user_model import Users
from api.v1.routes.utils import get_products_list
from flask import jsonify, request
from api.v1.authentication.decorators import auth_required, roles_required
from api.v1.authentication.utilities import current_user
from flask import Response
import json


@v1_bp.route('/open')
@auth_required
def open():
    user = current_user()
    print(user.email)
    return jsonify({'result': ''})



@v1_bp.route('/user/products', methods=['POST'])
def get_user_products():
    json_data = request.get_json()
    public_id = json_data['public_id']
    # obter o current user
    #user = current_user()
    # comparar os public_id
    #if user:

    #if user.public_id == public_id:
    # retornar os produtos do utilizador com o public_id
    user_products = get_products_list(Users.get_products(public_id))

    return Response(json.dumps(user_products), status=201, mimetype='application/json')
