from . import User_model, send_request, api_url, json, get_request
from flask import jsonify

def login(email, password):
    data = {"email": email, "password": password}
    response_json, response_status_code = send_request(api_url+"/auth/login", data)
    
    if response_status_code == 201:
        user = response_json['user']
        return User_model.User(id=user['id'], fname=user['first_name'], lname=user['last_name'], email=user['email'], role=user['role'], bdate=user['birth_date'], image=user['profile_image'], token=response_json['access_token'])
    #return User_model.User(id=2, fname="Joao", lname="Ventura", email="devil_man_13@hotmail.com", role=0, bdate="02/02/2020", image="2/8569", token="321CEFG4r5fFVWe")


def register(fname, lname, email, password, bdate):
    json = {"first_name": fname, "last_name": lname, "email": email, "password": password, "birth_date": bdate}
    response_json, response_status_code = send_request(api_url+"/auth/register", json)

    if response_status_code == 201:
        return "Success! Check your email to validate your account", "success"

    return response_json['message'], "danger"


def recoverPassword(email):
    json = {"email": email}
    response_json, response_status_code = send_request(api_url+"/auth/resetpwd", json)

    if response_status_code == 200:
        return "Success! Check your email to change your password", "success"

    return response_json['message'], "danger"


def resendEmail(email):
    json = {"email": email}
    response_json, response_status_code = send_request(api_url+"/auth/resendemail", json)

    if response_status_code == 200:
        return "Success! Check your email to validate your account", "success"

    return response_json['message'], "danger"


def sellProduct(product_name, product_description, product_price, product_user_id, product_category_id):
    json = {"product_name": product_name, "product_description": product_description, "product_price": product_price,
            "product_user_id": product_user_id, "product_category_id": product_category_id}
    response_json, response_status_code = send_request(api_url+"/products/sell", json)
    product_id = "3"
    if response_status_code == 201:
        return "Success! Your product was successfully uploaded", "success", product_id

    return response_json['message'], "danger", "0"
    #return "Success! Your product was successfully uploaded", "success", "3"


def getCategories():
    response_json, response_status_code = get_request(api_url+"/categories")
    if response_status_code == 200 or response_status_code == 201:
        return response_json['categories']
    return response_json['message'], "danger"
    #response_json=json.loads('{"categories":[{"id":"10", "name": "Nature"},{"id":"11", "name": "City"},{"id":"12", "name": "Vintage"}]}')
    #response_json = response_json['categories']
    #return response_json

def getProductDetails(user_owner_id, product_id):
     #response_json, response_status_code = get_request(api_url+"/product/"+user_owner_id+"/"+product_id+"/details")
     #if response_status_code == 200:
     #   return response_json['products']

     #return response_json['message'], "danger"
    return {"id": product_id, "name": "Naturescape","description": "My photo about nature","price": "20","user_id": user_owner_id,"user_name":"Heral","category_id": 1,"exclusivity": "false","rating": "None"}


def getNewProductsArrival():
     #response_json, response_status_code = get_request(api_url+"/products/new_arrivals")
     #if response_status_code == 200:
     #   return response_json['products']
     #return response_json['message'], "danger"
    return [
            {
                "id": 13,
                "name": "Naturescape",
                "description": "My photo about nature",
                "price": "20",
                "user_id": 3,
                "category_id": 1,
                "exclusivity": "false",
                "rating": "None"
            },
            {
                "id": 22,
                "name": "Urban city",
                "description": "My photo about a city",
                "price": "30",
                "user_id": 3,
                "category_id": 2,
                "exclusivity": "true",
                "rating": "None"
            },
            {
                "id": 6,
                "name": "Human Eyes",
                "description": "My photo about a girls eyes",
                "price": "40",
                "user_id": 1,
                "category_id": 4,
                "exclusivity": "false",
                "rating": "None"
            },
        {
            "id": 18,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 29,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 11,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 17,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 24,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 10,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 18,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 29,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 11,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        }
        ]

def getCategoryProducts(categoryName=None, page=1):
    #if categoryName is None:
    #    response_json, response_status_code = get_request(api_url+"/products/" + str(page))
    #else:
    #    response_json, response_status_code = get_request(api_url+"/products/" + categoryName + "/" + str(page))

    #if response_status_code == 200:
    #    return response_json['products']
    # return response_json['message'], "danger"
    return [
        {
            "id": 13,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 22,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 6,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 18,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 29,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 11,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 17,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 24,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 10,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 18,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 29,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 11,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        }
    ]


def getWishListProducts():
    # response_json, response_status_code = get_request(api_url+"/products/wishlist")
    # if response_status_code == 200:
    #    return response_json['products']
    #return response_json['message'], "danger"
    return [
        {
            "id": 13,
            "name": "Naturescape",
            "description": "My photo about nature",
            "": "",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 22,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 6,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 18,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 29,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 11,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 17,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 24,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 10,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 18,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 29,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 11,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        }
    ]


def getTopRated():
    # response_json, response_status_code = get_request(api_url+"/products/top_rated")
    # if response_status_code == 200:
    #    return response_json['products']
    #return response_json['message'], "danger"
    return [
        {
            "id": 18,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 29,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 10,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        }
    ]


def getAllUserProducts(user_id):
    # response_json, response_status_code = get_request(api_url+"/products/"+ user_id)
    # if response_status_code == 200:
    #    return response_json['products']
    #return response_json['message'], "danger"
    return [
        {
            "id": 18,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 29,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 22,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 17,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },        {
            "id": 13,
            "name": "Naturescape",
            "description": "My photo about nature",
            "": "",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 22,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 18,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 29,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        }
    ]


def getProductsForsale(user_id):
    # response_json, response_status_code = get_request(api_url+"/user/pforsale/"+user_id)
    # if response_status_code == 200:
    #   return response_json['products']
    # return response_json['message'], "danger"
    return [
        {
            "id": 13,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 22,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 6,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 18,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 29,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        },
        {
            "id": 11,
            "name": "Human Eyes",
            "description": "My photo about a girls eyes",
            "price": "40",
            "user_id": 1,
            "category_id": 4,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 17,
            "name": "Naturescape",
            "description": "My photo about nature",
            "price": "20",
            "user_id": 3,
            "category_id": 1,
            "exclusivity": "false",
            "rating": "None"
        },
        {
            "id": 24,
            "name": "Urban city",
            "description": "My photo about a city",
            "price": "30",
            "user_id": 3,
            "category_id": 2,
            "exclusivity": "true",
            "rating": "None"
        }
    ]
