#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 23:53:34 2017

@author: simondefrenet
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views