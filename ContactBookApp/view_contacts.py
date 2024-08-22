import tkinter as tk
from tkinter import ttk
from database import connect_db

def view_contacts_window():
    view_window = tk.Toplevel()
    view_window.title("View Contacts")
    
    tree = ttk.Treeview(view_window, columns=("Name", "Phone"), show='headings')
    tree.heading("Name", text="Name")
    tree.heading("Phone", text="Phone")
    tree.pack(fill=tk.BOTH, expand=True)
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone FROM contacts")
    contacts = cursor.fetchall()
    conn.close()

    for contact in contacts:
        tree.insert("", tk.END, values=contact)

    view_window.mainloop()
