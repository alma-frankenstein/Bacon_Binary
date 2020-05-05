#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, PasswordField, BooleanField, StringField
from wtforms.validators import DataRequired, DataRequired, Email, EqualTo, InputRequired, ValidationError
from models import User

class EncryptForm(FlaskForm):
    plaintext = TextAreaField()
    ciphertext = TextAreaField()
    submit = SubmitField('encrypt')

class DecryptForm(FlaskForm):
    ciphertext = TextAreaField()
    plaintext = TextAreaField()
    submit = SubmitField('decrypt')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('sign in')

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign in')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('that username\'s taken')
