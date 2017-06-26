#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 20:49:14 2017

@author: simondefrenet
"""

WTF_CSRF_ENABLED = True
SECRET_KEY = 'abasedepoppoppoppop'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://accounts.google.com/o/oauth2/v2/auth'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
