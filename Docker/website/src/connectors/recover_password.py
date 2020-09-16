from . import User_model, send_request, api_url, json
from flask import jsonify

def setNewPassword(token, password):
    json = {"token": token, "password":password}
    response_json, response_status_code = send_request(api_url+"/auth/setnewpassword", json)

    if response_status_code == 200:
        return True

    return False