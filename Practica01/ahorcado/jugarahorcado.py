#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Programa para Clase Ahorcado
Fecha: 15/08/2019
"""

from ahorcado import Ahorcado
import random

f=open("listado.txt", "r")
words = f.readlines()

word = words[random.randint(0,80383)]
word = word[:-1]
errors = random.randint(3,7)

ahorcado = Ahorcado(word,errors)

while 1:
    ahorcado.estado()
    if ahorcado.errores()==errors:
        break
    ch = input("introduzca una letra: ")
    ahorcado.jugar(ch)