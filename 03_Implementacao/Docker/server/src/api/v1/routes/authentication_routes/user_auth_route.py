from api.v1.routes import auth_bp
from api.v1.models.authentication.user_model import Users
from api.v1.authentication.decorators import auth_required
from api.v1.authentication.exceptions import MissingUserError, PraetorianError, AuthenticationError, ClaimCollisionError
from api.v1.routes.authentication_routes import guard
from api.v1.authentication.utilities import current_user
from flask import request, Response
import json
from sqlalchemy import exc


@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        json_data = request.get_json()
        email = json_data['email']
        password = json_data['password']
    except (ValueError, KeyError):
        # verificar se o status code e mesmo este
        return Response(json.dumps({'message': 'Invalid parameters'}), status=422, mimetype='application/json')

    try:
        user_auth = guard.authenticate(email, password)
        token = guard.encode_jwt_token(user_auth)
        user = Users.lookup(email)
        user_info = user.get_user_info()
        data = {'access_token': token, 'user': user_info}
        return Response(json.dumps(data), status=200, mimetype='application/json')
    except (
            ValueError, KeyError, MissingUserError, PraetorianError, AuthenticationError, ClaimCollisionError,
            exc.SQLAlchemyError):
        return Response(json.dumps({'message': 'Invalid email or password or email verification pending'}), status=401,
                        mimetype='application/json')

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        json_data = request.get_json()
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        email = json_data['email']
        password = json_data['password']
        birth_date = json_data['birth_date']
    except (ValueError, KeyError):
        # verificar se o status code e mesmo este
        return Response(json.dumps({'message': 'Invalid parameters'}), status=422, mimetype='application/json')

    # validar os campos (tamanho etc)

    user = Users.lookup(email)  # verifica se o user ja existe em caso de nao existir retorna none
    if not user:
        new_user = None
        #try:
        password = guard.hash_password(password)
        new_user = Users.create_user(first_name, last_name, email, password, birth_date)
        guard.send_registration_email(email, user=new_user)
        return Response(json.dumps({'message': 'User successfully registered'}), status=201,
                            mimetype='application/json')
        #except(ValueError, KeyError, PraetorianError, ClaimCollisionError, exc.SQLAlchemyError):
        #    Users.remove_user(new_user)
        #    return Response(json.dumps({'message': 'Unable to register user'}), status=204, mimetype='application/json')
    return Response(json.dumps({'message': 'User already exists'}), status=202, mimetype='application/json')


@auth_bp.route('/verify', methods=['GET'])
def active():
    try:
        token = request.args['token']
        user = guard.get_user_from_registration_token(token)
        user.active_user()
        return Response(json.dumps({'message': 'User is now valid'}), status=201, mimetype='application/json')
    except (ValueError, KeyError, PraetorianError):
        return Response(json.dumps({'message': 'Cannot verify the user'}), status=204, mimetype='application/json')


@auth_bp.route('/resetpwd', methods=['POST'])
def reset_password():
    try:
        json_data = request.get_json()
        email = json_data['email']
    except (ValueError, KeyError):
        # verificar se o status code e mesmo este
        return Response(json.dumps({'message': 'Invalid parameters'}), status=422, mimetype='application/json')
    try:
        guard.send_reset_email(email)
        return Response(json.dumps({'message': 'Please check your email to change the password'}), status=200,
                        mimetype='application/json')
    except (ValueError, KeyError, MissingUserError, PraetorianError):
        return Response(json.dumps({'message': 'Fail to send reset password email'}), status=200,
                        mimetype='application/json')


@auth_bp.route('/resendemail', methods=['POST'])
def resend_email():
    try:
        json_data = request.get_json()
        email = json_data['email']
    except (ValueError, KeyError):
        # verificar se o status code e mesmo este
        return Response(json.dumps({'message': 'Invalid parameters'}), status=422, mimetype='application/json')
    try:
        guard.send_registration_email(email)
        return Response(json.dumps({'message': 'Please check your email to verify the account'}), status=200,
                        mimetype='application/json')
    except(ValueError, KeyError, PraetorianError, ClaimCollisionError):
        return Response(json.dumps({'message': 'Fail to send verification email'}), status=400,
                        mimetype='application/json')


@auth_bp.route('/completeresetpwd', methods=['POST'])
def complete_reset_password():
    try:
        json_data = request.get_json()
        password = guard.hash_password(json_data['password'])
        token = request.args['token']
    except (ValueError, KeyError):
        # verificar se o status code e mesmo este
        return Response(json.dumps({'message': 'Invalid parameters'}), status=422, mimetype='application/json')
    try:
        user = guard.validate_reset_token(token)
        user.password = password
        return Response(json.dumps({'message': 'Password changed'}), status=200,
                        mimetype='application/json')
    except (ValueError, KeyError, PraetorianError):
        return Response(json.dumps({'message': 'Fail to change password'}), status=400,
                        mimetype='application/json')


@auth_bp.route('/currentuser', methods=['GET'])
@auth_required
def get_current_user():
    try:
        user = current_user()
        user_info = user.get_user_info()
        data = {'user': user_info}
        return Response(json.dumps(data), status=201, mimetype='application/json')
    except (ValueError, KeyError, PraetorianError):
        return Response(json.dumps({'message': 'User not found'}), status=401, mimetype='application/json')
