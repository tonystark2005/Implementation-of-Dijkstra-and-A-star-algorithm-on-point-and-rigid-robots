# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:29:34 2019

@author: sanke
"""

"""
start_point=input("Enter start point seperated by a space : ")
goal_point=input("Enter goal point : ") 
resolution=input("Enter resolution : ")
print(start_point+ goal_point+ resolution)
"""
import time
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
start[0]=int(start[0]/resolution)
start[1]=int(start[1]/resolution)
while True:
    if start[0]<0 or start[0]>int(249/resolution) or start[1]<0 or start[1]>int(149/resolution):
        print("Try again")
        break
    goal=input("Enter goal point separated by space: ")
    goal=goal.split(' ')
    goal = list(map(int, goal))
    goal[0]=int(goal[0]/resolution)
    goal[1]=int(goal[1]/resolution)
    while True:
        if goal[0]<0 or goal[0]>int(249/resolution) or goal[1]<0 or goal[1]>int(149/resolution):
            print("Try again")
            break

    

        start_time = time.time()
        import Space
        import math
        import time

        graph=Space.Obstacle_map(radius, clearance, resolution)
#print(graph)
        if tuple(goal) in graph.keys()==False:
                print("Goal is in obstacle space")
           
        def dijkstra(graph,start,goal):
            shortest_distance = {}
            predecessor = {}
            exploredNodes= collections.OrderedDict()
            unseenNodes = graph
            infinity = math.inf
            path = []
            for node in unseenNodes:
                shortest_distance[node] = infinity
            shortest_distance[start] = 0
            while unseenNodes:
                minNode = None
                for node in unseenNodes:
                    if minNode is None:
                        minNode = node
                    elif shortest_distance[node] < shortest_distance[minNode]:
                        minNode = node
         
                for childNode, weight in graph[minNode].items():
                    if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                        shortest_distance[childNode] = weight + shortest_distance[minNode]
                        predecessor[childNode] = minNode
                exploredNodes.update(unseenNodes.pop(minNode))
         
            currentNode = goal
            while currentNode != start:
                try:
                    path.insert(0,currentNode)
                    currentNode = predecessor[currentNode]
                except KeyError:
                    print('Path not reachable')
                    break
            path.insert(0,start)
            if shortest_distance[goal] != infinity:
                print('Shortest distance is ' + str(shortest_distance[goal]))
                #print('And the path is ' + str(path))
                open('path_dij.txt', 'w').write('\n'.join('%s\t%s' % x for x in path))
                open('node_dij.txt', 'w').write('\n'.join('%s\t%s' % x for x in exploredNodes))
         
        dijkstra(graph, tuple(start), tuple(goal))
        end_time = time.time()
        print("Total time: "+str(end_time-start_time))
        break
    break