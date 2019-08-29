#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Distancia de Hamming
Fecha: 29/08/2019
"""
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

def tokenizar(fileroute):
    toktok = ToktokTokenizer()
    esTokenizadorOraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
    f = open(fileroute,"r")
    contents = f.read()
    oraciones = esTokenizadorOraciones.tokenize(contents)
    data = []
    for oracion in oraciones:
        for t in toktok.tokenize(oracion):
                data.append(t)
    return data

def frecuencias(tokens):
    frec = dict()
    for token in tokens:
        if token in frec:
            frec[token] += 1
        else:
            frec[token] = 1
    return frec

def removestopwords():
    print(stopwords.words("spanish"))

if __name__ == "__main__":
    data = tokenizar('recursos/practica3.txt')
    frec = frecuencias(data)
    frecsorted = sorted(frec.items(),key=lambda x: x[1])
    
    for element in frecsorted:
        print(element[0], " => ", element[1])

    removestopwords()