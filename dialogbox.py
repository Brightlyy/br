import tkinter as tk
import tkinter.simpledialog as sd

def get_name():
    name = sd.askstring("Name", "Enter your name:")
    if name:
        print("Hello,", name)
    else:
        print("No name entered.")

root = tk.Tk()
tk.Button(root, text="Get Name", command=get_name).pack()
root.mainloop()
