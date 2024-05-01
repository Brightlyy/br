import tkinter as tk
from tkinter import ttk
import psycopg2

# Function to add data to PostgreSQL database
def add_data():
    name = name_entry.get()
    age = age_entry.get()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    update_table()

# Function to update the table with data from PostgreSQL database
def update_table():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for i in treeview.get_children():
        treeview.delete(i)
    for row in rows:
        treeview.insert("", "end", values=row)

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
    name VARCHAR(100),
    age INTEGER
)
"""
cursor.execute(create_table_query)
conn.commit()

# Grant permissions to the user
grant_query = "GRANT ALL PRIVILEGES ON TABLE users TO bright"
cursor.execute(grant_query)
conn.commit()

# Create Tkinter GUI
root = tk.Tk()
root.title("User Data")

# Create input fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=5, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add", command=add_data)
add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create table to display data
treeview = ttk.Treeview(root, columns=("Name", "Age"), show="headings")
treeview.heading("Name", text="Name")
treeview.heading("Age", text="Age")
treeview.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Update table with existing data
update_table()

root.mainloop()

# Close cursor and connection
cursor.close()
conn.close()
