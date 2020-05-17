from api.v1.routes import admin_bp
from api.v1.models.user_model import Users
from api.v1.routes.utils import get_users_list
from flask import Response
import json


# criar utilizador

# passar o user a admin

# alterar dados do user

# remover user

# numero de produtos vendidos por mes

# media de produtos vendidos por dia

# user com mais vendas

# obter todos os users
@admin_bp.route('/users', methods=['GET'])
def get_all_users():
    users = Users.get_all_users()
    users_list = {}
    if users:
        users_list = get_users_list(users)
    return Response(json.dumps(users_list), status=201, mimetype='application/json')
