# -*- coding:utf-8 -*-

import sys
import re
import networkx as nx
import matplotlib.pyplot as plt

if len(sys.argv)>=2:
    words = sys.argv.copy()
    del words[0]

    f = open('wikipedia_es_abstracts.txt',"r")
    contents = f.readlines()
    abstractsPassed = ""
    for line in contents:
        mark = True
        for word in words:
            if word not in line:
                mark = False
        if mark:
            abstractsPassed = abstractsPassed + line + "\n"
    
    patron1 = re.compile(r"((la|el|los|las)\s([\w\s]+)\s(es|son)\s([\w\s]+))")
    patron2 = re.compile(r"(([\w,]+)\s(tal como|por ejemplo|como por ejemplo|tal como:|así como|así como)\s([\w,\s]+))")
    patron3 = re.compile(r"(([\w\s]+)\s(forma parte (de|del))\s([\w\s]+))")
    patron4 = re.compile(r"(([\w\s]+)\s(perteneciente|pertenece|pertenecientes|pertenecen)\s([\w\s]+))")
    
    repatron1 = patron1.findall(abstractsPassed)
    repatron2 = patron2.findall(abstractsPassed)
    repatron3 = patron3.findall(abstractsPassed)
    repatron4 = patron4.findall(abstractsPassed)

    nodes = []
    aristas = []
    for match in repatron1:
        if match[2] not in nodes:
            nodes.append(match[2])
        if match[2] not in nodes:
            nodes.append(match[4])
        aristas.append((match[2],match[4]))
        
    for match in repatron2:
        if match[1] not in nodes:
            nodes.append(match[1])
        if match[3] not in nodes:
            nodes.append(match[3])
        aristas.append((match[1],match[3]))

    for match in repatron3:
        if match[1] not in nodes:
            nodes.append(match[1])
        if match[4] not in nodes:
            nodes.append(match[4])
        aristas.append((match[1],match[4]))
            
    for match in repatron4:
        if match[1] not in nodes:
            nodes.append(match[1])
        if match[3] not in nodes:
            nodes.append(match[3])
        aristas.append((match[1],match[3]))
    
    G = nx.DiGraph()    
    G.add_nodes_from(nodes)
    G.add_edges_from(aristas)
    pos=nx.spring_layout(G)
    nx.draw_networkx_labels(G, pos, labels=dict([(i,i) for i in nodes]))
    nx.draw(G,pos)
    plt.show()

else:
    print("sin parametros de entrada, saliendo del script")