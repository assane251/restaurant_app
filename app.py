from flask import Flask, render_template, flash, redirect, url_for, request
from flask_migrate import Migrate
from config import Config
from models import db, User
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import random, string
import datetime

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

mail = Mail(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Utilisation d'un dictionnaire pour stocker les codes de vérification
verification_codes = {}

def generate_verification_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

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
            flash('Ce compte existe déjà', 'error')
            return redirect(url_for('register'))
        else:
            new_user = User(nom=nom, prenom=prenom, email=email, password=generate_password_hash(password))
            try:
                print("Ajout de l'utilisateur à la base de données...")
                verification_code = generate_verification_code()
                print(verification_code)
                expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
                verification_codes[email] = {'code': verification_code, 'expiration': expiration_time}

                msg = Message('Verification Code', recipients=[email])
                msg.body = f'Your verification code is {verification_code}. It will expire in 1 minute.'
                mail.send(msg)
                db.session.add(new_user)
                db.session.commit()
                print("Utilisateur ajouté avec succès !")

                flash('A verification code has been sent to your email. Please enter it below.', 'info')
                return redirect(url_for('verify', email=email))
              
            except Exception as e:
                db.session.rollback()
                flash(f'Erreur de l\'insertion: {str(e)}', 'error')
                print(f"Erreur lors de l'insertion: {str(e)}")
              
    return render_template('register.html')

@app.route('/verify_email/<email>', methods=['GET', 'POST'])
def verify(email):
    if request.method == 'POST':
        code = request.form.get('code')
        verification_data = verification_codes.get(email)

        if verification_data and verification_data['code'] == code and verification_data['expiration'] > datetime.datetime.now():
            user = User.query.filter_by(email=email).first()
            user.verified = True
            db.session.commit()

            # Supprimez le code de vérification après utilisation
            del verification_codes[email]

            flash('Your account has been verified!', 'success')
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid or expired verification code. Please try again.', 'error')

    return render_template('verify.html', email=email)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password): 
            if user.verified:
                login_user(user)
                flash('You are now logged in!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Please verify your email before logging in.', 'warning')
                return redirect(url_for('verify', email=email))

        flash('Invalid email or password', 'error')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("Connexion réussie à la base de données !")
        except Exception as e:
            print("Erreur lors de la connexion à la base de données :", e)
    app.run(debug=True)
