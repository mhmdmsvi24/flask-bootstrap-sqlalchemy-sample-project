import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration (default settings for all environments)"""

    WTF_SECRET_KEY = os.getenv("WTF_SECRET_KEY")
