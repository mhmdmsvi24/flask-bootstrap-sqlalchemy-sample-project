import re

from wtforms.validators import ValidationError


class PasswordValidator:
    """Custom password validator enforcing security requirements."""

    def __init__(self, message=None):
        self.message = message or "The password must match the security requirements."

        # Define validation rules
        self.rules = [
            (lambda pwd: len(pwd) >= 8, "Minimum 8 characters required"),
            (
                lambda pwd: re.search(r"[A-Z]", pwd),
                "Password must contain at least one uppercase letter (A-Z)",
            ),
            (
                lambda pwd: re.search(r"[a-z]", pwd),
                "Password must contain at least one lowercase letter (a-z)",
            ),
            (
                lambda pwd: re.search(r"\d", pwd),
                "Password must contain at least one digit (0-9)",
            ),
            (
                lambda pwd: re.search(
                    r"[!@#$%^&*()_+\-=\{\}\[\]\|\\:;“‘<>\.\?\/~`]", pwd
                ),
                "Password must contain at least one special character: !@#$%^&*()_+-={}[]|\\:;“‘<>.?/~`",
            ),
        ]

    def __call__(self, form, field):
        password = field.data or ""

        for rule, error_message in self.rules:
            if not rule(password):
                raise ValidationError(error_message)
