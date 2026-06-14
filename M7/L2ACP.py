import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def calculate_age():
    """Read the entered birth‑date, compute the age and show it."""
    try:
        # Extract values from the entry widgets
        day   = int(entry_day.get())
        month = int(entry_month.get())
        year  = int(entry_year.get())

        # Build a date object; this will raise ValueError for impossible dates
        birth_date = datetime(year, month, day)

        today = datetime.today()
        # Basic year‑difference
        age = today.year - birth_date.year

        # If birthday hasn't occurred yet this year, subtract one
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_var.set(str(age))
    except ValueError:
        messagebox.showerror("Invalid Input",
                           "Please enter a valid day, month and year (e.g., 5 12 1990).")


# ----------------------------------------------------------------------
# UI layout
# ----------------------------------------------------------------------
root = tk.Tk()
root.title("Age Calculator")
root.geometry("320x250")
root.resizable(False, False)

# --- Labels & entry fields ------------------------------------------------
lbl_title = tk.Label(root, text="Enter your Date of Birth", font=("Helvetica", 14))
lbl_title.pack(pady=(20, 10))

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Day:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_day = tk.Entry(frame_inputs, width=5)
entry_day.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Month:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_month = tk.Entry(frame_inputs, width=5)
entry_month.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Year:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_year = tk.Entry(frame_inputs, width=8)
entry_year.grid(row=2, column=1, padx=5, pady=5)

# --- Result display -------------------------------------------------------
result_var = tk.StringVar()
tk.Label(root, text="Your Age:", font=("Helvetica", 12)).pack(pady=(15, 5))
tk.Label(root, textvariable=result_var,
         font=("Helvetica", 20, "bold"), fg="#0066CC").pack()

# --- Calculate button ------------------------------------------------------
btn_calc = tk.Button(root, text="Calculate Age",
                     command=calculate_age, bg="#28a745", fg="white",
                     font=("Helvetica", 12), width=15)
btn_calc.pack(pady=20)

root.mainloop()
