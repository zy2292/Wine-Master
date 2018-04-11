#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:17:11 2018

@author: Keran
"""


from content_management import content
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

TOPIC_DICT = content()


@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT)

@app.route('/product/')
def welcome():
    quotes = [ "'Penicillin cures, but wine makes people happy.' - Alexander Fleming",
               "'Anyone who tries to make you believe that he knows all about wines is obviously a fake.' - Leon Adams",
               "'Wine is the most healthful and most hygienic of beverages.' - Louis Pasteur",
               "'Nothing makes the future look so rosy as to contemplate it through a glass of Chambertin.' - Napoleon Bonaparte",
               "'Life is too short to drink bad wine.' - Anonymous"
              ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]
    return render_template('product.html',**locals())

@app.route('/upload/', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename
    return render_template('upload.html')


if __name__ == "__main__":
    app.run()
		