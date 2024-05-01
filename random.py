import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
import random
import requests
from PIL import Image, ImageTk
import io

# Define login_window at global level
login_window = None

# Function to add data to PostgreSQL database
def register_user():
    username = reg_username_entry.get()
    password = reg_password_entry.get()
    # Check if username already exists
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone() is not None:
        messagebox.showerror("Error", "Username already exists!")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")

def login_user():
    global login_window  # Declare login_window as global
    username = login_username_entry.get()
    password = login_password_entry.get()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    if cursor.fetchone() is not None:
        if login_window:
            login_window.destroy()  # Destroy the existing login window
        show_random_image()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def show_random_image():
    global login_window  # Declare login_window as global
    login_window = tk.Toplevel(root)
    login_window.title("Random Bird Image")
    login_window.geometry("400x400")

    # Fetch random bird image from web using Pexels API
    headers = {"Authorization": "hRi93KLPR025c2r4p9dP8C2Y5V0iVX7ETAFs3yISYiNg7qdmOJmUjIXj"}
    response = requests.get("https://api.pexels.com/v1/search?query=bird", headers=headers)
    if response.status_code == 200:
        data = response.json()
        photos = data.get("photos", [])
        if photos:
            random_photo = random.choice(photos)
            image_url = random_photo.get("src", {}).get("original", "")
            image_data = requests.get(image_url).content
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((400, 400), Image.LANCZOS)  # Corrected line
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(login_window, image=photo)
            label.image = photo
            label.pack()
        else:
            messagebox.showerror("Error", "No bird images found.")
    else:
        messagebox.showerror("Error", f"Failed to fetch random bird image: {response.status_code}")

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="nd",
    user="bright",
    password="8680",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(100)
)
"""
cursor.execute(create_table_query)
conn.commit()

# Create Tkinter GUI
root = tk.Tk()
root.title("Login Form")

# Register Form
reg_frame = ttk.Frame(root)
reg_frame.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(reg_frame, text="Register").grid(row=0, columnspan=2, padx=5, pady=5)

ttk.Label(reg_frame, text="Username:").grid(row=1, column=0, padx=5, pady=5)
reg_username_entry = ttk.Entry(reg_frame)
reg_username_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(reg_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
reg_password_entry = ttk.Entry(reg_frame, show="*")
reg_password_entry.grid(row=2, column=1, padx=5, pady=5)

reg_button = ttk.Button(reg_frame, text="Register", command=register_user)
reg_button.grid(row=3, columnspan=2, padx=5, pady=5)

# Login Form
login_frame = ttk.Frame(root)
login_frame.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(login_frame, text="Login").grid(row=0, columnspan=2, padx=5, pady=5)

ttk.Label(login_frame, text="Username:").grid(row=1, column=0, padx=5, pady=5)
login_username_entry = ttk.Entry(login_frame)
login_username_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(login_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
login_password_entry = ttk.Entry(login_frame, show="*")
login_password_entry.grid(row=2, column=1, padx=5, pady=5)

login_button = ttk.Button(login_frame, text="Login", command=login_user)
login_button.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()

# Close cursor and connection
cursor.close()
conn.close()
