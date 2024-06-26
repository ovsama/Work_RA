import tkinter as tk
from tkinter import messagebox
import os

# Function to generate file structure
def generate_file_structure():
    brand_name = brand_name_entry.get()
    ccr_ro = ccr_ro_entry.get()
    variation_title = variation_title_entry.get()
    dispatch_number = dispatch_number_entry.get()

    folder_name = f"Var CMC-{brand_name} -{ccr_ro}- {variation_title}-Dispatch {dispatch_number}"

    # Create the main folder
    main_folder = os.path.join(os.getcwd(), folder_name)
    os.makedirs(main_folder, exist_ok=True)

    # Create the "0000" folder
    zero_folder = os.path.join(main_folder, "0000")
    os.makedirs(zero_folder, exist_ok=True)

    # Create the "Non-eCTD" folder inside "0000"
    non_ectd_folder = os.path.join(zero_folder, 'Non-eCTD')
    os.makedirs(non_ectd_folder, exist_ok=True)

    # Create M1 folders inside "Non-eCTD"
    m1_folder = os.path.join(non_ectd_folder, 'M1')
    os.makedirs(m1_folder, exist_ok=True)
    m1_local_folder = os.path.join(m1_folder, 'M1 Local')
    os.makedirs(m1_local_folder, exist_ok=True)
    m1_corporate_folder = os.path.join(m1_folder, 'M1 Corporate')
    os.makedirs(m1_corporate_folder, exist_ok=True)

    # Create M2 folder inside "Non-eCTD"
    m2_folder = os.path.join(non_ectd_folder, 'M2')
    os.makedirs(m2_folder, exist_ok=True)

    # Show success message
    messagebox.showinfo("Success", f"File structure '{folder_name}' generated successfully!")

# Function to copy text from entry
def copy_text(entry):
    entry.clipboard_clear()
    entry.clipboard_append(entry.get())

# Function to cut text from entry
def cut_text(entry):
    copy_text(entry)
    entry.delete(0, "end")

# Function to paste text into entry
def paste_text(entry):
    entry.insert("end", entry.clipboard_get())

# Create the main window
root = tk.Tk()
root.title("Variation Dossier Folders-Generator by OE")

# Create labels and entry fields
labels = ["Brand Name:", "CCR-RO:", "Variation Title:", "Dispatch Number:"]
entries = []

for i, label_text in enumerate(labels):
    tk.Label(root, text=label_text).grid(row=i, column=0, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, columnspan=3, sticky="we")
    entry.bind("<FocusIn>", lambda e, widget=entry: set_focus(widget))
    entry.bind("<Button-3>", lambda e, widget=entry: show_context_menu(e, widget))
    entries.append(entry)

# Define entry fields with global scope
brand_name_entry = entries[0]
ccr_ro_entry = entries[1]
variation_title_entry = entries[2]
dispatch_number_entry = entries[3]

# Function to set the entry with focus
def set_focus(entry):
    global current_entry
    current_entry = entry

# Function to show context menu
def show_context_menu(event, entry):
    context_menu = tk.Menu(root, tearoff=0)
    context_menu.add_command(label="Copy", command=lambda: copy_text(entry))
    context_menu.add_command(label="Cut", command=lambda: cut_text(entry))
    context_menu.add_command(label="Paste", command=lambda: paste_text(entry))
    context_menu.tk_popup(event.x_root, event.y_root)

# Create a button to generate the file structure
generate_button = tk.Button(root, text="Generate Variation Dossier Structure", command=generate_file_structure)
generate_button.grid(row=len(labels), column=0, columnspan=4, pady=(10, 0))

# Run the main event loop
root.mainloop()
