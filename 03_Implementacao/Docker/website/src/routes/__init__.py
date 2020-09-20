from flask import (flash, g, redirect, render_template, request, session, url_for)
from ..forms.login_register import RegisterForm, LoginForm, RecoverForm, ResendEmailForm
from ..forms.upload_product import UploadForm
from ..forms.pay import PaymentForm
from ..forms.recover_password import RecoverPasswordForm
from ..forms.confirm_email import ConfirmEmailForm
from ..connectors.api_connector import getProductDetails, getWishListProducts, sellProduct, getProductsForsale, login, register, recoverPassword, resendEmail, getCategories, getCategoryProducts, getNewProductsArrival, getAllUserProducts, getTopRated
from ..connectors.payment import checkoutPayment
from ..connectors.recover_password import setNewPassword
from ..connectors.confirm_email import setConfirmEmail
from ..models import dummy, User_model
from .. import app, APP_ROOT, os
from ..models.water_mark import water_mark_image
import json


@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']


