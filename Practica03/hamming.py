#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Distancia de Hamming
Fecha: 29/08/2019
"""

word1 = input("Introduzca una palabra: ")
word2 = input("Introduzca OTRA palabra del mismo tamaño: ")

if len(word1) == len(word2):
    word1ls = list(word1)
    word2ls = list(word2)
    count = 0
    for i in range(len(word1)):
        if not word1ls[i] == word2ls[i]:
            count = count + 1
        
    print("hamming("+word1+", "+word2+") = "+str(count))
else:
    print("Las palabras son de diferente tamaño, no se puede ejecutar la prueba")