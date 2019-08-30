#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Clase Ahorcado
Fecha: 15/08/2019
"""


class Ahorcado:
    p = ""
    characters = list()
    e = 0
    E = 0
    
    def __init__(self,p,E):
        self.p = p
        self.E = E
        
    def jugar(self,c):
        if len(c)>1:
            print("Error, solamente se acepta un caracter")
        else:
            if c in self.p:
                self.characters.append(c)
            else:
                self.e += 1
    
    def errores(self):
        return self.e
                
    def estado(self):
        tempList = list(self.p)
        band = 1
        for c in tempList:
            if c in self.characters or self.e == self.E:
                print(c," ",end="")
            else:
                print("_"," ",end="")
                band = 0
                
        if self.e < self.E and band == 0:
            print("(",self.E-self.e," errores posibles)")
        elif band == 1 and self.e == self.E:
            print("(PERDISTE)")
        else:
            print("(GANASTE)")
            self.e = self.E