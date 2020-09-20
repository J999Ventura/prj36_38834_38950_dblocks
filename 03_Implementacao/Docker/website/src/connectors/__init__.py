from ..models import User_model
import requests
import json

api_url="http://product-services:8080/api/v1";

def send_request(url, data):
    messageDict = '{"message": "Something went wrong!"}'
    response = requests.post(url, json=data)
    try:
        if response.status_code == 404 or response.status_code == 500:
            return json.loads(messageDict), None
        return response.json(), response.status_code
    except:
        return json.loads(messageDict), None

def get_request(url):
    messageDict = '{"message": "Something went wrong!"}'
    response = requests.get(url)
    try:
        if response.status_code == 404 or response.status_code == 500:
            return json.loads(messageDict), None
        return response.json(), response.status_code
    except:
        return json.loads(messageDict), None