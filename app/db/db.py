import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import Role, User

from app.main import main_bp

# SQL alchemy init
basedir = os.path.abspath(os.path.dirname(__file__))


main_bp.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
main_bp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(main_bp)
Migrate(main_bp, db)


@main_bp.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
