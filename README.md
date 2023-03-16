# graph_library
A Graph Library, with insert edge, insert vertex, DFS, BFS, Dijkstra, Find Path between u-v

You will need to have python3 installed to run this on ubuntu

Run with command "python3 main.py" in ubuntu.

A graph library written in python. Main.py is the driver and uses tkinter as the UI. You will be able to select which operation you would like to perform in the dropdown box and
press the execute button. A popup window will ask you for the appropriate information, like starting node. It will then return the results in another popup window.

(NOTE: this is meant to be a program focusing on the library. The UI and main is strictly built to demonstrate the graph library in graph.py. main.py is not a fully fledged program.)
The options are:
insert edge
 -adds the edge between two existing nodes in the graph and returns the updated graph list 
insert vertex
 -adds a vertex to the graph if it does not already exist and returns updated graph
DFS
 -performs a dfs and returns the edges traversed during the search.
BFS
 -performs a bfs and returns the edges traversed during the search.
Dijkstra
 -performs dijkstra on a weighted graph and returns the distance to each node from the start point, and returns optimal paths for each one.
Find Path between u-v
 -performs a modified bfs to find a path between u and v

Below are the graphs I use in main for demonstration. All operations are performed using this adjacency lists.

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

weighted_graph = {'A': set([('B', 4), ('C', 2)]),
                  'B': set([('A', 4), ('C', 1), ('D', 3), ('E', 2)]),
                  'C': set([('A', 2), ('B', 1)]),
                  'D': set([('B', 3), ('E', 5)]),
                  'E': set([('B', 2), ('D', 5)])}