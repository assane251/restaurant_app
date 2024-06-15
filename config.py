from dotenv import load_dotenv
import os
# chargement 
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI =os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

