#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Clase agente
Fecha: 22/08/2019
"""
import random

class Agente:
    m = 0
    O = []
    vocales = ['a','e','i','o','u']
    consonantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    
    def __init__(self,m):
        self.m = m
        self.O = [[] for i in range(m)]

    def nombrar(self):
        longitud = random.randint(1,8)
        contador = 0
        nombre = ""
        while contador<longitud:
            nombre = nombre + self.consonantes[random.randint(0,20)]
            nombre = nombre + self.vocales[random.randint(0,4)]
            contador += 1
        return nombre

    def enunciar(self,k,oyente):
        nombre = ""
        resultado = False

        if len(self.O[k]) == 0:
            nombre = self.nombrar()
            self.O[k].append(nombre)
        else:
            nombre = min(self.O[k],key=len)

        if nombre in oyente.O[k]:
            self.O[k] = [nombre]
            oyente.O[k] = [nombre]
            resultado  = True
        else:
            oyente.O[k].append(nombre)
            resultado = False

        return resultado