import tkinter as tk
from database import connect_db

def add_contact_window():
    add_window = tk.Toplevel()
    add_window.title("Add Contact")
    add_window.geometry("400x200")   
    add_window.resizable(False, False) 

    
    tk.Label(add_window, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Phone Number").grid(row=1, column=0)
    phone_entry = tk.Entry(add_window)
    phone_entry.grid(row=1, column=1)
    
    tk.Label(add_window, text="Email").grid(row=2, column=0)
    email_entry = tk.Entry(add_window)
    email_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Address").grid(row=3, column=0)
    address_entry = tk.Entry(add_window)
    address_entry.grid(row=3, column=1)
    
    def save_contact():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                       (name, phone, email, address))
        conn.commit()
        conn.close()
        add_window.destroy()

    tk.Button(add_window, text="Save", command=save_contact).grid(row=4, columnspan=2)

    add_window.mainloop()
