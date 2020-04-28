from flask import Flask, render_template, url_for, redirect
from forms import EncryptForm, DecryptForm
from config import Config
from bacon_cipher import encrypt_message, decrypt_message

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/bacon')
def greet():
    return 'hello bacon'

@app.route('/encrypted/<ciphertext>')
def show_encrypted_text():
    return ciphertext


# @app.route('/word/<int:word_key>')
# def word_by_key(word_key):
#     word = dictionary_db[word_key]
#     return word

@app.route('/encrypt', methods = ['GET', 'POST'])
def encrypt():
    form = EncryptForm()
    if form.is_submitted():
        plaintext_input = form.plaintext.data
        ciphertext = encrypt_message(plaintext_input)
        return render_template('encrypted.html', encrypted_text=ciphertext)
    return render_template('encrypt.html', form=form)

@app.route('/decrypt', methods = ['GET', 'POST'])
def decrypt():
    form = DecryptForm()
    if form.is_submitted():
        ciphertext_input = form.ciphertext.data
        plaintext = decrypt_message(ciphertext_input)
        return render_template('decrypted.html', decrypted_text=plaintext)
    return render_template('decrypt.html', form=form)