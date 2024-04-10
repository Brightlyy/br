import tkinter as tk

def button_click():
    print("Button clicked!")

def radio_button_click():
    selected_option = radio_var.get()
    print("Selected option:", selected_option)

# Create the main application window
root = tk.Tk()
root.title("Buttons and Radio Buttons Example")

# Create a button
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

# Create a label for the radio buttons
radio_label = tk.Label(root, text="Select an option:")
radio_label.pack()

# Create a variable to hold the selected radio button value
radio_var = tk.StringVar()

# Create radio buttons
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=radio_button_click)
radio_button1.pack()

radio_button2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=radio_button_click)
radio_button2.pack()

# Run the Tkinter event loop
root.mainloop()
