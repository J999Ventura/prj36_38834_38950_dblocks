from flask import Flask
from flask import send_file
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__, static_folder="static")
Bootstrap(app)
# Aplication key, to not allow xss, csrf, or injections on forms
app.secret_key = os.urandom(24)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
from .routes import home, profile, product_grid, product_sell, contact, product_details, checkout, wishlist, recover_password, confirm_email