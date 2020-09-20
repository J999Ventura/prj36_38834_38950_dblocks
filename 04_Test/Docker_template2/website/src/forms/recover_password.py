from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo


class RecoverPasswordForm(FlaskForm):
    newpassword = PasswordField('New Password', validators=[InputRequired(), DataRequired(), Length(min=6, max=50)])
    confirmnewpassword = PasswordField('Confirm New Password', validators=[InputRequired(), DataRequired(), EqualTo('newpassword')])
    submitnewpassword = SubmitField('Submit request')