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
    selectedAgentA = random.randint(0,n-1)
    selectedAgentB = random.randint(0,n-1)
    selectedObject = random.randint(0,m-1)
    while selectedAgentA == selectedAgentB:
        selectedAgentB = random.randint(0,n-1)
    
    agentes[selectedAgentA].enunciar(selectedObject,agentes[selectedAgentB])

    print("Interacción " + str(t))
    for x in range(n):
        print("Agente " + str(x) + " tiene ")
        print(agentes[x].O)

    print("------------------------------------------------------------")

            