import tkinter as tk

def resize_window(event):
    # Function to handle window resize event
    width = event.width
    height = event.height
    print(f"Window resized to width={width}, height={height}")

# Create main application window
root = tk.Tk()

# Bind window resize event to the root window
root.bind("<Configure>", resize_window)

# Run the Tkinter event loop
root.mainloop()
