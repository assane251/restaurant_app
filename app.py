from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hello world'

# class RegisterFrame(FlaskForm):
#     username = StringField(label='username')
#     email_address = StringField(label='email address')
#     password = PasswordField(label='password')
#     confirm_password = PasswordField(label='confirm password')
#     submit = SubmitField(label='submit')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    # form = RegisterFrame()
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
