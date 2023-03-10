from collections import deque
import heapq

class Graph:
    def __init__(self) -> None:
        pass
    
    def insert_edge(self, graph, u, v):
         # add v to the adjacency list of u and vice versa
        if u and v in graph:
            graph[u].add(v)
            graph[v].add(u)
            return True
        else:
            return False


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
    
    def dijkstra(self, graph, start):
        # Initialize distances, previous nodes, and visited set
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        previous = {node: None for node in graph}
        visited = set()

        # Create a priority queue and add the starting node
        pq = [(0, start)]

        while pq:
            # Get the node with the smallest distance
            current_distance, current_node = heapq.heappop(pq)

            # Skip this node if we already processed it
            if current_node in visited:
                continue

            # Add it to the visited set
            visited.add(current_node)

            # Update the distances of its neighbors
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # Reconstruct paths from start to all other nodes
        paths = {node: [] for node in graph}
        for node in graph:
            if node == start:
                paths[node] = [start]
            elif previous[node] is None:
                paths[node] = []
            else:
                path = [node]
                while previous[path[-1]] != start:
                    path.append(previous[path[-1]])
                path.append(start)
                path.reverse()
                paths[node] = path

        return distances, paths
    
    def find_path(self, graph, u, v):
        Q = deque()
        visited = set()
        path = {u: None}

        Q.append(u)
        visited.add(u)

        while Q:
            o = Q.popleft()

            if o == v:
                # Reconstruct the path by following the previous pointers
                path_list = [o]
                while path[path_list[-1]] is not None:
                    path_list.append(path[path_list[-1]])
                path_list.reverse()
                return path_list

            for w in graph[o]:
                if w not in visited:
                    visited.add(w)
                    path[w] = o
                    Q.append(w)

        # If we reach here, there is no path from start to end
        return None