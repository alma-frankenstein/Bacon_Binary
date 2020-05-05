#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# combines __init__.py and app.py files from Grinberg tutorial

from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from bacon_cipher import plaintext_to_biliteral, biliteral_to_plaintext, biliteral_to_decoy, decoy_to_biliteral
from frankenstein import frankenstein
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from models import User, Message
from forms import RegistrationForm, EncryptForm, DecryptForm, LoginForm


@app.shell_context_processor # when 'flask shell' command runs, it registers the return values in the shell session
def make_shell_context():
    return {'db': db, 'User': User, 'Message': Message}

@app.route('/bacon') # = 'index' in Grinberg
@app.route('/')
@login_required
def greet():
    return render_template('greet.html')
    #return 'hello bacon'

# @app.route('/encrypted/<ciphertext>') # ?
# def show_encrypted_text():
#     return ciphertext

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('encrypt'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('wrong username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('greet')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/encrypt', methods = ['GET', 'POST'])
@login_required
def encrypt():
    form = EncryptForm()
    if form.is_submitted():
        plaintext_input = form.plaintext.data
        ciphertext = plaintext_to_biliteral(plaintext_input)
        encrypted_decoy = biliteral_to_decoy(frankenstein, ciphertext)
        return render_template('encrypted.html', encrypted_text=encrypted_decoy)
    return render_template('encrypt.html', form=form)

@app.route('/decrypt', methods = ['GET', 'POST'])
def decrypt():
    form = DecryptForm()
    if form.is_submitted():
        decoy = form.ciphertext.data
        biliteral = decoy_to_biliteral(decoy)
        decrypted_text = biliteral_to_plaintext(biliteral)
        return render_template('decrypted.html', decrypted_text=decrypted_text)
    return render_template('decrypt.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('greet'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('now you\'re registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
