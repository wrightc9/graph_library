from graph import Graph as g
import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox
import networkx as nx

root = tk.Tk()
root.title("Graph Library")
root.geometry("250x200")
root.eval('tk::PlaceWindow . center')


options = ["Insert Edge", "Insert Vertex", "DFS", "BFS", "Dijkstra", "Find Path"]
var = tk.StringVar(value=options[0])
menu = tk.OptionMenu(root, var, *options)
menu.pack(pady=10, anchor="center")

guser = g()

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


G = nx.DiGraph()

def execute():
    option = var.get()
    if option == "Insert Edge":
        start_end = simpledialog.askstring("Insert Edge", "Enter start and end nodes (separated by a space):")
        if start_end is not None:
            start, end = start_end.split()
        
        if start and end:
            if guser.insert_edge(graph, start, end):
                print("Updated edges in Graph:")
                print(graph)
            else:
                print("Either vertex {} or vertex {} does not exist in the current graph.".format(start, end))

        else:
            print("Invalid input.")
    
    elif option == "Insert Vertex":
        vertex = simpledialog.askstring("Vertex", "Enter the vertex to add:")
        guser.insert_vertex(graph, vertex)

        print("New Graph with added Vertex:")
        print(graph)

    elif option == "DFS":
        start_node = simpledialog.askstring("Start Node", "Enter the starting node:")

        tree = guser.dfs(graph, start_node)

        print("Edges:")
        print(tree)
        
    elif option == "BFS":
        start_node = simpledialog.askstring("Start Node", "Enter the starting node:")
        tree = guser.bfs(graph, start_node)
        
        print("Edges:")
        print(tree)

    elif option == "Dijkstra":
        start_node = simpledialog.askstring("Start Node", "Enter the starting node:")
        distances, paths = guser.dijkstra(weighted_graph, start_node)

        print("Distances to from {} to all other vertices:".format(start_node))
        print(distances)
        print("Paths from {} to all other vertices.".format(start_node))
        print(paths)
        
    elif option == "Find Path":
        start_end = simpledialog.askstring("Find Path", "Enter start and end nodes (separated by a space):")
        if start_end is not None:
            start, end = start_end.split()

        if start and end:
            guser.find_path(graph, start, end)
        else:
            print("Invalid input.")

    else:
        print("Invalid option selected.")

# Create button to execute selected option
execute_button = tk.Button(root, text="Execute", command=execute)
execute_button.pack(pady=10, anchor="center")

root.mainloop()