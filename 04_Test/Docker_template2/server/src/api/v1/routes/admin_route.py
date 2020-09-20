from api.v1.routes import admin_bp
from api.v1.models.authentication.user_model import Users
from api.v1.utils import get_users_list
from flask import Response, request
from api.v1.routes.authentication_routes import guard
from api.v1.authentication.decorators import roles_required
import json
from sqlalchemy import exc


# criar utilizador
@admin_bp.route('/users/create', methods=['POST'])
@roles_required('Admin')
def create_user():
    try:
        json_data = request.get_json()
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        email = json_data['email']
        password = json_data['password']
        birth_date = json_data['birth_date']
    except (ValueError, KeyError):
        return Response(json.dumps({'message': 'Invalid parameters'}), status=422, mimetype='application/json')

    user = Users.lookup(email)  # verifica se o user ja existe em caso de nao existir retorna none
    if not user:
        new_user = None
        try:
            password = guard.hash_password(password)
            new_user = Users.create_user(first_name, last_name, email, password, birth_date, True)
            return Response(json.dumps({'message': 'User successfully created'}), status=201,
                            mimetype='application/json')
        except(ValueError, KeyError, exc.SQLAlchemyError):
            Users.remove_user(new_user)
            return Response(json.dumps({'message': 'Unable to create user'}), status=404, mimetype='application/json')
    return Response(json.dumps({'message': 'User already exists'}), status=202, mimetype='application/json')


# passar o user a admin

# alterar dados do user

# remover user

# numero de produtos vendidos por mes

# media de produtos vendidos por dia

# user com mais vendas

# obter todos os users
@admin_bp.route('/users', methods=['GET'])
@roles_required('Admin')
def get_all_users():
    try:
        users = Users.get_all_users()
        users_list = get_users_list(users)
        return Response(json.dumps(users_list), status=201, mimetype='application/json')
    except (ValueError, exc.SQLAlchemyError):
        return Response(json.dumps({'message': 'Fail to get users'}), status=400,
                        mimetype='application/json')
