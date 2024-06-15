from flask import Flask, render_template
from flask_migrate import Migrate
from config import Config
from model import db, Plat, User, Commande, CommandePlat



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app,db)



@app.route('/')
def index():
    return 'Hello World!' #render_template('')


if __name__ == '__main__':
    with app.app_context():
        try:
            # Créer toutes les tables définies dans les modèles
            db.create_all()
            print("Connexion réussie à la base de données !")
        except Exception as e:
            print("Erreur lors de la connexion à la base de données :", e)
    app.run(debug=True)  
