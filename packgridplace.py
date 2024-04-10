import tkinter as tk

def pack_example():
    pack_window = tk.Toplevel(root)
    pack_window.title("Pack Example")
    label = tk.Label(pack_window, text="This is a Pack Example")
    label.pack()

def grid_example():
    grid_window = tk.Toplevel(root)
    grid_window.title("Grid Example")
    label1 = tk.Label(grid_window, text="Label 1")
    label1.grid(row=0, column=0)
    label2 = tk.Label(grid_window, text="Label 2")
    label2.grid(row=0, column=1)
    label3 = tk.Label(grid_window, text="Label 3")
    label3.grid(row=1, column=0, columnspan=2)

def place_example():
    place_window = tk.Toplevel(root)
    place_window.title("Place Example")
    label = tk.Label(place_window, text="This is a Place Example")
    label.place(x=50, y=50)

root = tk.Tk()
root.title("Geometry Managers Example")

pack_button = tk.Button(root, text="Pack Example", command=pack_example)
pack_button.pack(pady=10)

grid_button = tk.Button(root, text="Grid Example", command=grid_example)
grid_button.pack(pady=10)

place_button = tk.Button(root, text="Place Example", command=place_example)
place_button.pack(pady=10)

root.mainloop()
