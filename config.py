from dotenv import load_dotenv
import os
# chargement 
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI =os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_DEBUG=os.getenv("FLASK_DEBUG")
    FLASK_APP=os.getenv("FLASK_APP")
    FLASK_ENV=os.getenv("FLASK_ENV")
    SECRET_KEY=os.getenv("SECRET_KEY")

