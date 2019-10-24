#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Clasificador de regresión logística
Fecha: 10/10/2019
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from metrics import precision
from vectorization import vectorizerV2 as vectorizer
from vectorization import baselineMajorityClass

import nltk
from nltk.tokenize.toktok import ToktokTokenizer

df = pd.read_csv('author_corpus.txt',sep='\t',index_col=False,names=["autor","texto"])

# Remueve autor 5, que es igual al 4
df = df[:][df['autor']!=5]

X_raw = df['texto']

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

y = df['autor'].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X_vectors,y,test_size=0.3,random_state=101)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

y_fake = baselineMajorityClass(y_train,len(y_test))

print('\nPrecisión Baseline: {0}'.format(precision(y_test, y_fake)))
print('\nPrecisión Regresión: {0}'.format(precision(y_pred, y_test)))