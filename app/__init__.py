from flask import Flask

from .config import Config
from .extensions import Bootstrap


def create_app():
    # Init
    app = Flask(__name__)

    WTF_SECRET_KEY = Config.WTF_SECRET_KEY
    app.config["SECRET_KEY"] = WTF_SECRET_KEY

    if app.config["SECRET_KEY"] and app.config["SECRET_KEY"] != WTF_SECRET_KEY:
        raise ValueError("Invalid SECRET KEY for WTF!")

    # Extensions
    Bootstrap(app)

    return app
