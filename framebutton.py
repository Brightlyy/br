import tkinter as tk

def button_click():
    print("Button clicked!")

# Create the root window
root = tk.Tk()
root.title("Tkinter Example")

# Create a frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create a button
button = tk.Button(frame, text="Click Me!", command=button_click)
button.pack()

# Run the Tkinter event loop
root.mainloop()
