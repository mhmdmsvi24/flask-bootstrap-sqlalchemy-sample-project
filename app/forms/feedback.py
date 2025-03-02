from flask_wtf import FlaskForm
from wtforms import EmailField, HiddenField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class FeedbackForm(FlaskForm):
    name = StringField(
        "Your name: ",
        validators=[
            Length(3, message="Invalid Length: Minim 3 characters"),
            DataRequired(message="Required Field"),
        ],
    )
    email = EmailField(
        "Your Email: ",
        validators=[
            Email(message="Invalid Email Address!"),
            DataRequired(message="Required Field"),
        ],
    )
    message = TextAreaField(
        "Your Feedback: ",
        validators=[
            Length(
                8, 100, "Invalid Length: between minimum 8 and maximum 100 characters"
            ),
            DataRequired(message="Required Field"),
        ],
    )
    hidden = HiddenField()
    submit = SubmitField("Submit")
