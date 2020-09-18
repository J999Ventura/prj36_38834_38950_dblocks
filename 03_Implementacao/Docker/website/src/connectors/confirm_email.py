from . import User_model, send_request, api_url, json
from flask import jsonify

def setConfirmEmail(token):
    json = {"token": token}
    response_json, response_status_code = send_request(api_url+"/auth/confirmemail", json)

    if response_status_code == 200:
        return True

    return False