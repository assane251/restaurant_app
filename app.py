import random
from flask import Flask, json, render_template, jsonify, flash, session
from flask_mail import Mail, Message
from flask_migrate import Migrate
from config import Config
from models import db, Plat, User, Commande, CommandePlat
from flask import Flask, url_for, redirect, render_template, request
from flask_migrate import Migrate
from flask_login import (
    LoginManager,
    logout_user,
    login_user,
    current_user,
    login_required,
)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from data import plats
from authlib.integrations.flask_client import OAuth
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer import oauth_authorized

import sys

sys.setrecursionlimit(15000)

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)
login_manager = LoginManager()


login_manager.init_app(app)


# fichier_json = 'myjson.json'

# with open(fichier_json, 'r') as json_file:
# json_data = json.load(json_file)

# client_id = json_data['web']['client_id']
# client_secret = json_data['web']['client_secret']

client_id = "76986610716-puqfecpsnpqm0hjcm9pvh7sj3d3chpoe.apps.googleusercontent.com"
client_secret = "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"

google_bp = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    scope=['profile', 'email', 'https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/drive.readonly'],
    redirect_to='http://localhost:5000/google_login/authorized'  
)
app.register_blueprint(google_bp, url_prefix="/google_login")

google_bp = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    scope=[
        "profile",
        "email",
        "https://www.googleapis.com/auth/gmail.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ],
    redirect_to="http://localhost:5000/google_login/authorized",
)
# app.register_blueprint(google_bp, url_prefix="/google_login")

# oauth = OAuth(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def index():

    return render_template("index.html", plats=plats)

def generate_verification_code():
    return "".join(str(random.randint(0, 9)) for _ in range(6))






@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST': 
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        email = request.form.get('email')
        password = request.form.get('password')
        
        verification_code = generate_verification_code()
        print("verification_code")

        # Envoyer l'e-mail de vérification
        # msg = Message('Code de vérification', recipients=[email])
        # msg.body = f"Votre code de vérification est : {verification_code}"
        # mail.send(msg)

        if not all([nom, prenom, email, password]):
            return flash({"message": "Vous devez remplir tous les champs"})

        user = User.query.filter_by(email=email).first()
        if user:
            flash({"message": "ce email a deja un compte"})
            return redirect(url_for("login"))
        
        user = User.query.filter_by(email=email).first()
        
        if user: 
            flash({'message': 'ce email a deja un compte'})
            return redirect(url_for('login'))
        else:
            new_user = User(
                nom=nom,
                prenom=prenom,
                email=email,
                password=generate_password_hash(password),
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash({"message": "Votre inscription a reussit"})
                return redirect(url_for("index"))
            except:
                flash({"message": "erreur"})
                print("erreur")
              
              
    return render_template('register.html')


# @app.route('/verify', methods=['GET', 'POST'])
# def verify():
#     if request.method == 'POST':
#         entered_code = request.form['code']
#         stored_code = session.get('verification_code')

#         if entered_code == stored_code:
#             # Le code est correct, connectez l'utilisateur automatiquement
#             # Vous pouvez ajouter ici la logique pour connecter l'utilisateur
#             return "Code vérifié. Vous êtes connecté maintenant."
#         else:
#             return "Code incorrect. Veuillez réessayer."

#     return render_template('verify_email.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            print("reussit")
            # flash({'message': 'Vous etes connecter'})

            return redirect(url_for("index"))
        else:
            print("echec")
            # flash({'message': 'email ou password incorrect'})

            return redirect(url_for("login"))
    return render_template("login.html")


@app.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get("/oauth2/v2/userinfo")
    if not resp.ok:
        flash("Échec de la connexion Google", 'danger')
        return redirect(url_for('login'))

    user_info = resp.json()
    email = user_info["email"]
    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(email=email)
        db.session.add(user)
        db.session.commit()

    login_user(user)
    flash("Vous êtes connecté avec Google", "success")
    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@oauth_authorized.connect_via(google_bp)
def google_logged_in(blueprint, token):
    resp = blueprint.session.get("/oauth2/v2/userinfo")
    if resp.ok:
        user_info = resp.json()
        email = user_info["email"]
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email)
            db.session.add(user)
            db.session.commit()
        login_user(user)


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    plat = request.form.to_dict()
    cart = session.get("cart", [])
    cart.append(plat)
    session["cart"] = cart
    session["cart_count"] = len(cart)
    return jsonify({"count": session["cart_count"]})


# @app.route("/cart", methods=["POST", "GET"])
# def cart():
#     if request.method == "POST":
#         if current_user.is_authenticated:
#             flash({"message": f"Merci  pour votre commande"})
#             print("Compte existe")
#         else:
#             nom = request.form.get("nom")
#             prenom = request.form.get("prenom")
#             email = request.form.get("email")
#             password = request.form.get("password")
#             new_user = User(
#                 nom=nom,
#                 prenom=prenom,
#                 email=email,
#                 password=generate_password_hash(password),
#             )
#             db.session.add(new_user)
#             db.session.commit()
#             flash({"message": f"Merci Compte a ete creer"})
#             print("Compte a ete creer")
#     cart = session.get("cart", [])
#     return render_template("cart.html", cart=cart)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/blog")
def blog():
    return render_template("blog.html", plats=plats)


@app.route("/boutique")
def boutique():

    return render_template("boutique.html", plats=plats)
    


@app.route("/commande", methods=["GET", "POST"])
# @login_required
def commande():
    if request.method == " POST":
        pass
        # user_id = current_user.id
        # date_commande = datetime.utcnow()
        # statut = "En Cours"
        # commande = Commande(user_id=user_id, date_commande=date_commande, statut=statut)
        # db.session.add(commande)
        # db.session.commit()

    else:
        flash("message", "erreur")
    
    cart = session.get("cart", [])

    return render_template('commande.html', cart=cart)


if __name__ == '_main_':
    with app.app_context():
        try:
            # Créer toutes les tables définies dans les modèles
            db.create_all()
            print("Connexion réussie à la base de données !")
        except Exception as e:
            print("Erreur lors de la connexion à la base de données :", e)

    app.run(debug=True)
