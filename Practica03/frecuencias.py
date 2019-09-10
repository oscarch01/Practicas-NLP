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
from nltk.stem.snowball import SnowballStemmer

def tokenizar(fileroute):
    toktok = ToktokTokenizer()
    esTokenizadorOraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
    f = open(fileroute,"r")
    contents = f.read()
    oraciones = esTokenizadorOraciones.tokenize(contents)
    data = []
    for oracion in oraciones:
        for t in toktok.tokenize(oracion):
                data.append(t.lower())
    return data

def frecuencias(tokens):
    frec = dict()
    for token in tokens:
        if token in frec:
            frec[token] += 1
        else:
            frec[token] = 1
    return frec

def removestopwords(tokens):
    tnk = tokens
    leng = len (tnk)
    stpwds = stopwords.words("spanish")
    puntiaction = ["?", "¿", "¡", "!", " ", ",", ".", ";", ":", "(", ")", "-", "...", "\"", "”", "–", "%", "“"]
    i=0
    while (i<leng):    
        if tnk[i] in stpwds:
            tnk.remove(tnk[i])
            leng -= 1
            continue
        if tnk[i] in puntiaction:
            tnk.remove(tnk[i])
            leng -= 1
            continue
        i += 1
    return tnk

def sorttokens(tokens):
    frecsorted = sorted(frec.items(),key=lambda x: x[1])
    return frecsorted

def stemming(tokens):
    data = []
    stemmer = SnowballStemmer("spanish")
    for t in tokens:
        data.append(stemmer.stem(t))
    return data

def lematizacionIngenua(tokens):
    tk = tokens
    l = open("recursos/lemmatization-es.txt","r")
    lines = l.readlines()
    lemdic = dict()
    for line in lines:
        temp = line.rstrip("\n")
        word = temp.split("	")
        lemdic[word[1]] = word[0]

    for t in tk:
        if t in lemdic.keys():
            tk[tk.index(t)] = lemdic.get(t)
    
    return tk

if __name__ == "__main__":
    route = input("Escriba la ruta de su archivo a analizar: ")
    #route = "recursos/practica3.txt"
    data = tokenizar(route)
    data2 = removestopwords(data)
    print("Distribución de frecuencias (sin stopwords) para archivo: ", route)
    frec = frecuencias(data2)
    frecsorted = sorttokens(frec)        
    for element in frecsorted:
        print(element[0], " => ", element[1])

    data3 = stemming(data2)
    print("Distribución de frecuencias (sin stopwords, con stemming) para archivo: ", route)
    frec = frecuencias(data3)
    frecsorted = sorttokens(frec)        
    for element in frecsorted:
        print(element[0], " => ", element[1])

    data4 = lematizacionIngenua(data2)
    print("Distribución de frecuencias (sin stopwords, con lematizacion) para archivo: ", route)
    frec = frecuencias(data4)
    frecsorted = sorttokens(frec)        
    for element in frecsorted:
        print(element[0], " => ", element[1])