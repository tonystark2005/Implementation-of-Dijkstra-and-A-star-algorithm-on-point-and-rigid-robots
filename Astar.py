# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:58:05 2019

@author: sanke
"""

from __future__ import print_function
import Create_Map_Astar as gr
import collections

radius=input("Enter radius: ")
radius=int(radius)
clearance=input("Enter clearance: ")
clearance=int(clearance)
resolution=input("Enter resolution: ")
resolution=float(resolution)
start=input("Enter Start point separated by space: ")
start=start.split(' ')
start = list(map(int, start))
goal=input("Enter goal point separated by space: ")
goal=goal.split(' ')
goal = list(map(int, goal))

start[0]=int(start[0]/resolution)
start[1]=int(start[1]/resolution)
goal[0]=int(goal[0]/resolution)
goal[1]=int(goal[1]/resolution)


while True:
    if start[0]<0 or start[0]>int(249/resolution) or start[1]<0 or start[1]>int(149/resolution):
        print("Try again: Start is not inside the map")
        break
    while True:
        if goal[0]<0 or goal[0]>int(249/resolution) or goal[1]<0 or goal[1]>int(149/resolution):
            print("Try again")
            break

 
        elements=gr.elements(radius,clearance,resolution)
        if tuple(goal) in elements==False:
                print("Goal is in obstacle space")
        class AStarMap(object):
            
            def heuristic(self, start, goal):
        		#Use Manhattan distance heuristic if we can move one square either
        		#adjacent or diagonal
                dx= abs(start[0] - goal[0])
                dy= abs(start[1] - goal[1])
                return dx + dy
            
            def get_vertex_neighbours(self, pos):
                n= []
        		#Moves allow link a chess king
                if pos in elements:
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
                        x2= pos[0] + dx
                        y2 = pos[1] + dy
                        if (x2,y2) in elements:
                            n.append((x2, y2))
                return n
        
            def move_cost(self, a, b):
                if(abs(a[0]-b[0])==1 and abs(a[1]-b[1])==1):
                    return 2**0.5
                elif (abs(a[0]-b[0])==0 or abs(a[0]-b[0])==1) and (abs(a[1]-b[1])==0 or abs(a[1]-b[1])==1):
                    return 1
         
        def AStar(graph, start, goal):
         
        	G = {} #Actual movement cost to each position from the start position
        	F = {} #Estimated movement cost of start to goal going via this position
         
        	#Initialize starting values
        	G[start] = 0 
        	F[start] = graph.heuristic(start, goal)
         
        	closedVertices = collections.OrderedDict()
        	openVertices = set([start])
        	cameFrom = {}
         
        	while len(openVertices) > 0:
        		#Get the vertex in the open list with the lowest F score
        		current = None
        		currentFscore = None
        		for pos in openVertices:
        			if current is None or F[pos] < currentFscore:
        				currentFscore = F[pos]
        				current = pos
         
        		#Check if we have reached the goal
        		if current == goal:
        			#Retrace our route backward
        			path = [current]
        			while current in cameFrom:
        				current = cameFrom[current]
        				path.append(current)
        			path.reverse()
        			return path, F[goal], closedVertices #Done!
         
        		#Mark the current vertex as closed
        		openVertices.remove(current)
        		closedVertices.update({current:0})
         
        		#Update scores for vertices near the current position
        		for neighbour in graph.get_vertex_neighbours(current):
        			if neighbour in closedVertices: 
        				continue #We have already processed this node exhaustively
        			candidateG = G[current] + graph.move_cost(current, neighbour)
         
        			if neighbour not in openVertices:
        				openVertices.add(neighbour) #Discovered a new vertex
        			elif candidateG >= G[neighbour]:
        				continue #This G score is worse than previously found
         
        			#Adopt this G score
        			cameFrom[neighbour] = current
        			G[neighbour] = candidateG
        			H = graph.heuristic(neighbour, goal)
        			F[neighbour] = G[neighbour] + H
                
        	raise RuntimeError("A* failed to find a solution")
        break
    break
if __name__=="__main__":
    graph = AStarMap()
    result, cost, explored_nodes = AStar(graph, tuple(start), tuple(goal))
    open('node_astar.txt', 'w').write('\n'.join('%s\t%s' % x for x in explored_nodes))
    open('path_astar.txt', 'w').write('\n'.join('%s\t%s' % x for x in result))
    print ("route", result)
    print ("cost", cost)
      
    
    
    
    