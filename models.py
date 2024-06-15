from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String,Text, Boolean, DECIMAL, ForeignKey, DateTime
from flask_login import UserMixin
import datetime
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(255), nullable=False)
    prenom = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    commandes = relationship('Commande', back_populates='user')
    
class Plat(db.Model):
    __tablename__ = 'plat'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(255), nullable=False)
    ingredient = Column(Text, nullable=False)
    disponibilite = Column(Boolean, default=True)
    prix = Column(DECIMAL(10, 2), nullable=False)
    description = Column(Text, nullable=True)
    quantite = Column(Integer, nullable=False)

    commande_plats = relationship('CommandePlat', back_populates='plat')
    
class Commande(db.Model):
    __tablename__ = 'commande'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    date_commande = Column(DateTime, default=datetime.datetime.utcnow)
    statut = Column(String(50), nullable=False, default='En cours')

    user = relationship('User', back_populates='commandes')
    commande_plats = relationship('CommandePlat', back_populates='commande')
    
class CommandePlat(db.Model):
    __tablename__ = 'commande_plat'
    id = Column(Integer, primary_key=True, autoincrement=True)
    commande_id = Column(Integer, ForeignKey('commande.id'), nullable=False)
    plat_id = Column(Integer, ForeignKey('plat.id'), nullable=False)
    quantite = Column(Integer, nullable=False)
    prix_unitaire = Column(DECIMAL(10, 2), nullable=False)

    commande = relationship('Commande', back_populates='commande_plats')
    plat = relationship('Plat', back_populates='commande_plats')