import tkinter as tk

# Function to draw a rectangle on the canvas
def draw_rectangle():
    canvas.create_rectangle(50, 50, 200, 150, fill="blue")

# Create the main application window
root = tk.Tk()
root.title("Canvas Example")

# Create a Canvas widget
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Create a button to trigger drawing
button = tk.Button(root, text="Draw Rectangle", command=draw_rectangle)
button.pack()

# Start the Tkinter event loop
root.mainloop()
