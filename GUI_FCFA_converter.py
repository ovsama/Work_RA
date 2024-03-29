import tkinter as tk

# Function to convert EUR to FCFA
def convert():
    try:
        amount_eur = float(entry.get())
        amount_fcfa = amount_eur * 655.957  # Fixed exchange rate
        result_label.config(text=f"{amount_eur:.2f} EUR is equal to {amount_fcfa:.2f} FCFA")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create input label and entry
input_label = tk.Label(root, text="Enter amount in EUR:")
input_label.pack()

entry = tk.Entry(root)
entry.pack()

# Create convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

# Create label for displaying result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
