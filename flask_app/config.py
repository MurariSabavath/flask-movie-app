import os
class Config():
    API_KEY = os.environ.get("API_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    SECRET_KEY = os.environ.get("SECRET_KEY")
    URL = os.environ.get("URL")
