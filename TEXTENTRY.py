import tkinter as tk

def get_input():
    user_input = entry.get()
    print("User input:", user_input)

# Create a Tkinter window
root = tk.Tk()
root.title("Text Entry Example")

# Create a label widget
label = tk.Label(root, text="Enter text:")
label.pack()

# Create a text entry widget
entry = tk.Entry(root)
entry.pack()

# Create a button to get the input
button = tk.Button(root, text="Get Input", command=get_input)
button.pack()

# Run the Tkinter event loop
root.mainloop()
