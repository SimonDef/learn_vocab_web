#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 00:15:37 2017

@author: simondefrenet
"""

from flask import request, render_template, flash, redirect, url_for, session, logging
from app import app
from .forms import LoginForm, Reply
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from app.learnvocab import dictionnary, language1, language2, loadWords, chooseWord

import random

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')
    
@app.route('/words')
def words():
    return render_template("words.html",
                           title='words', words = dictionnary, language1 = language1, language2 = language2)
        
@app.route('/learnvocab', methods=['GET', 'POST'])
def learnvocab():
    form = Reply(request.form)
    message='Press question to start'
    global correct_guess
    if request.method=="GET":
        #display question
        #test=random.choice(["simple","choose4"])
        tested_language=random.choice([language1,language2])
        testword=chooseWord(dictionnary)
        if tested_language==language1:
            correct_guess=testword[0]
        else:
            correct_guess=testword[1]
        return render_template("learnvocab.html", title='Learn Vocab', 
                               form=form,
                               testword=testword,
                               tested_language=tested_language,
                               language1 = language1, 
                               language2 = language2
                               )
    
    if request.method=="POST":
        #get answers
        if form.reply.data == correct_guess:
            message='This is correct'
            return render_template("learnvocab.html", title='Learn Vocab', 
                               form=form,
                               message=message
                               )
        else:
            message='you re wrong, you should try again'
            return render_template("learnvocab.html", title='Learn Vocab', 
                               form=form,
                               message=message)
    return render_template("learnvocab.html", form=form )
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
    
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')