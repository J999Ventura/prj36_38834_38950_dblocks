from . import api_url, get_request
from flask import jsonify

def setConfirmEmail(token):
    response_json, response_status_code = get_request(api_url + "/auth/verify?token=" + token)
    if response_status_code == 201:
        return "Success! Your account is now verified", "success"
    return response_json['message'], "danger"