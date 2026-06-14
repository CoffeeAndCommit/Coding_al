import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_user.get()
    password = entry_pass.get()
    if username and password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Error", "Please enter both username and password.")

# Set up main window
root = tk.Tk()
root.title("Login App")
root.geometry("500x500")

# Username label and entry
lbl_user = tk.Label(root, text="Username:")
lbl_user.pack(pady=(20, 5))
entry_user = tk.Entry(root)
entry_user.pack()

# Password label and entry
lbl_pass = tk.Label(root, text="Password:")
lbl_pass.pack(pady=(10, 5))
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

# Login button
btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack(pady=15)

root.mainloop()
