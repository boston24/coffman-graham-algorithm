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

    if iteration == 1: 
        iteration_list = makeListStart
    else:
        iteration_list = makeList

def makeListStart():
    out = []
    for node in list:
        if not node.kids:
            out.append(node) 

graph = Graph(list)

graph.showGraph([])      
#graph.showTimeline(makeListForTimetable(list))      
