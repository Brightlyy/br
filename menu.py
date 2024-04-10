import tkinter as tk

def hello():
    print("Hello!")

root = tk.Tk()
root.title("Menu Example")

# Create a Menu bar
menubar = tk.Menu(root)

# Create a File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=hello)
file_menu.add_command(label="Open", command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Create an Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut", command=hello)
edit_menu.add_command(label="Copy", command=hello)
edit_menu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=edit_menu)

# Display the Menu bar
root.config(menu=menubar)

# Create a PopupMenu
popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="Cut", command=hello)
popup_menu.add_command(label="Copy", command=hello)
popup_menu.add_command(label="Paste", command=hello)

# Bind the PopupMenu to the right-click event
def popup(event):
    popup_menu.post(event.x_root, event.y_root)

root.bind("<Button-3>", popup)

root.mainloop()
