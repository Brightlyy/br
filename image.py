import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Image Display Example")

# Load the image file
# Note: You can use only GIF, PGM, or PPM formats with PhotoImage
image_path = "/home/bright/Downloads/ZTo1tdex.jpg"
image = tk.PhotoImage(file=image_path)

# Create a label widget to display the image
label = tk.Label(root, image=image)
label.pack()

# Run the Tkinter event loop
root.mainloop()
