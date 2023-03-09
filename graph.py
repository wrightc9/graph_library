from collections import deque

class Graph:
    def __init__(self) -> None:
        pass
    
    def insert_edge(self, graph, u, v):
         # add v to the adjacency list of u and vice versa
        graph[u].add(v)
        graph[v].add(u)

    def insert_vertex(self, graph, vertex):
        if vertex not in graph:
            graph[vertex] = set()

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
        Q = deque()
        L = []
        
        Q.append(start)
        visited = {start}
        
        while Q:
            v = Q.popleft()
            
            for w in graph[v]:
                if w not in visited:
                    L.append((v, w))
                    Q.append(w)
                    visited.add(w)
        
        return L
    
    def dijkstra(self, graph, start, end):
        print("Dijkstra")
    
    def find_path(self, graph, u, v):
        print("Find Path from {} to {}".format(u, v))