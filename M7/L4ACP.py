import tkinter as tk
from tkinter import messagebox


def calculate_interest():
    """Compute Simple and Compound Interest and display results.
    Simple Interest = P * T * R / 100
    Compound Interest = P * ((1 + R/100) ** T) - P
    """
    try:
        principal = float(entry_principal.get())
        time_years = float(entry_time.get())
        rate = float(entry_rate.get())
        if principal < 0 or time_years < 0 or rate < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter positive numeric values for all fields.")
        return

    simple_interest = principal * time_years * rate / 100.0
    compound_interest = principal * ((1 + rate / 100.0) ** time_years) - principal

    si_var.set(f"{simple_interest:.2f}")
    ci_var.set(f"{compound_interest:.2f}")

# ----------------------------------------------------------------------
# UI Layout
# ----------------------------------------------------------------------
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Input fields
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=15)

# Principal
tk.Label(frame_inputs, text="Principal Amount:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_principal = tk.Entry(frame_inputs, width=15)
entry_principal.grid(row=0, column=1, padx=5, pady=5)

# Time (years)
tk.Label(frame_inputs, text="Time (years):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_time = tk.Entry(frame_inputs, width=15)
entry_time.grid(row=1, column=1, padx=5, pady=5)

# Rate (% per annum)
tk.Label(frame_inputs, text="Rate (%):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_rate = tk.Entry(frame_inputs, width=15)
entry_rate.grid(row=2, column=1, padx=5, pady=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate_interest,
          bg="#0066CC", fg="white", font=("Helvetica", 10), width=12).pack(pady=10)

# Results
frame_results = tk.Frame(root)
frame_results.pack(pady=10)

si_var = tk.StringVar(value="0.00")
ci_var = tk.StringVar(value="0.00")

tk.Label(frame_results, text="Simple Interest:").grid(row=0, column=0, sticky="e", padx=5)
tk.Label(frame_results, textvariable=si_var, fg="#006600", font=("Helvetica", 12, "bold")).grid(row=0, column=1, sticky="w", padx=5)

tk.Label(frame_results, text="Compound Interest:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Label(frame_results, textvariable=ci_var, fg="#CC0000", font=("Helvetica", 12, "bold")).grid(row=1, column=1, sticky="w", padx=5, pady=5)

root.mainloop()
