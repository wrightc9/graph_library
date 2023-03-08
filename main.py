from graph import Graph as g
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.title("Graph Library")
root.geometry("250x200")
root.eval('tk::PlaceWindow . center')


options = ["Insert Edge", "Insert Vertex", "DFS", "BFS", "Dijkstra", "Find Path"]
var = tk.StringVar(value=options[0])
menu = tk.OptionMenu(root, var, *options)
menu.pack(pady=10, anchor="center")

guser = g()
def execute():
    option = var.get()
    if option == "Insert Edge":
        guser.insert_edge()
        
    elif option == "Insert Vertex":
        guser.insert_vertex()

    elif option == "DFS":
        guser.dfs()

    elif option == "BFS":
        guser.bfs()

    elif option == "Dijkstra":
        guser.dijkstra()

    elif option == "Find Path":
        start_node = simpledialog.askstring("Start Node", "Enter the starting node:")
        end_node = simpledialog.askstring("End Node", "Enter the ending node:")

        if start_node and end_node:
            guser.find_path(start_node, end_node)
        else:
            print("Invalid input.")

    else:
        print("Invalid option selected.")

# Create button to execute selected option
execute_button = tk.Button(root, text="Execute", command=execute)
execute_button.pack(pady=10, anchor="center")

root.mainloop()