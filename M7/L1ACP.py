import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        product = a * b
        result_var.set(str(product))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x200")

# First number
lbl_a = tk.Label(root, text="First number:")
lbl_a.pack(pady=(20, 5))
entry_a = tk.Entry(root)
entry_a.pack()

# Second number
lbl_b = tk.Label(root, text="Second number:")
lbl_b.pack(pady=(10, 5))
entry_b = tk.Entry(root)
entry_b.pack()

# Result display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 14))
result_label.pack(pady=10)

# Calculate button
btn = tk.Button(root, text="Calculate Product", command=calculate)
btn.pack(pady=10)

root.mainloop()