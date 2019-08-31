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
from nltk.metrics.distance import edit_distance

data = set()
l = open("recursos/lemmatization-es.txt","r")
lines = l.readlines()
for line in lines:
    temp = line.rstrip("\n")
    word = temp.split("	")
    data.add(word[0])
    data.add(word[1])

l = open("recursos/listado-general.txt","r")
lines = l.readlines()
for line in lines:
    temp = line.rstrip("\n")
    data.add(temp)

toktok = ToktokTokenizer()
esTokenizadorOraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')   
stpwds = stopwords.words("spanish")
puntiaction = ["?", "¿", "¡", "!", " ", ",", ".", ";", ":", "(", ")", "-", "...", "\"", "”", "–", "%", "“", "\n"]

l = open("recursos/corrigeme.txt","r")
contents = l.read()
oraciones = esTokenizadorOraciones.tokenize(contents)
ef = open("recursos/corregido.txt","w")
for oracion in oraciones:
    corrline = []
    for t in toktok.tokenize(oracion):
        print("testing", t)
        if (t.lower() in stpwds) or (t.lower() in puntiaction) or (t.lower() in data):
            corrline.append(t)
        else:
            val = ""
            minv = 1000
            for cword in data:
                ed = edit_distance(t,cword)
                if ed<minv:
                    minv = ed
                    val = cword
            
            corrline.append(val)
    print(corrline)
    separator = " "
    ef.write(separator.join(corrline))
    ef.write("\n")

