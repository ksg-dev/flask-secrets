from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class MyForm(FlaskForm):
    email = StringField("email")
    password = PasswordField("password")