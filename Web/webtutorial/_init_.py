#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:17:11 2018

@author: Keran
"""

from flask import Flask, render_template
from content_management import content

TOPIC_DICT = content()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT)


if __name__ == "__main__":
    app.run()
		