import tkinter as tk
from tkinter import messagebox
import json

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Function to load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)

# Add new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if not name or not phone:
        messagebox.showerror("Input Error", "Name and Phone are required.")
        return
    
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    save_contacts(contacts)
    update_contact_list()
    clear_fields()

# Edit an existing contact
def edit_contact():
    selected_contact = contact_listbox.curselection()
    if not selected_contact:
        messagebox.showwarning("Selection Error", "Please select a contact to edit.")
        return
    
    contact = contacts[selected_contact[0]]
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    
    name_entry.insert(0, contact['name'])
    phone_entry.insert(0, contact['phone'])
    email_entry.insert(0, contact['email'])
    address_entry.insert(0, contact['address'])
    
    delete_contact()

# Delete an existing contact
def delete_contact():
    selected_contact = contact_listbox.curselection()
    if not selected_contact:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")
        return
    
    contact = contacts[selected_contact[0]]
    contacts.remove(contact)
    save_contacts(contacts)
    update_contact_list()
    clear_fields()

# Update the list of contacts in the Listbox
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Initialize the main application window
app = tk.Tk()
app.title("Contact Book")
app.geometry("500x400")

# Load existing contacts from file
contacts = load_contacts()

# Create input fields and labels
name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(app, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
phone_entry = tk.Entry(app)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(app, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(app)
email_entry.grid(row=2, column=1, padx=10, pady=5)

address_label = tk.Label(app, text="Address:")
address_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
address_entry = tk.Entry(app)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Create buttons
add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, padx=10, pady=10)

edit_button = tk.Button(app, text="Edit Contact", command=edit_contact)
edit_button.grid(row=4, column=1, padx=10, pady=10)

delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=2, padx=10, pady=10)

# Create listbox to display contacts
contact_listbox = tk.Listbox(app, width=50, height=10)
contact_listbox.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Populate the listbox with existing contacts
update_contact_list()

# Start the Tkinter event loop
app.mainloop()
