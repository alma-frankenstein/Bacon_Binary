from flask import Flask, render_template
from forms import EncryptForm, DecryptForm
from config import Config
from bacon_cipher import plaintext_to_biliteral, biliteral_to_plaintext, biliteral_to_decoy, decoy_to_biliteral
from frankenstein import frankenstein

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/bacon')
def greet():
    return 'hello bacon'

@app.route('/encrypted/<ciphertext>')
def show_encrypted_text():
    return ciphertext


@app.route('/encrypt', methods = ['GET', 'POST'])
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