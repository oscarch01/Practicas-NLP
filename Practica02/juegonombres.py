#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Juego de Nombres
Fecha: 22/08/2019
"""
from agente import Agente
import random

n = 14
m = 7
max_t = 1000
agentes = []

for x in range(n):
    agentes.append(Agente(m))

for t in range(max_t):
    bandera = True
    selectedAgentA = random.randint(0,n-1)
    selectedAgentB = random.randint(0,n-1)
    selectedObject = random.randint(0,m-1)
    while selectedAgentA == selectedAgentB:
        selectedAgentB = random.randint(0,n-1)
    
    agentes[selectedAgentA].enunciar(selectedObject,agentes[selectedAgentB])
    
    palabrasAContar = [[] for i in range(m)]

    for agente in agentes:
        for o in range(m):
            if len(agente.O[o]) == 0:
                bandera = False
            for palabra in agente.O[o]:
                if not palabra in palabrasAContar[o]:
                    palabrasAContar[o].append(palabra)
                if len(palabrasAContar[o])>1:
                    bandera = False

    contNombresTotales = 0
    longTotal = 0
    for l in palabrasAContar:
        contNombresTotales += len(l)
        for w in l:
            longTotal += len(w)

    print("interacción: "+str(t)+", "+"Nombres totales: "+str(contNombresTotales)+"")
    for x in range(m):
        print("Nombres para el Objeto "+str(x)+": "+str(len(palabrasAContar[x])))
    print("Longitud promedio de los nombres: "+str(longTotal/contNombresTotales))

    #print("Interacción " + str(t))
    #for x in range(n):
    #    print("Agente " + str(x) + " tiene ")
    #    print(agentes[x].O)

    print("------------------------------------------------------------")
    if bandera:
        break

            