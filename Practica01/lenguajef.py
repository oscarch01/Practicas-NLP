#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Lenguaje de la F
Fecha: 15/08/2019
"""

text = input("Introduzca una frase o palabra: ")

text = text.lower()

text = text.replace("a","afa")
text = text.replace("e","efe")
text = text.replace("i","ifi")
text = text.replace("o","ofo")
text = text.replace("u","ufu")

text = text.replace("á","áfa")
text = text.replace("é","éfe")
text = text.replace("í","ífi")
text = text.replace("ó","ófo")
text = text.replace("ú","úfu")

textarr = text.split()

text = ""

for word in textarr:
    if word.endswith("y") and len(word)>1:
        word = word + "fi"
        text += word + " "
    else:
        text += word + " "
    
print("Su frase es: ",text)