from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length


class CustomerForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(),
                                                       Length(min=2, max=100)])
    second_name = StringField('Second Name', validators=[InputRequired(),
                                                         Length(min=2, max=100)])
    last_name = StringField('Last Name', validators=[InputRequired(),
                                                     Length(min=2, max=100)])
    phone_number = StringField('Phone Number', validators=[InputRequired(),
                                                           Length(min=11, max=11)])
    email_address = StringField('Email Address', validators=[InputRequired(),
                                                             Length(min=6, max=35)])
    address = StringField('Address', validators=[InputRequired(),
                                                 Length(min=6, max=100)])
    submit = SubmitField('Confirm')
