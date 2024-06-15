
from flask import Flask, render_template
from flask_migrate import Migrate
from config import Config
from models import db, Plat, User, Commande, CommandePlat
from flask import Flask, url_for, redirect, render_template, request
from flask_migrate import Migrate
from flask_login import LoginManager, logout_user, login_user, current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id): 
    return User.get_or_404(id)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST': 
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user: 
            redirect(url_for('login'))
        else:
            new_user = User(nom=nom, prenom=prenom, email=email, password=generate_password_hash(password))
            try:
              db.session.add(new_user)
              db.session.commit()
              print('insertion reussit')
            except:
              print('Erreur')
              
              
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password): 
            login_user(user)
            redirect(url_for('acceuil'))
        else:
            redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        try:
            # Créer toutes les tables définies dans les modèles
            db.create_all()
            print("Connexion réussie à la base de données !")
        except Exception as e:
            print("Erreur lors de la connexion à la base de données :", e)
    app.run(debug=True)  
