import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Scrollable Text Widget")

# Create a scrolled text widget
scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
scroll_text.pack(expand=True, fill="both")

# Insert some text into the scrolled text widget
for i in range(50):
    scroll_text.insert(tk.END, f"This is line {i}\n")

root.mainloop()




