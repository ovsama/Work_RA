
import tkinter as tk
from PIL import Image, ImageTk

def eur_to_fcfa(amount_eur):
    exchange_rate = 655.957
    amount_fcfa = amount_eur * exchange_rate
    return amount_fcfa

def convert():
    try:
        amount_eur = float(entry.get())
        amount_fcfa = eur_to_fcfa(amount_eur)
        result_text.delete("1.0", "end")  # Clear previous result
        result_text.insert("end", f"{amount_fcfa:.2f}")  # Insert only FCFA amount
    except ValueError:
        result_text.delete("1.0", "end")  # Clear previous result
        result_text.insert("end", "Please enter a valid number")  # Insert error message

def select_fcfa(event):
    try:
        start = result_text.search(" ", "1.0", backwards=True, stopindex="end")
        end = result_text.search(" ", start, stopindex="end")
        result_text.tag_add("sel", start, end)
    except tk.TclError:
        pass

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create input label and entry
input_label = tk.Label(root, text="Enter amount in EUR:")
input_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

# Create convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=0, column=2, padx=10, pady=10)

# Create label for displaying result
result_text = tk.Text(root, height=2, width=40, wrap="word")
result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Bind right-click event to select FCFA amount
result_text.bind("<Button-3>", select_fcfa)

# Run the application
root.mainloop()
