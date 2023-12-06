import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# Function to handle adding contacts to the contact list
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name and phone:
        contact = Contact(name, phone)
        contacts.append(contact)
        update_contact_list()
        clear_entry_fields()
    else:
        messagebox.showwarning("Incomplete Information", "Please enter both name and phone number.")

# Function to update the contact list in the Listbox
def update_contact_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

# Function to handle searching for a contact
def search_contact():
    query = search_entry.get().lower()
    search_results = [contact for contact in contacts if query in contact.name.lower()]
    
    if search_results:
        update_contact_list_search(search_results)
    else:
        messagebox.showinfo("Search Results", "No matching contacts found.")

# Function to update the contact list based on search results
def update_contact_list_search(search_results):
    listbox.delete(0, tk.END)
    for contact in search_results:
        listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

# Function to clear entry fields
def clear_entry_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Create the main Tkinter window
root = tk.Tk()
root.title("Contact Management System")

# Entry widgets for adding contacts
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

phone_entry = tk.Entry(root, width=30)
phone_entry.pack(pady=5)

# Buttons to add contacts
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(pady=5)

# Entry widget for searching contacts
search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=5)

# Button to search contacts
search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.pack(pady=5)

# Listbox to display contacts
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack(pady=10)

# Start with some sample contacts
contacts = [Contact("John Doe", "123-456-7890"), Contact("Jane Smith", "987-654-3210")]
update_contact_list()

# Start the Tkinter event loop
root.mainloop()
