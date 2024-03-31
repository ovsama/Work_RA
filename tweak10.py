import tkinter as tk
from PIL import Image, ImageTk

def eur_to_fcfa(amount_eur):
    exchange_rate = 655.957
    amount_fcfa = amount_eur * exchange_rate
    return amount_fcfa

def copy_text(widget):
    widget.clipboard_clear()
    widget.clipboard_append(widget.get("1.0", "end-1c"))

def convert(event=None):
    try:
        amount_str = entry.get().replace(',', '.')  # Replace commas with periods
        amount_eur = float(amount_str)
        amount_fcfa = eur_to_fcfa(amount_eur)
        result_text.config(state="normal")  # Enable the text box temporarily
        result_text.delete("1.0", "end")  # Clear previous result
        result_text.insert("end", f"{amount_eur:.2f} EUR is equal to {amount_fcfa:.2f} FCFA")  # Insert new result
        result_text.config(state="disabled")  # Disable the text box again
    except ValueError:
        result_text.config(state="normal")  # Enable the text box temporarily
        result_text.delete("1.0", "end")  # Clear previous result
        result_text.insert("end", "Please enter a valid number")  # Insert error message
        result_text.config(state="disabled")  # Disable the text box again

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
result_text = tk.Text(root, height=2, width=40, wrap="word", state="disabled")
result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Add context menu to entry widget
entry_menu = tk.Menu(root, tearoff=0)
entry_menu.add_command(label="Copy", command=lambda: copy_text(entry))
entry.bind("<Button-3>", lambda e: entry_menu.post(e.x_root, e.y_root))

# Add context menu to result_text widget
result_text_menu = tk.Menu(root, tearoff=0)
result_text_menu.add_command(label="Copy", command=lambda: copy_text(result_text))
result_text.bind("<Button-3>", lambda e: result_text_menu.post(e.x_root, e.y_root))

# Bind the Enter key to the convert function
root.bind("<Return>", convert)

# Run the application
root.mainloop()
