from os import path, environ


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = environ.get("SECRET_KEY", "defaultsecretkey123!456@")
    FLASK_ADMIN_SWATCH = 'Cerulean'

    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "upload")
