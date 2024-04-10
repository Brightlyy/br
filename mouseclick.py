import tkinter as tk

def left_click(event):
    print("Left mouse button clicked")

def right_click(event):
    print("Right mouse button clicked")

root = tk.Tk()
root.title("Mouse Events Example")

# Bind left-click event
root.bind("<Button-1>", left_click)

# Bind right-click event
root.bind("<Button-3>", right_click)

root.mainloop()
