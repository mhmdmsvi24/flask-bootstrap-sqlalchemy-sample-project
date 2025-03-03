from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from .custom_validators.passwordvalidator import PasswordValidator


class LoginForm(FlaskForm):
    email = EmailField(
        "Your Email: ",
        validators=[
            Email(message="Invalid Email Address!"),
            DataRequired(message="Required Field"),
        ],
    )
    password = PasswordField("Your Password", validators=[PasswordValidator()])
    submit = SubmitField("Register")
