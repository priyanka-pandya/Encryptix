import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
from database import create_connection
from main import init_main_window

def login_window():
    login_win = tk.Tk()
    login_win.title("Login")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Username:").pack(pady=5)
    username_entry = tk.Entry(login_win)
    username_entry.pack(pady=5)

    tk.Label(login_win, text="Password:").pack(pady=5)
    password_entry = tk.Entry(login_win, show="*")
    password_entry.pack(pady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT password_hash FROM users WHERE username=?', (username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            stored_password_hash = result[0]
            input_password_hash = hashlib.sha256(password.encode()).hexdigest()
            if stored_password_hash == input_password_hash:
                messagebox.showinfo("Login Success", "Welcome to the Contact Book!")
                login_win.destroy()
                init_main_window()
            else:
                messagebox.showwarning("Login Failed", "Incorrect password.")
        else:
            messagebox.showwarning("Login Failed", "Username not found.")

    tk.Button(login_win, text="Login", command=login).pack(pady=20)

    login_win.mainloop()

if __name__ == "__main__":
    login_window()
