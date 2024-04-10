import tkinter as tk

def mouse_motion(event):
    # Function to handle mouse motion event
    print(f"Mouse moved to ({event.x}, {event.y})")

# Create main application window
root = tk.Tk()

# Bind mouse motion event to the root window
root.bind("<Motion>", mouse_motion)

# Run the Tkinter event loop
root.mainloop()
