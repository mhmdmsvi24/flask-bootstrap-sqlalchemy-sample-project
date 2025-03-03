from flask import redirect, render_template

from app import create_app
from app.forms import FeedbackForm, LoginForm, SignupForm

from .error_handlers import internal_server_error, page_not_found

app = create_app()


# Routes
@app.route("/")
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


@app.route("/user/<int:id>")
def user(id):
    return render_template("users/user.html", user=fetched_user[id])


@app.route("/feedback", methods=["GET", "POST"])
def submitFeedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        return redirect("/")

    return render_template("/forms/feedback.html", user=fetched_user[12], form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect("/")

    return render_template("/forms/login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        return redirect("/")

    return render_template("/forms/signup.html", form=form)


# Error Handlers
app.register_error_handler(404, page_not_found)
app.register_error_handler(404, internal_server_error)


if __name__ == "__main__":
    app.run(debug=True)  # Change debug=False for production
