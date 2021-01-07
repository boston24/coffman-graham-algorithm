from node import Node
from graph import Graph

list = []
z1 = Node("z1",[],[])
z2 = Node("z2",[],[])
z3 = Node("z3",[],[])
z4 = Node("z4",[],[])
z5 = Node("z5",[],[])
z6 = Node("z6",[],[])
z7 = Node("z7",[],[])
z8 = Node("z8",[],[])

z1.addKids([z3,z4])
z2.addKids([z3,z4])
z3.addKids([z4,z5,z6,z7])
z4.addKids([z5,z6])
z5.addKids([z7,z8])
z6.addKids([z7,z8])
z7.addKids([z8])

list.clear()
list.append(z1)
list.append(z2)
list.append(z3)
list.append(z4)
list.append(z5)
list.append(z6)
list.append(z7)
list.append(z8)


#graph = Graph(list)