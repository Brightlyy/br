import tkinter as tk
from tkinter import ttk

# Create a Tkinter window
root = tk.Tk()

# Create a list of options for the combo box
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=options)

# Set a default value for the combo box
combo_box.set("Select an option")

# Pack the combo box into the window
combo_box.pack()

# Function to get the current selection index
def get_current_selection():
    index = combo_box.current()
    print("Current selection index:", index)

# Button to get the current selection index
get_selection_button = tk.Button(root, text="Get Current Selection Index", command=get_current_selection)
get_selection_button.pack()

# Main loop
root.mainloop()
