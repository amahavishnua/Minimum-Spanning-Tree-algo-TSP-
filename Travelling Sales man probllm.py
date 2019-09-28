# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 03:45:16 2019

@author: Mahavishnu
"""

import networkx as nx
import math


# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return a 2-approximation of an optimal Hamiltonian cycle.

def approximation(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    gr = nx.minimum_spanning_tree(g)

    print(list(nx.dfs_preorder_nodes(gr, 0)))
    
    gr_list = list(nx.dfs_preorder_nodes(gr, 0))
    done_list = [gr_list[0]]
    weight = 0
    print("Starting done_list", done_list)

    for i in range(len(gr_list)-1):
        #If the next node has already been traversed once, drop it
        #move to the next one
        print("Got nodes to add {} {} with weight {}".format(gr_list[i], gr_list[i+1], g[gr_list[i]][gr_list[i+1]]['weight']))
        if gr_list[i+1] in done_list:
            print(gr_list[i+1], "is already in list. Skipping..")
            continue
        
        weight += g[gr_list[i]][gr_list[i+1]]['weight']
        done_list.append(gr_list[i+1])
        print("Current done_list", done_list)

    #Finally add the weight from the last node to first node of the spanning tree
    print("Current weight without connecting last and first node", weight)
    print("Final nodes to add {} {} with weight {}".format(gr_list[len(gr_list)-1], gr_list[0],g[gr_list[len(gr_list)-1]][gr_list[0]]['weight']))

    # weight += g[gr_list[0]][len(gr_list)-1]['weight']
    weight += g[gr_list[len(gr_list)-1]][gr_list[0]]['weight']
    
    # print(gr, type(gr))
    # You might want to use the function "nx.minimum_spanning_tree(g)"
    # which returns a Minimum Spanning Tree of the graph g

    # You also might want to use the command "list(nx.dfs_preorder_nodes(graph, 0))"
    # which gives a list of vertices of the given graph in depth-first preorder.



    return weight



# This function computes the distance between two points.
def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# This function receives a list of 2-tuples representing the points' coordinates,
# and returns the corresponding graph.
def get_graph(coordinates):
    g = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1):
            g.add_edge(i, j, weight=dist(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]))
    return g

# This function computes the weight of the given cycle.
def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    # Write your code here.
    return sum(g[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1)) + g[cycle[0]][cycle[-1]]['weight']


         
    
    

   
# # Here is a test case:
# # Create an empty graph. 
g = nx.Graph()
# # Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight = 2)
# We work with undirected graphs, so once we add an edge from 0 to 1, it automatically creates an edge of the same weight from 1 to 0.
g.add_edge(1, 2, weight = 2)
g.add_edge(2, 3, weight = 2)
g.add_edge(3, 0, weight = 2)
g.add_edge(0, 2, weight = 1)
g.add_edge(1, 3, weight = 1)
# print(branch_and_bound(g))
# # print(average(g))
print(approximation(g))

# g = nx.Graph()
# # Now we will add 6 edges between 4 vertices
# g.add_edge(0, 1, weight = 2)
# # We work with undirected graphs, so once we add an edge from 0 to 1, it automatically creates an edge of the same weight from 1 to 0.
# g.add_edge(0, 2, weight = 1)
# g.add_edge(0, 3, weight = 1)
# g.add_edge(0, 4, weight = 1)
# g.add_edge(1, 2, weight = 1)
# g.add_edge(1, 3, weight = 2)
# g.add_edge(1, 4, weight = 1)
# g.add_edge(2, 3, weight = 1)
# g.add_edge(2, 4, weight = 1)
# g.add_edge(3, 4, weight = 2)


print("New example")
coordinates = [(174, 25), (129, 99), (268, 212), (211, 209), (156, 82)]
g1 = get_graph(coordinates)
print(approximation(g1))