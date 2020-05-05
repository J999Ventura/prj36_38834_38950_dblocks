from api.v1.routes import v1_bp
from api.v1.models.user_model import Users
from flask import jsonify, request
from api.v1.authentication.decorators import auth_required, roles_required
from api.v1.authentication.utilities import current_user


@v1_bp.route('/open')
@auth_required
def open():
    user = current_user()
    print(user.email)
    return jsonify({'result': ''})


@v1_bp.route('/users', methods=['GET'])
def get_all_users():
    users = Users.query.all()
    if users:
        output = []

        for user in users:
            user_data = {}
            user_data['public_id'] = user.public_id
            user_data['first_name'] = user.first_name
            user_data['password'] = user.password
            user_data['email'] = user.email
            output.append(user_data)
        return jsonify({'users': output})
    return jsonify({'result': 'No users found'})



