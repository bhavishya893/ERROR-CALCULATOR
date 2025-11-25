import tkinter as tk
from tkinter import messagebox
import re
def calculate():
    try:
        values_str = entry_values.get().strip()
        true_str = entry_true.get().strip()
        if not values_str:
            messagebox.showerror("Input Error", "Please enter measured values.")
            return
        number_strings = re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', values_str)
        if not number_strings:
            messagebox.showerror("Input Error", "No valid numbers found in measured values.")
            return
        values = [float(s) for s in number_strings]
        n = len(values)
        mean_val = sum(values) / n
        if n > 1:
            variance = sum((x - mean_val) ** 2 for x in values) / (n - 1)
        else:
            variance = 0.0
        std_dev = variance ** 0.5
        abs_error = rel_error = pct_error = None
        if true_str:
            try:
                true_val = float(true_str)
            except ValueError:
                messagebox.showerror("Input Error", "True value must be a number.")
                return
            abs_error = abs(mean_val - true_val)
            if true_val != 0:
                rel_error = abs_error / abs(true_val)
                pct_error = rel_error * 100
            else:
                rel_error = float('inf')
                pct_error = float('inf')
        label_mean_val.config(text=f"{mean_val:.5g}")
        label_var_val.config(text=f"{variance:.5g}")
        label_std_val.config(text=f"{std_dev:.5g}")
        if abs_error is not None:
            label_abs_val.config(text=f"{abs_error:.5g}")
            label_rel_val.config(text=f"{rel_error:.5g}")
            label_pct_val.config(text=f"{pct_error:.5g}")
        else:
            label_abs_val.config(text="N/A")
            label_rel_val.config(text="N/A")
            label_pct_val.config(text="N/A")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")
root = tk.Tk()
root.title("Error & Statistics Calculator")
tk.Label(root, text="Measured values (any separators ok):").grid(
    row=0, column=0, sticky="w", padx=5, pady=5
)
entry_values = tk.Entry(root, width=40)
entry_values.grid(row=0, column=1, padx=5, pady=5)
tk.Label(root, text="True value (for error calc):").grid(
    row=1, column=0, sticky="w", padx=5, pady=5
)
entry_true = tk.Entry(root, width=20)
entry_true.grid(row=1, column=1, sticky="w", padx=5, pady=5)
tk.Button(root, text="Calculate", command=calculate).grid(
    row=2, column=0, columnspan=2, pady=8
)
row = 3
tk.Label(root, text="Mean:").grid(row=row, column=0, sticky="w", padx=5)
label_mean_val = tk.Label(root, text="-")
label_mean_val.grid(row=row, column=1, sticky="w", padx=5)
row += 1
tk.Label(root, text="Variance:").grid(row=row, column=0, sticky="w", padx=5)
label_var_val = tk.Label(root, text="-")
label_var_val.grid(row=row, column=1, sticky="w", padx=5)
row += 1
tk.Label(root, text="Standard deviation:").grid(row=row, column=0, sticky="w", padx=5)
label_std_val = tk.Label(root, text="-")
label_std_val.grid(row=row, column=1, sticky="w", padx=5)
row += 1
tk.Label(root, text="Absolute error:").grid(row=row, column=0, sticky="w", padx=5)
label_abs_val = tk.Label(root, text="-")
label_abs_val.grid(row=row, column=1, sticky="w", padx=5)
row += 1
tk.Label(root, text="Relative error:").grid(row=row, column=0, sticky="w", padx=5)
label_rel_val = tk.Label(root, text="-")
label_rel_val.grid(row=row, column=1, sticky="w", padx=5)
row += 1
tk.Label(root, text="Percentage error (%):").grid(row=row, column=0, sticky="w", padx=5)
label_pct_val = tk.Label(root, text="-")
label_pct_val.grid(row=row, column=1, sticky="w", padx=5)
root.mainloop()
