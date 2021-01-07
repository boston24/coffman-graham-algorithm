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

def makeListForTimetable(list,cpu):
    jobs = []
    tasks_in_row = [[] for _ in range(len(list))]

    counter = 0

    for node in list:
        if counter == 0:
            tasks_in_row[0].append(node)
        else:           
            i=0
            while i<len(tasks_in_row):
                check = True
                for task in tasks_in_row[i]:
                    print("Is "+str(task.name)+" in "+str(node.name))
                    if isPrevious(task,node):
                        print("Yes")
                        check = False
                        break
                if not check or len(tasks_in_row[i])>=cpu:
                    i += 1
                else:
                    print("Adding "+str(node.name)+" in column no."+str(i))
                    tasks_in_row[i].append(node)
                    i = len(tasks_in_row)
        counter +=1


    for col in tasks_in_row:
        print("\n")
        for task in col:
            print(task.name,end=" ")


        #jobs.append(dict(Name=name, Start=start, Finish=finish, Row=free_space[0], Time=time))
    
    return 1

def isPrevious(n1,n2):
    if n1 == n2:
        return True
    else:
        for parent in n2.parents:
            if isPrevious(n1,parent):
                return True


start()
graph = Graph(list)


for node in list:
    print("\nTask: "+str(node.name)+", label="+str(node.label)+", s_list: ",end="[ ")
    for i in node.s_list:
        print(i, end=" ")
    print("]")

ordered_by_label = []
ordered_by_label = sorted(list, key=lambda x : x.label, reverse=True)
print("\nOrdered by label = ", end="{ ")
for node in ordered_by_label:
    print(node.name, end=" ")
print("}\n")

#graph.showTimeline(makeListForTimetable(ordered_by_label))
makeListForTimetable(ordered_by_label,2)

#graph.showGraph([]) 
#graph.showTimeline(makeListForTimetable(list))      
