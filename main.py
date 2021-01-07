import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from node import Node
from graph import Graph
from data import *
from networkx.drawing.nx_agraph import graphviz_layout
import plotly.express as px

def start():
    n = len(list)
    iteration = 1
    iteration_list = []
    iteration_list_temp = []

    while iteration<=n:

        if iteration == 1: 
            iteration_list = makeListStart()
        else:
            print("--------------------------------------------")
            iteration_list_temp = []
            
            for node in iteration_list:
                for parent in node.parents:
                    if parent not in iteration_list_temp:
                        iteration_list_temp.append(parent)
            
            iteration_list = []
            
            '''
            print("Temporary iteration list: ",end="[ ")
            for task in iteration_list_temp:
                print(task.name, end=" ")
            print("]")'''

            for node in iteration_list_temp:
                check = 1
                for kid in node.kids:
                    if kid.label == None:
                        check = 0
                    else:
                        if kid.label not in node.s_list:
                            node.s_list.append(kid.label)
                if check == 1:
                    iteration_list.append(node)
        
        for node in iteration_list:
            node.s_list = sorted(node.s_list, reverse=True)

        print("Iteration no. "+str(iteration))
        print("A = ",end="{ ")
        for task in iteration_list:
            print(task.name, end=" ")
        print("}")

        sorted_by_s_list = sorted(iteration_list, key=lambda x: (len(x.s_list),sum(x.s_list)))

        print("A (sorted) = ",end="{ ")
        for task in sorted_by_s_list:
            print(task.name, end=" ")
        print("}")

        for node in sorted_by_s_list:
            node.label = iteration
            print("Set label of "+str(node.name)+" with "+str(iteration))
            iteration += 1

def makeListStart():
    out = []
    for node in list:
        if not node.kids:
            out.append(node) 
    return out


start()

for node in list:
    print("\nTask: "+str(node.name)+", label="+str(node.label)+", s_list: ",end="[ ")
    for i in node.s_list:
        print(i, end=" ")
    print("]")

#graph = Graph(list)
#graph.showGraph([]) 
#graph.showTimeline(makeListForTimetable(list))      
