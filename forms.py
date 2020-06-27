#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class EncryptForm(FlaskForm):
    plaintext = TextAreaField('message to encrypt')
    ciphertext = TextAreaField()
    submit = SubmitField('encrypt')


class DecryptForm(FlaskForm):
    ciphertext = TextAreaField('text to decrypt')
    plaintext = TextAreaField()
    submit = SubmitField('decrypt')
