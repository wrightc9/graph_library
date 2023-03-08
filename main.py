from graph import Graph as g
import tkinter as tk
from tkinter import simpledialog
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

G = nx.DiGraph()

def execute():
    option = var.get()
    if option == "Insert Edge":
        start_end = simpledialog.askstring("Shortest Path", "Enter start and end nodes (separated by a space):")
        if start_end is not None:
            start, end = start_end.split()
        
        if start and end:
            guser.insert_edge(graph, start, end)
        else:
            print("Invalid input.")
    
        print(graph)
        
    elif option == "Insert Vertex":
        guser.insert_vertex(graph)

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
        guser.dijkstra(graph)

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