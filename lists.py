import tkinter as tk

def on_select(event):
    # Get the selected item from the list
    selected_item = listbox.get(listbox.curselection())
    # Print the selected item to the console
    print("Selected item:", selected_item)

# Create the main application window
root = tk.Tk()
root.title("Listbox Example")

# Create a Listbox widget
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack()

# Add items to the Listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

# Bind the on_select function to the Listbox widget
listbox.bind('<<ListboxSelect>>', on_select)

# Run the Tkinter event loop
root.mainloop()
