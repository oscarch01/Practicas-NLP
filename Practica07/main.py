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

df = pd.read_csv('author_corpus.txt',sep='\t',index_col=False,names=["autor","texto"])

# Remueve autor 5, que es igual al 4
df = df[:][df['autor']!=5]

X_raw = df['texto']

collection,vocabulary = td_matrix(X_raw)

print(collection)