import tkinter as tk
from tkinter import messagebox
from database import connect_db

 
def update_contact_window():
    update_window = tk.Toplevel()
    update_window.title("Update Contact")
    update_window.geometry("400x200")   
    update_window.resizable(False, False) 
    
    tk.Label(update_window, text="Enter Name or Phone Number").grid(row=0, column=0)
    search_entry = tk.Entry(update_window)
    search_entry.grid(row=0, column=1)
    
    def search_contact():
        search_term = search_entry.get()
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE name = ? OR phone = ?", (search_term, search_term))
        contact = cursor.fetchone()
        conn.close()

        if contact:
            name_entry.delete(0, tk.END)
            name_entry.insert(0, contact[1])
            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, contact[2])
            email_entry.delete(0, tk.END)
            email_entry.insert(0, contact[3])
            address_entry.delete(0, tk.END)
            address_entry.insert(0, contact[4])
        else:
            messagebox.showerror("Error", "Contact not found")

    def update_contact():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE phone=?", 
                       (name, phone, email, address, phone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Contact updated successfully")
        update_window.destroy()

    tk.Button(update_window, text="Search", command=search_contact).grid(row=1, column=0, columnspan=2)
    
    tk.Label(update_window, text="Name").grid(row=2, column=0)
    name_entry = tk.Entry(update_window)
    name_entry.grid(row=2, column=1)

    tk.Label(update_window, text="Phone Number").grid(row=3, column=0)
    phone_entry = tk.Entry(update_window)
    phone_entry.grid(row=3, column=1)
    
    tk.Label(update_window, text="Email").grid(row=4, column=0)
    email_entry = tk.Entry(update_window)
    email_entry.grid(row=4, column=1)

    tk.Label(update_window, text="Address").grid(row=5, column=0)
    address_entry = tk.Entry(update_window)
    address_entry.grid(row=5, column=1)
    
    tk.Button(update_window, text="Update", command=update_contact).grid(row=6, columnspan=2)

    update_window.mainloop()