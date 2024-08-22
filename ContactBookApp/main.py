import tkinter as tk
from tkinter import ttk, PhotoImage
from add_contact import add_contact_window
from view_contacts import view_contacts_window 
from search_contact import search_contact_window 
from update_contact import update_contact_window
from delete_contact import delete_contact_window

def main():
    root = tk.Tk()
    root.title("Contact Book")
    root.configure(background='#ADD8E6')    
    root.geometry("550x350")
    
    welcome_label = tk.Label(root, text="Welcome to Contact Book", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    instructions_label = tk.Label(root, text="Use the buttons above to manage your contacts.", font=("Helvetica", 12))
    instructions_label.pack(side=tk.BOTTOM, fill=tk.X, pady=20)


    icon = PhotoImage(file="con.png")   
    root.iconphoto(False, icon)

     

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Add Contact", command=add_contact_window).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="View Contacts", command=view_contacts_window).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Search Contact", command=search_contact_window).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Update Contact", command=update_contact_window).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Delete Contact", command=delete_contact_window).pack(side=tk.LEFT, padx=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
