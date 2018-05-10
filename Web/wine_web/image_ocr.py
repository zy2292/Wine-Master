import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import pytesseract


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import nltk.stem
from nltk.tokenize import word_tokenize
from datetime import datetime
import string
from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer
from py_stringmatching.tokenizer.qgram_tokenizer import QgramTokenizer
from py_stringmatching.similarity_measure.tversky_index import TverskyIndex
from multiprocessing import Pool
from functools import partial

def str_process(string):
    string=string.replace('\n','')
    string=string.replace(' ', '')
    string=''.join([*filter(str.isalnum, string)])
    string=''.join(string)
    string=string.upper()
    return string

def get_tversky_index(proto, query, n=3, beta=0.5):
    tversky = TverskyIndex(beta=beta)
    qgram = QgramTokenizer(qval=n, padding=False)
    inters = tversky.get_sim_score(qgram.tokenize(query), qgram.tokenize(proto))
    return inters

def match_col(arg, query, wine, n=3):
    col, beta = arg
    table = wine[col]
    score = table.apply(lambda x: get_tversky_index(x, query, n=n, beta=beta))
    return score

def get_weighted_index(text,wine,wineshow):
    cols = ['designation', 'province','region_1','variety','winery','year']
    betas = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    args = zip(cols, betas)

    pool = Pool()
    func = partial(match_col, query=text,wine=wine, n=3)
    score = pool.map(func, args)
    wine['scores'] = np.average(score, axis=0, weights=[1, 0.1, 1.3, 1, 1, 1.6])
    result = wineshow[wine['scores']==max(wine['scores'])]
    if result.shape[0] > 8:
        result = result.sample(8)
    pool.close()
    pool.join()
    return result

def matching(image,wine,wineshow):
    text = pytesseract.image_to_string(image, config = '--psm 3', lang = 'eng+fra+deu+ita+spa+por+afr')
    if text!='':
        text=str_process(text)
        result=get_weighted_index(text,wine,wineshow)[[ 'province', 'designation', 'variety', 'winery', 'year', 'description', 'price']].to_html()
    else:
        result='<h2>Cannot Read Anything</h2>'
    return result
