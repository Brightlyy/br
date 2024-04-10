import tkinter as tk
from PIL import Image, ImageTk

# Create a Tkinter window
root = tk.Tk()
root.title("Image Display Example")

# Use the provided absolute path for the image file
image_path = "/home/bright/Downloads/illia-horokhovsky-1aWfiZOq0zg-unsplash.jpg"

try:
    # Open the image file using Pillow
    image_pil = Image.open(image_path)

    # Convert the Pillow image to a Tkinter-compatible format
    image_tk = ImageTk.PhotoImage(image_pil)

    # Create a label widget to display the image
    label = tk.Label(root, image=image_tk)
    label.pack()

    # Keep a reference to the image to prevent it from being garbage collected
    label.image = image_tk

except Exception as e:
    # Handle the error if the image couldn't be loaded
    print("Error:", e)

# Run the Tkinter event loop
root.mainloop()
