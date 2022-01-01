#!/usr/bin/python
#
# Author: Alexander Castro
# Description: A Python implementation of the A* search algorithm.
#
from __future__ import print_function
from math import sqrt

#
# A dictionary defining the x,y coordinates of each city string name
#
location={"arad":(1.75,10.75), "zerind":(2.5,12.5), "sibiu":(6.75,9.25),
          "timisoara":(1.75,7), "oradea":(3.3,14), "lugoj":(4.8,5.8),
          "mehadia":(5,4), "drobeta":(4.8,2.5), "craiova":(8.75,1.75),
          "rimnicu":(8,7), "fagaras":(10.5, 9), "pitesti":(11.75,5.25),
          "bucharest":(15,3.5), "giurgiu":(14,1) }
#
# A list of the distances between cities in the map.
#
map = [("arad","zerind",75),
       ("arad","sibiu",140),
       ("arad","timisoara",118),
       ("zerind","oradea",71),
       ("oradea","sibiu",151),
       ("timisoara","lugoj",111),
       ("lugoj","mehadia",70),
       ("mehadia","drobeta",75),
       ("drobeta","craiova",120),
       ("craiova","rimnicu",146),
       ("rimnicu","sibiu",80),
       ("craiova","pitesti",138),
       ("rimnicu","pitesti",97),
       ("sibiu","fagaras",99),
       ("pitesti","bucharest",101),
       ("fagaras","bucharest",211),
       ("giurgiu","bucharest",90)]

#
# A list of the routes we will use for testing, designating starting and ending cities in tuples.
#
routes = [('arad','bucharest'),    # Optimal path: Arad-140-Sibiu-80-Rimnicu-97-Pitesti-101-Bucharest (total 418)
          ('arad','oradea'),       # Optimal path: Arad-75-Zerind-71-Oradea (total 146)
          ('sibiu','bucharest'),   # Optimal path: Sibiu-80-Rimnicu-97-Pitesti-101-Bucharest (total 278)
          ('rimnicu','drobeta'),   # Optimal path: Rimnicu-146-Craiova-120-Dobreta (total 266)
          ('timisoara','craiova'), # Optimal path: Timisoara-111-Lugoj-70-Mehadia-75-Dobreta-120-Craiova (total 376)
          ('pitesti','oradea')]    # Optimal path: Pitesti-97-Rimnicu-80-Sibiu-151-Oradea (total 328)

roadmap=map

#
# Define the heuristic functions. Each function accepts two strings, start city and end city, and uses the location dictionary to retrieve the coordinates and perform operations.
#
def h_sld(start,end):
    # Heuristic 1: Straight Line Distance ((x2-x1)^2 + (y2-y1)^2)^1/2
    return sqrt((location[end][0] - location[start][0])**2 + (location[end][1] - location[start][1])**2)
def h_md(start,end):
    # Heuristic 2: Manhattan Distance (x2-x1)+(y2-y1)
    return sqrt(abs(location[end][0] - location[start][0]) + abs(location[end][1] - location[start][1]))
def h_sum(start,end):
    # Heuristic 3: Sum of heuristics 1 and 2
    return h_sld(start,end) + h_md(start,end)
def h_avg(start,end):
    #Heuristic 4: Average of heuristics 1 and 2
    return (h_sld(start,end) + h_md(start,end)) / 2

#
# Map possible inputs to heuristic functions.
#
h_options = {1 : h_sld, 2 : h_md, 3 : h_sum, 4 : h_avg}

#
# Successor fn: successor(state,action)=list of states arrived at after action in state
#
def successor(roadmap,city):
    """generate list of successors of startcity in roadmap"""
    # assumes format of roadmap and that city is a strong
    successorList=[]
    for mapentry in roadmap:
        if mapentry[0]==city:
            successorList.append( (mapentry[1], mapentry[2]) )
        elif mapentry[1]==city:
            successorList.append( (mapentry[0], mapentry[2]) )
    return successorList

def ASTARtreesearch(fringe,goal,h_num):
    # Carry out a tree search for goal from node in fringe
    rubbish = list() # list of already searched cities
    ASTARcounter = 0 # simple counter to show number of A* searches performed
    print('\nA* Search from',fringe[0][0],'to',goal)
    print('{:>5s}{:>20s}{:>20s}'.format('count', 'root', 'fmin'))
    for x in range(45):
        print('-', end="")
    print('\n', end="")

    while len(fringe)>0:
        rootnode = fringe[0] # Strategy: pick min. f(n)
        g = rootnode[1] # Cost so far to reach node
        h = h_options[h_num](rootnode[0],goal) # Estimated cost from node to goal
        fmin = g + h
        for node in fringe:
            g = node[1]
            h = h_options[h_num](node[0],goal)
            f  = g + h
            if f < fmin:
                rootnode = node # find smallest
                fmin = f
        fringe.remove(rootnode) # 'pop' minium f(n) from fringe
        root = rootnode[0]
        #print('ASTAR Searches #', ASTARcounter,' ', root,' A* cost ', fmin)
        ASTARcounter += 1
        print('{:5}{:>20s}{:>20f}'.format(ASTARcounter, root, fmin))
        if root == goal:
            print('Found goal')
            return rootnode[2] + [goal]
        nextcitylist = successor(roadmap,root) # Assumes global scope roadmap
        rubbish.append(root)
        fringecity = list() #can't check fringe directly for duplicates
        for searchnode in fringe:
            fringecity.append(searchnode[0])
        for mapentry in nextcitylist:
            city = mapentry[0]
            stepcost = mapentry[1]
            if (city not in fringecity) and (city not in rubbish):
                newnode = [city,rootnode[1] + stepcost, rootnode[2] + [root]]
                fringe.append(newnode)
    return "No route to "+goal;

#
# Print user interaction guide and input options
#
print('Enter a number to select a heuristic\n1: Straight Line Distance 2: Manhattan Distance\n3: Sum of first two heuristics 4: Average of first two heuristics\n')

#
# Prompts user input to select heuristic and validates input and onl
#
while True:
     try:
         input_h_num = int(raw_input("Heuristic selected: "))
         if 1 <= input_h_num <= 4:
             break
     except ValueError:
        pass
     print('Sorry, you must enter a number between 1 and 4 to select a heuristic.')

for route in routes:
#myfringe = [ ['arad', 0, []] ]
    myfringe = [ [route[0], 0, []] ]
    ASTARtreesearch(myfringe,route[1],input_h_num)
