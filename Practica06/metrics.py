#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Función de calculo de presición de los resultados de regresión logística
Fecha: 10/10/2019
"""

def precision(predicted,baseline):
    sumatoryI = 0
    size = len(predicted)
    for i in range(size):
        I = 0
        if predicted[i] == baseline[i]:
            I = 1
        sumatoryI += I
    
    result = (1/size) * sumatoryI

    return result