import os
class Config():
    API_KEY = os.environ.get("API_KEY")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    URL = os.environ.get("URL")