from flask import Flask

from .config import Config
from .extensions import Bootstrap
from .main import main_bp


def create_app()->Flask:
    # Init
    app = Flask(__name__)

    WTF_SECRET_KEY = Config.WTF_SECRET_KEY
    app.config["SECRET_KEY"] = WTF_SECRET_KEY

    if app.config["SECRET_KEY"] and app.config["SECRET_KEY"] != WTF_SECRET_KEY:
        raise ValueError("Invalid SECRET KEY for WTF!")

    # Extensions
    Bootstrap(app)

    app.register_blueprint(main_bp)

    return app

app = create_app()
