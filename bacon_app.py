#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# combines __init__.py and app.py files from Grinberg tutorial

from flask import Flask, render_template, flash, url_for, redirect
from bacon_cipher import plaintext_to_biliteral, biliteral_to_plaintext, biliteral_to_decoy, decoy_to_biliteral
from config import Config
from frankenstein import frankenstein

app = Flask(__name__)
app.config.from_object(Config)

from forms import EncryptForm, DecryptForm


@app.route('/bacon')
@app.route('/')
def greet():
    return render_template('greet.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    form = EncryptForm()
    if form.is_submitted():
        plaintext_input = form.plaintext.data
        if len(plaintext_input) <= len(frankenstein)/5:
            ciphertext = plaintext_to_biliteral(plaintext_input)
            encrypted_decoy = biliteral_to_decoy(frankenstein, ciphertext)
            return render_template('encrypted.html', encrypted_text=encrypted_decoy)
        else:
            flash("The message is too long. Please enter a shorter message.")
            return redirect(url_for('encrypt'))
    return render_template('encrypt.html', form=form)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    form = DecryptForm()
    if form.is_submitted():
        decoy = form.ciphertext.data
        biliteral = decoy_to_biliteral(decoy)
        decrypted_text = biliteral_to_plaintext(biliteral)
        return render_template('decrypted.html', decrypted_text=decrypted_text)
    return render_template('decrypt.html', form=form)

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

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'test post 1'},
        {'author': user, 'body': 'test post 1'},
    ]
    return render_template('user.html', user=user, posts=posts)

