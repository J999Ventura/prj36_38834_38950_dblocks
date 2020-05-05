from api.v1.routes import auth_bp
from api.v1.models.user_model import Users
from api.v1.models import db
from api.v1.routes.authentication_routes import guard
from flask import jsonify, request, Response
import json


@auth_bp.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']

    user_auth = guard.authenticate(email, password)
    token = guard.encode_jwt_token(user_auth)
    user = Users.lookup(email)
    if user:
        user_info = Users.user_info(user)
        data = {'access_token': token, 'user': user_info}
        # json.dumps(data)
        return Response(json.dumps(data), status=201, mimetype='application/json')
    return Response(json.dumps({'message': 'User not found'}), status=401, mimetype='application/json')
    # return jsonify({'access_token': token})


@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        json_data = request.get_json()
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        email = json_data['email']
        password = json_data['password']
        birth_date = json_data['birth_date']
    except:
        # verificar se o status code e mesmo este
        return Response(json.dumps({'message': 'Invalid parameters'}), status=203, mimetype='application/json')

    # validar os campos (tamanho etc)

    user = Users.lookup(email)  # verifica se o user ja existe em caso de nao existir retorna none
    if not user:
        # try:
        password = guard.hash_password(password)
        new_user = Users.create_user(first_name, last_name, email, password, birth_date)
        guard.send_registration_email(email, user=new_user)
        return Response(json.dumps({'message': 'User successfully registrated'}), status=201,
                        mimetype='application/json')
        # except:
        #    Users.remove_user(email)
        #    return Response(json.dumps({'message': 'Failed to create user'}), status=401,
        #                mimetype='application/json')

    return Response(json.dumps({'message': 'User already exists'}), status=202, mimetype='application/json')


@auth_bp.route('/verify', methods=['GET'])
def active():
    # testar receber como post
    token = request.args['token']
    user = guard.get_user_from_registration_token(token)
    if user:
        user.is_active = True
        db.session.commit()
        return jsonify({'result': 'User is now valid'})
    return jsonify({'result': 'User does not exists'})


@auth_bp.route('/resetpwd', methods=['POST'])
def reset_password():
    try:
        json_data = request.get_json()
        email = json_data['email']
    except:
        # verificar se o status code e mesmo este
        return Response(json.dumps({'message': 'Invalid parameters'}), status=203, mimetype='application/json')
    guard.send_reset_email(email)
    return Response(json.dumps({'message': 'Please check your email to reset the password'}), status=200,
                    mimetype='application/json')


@auth_bp.route('/completeresetpwd', methods=['GET'])
def complete_reset_password():
    token = request.args['token']
    print('TOKEN: ', token)
    user = guard.validate_reset_token(token)
    print('USER', user)
    # user.password = password

    print(token)
    return Response(json.dumps({'message': 'Password changed'}), status=200,
                    mimetype='application/json')
