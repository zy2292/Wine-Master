import _pickle as cPickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from itertools import chain
import numpy as np
with open('/home/WineMaster/mysite/data/tfidf_matrix.pkl', 'rb') as infile:
    tfidf = cPickle.load(infile)


def get_recommendations(index,wine,wineshow):
    cos_query=cosine_similarity(tfidf,tfidf[index])
    cos_query=list(chain(*cos_query))
    sort_dist=np.argsort(cos_query)[::-1][1:6]
    result=wineshow.loc[sort_dist,:]
    return result

