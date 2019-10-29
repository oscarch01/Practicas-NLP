#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Matriz TF*IDF
Fecha: 24/10/2019
"""
import nltk
import math
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


def tokenize(line):
    toktok = ToktokTokenizer()
    tokens = []
    for t in toktok.tokenize(line):
        tokens.append(t.lower())
    return tokens

def lemmatize(tokens,lemDicGen):
    l = open("recursos/lemmatization-es.txt","r",encoding="utf-8")
    lines = l.readlines()
    lemdic = dict()
    if lemDicGen != '':
        lemdic = lemDicGen
    else:        
        for line in lines:
            temp = line.rstrip("\n")
            word = temp.split("	")
            lemdic[word[1]] = word[0]
        lemDicGen = lemdic
    
    for t in tokens:
        if t in lemdic.keys():
            tokens[tokens.index(t)] = lemdic.get(t)    
    return tokens,lemDicGen

def removeStopwords(tokens):
    leng = len(tokens)
    stpwds = stopwords.words("spanish")
    puntiaction = ["?", "¿", "¡", "!", " ", ",", ".", ";", ":", "(", ")", "-", "...", "\"", "”", "–", "%", "“", "|", "||", ".."]
    i=0
    while (i<leng):    
        if tokens[i] in stpwds:
            tokens.remove(tokens[i])
            leng -= 1
            continue
        if tokens[i] in puntiaction:
            tokens.remove(tokens[i])
            leng -= 1
            continue
        i += 1
    return tokens

def readfile(fileroute):
    f = open(fileroute,"r",encoding="utf-8")
    lines = f.readlines()
    return lines

def normalize(D):
    normalized_D = []
    vocabulary = []
    lemDicGen = ''
    for d in D:    
        d = tokenize(d)
        d = removeStopwords(d)
        d,lemDicGen = lemmatize(d,lemDicGen)
        for w in d:
            if w not in vocabulary:
                vocabulary.append(w)
        normalized_D.append(d)
    return normalized_D,vocabulary
    
def tfidf(t,d,D):
    countOft = d.count(t)
    tf = countOft/len(d)
    countOftinv = 0
    for dinv in D:
        countOftinv += dinv.count(t)
    idf = math.log(len(D)/countOftinv)
    return tf*idf

def td_matrix(D):
    normalized_D,vocabulary = normalize(D)        
    vocabulary.sort()
    collection = []
    for d in normalized_D:
        #For testing
        print(d)

        d_vector = []
        for t in vocabulary:
            d_vector.append(tfidf(t, d, normalized_D))
        collection.append(d_vector)
    return collection,vocabulary

def cos(a,b):
    lng = len(a)
    sumaxb = 0
    sumaacuad = 0
    sumabcuad = 0
    for i in range(lng):
        sumaxb += a[i] * b[i]
        sumaacuad += a[i] * a[i]
        sumabcuad += b[i] * b[i]
    return sumaxb/(math.sqrt(sumaacuad)*math.sqrt(sumabcuad))  

def cos_matrix(td_matrix):
    collection = []
    for d1 in td_matrix:
        d1CosVect = [] 
        for d2 in td_matrix:
            d1CosVect.append(cos(d1,d2))
        collection.append(d1CosVect)
    return collection

def print_matrix(matrix):
    lenDocuments = len(matrix)
    print("DX",end = '')
    print("\t",end = '')    
    for i in range(lenDocuments):
        pi = i+1
        print("D"+str(pi),end = '')
        print("\t",end = '')
    print("\n")
    count1 = 1
    for d1 in matrix:
        print("D"+str(count1),end = '')
        print("\t",end = '')
        for d2 in d1:
            print(d2,end = '')
            print("\t",end = '')
        print("\n")
        count1 += 1

def print_to_csv_file(matrix):
    csvf = open("matrix.csv","w+")
    lenDocuments = len(matrix)
    csvf.write("DX")
    csvf.write(",")    
    for i in range(lenDocuments):
        pi = i+1
        csvf.write("D"+str(pi))
        csvf.write(",")
    csvf.write("\n")
    count1 = 1
    for d1 in matrix:
        csvf.write("D"+str(count1))
        csvf.write(",")
        for d2 in d1:
            csvf.write(str(d2))
            csvf.write(",")
        csvf.write("\n")
        count1 += 1