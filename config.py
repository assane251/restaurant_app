from dotenv import load_dotenv
import os

# chargement du fichier .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    FLASK_DEBUG=os.getenv("FLASK_DEBUG")
    FLASK_APP=os.getenv("FLASK_APP")
    FLASK_ENV=os.getenv("FLASK_ENV")
    SECRET_KEY=os.getenv("SECRET_KEY")
    MAIL_SERVER=os.getenv("MAIL_SERVER")
    MAIL_PORT=os.getenv("MAIL_PORT")
    MAIL_USE_TLS=os.getenv("MAIL_USE_TLS")
    MAIL_USERNAME=os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD")
    MAIL_USE_TLS=os.getenv("MAIL_USE_TLS")
    MAIL_USE_SSL=os.getenv("MAIL_USE_SSL")

