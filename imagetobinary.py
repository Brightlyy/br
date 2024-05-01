import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image
import os

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Converter")

        self.images = []
        self.progress = 0

        # Create labels, entry boxes, and browse buttons for image selection
        self.image_entries = []
        for i in range(5):
            tk.Label(master, text=f"Image {i+1}:").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(master, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5)
            browse_button = tk.Button(master, text="Browse", command=lambda idx=i: self.browse_image(idx))
            browse_button.grid(row=i, column=2, padx=5, pady=5)
            self.image_entries.append(entry)

        # Output directory selection
        tk.Label(master, text="Output Location:").grid(row=5, column=0, padx=5, pady=5)
        self.output_entry = tk.Entry(master, width=50)
        self.output_entry.grid(row=5, column=1, padx=5, pady=5)
        self.output_browse_button = tk.Button(master, text="Browse", command=self.browse_output)
        self.output_browse_button.grid(row=5, column=2, padx=5, pady=5)

        # Submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.convert_images)
        self.submit_button.grid(row=6, columnspan=3, padx=5, pady=5)

        # Progress bar
        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.grid(row=7, columnspan=3, padx=5, pady=5)

        # Progress label
        self.progress_label = tk.Label(master, text="Progress: 0%")
        self.progress_label.grid(row=8, columnspan=3, padx=5, pady=5)

    def browse_image(self, idx):
        filename = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        self.image_entries[idx].delete(0, tk.END)
        self.image_entries[idx].insert(0, filename)

    def browse_output(self):
        directory = filedialog.askdirectory(title="Select Output Location")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, directory)

    def convert_images(self):
        output_dir = self.output_entry.get()
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for idx, entry in enumerate(self.image_entries):
            image_path = entry.get()
            if image_path:
                image = Image.open(image_path).convert("1")  # Convert image to binary (black and white)
                output_path = os.path.join(output_dir, f"image_{idx+1}_binary.txt")
                with open(output_path, "w") as f:
                    for pixel in image.getdata():
                        f.write(str(pixel) + "\n")
                self.images.append(output_path)
                self.progress += 20  # Increment progress by 20%
                self.progress_bar["value"] = self.progress  # Update progress bar value
                self.progress_label.config(text=f"Progress: {self.progress}%")  # Update progress label
                self.master.update_idletasks()

        self.progress = 0  # Reset progress for future use

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
