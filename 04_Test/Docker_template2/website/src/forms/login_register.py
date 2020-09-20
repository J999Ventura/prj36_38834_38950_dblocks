from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    fname = StringField('First Name', validators=[InputRequired(), DataRequired(), Length(min=4, max=20)])
    lname = StringField('Last Name', validators=[InputRequired(), DataRequired(), Length(min=4, max=20)])
    bdate = StringField('Birth Date', validators=[InputRequired(), DataRequired(), Length(min=8, max=8)])
    email = StringField('Email', validators=[InputRequired(), DataRequired(), Email()])
    password_reg = PasswordField('Password', validators=[InputRequired(), DataRequired(), Length(min=6, max=50)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), DataRequired(), EqualTo('password_reg')])
    submitreg = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), DataRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), DataRequired(), Length(min=6, max=50)])
    submitlog = SubmitField('Sign In')


class RecoverForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), DataRequired(), Email()])
    submitrec = SubmitField('Recover Password')


class ResendEmailForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), DataRequired(), Email()])
    submitresend = SubmitField('Resend Confirmation Email')
