#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'totally_secret'