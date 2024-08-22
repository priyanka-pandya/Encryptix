import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
from database import connect_db

def search_contact_window():
    search_window = tk.Toplevel()
    search_window.title("Search Contact")
    search_window.geometry("400x200")   
    search_window.resizable(False, False) 

    def perform_search():
        search_term = search_entry.get()

        if not search_term:
            messagebox.showerror("Input Error", "Please enter a search term.")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT name, phone, email, address FROM contacts WHERE name LIKE ? OR phone LIKE ?",
                       ('%' + search_term + '%', '%' + search_term + '%'))
        records = cursor.fetchall()
        conn.close()

        search_results.delete(*search_results.get_children())

        if not records:
            messagebox.showinfo("No Results", "No contacts found.")
        else:
            for record in records:
                search_results.insert("", "end", values=record)

    tk.Label(search_window, text="Search:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    search_entry = tk.Entry(search_window)
    search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tk.Button(search_window, text="Search", command=perform_search).grid(row=1, column=1, padx=10, pady=10, sticky="w")

    search_results = ttk.Treeview(search_window, columns=('Name', 'Phone', 'Email', 'Address'), show='headings')
    for col in ('Name', 'Phone', 'Email', 'Address'):
        search_results.heading(col, text=col)
    search_results.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    scrollbar = ttk.Scrollbar(search_window, orient="vertical", command=search_results.yview)
    search_results.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=2, column=2, sticky='ns')

    search_window.grid_columnconfigure(1, weight=1)   
