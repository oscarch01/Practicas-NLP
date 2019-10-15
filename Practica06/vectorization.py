#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Oscar Chacón
Titulo: Vectorización para clasificación de regresión logística
Fecha: 10/10/2019
"""

import numpy as np
import nltk
from nltk.tokenize.toktok import ToktokTokenizer

def vectorizer(raw_text):
    toktok = ToktokTokenizer()
    tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
    sentences = tokenizer.tokenize(raw_text)

    vector = []

    counterCommas = 0
    countersWordsInSentence = []
    for sentence in sentences:
        counterCommas += sentence.count(",")
        countersWordsInSentence.append(len(toktok.tokenize(sentence)))

    vector.append(counterCommas)

    sumatory = 0
    for counter in countersWordsInSentence:
        sumatory += counter

    averageWordsInSentence = sumatory/len(countersWordsInSentence)

    vector.append(averageWordsInSentence)

    vector.append(len(sentences))

    return np.array(vector)
    
def baselineMajorityClass(y_train,lenY_test):
    dictionaryOfCounters = dict()
    for y in y_train:
        if y not in dictionaryOfCounters:
            dictionaryOfCounters[y] = 1
        else:
            dictionaryOfCounters[y] += 1
    
    majorityKey = ''
    majorityValue = 0

    for key,value in dictionaryOfCounters.items():
        if value > majorityValue:
            majorityValue = value
            majorityKey = key

    vectorFake = []
    for i  in range(lenY_test):
        vectorFake.append(majorityKey)
    
    return np.array(vectorFake)

if __name__ == "__main__":
    text = "Por los códices pictográficos se tiene noticia de las alianzas matrimoniales que emparentaron a los nobles de la Mixteca Alta con los de la Mixteca Baja y el Valle de Puebla-Tlaxcala. En los códices de la Mixteca Alta aparece Tula y también el sacerdote de Quetzalcóatl que vivía en aquella ciudad. Uno de los hechos que subyace en la unificación ceremonial y cortesana bajo la tradición Mixteca-Puebla es el acercamiento de las élites, que buscaban fortalecerse mutuamente y construían una ideología común. La importancia de la ciudad de Tula en sus respectivas historias, la presencia del hombre-dios Quetzalcóatl, la práctica de la confirmación del mando en un reino que funcionaría como capital fueron rasgos de una ideología tolteca, que unificaba también a las élites del Posclásico. ¿Tuvo la ciudad de Tula (Tula, Hidalgo) un papel preponderante en la elaboración de las ideas políticas y religiosas que darían soporte al poder durante el Posclásico? ¿Y llevó Cholula la batuta en lo tocante a la consolidación cultural, artística, de ese vínculo que unía a los nobles en el Posclásico? Probablemente. En todo caso parecería que las noblezas mesoamericanas habían aprendido la lección de la crisis teotihuacana. Preferían favorecer un apoyo común, antes que disputarse sólo el poder regional."
    print(vectorizer(text))