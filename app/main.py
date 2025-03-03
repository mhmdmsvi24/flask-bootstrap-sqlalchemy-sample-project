from flask import Blueprint, redirect, render_template

from app.forms import FeedbackForm, LoginForm, SignupForm

from .error_handlers import internal_server_error, page_not_found

main_bp = Blueprint("main", __name__ )
# Routes
@main_bp.route("/")
def index():
    return render_template("index.html")


# Test User
fetched_user = {
    12: {
        "name": "mmd",
        "role": "Admin",
        "tags": ["SWE", "NE", "BC", "FS"],
    }
}


@main_bp.route("/user/<int:id>")
def user(id):
    return render_template("users/user.html", user=fetched_user[id])

@main_bp.route("/feedback", methods=["GET", "POST"])
def submitFeedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        return redirect("/")

    return render_template("/forms/feedback.html", user=fetched_user[12], form=form)


@main_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect("/")

    return render_template("/forms/login.html", form=form)


@main_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        return redirect("/")

    return render_template("/forms/signup.html", form=form)


# Error Handlers
main_bp.register_error_handler(404, page_not_found)
main_bp.register_error_handler(404, internal_server_error)

