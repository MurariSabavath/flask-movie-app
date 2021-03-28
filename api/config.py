import os
class Config():
    API_KEY = os.environ.get("API_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    URL = os.environ.get("URL")
#     API_KEY = 'a6d6836dce41469572be86049d892465'
#     SECRET_KEY = 'eb9493fa643a22204c3a3f1cc73ec3e2ca265550769a4085'
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
#     URL = 'https://api.themoviedb.org/3/'
