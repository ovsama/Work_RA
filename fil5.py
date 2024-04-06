import tkinter as tk
from tkinter import messagebox
import os
import datetime

def generate_file_structure():
    brand_name = brand_name_entry.get()
    dosage = dosage_entry.get()
    pharmaceutical_form = pharmaceutical_form_entry.get()
    country = country_entry.get()
    dispatch_number = dispatch_number_entry.get()

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

# Define entry fields with global scope
brand_name_entry = entries[0]
dosage_entry = entries[1]
pharmaceutical_form_entry = entries[2]
country_entry = entries[3]
dispatch_number_entry = entries[4]

# Create a button to generate the file structure
generate_button = tk.Button(root, text="Generate File Structure", command=generate_file_structure)
generate_button.grid(row=len(labels), columnspan=2)

# Run the main event loop
root.mainloop()
