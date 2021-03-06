import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join


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

def main(text,wine,wineshow):
    cols = cols = ['designation', 'province','region_1','variety','winery','year']
    betas = [0.5, 0.5, 0.5, 0.5, 0.5, 1]
    args = zip(cols, betas)

    pool = Pool()
    func = partial(match_col, query=text, wine=wine, n=3)
    score = pool.map(func, args)
    wine['scores'] = sum(score)
    result = wineshow[wine['scores']==max(wine['scores'])]
    if result.shape[0] > 8:
        result = result.sample(8)
    pool.close()
    pool.join()
    return result

def matching(text,wine,wineshow):
    text=str_process(text)
    result=main(text,wine,wineshow)
    return result
