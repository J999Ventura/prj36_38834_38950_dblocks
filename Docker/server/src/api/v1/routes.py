from flask import Blueprint,jsonify, request, make_response
from api.models import User
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


# Blueprint Declaration
v1 = Blueprint(
    'v1',
    __name__
)

# V1 Endpoints
@v1.route('/users', methods=['GET'])
def get_all_users():

    #verificar se tem acesso a api (ex: so pode ter acesso se for um admin ou se for um user com subscricao paga)
    #if not current_user.admin:
        #jsonify({'message' : 'Cannot access to api'})
    users = User.query.all()
    user_list = [user.serialize for user in users]
    return jsonify(user_list), 200

@v1.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'],method='sha256')
    new_user = User(public_id=str(uuid.uuid4()),name=data['name'],password=hashed_password,email=data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message' : 'New user created'})