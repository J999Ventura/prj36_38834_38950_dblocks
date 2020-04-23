from v1.routes import v1_bp
from ..models.User_model import Users
from ..models import db
from ..extensions import guard
from flask import jsonify, request
from flask_praetorian import auth_required,roles_required,current_user
import uuid
import datetime
from os import environ

@v1_bp.route('/login' , methods = ['POST'])
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']

    user = guard.authenticate(email,password)
    token = guard.encode_jwt_token(user)
    #enviar tambem o user

    return jsonify({'access_token' : token})

@v1_bp.route('/register',methods = ['POST'])
def register():
    json_data = request.get_json()
    first_name = json_data['first_name']
    last_name = json_data['last_name']
    email = json_data['email']
    password = json_data['password']
    birth_date = json_data['birth_date']

    #validar os campos (tamanho etc)

    user = Users.lookup(email) #verifica se o user ja existe em caso de nao existir retorna none
    if not user:
        new_user = Users(public_id=str(uuid.uuid4()),
                    first_name=first_name,
                    last_name = last_name,
                    password=guard.hash_password(password),
                    email=email,
                    birth_date = birth_date,
                    created_date = datetime.datetime.now(),
                    role_id = 3
                    ) 
        guard.send_registration_email(email,user=new_user)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'successfully sent registration email to user {}'.format(new_user.first_name)})

    return jsonify({'message': 'User already exists'})


@v1_bp.route('/protected')
@roles_required('Admin')
def protected():
    return jsonify({'result' : 'You are in a Admin area!'})

@v1_bp.route('/open')
def open():
    return jsonify({'result':'Hello'})

@v1_bp.route('/users', methods=['GET'])
def get_all_users():
    users = Users.query.all()
    if users:
        output = []

        for user in users:
            user_data = {}
            user_data['public_id']  = user.public_id
            user_data['first_name']  = user.first_name
            user_data['password']  = user.password
            user_data['email']  = user.email
            output.append(user_data)
        return jsonify({'users': output})
    return jsonify({'result' : 'No users found'})

@v1_bp.route('/verify', methods=['GET'])
def active():
    #testar receber como post
    token = request.args['token']
    user = guard.get_user_from_registration_token(token)
    if user:
        user.is_active = True
        db.session.commit()
        return jsonify({'result':'User is now valid'})
    return jsonify({'result':'User does not exists'})