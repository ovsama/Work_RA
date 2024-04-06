import tkinter as tk
from tkinter import messagebox
import os
import datetime

def generate_file_structure(brand_name, dosage, pharmaceutical_form, country, dispatch_number):
    today = datetime.date.today().strftime('%Y-%m-%d')
    folder_name = f"{today}-Renewal-{brand_name} {dosage} {pharmaceutical_form}-{country}-Dispatch{dispatch_number}"
    os.makedirs(folder_name)
    non_ectd_folder = os.path.join(folder_name, 'Non-eCTD')
    os.makedirs(non_ectd_folder)
    m1_folder = os.path.join(non_ectd_folder, 'M1')
    os.makedirs(m1_folder)
    m1_local_folder = os.path.join(m1_folder, 'M1 Local')
    os.makedirs(m1_local_folder)
    m1_corporate_folder = os.path.join(m1_folder, 'M1 Corporate')
    os.makedirs(m1_corporate_folder)
    m2_folder = os.path.join(non_ectd_folder, 'M2')
    os.makedirs(m2_folder)
    messagebox.showinfo("Success", f"File structure '{folder_name}' generated successfully!")

def generate_structure():
    brand_name = brand_name_entry.get()
    dosage = dosage_entry.get()
    pharmaceutical_form = pharmaceutical_form_entry.get()
    country = country_entry.get()
    dispatch_number = dispatch_number_entry.get()

    generate_file_structure(brand_name, dosage, pharmaceutical_form, country, dispatch_number)

# Create the main window
root = tk.Tk()
root.title("File Generator")

# Create labels and entry fields
labels = ["Brand Name:", "Dosage:", "Pharmaceutical Form:", "Country:", "Dispatch Number:"]
entries = []

for i, label_text in enumerate(labels):
    tk.Label(root, text=label_text).grid(row=i, column=0, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)
    entry.bind("<Button-3>", lambda e, entry=entry: entry.tk.call("tk_popup", entry.menu, e.x_root, e.y_root))
    entry.menu = tk.Menu(entry, tearoff=0)
    entry.menu.add_command(label="Cut", command=lambda entry=entry: entry.event_generate("<<Cut>>"))
    entry.menu.add_command(label="Copy", command=lambda entry=entry: entry.event_generate("<<Copy>>"))
    entry.menu.add_command(label="Paste", command=lambda entry=entry: entry.event_generate("<<Paste>>"))

# Create a button to generate the file structure
generate_button = tk.Button(root, text="Generate File Structure", command=generate_structure)
generate_button.grid(row=len(labels), columnspan=2)

# Run the main event loop
root.mainloop()
