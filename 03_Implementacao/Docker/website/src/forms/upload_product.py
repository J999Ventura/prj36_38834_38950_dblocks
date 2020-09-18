from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import StringField, BooleanField, SubmitField, DecimalField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length, NumberRange
from decimal import ROUND_HALF_UP
from ..connectors.api_connector import getCategories


class UploadForm(FlaskForm):
    prodname = StringField('Product Name', validators=[InputRequired(), DataRequired(), Length(min=4, max=20)])
    prodimage = FileField('Photo', validators=[FileRequired(), FileAllowed(['png', 'jpg'], "wrong format!")])
    prodprice = DecimalField('Price in €', places=2, rounding=ROUND_HALF_UP, validators=[DataRequired(), NumberRange(min=0.01, max=10000, message="You must enter a price between, 0.01 and 10000")])
    proddesc = StringField('Description', validators=[Length(min=2, max=100)])
    categories = getCategories()
    prodcatg = SelectField('Category', choices=[(category['id'], category['name']) for category in categories], validators=[DataRequired()])
    submitupload = SubmitField('Sell')
