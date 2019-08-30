# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Sumatoria 1 a 1 hasta n
Fecha: 15/08/2019
"""

n = input("Introduzca un número: ")

try:
    n = int(n)
    res = 0;
    for x in range(n):
        res = res + (x+1)
    print("El Resultado es: ",res)
except ValueError:
    print("No ha introducido un número")