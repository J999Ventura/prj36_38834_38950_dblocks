from . import json


class User():
    def __init__(self, id, fname, lname, email, role, bdate, image, token):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.role = role
        self.bdate = bdate
        self.image = image
        self.token = token
