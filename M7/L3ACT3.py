import tkinter as tk
from tkinter import ttk, messagebox


def convert_temperature():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        # Convert input to Celsius first
        if from_unit == "Celsius":
            celsius = value
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5 / 9
        else:  # Kelvin
            celsius = value - 273.15
        # Convert from Celsius to target unit
        if to_unit == "Celsius":
            result = celsius
        elif to_unit == "Fahrenheit":
            result = celsius * 9 / 5 + 32
        else:  # Kelvin
            result = celsius + 273.15
        result_var.set(f"{result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a numeric temperature.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x200")
root.resizable(False, False)

# Input field
tk.Label(root, text="Temperature:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_value = tk.Entry(root, width=10)
entry_value.grid(row=0, column=1, padx=5, pady=10)

# From unit combo
tk.Label(root, text="From:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=12)
combo_from.current(0)
combo_from.grid(row=1, column=1, padx=5, pady=5)

# To unit combo
tk.Label(root, text="To:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=12)
combo_to.current(1)
combo_to.grid(row=2, column=1, padx=5, pady=5)

# Calculate button
tk.Button(root, text="Convert", command=convert_temperature, bg="#0066CC", fg="white").grid(row=3, column=0, columnspan=2, pady=15)

# Result display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 14), fg="#009900")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
