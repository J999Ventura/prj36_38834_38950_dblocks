from v1.routes import v1_bp
from ..models.User_model import Users
from ..models import guard,db
from flask import jsonify, request
from flask_praetorian import auth_required,roles_required,current_user

@v1_bp.route('/login' , methods = ['POST'])
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']

    user = guard.authenticate(email,password)
    token = guard.encode_jwt_token(user)

    return jsonify({'access_token' : token})

@v1_bp.route('/protected')
@roles_required('Admin')
def protected():
    return jsonify({'result' : 'You are in a Admin area!'})

@v1_bp.route('/open')
def open():
    return jsonify({'result':'Hello'})

@v1_bp.route('/active' ,methods = ['POST'])
def active():
    json_data = request.get_json()
    email = json_data['email']
    user = Users.query.filter_by(email=email).first()
    if user:
        user.is_active = True
        db.session.commit()
        return jsonify({'result':'User is now valid'})
    return jsonify({'result':'User does not exists'})

@v1_bp.route("/users",  methods=['GET'])
def get_all_users():
    users = [user for user in Users.query.all()]
    return "Users"