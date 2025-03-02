import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5 as Bootstrap

# Env variables
load_dotenv()

# WTForms CSRF
SECRET_KEY = os.getenv("SECRET_KEY")

# Flask init
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = SECRET_KEY


# Routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<int:id>")
def user(id):
    fetched_user = {
        12: {
            "name": "mmd",
            "role": "Admin",
            "tags": ["SWE", "NE", "BC", "FS"],
        }
    }

    return render_template("user.html", user=fetched_user[id])


# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html", error="404"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("index.html", error="500"), 500
