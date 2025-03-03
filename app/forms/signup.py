from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from .custom_validators.passwordvalidator import PasswordValidator


class SignupForm(FlaskForm):
    username = StringField(
        "Your username: ",
        validators=[
            Length(3, message="Invalid Length: Minim 3 characters"),
            DataRequired(message="Required Field"),
        ],
    )
    password = PasswordField("Your Password", validators=[PasswordValidator()])
    email = EmailField(
        "Your Email: ",
        validators=[
            Email(message="Invalid Email Address!"),
            DataRequired(message="Required Field"),
        ],
    )
    submit = SubmitField("Submit")
