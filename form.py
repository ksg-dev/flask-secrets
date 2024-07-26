from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email


class MyForm(FlaskForm):
    email = StringField("Email",
                        validators=[
                            InputRequired(),
                            Email()
                        ]
                        )
    password = PasswordField("Password",
                             validators=[
                                 InputRequired(),
                                 Length(min=8, message="Password must be at least 8 characters")
                             ]
                             )
    submit = SubmitField("Log In")


