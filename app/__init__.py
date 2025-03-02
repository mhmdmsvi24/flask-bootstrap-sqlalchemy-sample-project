import os

from dotenv import load_dotenv
from flask import Flask

from .extensions import Bootstrap

# Env variables
load_dotenv()


def create_app():
    # Init
    app = Flask(__name__)

    SECRET_KEY = os.getenv("SECRET_KEY")
    app.config["SECRET_KEY"] = SECRET_KEY

    if app.config["SECRET_KEY"] and app.config["SECRET_KEY"] != SECRET_KEY:
        raise ValueError("Invalid SECRET KEY for WTF!")

    # Extensions
    Bootstrap(app)

    return app
