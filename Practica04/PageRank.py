#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón Vázquez
Titulo: Algoritmo de PageRank para textos
Fecha: 05/09/2019
"""
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from Nodo import Nodo
import re

class PageRank:
    nodos = dict()
    def quitarExpresionesRegulares(self,contenido):
        print(re.findall("(\w*\s*){1,}[,]\s\d\d\d\d",contenido))

    def tokenizar(self,fileRoute):
        toktok = ToktokTokenizer()
        esTokenizadorOraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
        archivo = open(fileRoute,"r")
        contenido = archivo.read()
        #self.quitarExpresionesRegulares(contenido)
        oraciones = esTokenizadorOraciones.tokenize(contenido)
        
        oracionesTokenizadas = []
        for oracion in oraciones:
            
            tokens = []
            for token in toktok.tokenize(oracion):
                    tokens.append(token.lower())
            
            oracionesTokenizadas.append(tokens)
        
        return oracionesTokenizadas


    def removerStopwords(self,oraciones):
        stopwordsEspaniol = stopwords.words("spanish")
        
        for oracion in oraciones:
            i = 0
            tamanio = len(oracion)
            while(i<tamanio):
                if oracion[i] in stopwordsEspaniol:
                    oracion.remove(oracion[i])
                    tamanio -= 1
                    continue
                i += 1

        return oraciones

    def lematizarIngenuamente(self,oraciones):
        archivo = open("recursos/lemmatization-es.txt","r",encoding="utf-8-sig")
        lineas = archivo.readlines()
        diccionarioLematizacion = dict()
        for linea in lineas:
            sinSalto = linea.rstrip("\n")
            palabras = sinSalto.split()
            diccionarioLematizacion[palabras[1]] = palabras[0]            

        for oracion in oraciones:
            for token in oracion:
                if token in diccionarioLematizacion.keys():
                    oracion[oracion.index(token)] = diccionarioLematizacion.get(token)
        
        return oraciones

    def PageRank(self,oraciones,iteraciones):
        for oracion in oraciones:
            i0 = 0            
            fin = len(oracion)
            while(i0<fin):
                i1 = i0 + 1
                token0 = oracion[i0]            
                
                if not token0 in self.nodos.keys():
                    self.nodos[token0] = Nodo()
                    self.nodos.get(token0).nombre = token0
                    self.nodos.get(token0).enlaces = set()

                while(i1<fin):
                    token1 = oracion[i1]

                    if not token1 in self.nodos.keys():                    
                        self.nodos[token1] = Nodo()
                        self.nodos.get(token1).nombre = token1
                        self.nodos.get(token1).enlaces = set()
                    
                    if not token1 in self.nodos.get(token0).enlaces:
                        self.nodos.get(token0).enlaces.add(token1)
                    
                    if not token0 in self.nodos.get(token1).enlaces:
                        self.nodos.get(token1).enlaces.add(token0)

                    i1 += 1
                
                i0 += 1    
        
        rankInicial = 1/len(self.nodos)
        for k,v in self.nodos.items():
            v.rank = rankInicial

        for i in range(iteraciones):  
            #print("iteración num. "+str(i+1))  
            for k,v in self.nodos.items():
                sumatoria = 0
                for e in v.enlaces:
                    sumatoria = sumatoria + (self.nodos.get(e).rank/len(self.nodos.get(e).enlaces))
                v.rank = sumatoria

                #print(k + ' tiene un ranking actual de: '+ str(v.rank))
            
                    
                

if __name__ == "__main__":
    pr = PageRank()
    fr = "recursos/analizame.txt"
    tokens = pr.tokenizar(fr)
    #print(pr.removerStopwords(tokens))
    #print("\n")
    #print("\n")
    #print("\n")
    #print(pr.lematizarIngenuamente(tokens))
    #print("\n")
    #print("\n")
    #print("\n")
    pr.PageRank(tokens,1000)
    for nombre,nodo in pr.nodos.items():
        print(nodo.nombre + " tiene un ranking de: "+ str(nodo.rank))