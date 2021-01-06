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

    while iteration<n:
            
        ##if iteration == 4:
        ##    iteration = n

        iteration_list_temp = iteration_list
        iteration_list = []

        if iteration == 1: 
            iteration_list = makeListStart()

        else:
            for node in iteration_list_temp:
                for kid in node.kids:
                    check = 1
                    for parent in kid.parents:
                        if parent.label == None:
                            check = 0
                    if check == 1:
                        iteration_list.append(kid)

        iteration_list = sorted(iteration_list, key=lambda x: x.name)

        print("Iteration no. "+str(iteration))
        print("Tasks to label: ",end="[ ")
        for task in iteration_list:
            print(task.name, end=" ")
        print("]")

        for node in iteration_list:
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

#graph = Graph(list)
#graph.showGraph([]) 
#graph.showTimeline(makeListForTimetable(list))      
