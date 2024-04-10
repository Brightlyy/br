import tkinter as tk

def key_pressed(event):
    # Function to handle key press event
    print(f"Key pressed: {event.keysym}")

# Create main application window
root = tk.Tk()

# Bind key press event to the root window
root.bind("<Key>", key_pressed)

# Run the Tkinter event loop
root.mainloop()
