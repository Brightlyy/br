import tkinter as tk

def on_focus_in(event):
    # Function to handle focus in event
    print(f"Focus in: {event.widget}")

def on_focus_out(event):
    # Function to handle focus out event
    print(f"Focus out: {event.widget}")

root = tk.Tk()
root.title("Focus Change Example")

# Create two entry widgets
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# Bind focus in and focus out events to the entry widgets
entry1.bind("<FocusIn>", on_focus_in)
entry1.bind("<FocusOut>", on_focus_out)
entry2.bind("<FocusIn>", on_focus_in)
entry2.bind("<FocusOut>", on_focus_out)

# Place the entry widgets in the window
entry1.pack()
entry2.pack()

root.mainloop()
