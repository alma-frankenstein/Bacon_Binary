from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField

class EncryptForm(FlaskForm):
    plaintext = TextAreaField()
    ciphertext = TextAreaField()
    submit = SubmitField('encrypt')

class DecryptForm(FlaskForm):
    ciphertext = TextAreaField()
    plaintext = TextAreaField()
    submit = SubmitField('decrypt')
