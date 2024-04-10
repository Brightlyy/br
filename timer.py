import tkinter as tk

def update_timer():
    # Function to update the timer
    current_time = int(timer_label["text"])
    current_time += 1
    timer_label["text"] = str(current_time)
    # Schedule the update_timer function to be called again after 1000 milliseconds (1 second)
    timer_label.after(1000, update_timer)

# Create main application window
root = tk.Tk()
root.title("Timer Example")

# Create a label to display the timer
timer_label = tk.Label(root, text="0", font=("Helvetica", 24))
timer_label.pack(pady=20)

# Start the timer by calling the update_timer function
update_timer()

# Run the Tkinter event loop
root.mainloop()
