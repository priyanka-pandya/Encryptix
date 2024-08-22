import tkinter as tk
from tkinter import messagebox
from database import connect_db

def delete_contact_window():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Contact")
    delete_window.geometry("400x200")   
    delete_window.resizable(False, False)  
    
    tk.Label(delete_window, text="Enter Name or Phone Number").grid(row=0, column=0)
    search_entry = tk.Entry(delete_window)
    search_entry.grid(row=0, column=1)
    
    def delete_contact():
        search_term = search_entry.get()
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE name = ? OR phone = ?", (search_term, search_term))
        conn.commit()
        conn.close()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Contact deleted successfully")
        else:
            messagebox.showerror("Error", "Contact not found")
        delete_window.destroy()

    tk.Button(delete_window, text="Delete", command=delete_contact).grid(row=1, columnspan=2)

    delete_window.mainloop()
