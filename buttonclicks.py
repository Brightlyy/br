import tkinter as tk

def button_click():
    # Function to handle button click event
    print("Button clicked!")

# Create main application window
root = tk.Tk()

# Create a Button widget
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

# Run the Tkinter event loop
root.mainloop()
