import os

def database_uri_replace():
    uri = os.environ.get('DATABASE_URL')
    if uri and uri.startswith("postgres://"):
        return uri.replace("postgres://", "postgresql://", 1)
    return uri

class Config():
    API_KEY = os.environ.get("API_KEY")
    SQLALCHEMY_DATABASE_URI = database_uri_replace()
    SECRET_KEY = os.environ.get("SECRET_KEY")
    URL = os.environ.get("URL")

