import tkinter as tk
from tkinter import messagebox


def convert_length():
    """Convert between length units based on user selection."""
    try:
        value = float(entry_value.get())
        from_unit, to_unit = var_option.get().split(" → ")
        # Conversion factors to meters
        to_meters = {
            "Meters": 1.0,
            "Kilometers": 1000.0,
            "Centimeters": 0.01,
            "Millimeters": 0.001,
            "Feet": 0.3048,
            "Inches": 0.0254,
            "Yards": 0.9144,
            "Miles": 1609.344,
        }
        # Convert input to meters, then to target unit
        meters = value * to_meters[from_unit]
        result = meters / to_meters[to_unit]
        result_var.set(f"{result:.4f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a numeric value.")
    except KeyError:
        messagebox.showerror("Unsupported unit", "Selected conversion is not supported.")

root = tk.Tk()
root.title("Length Converter")
root.geometry("340x250")
root.resizable(False, False)

# Input field
tk.Label(root, text="Enter length:").pack(pady=(20, 5))
entry_value = tk.Entry(root, width=20)
entry_value.pack()

# Conversion options
units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Feet", "Inches", "Yards", "Miles"]
var_option = tk.StringVar(value="Meters → Feet")
frame_options = tk.Frame(root)
frame_options.pack(pady=10)
for from_u in units:
    for to_u in units:
        if from_u != to_u:
            opt = f"{from_u} → {to_u}"
            tk.Radiobutton(frame_options, text=opt, variable=var_option, value=opt).pack(anchor="w")

# Result display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 14), fg="#0066CC")
result_label.pack(pady=10)

# Convert button
tk.Button(root, text="Convert", command=convert_length, bg="#28a745", fg="white").pack(pady=10)

root.mainloop()
