from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo


class ConfirmEmailForm(FlaskForm):
    submitconfirmemail = SubmitField('Confirm Your Email')