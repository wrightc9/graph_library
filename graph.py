import networkx as nx

class Graph:
    def __init__(self) -> None:
        pass
    
    def insert_edge(self):
        print("Insert edge")

    def insert_vertex(self):
        print("Insert Vertex")

    def dfs(self):
        print("DFS")
    
    def bfs(self):
        print("BFS")
    
    def dijkstra(self):
        print("Dijkstra")
    
    def find_path(self, u, v):
        print("Find Path from {} to {}".format(u, v))