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
tk.Label(root, text="Brand Name:").grid(row=0, column=0, sticky="e")
brand_name_entry = tk.Entry(root)
brand_name_entry.grid(row=0, column=1)

tk.Label(root, text="Dosage:").grid(row=1, column=0, sticky="e")
dosage_entry = tk.Entry(root)
dosage_entry.grid(row=1, column=1)

tk.Label(root, text="Pharmaceutical Form:").grid(row=2, column=0, sticky="e")
pharmaceutical_form_entry = tk.Entry(root)
pharmaceutical_form_entry.grid(row=2, column=1)

tk.Label(root, text="Country:").grid(row=3, column=0, sticky="e")
country_entry = tk.Entry(root)
country_entry.grid(row=3, column=1)

tk.Label(root, text="Dispatch Number:").grid(row=4, column=0, sticky="e")
dispatch_number_entry = tk.Entry(root)
dispatch_number_entry.grid(row=4, column=1)

# Create a button to generate the file structure
generate_button = tk.Button(root, text="Generate File Structure", command=generate_structure)
generate_button.grid(row=5, columnspan=2)

# Run the main event loop
root.mainloop()
