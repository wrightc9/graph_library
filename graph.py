from collections import deque

class Graph:
    def __init__(self) -> None:
        pass
    
    def insert_edge(self, graph, u, v):
         # add v to the adjacency list of u
        graph[u].add(v)
        # add u to the adjacency list of v
        graph[v].add(u)

    def insert_vertex(self, graph):
        print("Insert Vertex")

    def dfs(self, graph, node):
        stack = []
        visited = []
        edges = []

        stack.append(node)
        visited.append(node)
        while stack:
            v = stack.pop()
            
            for w in graph[v]:
                if w not in visited:
                    edges.append((v,w))
                    stack.append(w)
                    visited.append(w)
        
        return edges
    
    def bfs(self, graph, start):
        Q = deque() # create a queue for BFS
        L = [] # create a list to store the edges
        
        Q.append(start) # enqueue the source vertex s
        visited = {start} # mark s as visited
        
        while Q: # while the queue is not empty
            v = Q.popleft() # dequeue the front vertex
            
            for w in graph[v]: # for all neighbors w of v in graph g
                if w not in visited: # if w is not visited
                    L.append((v, w)) # add (v,w) edge to the list
                    Q.append(w) # enqueue w
                    visited.add(w) # mark w as visited
        
        return L
    
    def dijkstra(self, graph):
        print("Dijkstra")
    
    def find_path(self, graph, u, v):
        print("Find Path from {} to {}".format(u, v))