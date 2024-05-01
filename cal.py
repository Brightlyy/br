import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")
        self.memory = 0

        self.entry = ttk.Entry(master, width=30)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('M+', 5, 1), ('M-', 5, 2), ('MR', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('sqrt', 6, 3),
            ('pi', 7, 0), ('(', 7, 1), (')', 7, 2), ('^', 7, 3),
            ('%', 8, 0), ('log', 8, 1), ('exp', 8, 2), ('abs', 8, 3),
        ]

        for (text, row, col) in buttons:
            ttk.Button(self.master, text=text, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, text):
        if text == 'C':
            self.entry.delete(0, tk.END)
        elif text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

        elif text == 'M+':
            try:
                self.memory += eval(self.entry.get())
            except:
                pass
        elif text == 'M-':
            try:
                self.memory -= eval(self.entry.get())
            except:
                pass
        elif text == 'MR':
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.memory)
        elif text == 'sin':
            self.entry.insert(tk.END, math.sin(eval(self.entry.get())))
        elif text == 'cos':
            self.entry.insert(tk.END, math.cos(eval(self.entry.get())))
        elif text == 'tan':
            self.entry.insert(tk.END, math.tan(eval(self.entry.get())))
        elif text == 'sqrt':
            self.entry.insert(tk.END, math.sqrt(eval(self.entry.get())))
        elif text == 'pi':
            self.entry.insert(tk.END, math.pi)
        elif text == '^':
            self.entry.insert(tk.END, '**')
        elif text == '%':
            self.entry.insert(tk.END, '/100')
        elif text == 'log':
            self.entry.insert(tk.END, 'math.log10(')
        elif text == 'exp':
            self.entry.insert(tk.END, 'math.exp(')
        elif text == 'abs':
            self.entry.insert(tk.END, 'abs(')
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
