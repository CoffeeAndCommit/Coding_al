import tkinter as tk
from tkinter import messagebox


def calculate_denominations():
    """Calculate number of notes/coins for given amount.
    Supports common Indian denominations: 2000, 500, 200, 100, 50, 20, 10, 5, 2, 1.
    """
    try:
        amount = int(entry_amount.get())
        if amount < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a positive integer amount.")
        return

    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    results = {}
    remaining = amount
    for d in denominations:
        count, remaining = divmod(remaining, d)
        results[d] = count

    # Update UI fields
    for d, var in result_vars.items():
        var.set(str(results[d]))

# ----------------------------------------------------------------------
# UI Layout
# ----------------------------------------------------------------------
root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

# Header
tk.Label(root, text="Enter total amount (₹)",
         font=("Helvetica", 14), bg="#f0f4f8").pack(pady=(20, 10))

entry_amount = tk.Entry(root, width=20, font=("Helvetica", 12))
entry_amount.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate_denominations,
          bg="#0066CC", fg="white", font=("Helvetica", 10), width=15).pack(pady=15)

# Result section
frame_res = tk.Frame(root, bg="#f0f4f8")
frame_res.pack(pady=10)

result_vars = {}
for idx, denom in enumerate([2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]):
    tk.Label(frame_res, text=f"₹{denom}", font=("Helvetica", 11),
             bg="#f0f4f8").grid(row=idx, column=0, sticky="e", padx=5, pady=2)
    var = tk.StringVar(value="0")
    result_vars[denom] = var
    tk.Label(frame_res, textvariable=var, font=("Helvetica", 11, "bold"),
             bg="#f0f4f8").grid(row=idx, column=1, sticky="w", padx=5, pady=2)

root.mainloop()
