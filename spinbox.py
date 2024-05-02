import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Spinbox Example")

# Function to handle spinbox value change
def on_spinbox_change():
    selected_value = spinbox.get()
    print("Selected value:", selected_value)

# Create a Spinbox widget
spinbox = tk.Spinbox(root, from_=0, to=10, command=on_spinbox_change)
spinbox.pack(pady=20)

# Set the initial value of the Spinbox
spinbox.delete(0, tk.END)
spinbox.insert(0, 5)

# Main loop
root.mainloop()
