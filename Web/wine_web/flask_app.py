from flask import Flask, flash, redirect, render_template, request, session, abort
import numpy as np
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import text_matching
import image_ocr
import winerd
from PIL import Image
from tempfile import mkdtemp
from werkzeug import secure_filename
from os.path import  join

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="WineMaster",
    password="sqlpassword",
    hostname="WineMaster.mysql.pythonanywhere-services.com",
    databasename="WineMaster$default",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

db_uri = SQLALCHEMY_DATABASE_URI
engine = create_engine(db_uri)
wine = pd.read_sql_query('SELECT * FROM wine_data', engine)
wineshow = pd.read_sql_query('SELECT * FROM wine_data', engine)
pd.set_option('display.max_colwidth', 10000)
def str_process(string):
    string=string.replace('\n','')
    string=string.replace(' ', '')
    string=''.join([*filter(str.isalnum, string)])
    string=''.join(string)
    string=string.upper()
    return string
wine['designation']=wine['designation'].apply(str).apply(str_process)
wine['province']=wine['province'].apply(str).apply(str_process)
wine['region_1']=wine['region_1'].apply(str).apply(str_process)
wine['variety']=wine['variety'].apply(str).apply(str_process)
wine['winery']=wine['winery'].apply(str).apply(str_process)
wine['year']=wine['year'].fillna(0).apply(int).apply(str).apply(str_process)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/input")
def index():
    return render_template('input.html')


@app.route('/predict', methods=['POST'])
def make_prediction():
	if request.method=='POST':
	    file = request.form['text']
	#if not file: return render_template('input.html', label="No file")
	prediction = text_matching.matching(file,wine,wineshow)[[  'province', 'designation', 'variety', 'winery', 'year', 'description', 'price']]
	return render_template('predict.html',table=prediction.to_html())

@app.route("/image")
def image():
    return render_template('image.html')

@app.route("/predictpic",methods=[ 'POST'])
def predictpic():
    if request.method == 'POST' :
        tempdir = mkdtemp()
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = join(tempdir, filename)
        file.save(filepath)
        image=Image.open(filepath).convert("L")
        prediction = image_ocr.matching(image,wine,wineshow)
    return render_template('predict.html',table=prediction)

@app.route('/recommend', methods=['POST'])
def make_recommendation():
	if request.method=='POST':
	    index = request.form['text']
	#if not file: return render_template('input.html', label="No file")
	recommendation = winerd.get_recommendations(index, wine,wineshow)[[ 'province', 'designation', 'variety', 'winery', 'year', 'description', 'price']]
	#return recommendation.iloc[1,1]
	return render_template('recommend.html', ttable=recommendation.to_html())
	#return index






