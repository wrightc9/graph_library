from graph import Graph as g
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

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



def execute():
    option = var.get()
    if option == "Insert Edge":
        start_end = simpledialog.askstring("Insert Edge", "Enter start and end nodes (separated by a space):")
        if start_end is not None:
            start, end = start_end.split()
        else:
            message = "Please Enter a start and end node"
            messagebox.showerror("Error", message)

        if start and end:
            if guser.insert_edge(graph, start, end):
                message = "Updated edges in Graph:\n\n{}".format(graph)
                messagebox.showinfo("Success", message)
            else:
                message = "Either vertex {} or vertex {} does not exist in the current graph.".format(start, end)
                messagebox.showerror("Error", message)
        else:
            message = "Invalid Input"
            messagebox.showerror("Error", message)
    
    elif option == "Insert Vertex":
        vertex = simpledialog.askstring("Vertex", "Enter the vertex to add:")
        
        if guser.insert_vertex(graph, vertex):
            message = "New Graph with added Vertex:\n\n{}".format(graph)
            messagebox.showinfo("Success", message)
        else:
            message = "Vertex {} already exists in the graph.".format(vertex)
            messagebox.showerror("Error", message)

    elif option == "DFS":
        start_node = simpledialog.askstring("Start Node", "Enter the starting node:")

        tree = guser.dfs(graph, start_node)

        if len(tree) != 0:
            message = "Edges from DFS search:\n\n{}".format(tree)
            messagebox.showinfo("Success", message)
        else:
            message = "Vertex {} does not exist in the graph.".format(start_node)
            messagebox.showerror("Error", message)
        
    elif option == "BFS":
        start_node = simpledialog.askstring("Start Node", "Enter the starting node:")
        tree = guser.bfs(graph, start_node)
        
        if len(tree) != 0:
            message = "Edges from BFS search:\n\n{}".format(tree)
            messagebox.showinfo("Success", message)
        else:
            message = "Vertex {} does not exist in the graph.".format(start_node)
            messagebox.showerror("Error", message)

    elif option == "Dijkstra":
        start_node = simpledialog.askstring("Start Node", "Enter the starting node:")

        distances, paths = guser.dijkstra(weighted_graph, start_node)
        
        message = "Distances to from {} to all other vertices:\n\n{}Paths from {} to all other vertices.\n\n{}".format(start_node, distances, start_node, paths)
        messagebox.showinfo("Success", message)
        
    elif option == "Find Path":
        start_end = simpledialog.askstring("Find Path", "Enter start and end nodes (separated by a space):")
        if start_end is not None:
            start, end = start_end.split()
        else:
            message = "Please Enter a start and end node (seperated by a space)"
            messagebox.showerror("Error", message)

        if start and end:
            path = guser.find_path(graph, start, end)
            if path is not None:
                message = "Path from {} to {}: \n\n{}".format(start, end, path)
                messagebox.showinfo("Success", message)
            else:
                message= "No valid path from {} to {}".format(start, end)
                messagebox.showerror("Error", message)
        else:
            message = "Invalid Input"
            messagebox.showerror("Error", message)

    else:
        message = "Invalid option selected."
        messagebox.showerror("Error", message)

# Create button to execute selected option
execute_button = tk.Button(root, text="Execute", command=execute)
execute_button.pack(pady=10, anchor="center")

root.mainloop()