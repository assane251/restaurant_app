
from flask import Flask, render_template
from flask_migrate import Migrate
from config import Config
from model import db, Plat, User, Commande, CommandePlat
from flask import Flask, url_for, redirect, render_template
from flask_migrate import Migrate
from flask_login import LoginManager, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app,db)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    # form = RegisterFrame()
    return render_template('register.html')



if __name__ == '__main__':
    with app.app_context():
        try:
            # Créer toutes les tables définies dans les modèles
            db.create_all()
            print("Connexion réussie à la base de données !")
        except Exception as e:
            print("Erreur lors de la connexion à la base de données :", e)
    app.run(debug=True)  
