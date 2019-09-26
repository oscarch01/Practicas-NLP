# -*- coding:utf-8 -*-

import sys
import re
import networkx as nx
import matplotlib.pyplot as plt

if len(sys.argv)>=2:
    words = sys.argv.copy()
    del words[0]

    f = open('wikipedia_es_abstracts.txt',"r",encoding="utf8")
    contents = f.readlines()
    abstractsPassed = ""
    for line in contents:
        mark = True
        for word in words:
            if word not in line:
                mark = False
        if mark:
            abstractsPassed = abstractsPassed + line + "\n"
    
    patron1 = re.compile(r"((la|el|los|las|un|unos|una|unas)\s([á-úü\w]+)\s(es el|es la|es más|es una|es un|es también una|es|son los|son las|son una|son un|fue un|son)\s([á-úü\w]+))")
    patron2 = re.compile(r"(([á-úü\w]+)\s(tal como|así tambien|así como|como por|por ejemplo|tambien conocida como|tambien conocido como|tal como:|conocida como|como:|como un|como una de los|como uno de los|como una de las|como una|como uno|como)\s([á-úü\w]+))")
    patron3 = re.compile(r"(([á-úü\w]+)\s(forma parte (de la|del|de))\s([á-úü\w]+))")
    patron4 = re.compile(r"(([á-úü\w]+)\s(que pertenece|que pertenece al|pertenece|perteneciente al|perteneciente)\s([á-úü\w]+))")
    
    repatron1 = patron1.findall(abstractsPassed)
    repatron2 = patron2.findall(abstractsPassed)
    repatron3 = patron3.findall(abstractsPassed)
    repatron4 = patron4.findall(abstractsPassed)

    nodes = []
    edges = []
    for match in repatron1:
        if match[2] not in nodes:
            nodes.append(match[2])
        if match[4] not in nodes:
            nodes.append(match[4])
        edges.append((match[2],match[4]))
        
    for match in repatron2:
        if match[1] not in nodes:
            nodes.append(match[1])
        if match[3] not in nodes:
            nodes.append(match[3])
        edges.append((match[1],match[3]))

    for match in repatron3:
        if match[1] not in nodes:
            nodes.append(match[1])
        if match[4] not in nodes:
            nodes.append(match[4])
        edges.append((match[1],match[4]))
            
    for match in repatron4:
        if match[1] not in nodes:
            nodes.append(match[1])
        if match[3] not in nodes:
            nodes.append(match[3])
        edges.append((match[1],match[3]))
    
    print(abstractsPassed)
    print("---------")
    print(nodes)
    print("---------")
    print(edges)

    G = nx.DiGraph()    
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    pos=nx.spring_layout(G)
    nx.draw_networkx_labels(G, pos, labels=dict([(i,i) for i in nodes]))
    nx.draw(G,pos)
    plt.show()

else:
    print("sin parametros de entrada, saliendo del script")