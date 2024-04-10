import tkinter as tk

def hello():
    print("Hello!")

def popup(event):
    # Create a popup menu
    popup_menu = tk.Menu(root, tearoff=0)
    popup_menu.add_command(label="Cut", command=hello)
    popup_menu.add_command(label="Copy", command=hello)
    popup_menu.add_command(label="Paste", command=hello)

    # Display the popup menu at the location of the right-click event
    popup_menu.post(event.x_root, event.y_root)

root = tk.Tk()
root.title("Popup Menu Example")

# Bind the right-click event to the popup function
root.bind("<Button-3>", popup)

root.mainloop()
