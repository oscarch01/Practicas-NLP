#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Archivo principal para reducción de dimencionalidad
Fecha: 24/10/2019
"""
from tfidf import *

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.decomposition import TruncatedSVD
from sklearn.utils.extmath import randomized_svd
from vectorization import vectorizerV2 as vectorizer
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm
import seaborn

df = pd.read_csv('author_corpus-test.txt',sep='\t',index_col=False,names=["autor","texto"])

# Remueve autor 5, que es igual al 4
df = df[:][df['autor']!=5]

X_raw = df['texto']

print("Ejercicio 1: Modelado de Tópicos a partir de Matriz TF-IDF")

collection,vocabulary = td_matrix(X_raw)

svd = TruncatedSVD(n_components=100)
svd.fit(collection)
sigma = svd.singular_values_
Vt = svd.components_

for i in range(10):
    print("Topico %s: " % i)
    best_terms = [(importance, term) for term, importance in zip(vocabulary, Vt[i])]
    best_terms.sort(reverse=True)
    for importance, term in best_terms[:10]:
        print("Termino: %s, Importancia: %.2E" % (term, importance))

print("--------------------------------------------------------------------------------")
print("Ejercicio 2: Representación en 2D y 3D")

wordsDict = dict()
toktok = ToktokTokenizer()
tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
for txt in X_raw:
    sentences = tokenizer.tokenize(txt)
    for sentence in sentences:
        for token in toktok.tokenize(sentence):
            if token not in wordsDict:
                wordsDict[token] = 0

X_vectors = np.array([])
for i in range(len(X_raw)):
    if len(X_vectors) == 0:        
        X_vectors = vectorizer(X_raw[:].iloc[i],wordsDict.copy())
    else:
        X_vectors = np.vstack([X_vectors,vectorizer(X_raw[:].iloc[i],wordsDict.copy())])

svd2 = TruncatedSVD(n_components=100)
svd2.fit(X_vectors)
Vt2 = svd2.components_

B2 = X_vectors.dot(Vt2[0:2].transpose())
B2_labeled = np.hstack([B2, df[['autor']].to_numpy()])
B2_df = pd.DataFrame(B2_labeled, columns=["x", "y", "autor"])
seaborn.scatterplot(x="x", y="y", hue="autor", legend="full", data=B2_df)
pyplot.show()

B3 = X_vectors.dot(Vt2[0:3].transpose())
B3_labeled = np.hstack([B3, df[['autor']].to_numpy()])
B3_df = pd.DataFrame(B3_labeled, columns=["x", "y", "z", "autor"])
fig = pyplot.figure()
ax = Axes3D(fig)
colors = ["b", "g", "r", "c", "m", "y", "k", "w", "silver", "rosybrown", "darkred", "peru", "yellow", "powderblue", "deeppink", "navy", "seagreen"]
for i, cat in enumerate(list(set(B3_df['autor']))):
    sub_B3_df = B3_df[B3_df['autor'] == cat]
    ax.scatter(sub_B3_df['x'], 
               sub_B3_df['y'], 
               sub_B3_df['z'],
               c=colors[i])
pyplot.show()
