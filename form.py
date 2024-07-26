from flask_wtf import FlaskForm
from wtforms import StringField

class MyForm(FlaskForm):
    email = StringField("email")
    password = StringField("password")