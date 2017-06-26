#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 20:52:20 2017

@author: simondefrenet
"""

from flask_wtf import Form
from wtforms import StringField, BooleanField, TextField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class Reply(Form):
    reply = TextField('Your Guess', validators=[DataRequired()])
