import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_choice.get()
        result = 0

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Please select an operation.")
            return

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields for numbers
label_num1 = tk.Label(root, text="First Number:")
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = tk.Label(root, text="Second Number:")
label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Operation choice
label_operation = tk.Label(root, text="Operation:")
label_operation.grid(row=2, column=0, padx=5, pady=5)

operation_choice = tk.StringVar(root)
operation_choice.set("Add")  # default value
operations = ["Add", "Subtract", "Multiply", "Divide"]
option_menu = tk.OptionMenu(root, operation_choice, *operations)
option_menu.grid(row=2, column=1, padx=5, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2, padx=5, pady=10)

# Result display
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()