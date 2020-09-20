from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length, NumberRange
import json
import datetime


def getMonths():
    response_json = json.loads('{"months":[{"id":"01", "name": "Jan"},'
                               '{"id":"02", "name": "Feb"},'
                               '{"id":"03", "name": "Mars"},'
                               '{"id":"04", "name": "Apr"},'
                               '{"id":"05", "name": "May"},'
                               '{"id":"06", "name": "Jun"},'
                               '{"id":"07", "name": "Jul"},'
                               '{"id":"08", "name": "Aug"},'
                               '{"id":"09", "name": "Sep"},'
                               '{"id":"10", "name": "Oct"},'
                               '{"id":"11", "name": "Nov"},'
                               '{"id":"12", "name": "Dec"}]}')
    response_json = response_json['months']

    return response_json


def getYears():
    now = datetime.datetime.now()
    present_year = now.year;
    response_json = json.loads(
        '{"years":[{"id":"'+str(present_year)+'", "name": "'+str(present_year)+'"},'
        '{"id":"'+str(present_year+1)+'", "name": "'+str(present_year+1)+'"},'
        '{"id":"'+str(present_year+2)+'", "name": "'+str(present_year+2)+'"},'
        '{"id":"'+str(present_year+3)+'", "name": "'+str(present_year+3)+'"},'
        '{"id":"'+str(present_year+4)+'", "name": "'+str(present_year+4)+'"}]}')
    response_json = response_json['years']

    return response_json


class PaymentForm(FlaskForm):
    cardName = StringField('Card Holder', validators=[InputRequired(), DataRequired(), Length(min=4, max=20)])
    cardNumber = StringField('Card Number', validators=[InputRequired(), DataRequired(), Length(min=4, max=20)])
    cvc = IntegerField('CVC', validators=[DataRequired(), NumberRange(min=0, max=999, message="You must enter a CVC number between 0 and 999")])
    months = getMonths()
    years = getYears()
    month = SelectField('Select Month', choices=[(month['id'], month['name']) for month in months], validators=[DataRequired()])
    year = SelectField('Select Year', choices=[(year['id'], year['name']) for year in years], validators=[DataRequired()])
    submitPayment = SubmitField('Pay')


