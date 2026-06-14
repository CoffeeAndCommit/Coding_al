import tkinter as tk
from tkinter import messagebox


def assess_strength():
    """Determine password strength based on its length.
    - < 6 characters : Weak
    - 6‑10 characters : Medium
    - > 10 characters : Strong
    """
    pwd = entry_pwd.get()
    if not pwd:
        messagebox.showwarning("Input required", "Please enter a password.")
        return
    length = len(pwd)
    if length < 6:
        strength = "Weak"
        color = "#FF4C4C"   # red
    elif length <= 10:
        strength = "Medium"
        color = "#FFA500"   # orange
    else:
        strength = "Strong"
        color = "#4CAF50"   # green
    result_var.set(strength)
    result_label.config(fg=color)

# ----------------------------------------------------------------------
# UI Layout
# ----------------------------------------------------------------------
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("340x200")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

# Header
header = tk.Label(root, text="Enter a password to evaluate its strength",
                  font=("Helvetica", 12), bg="#f0f4f8")
header.pack(pady=(20, 10))

# Password entry
entry_pwd = tk.Entry(root, show="*", width=30, font=("Helvetica", 11))
entry_pwd.pack(pady=5)

# Check button
check_btn = tk.Button(root, text="Check Strength", command=assess_strength,
                      bg="#0066CC", fg="white", font=("Helvetica", 10), width=15)
check_btn.pack(pady=10)

# Result display
result_var = tk.StringVar(value="")
result_label = tk.Label(root, textvariable=result_var,
                        font=("Helvetica", 14, "bold"), bg="#f0f4f8")
result_label.pack(pady=5)

root.mainloop()
