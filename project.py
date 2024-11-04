import tkinter as tk
from tkinter import messagebox, Toplevel, Listbox, Entry, END, simpledialog, font

class ContactSaver:
    def __init__(self, root):
        self.root = root
        root.title('Contact Saver')
        root.configure(bg='#f0f0f0')  # Light grey background for the main window

        # Setting custom fonts
        label_font = font.Font(family="Helvetica", size=12, weight="bold")
        entry_font = font.Font(family="Helvetica", size=12)
        button_font = font.Font(family="Helvetica", size=12, weight="bold")

        # Create labels and entries for the form
        tk.Label(root, text='Name:', font=label_font, bg='#f0f0f0').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.name_entry = tk.Entry(root, font=entry_font)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky='we')

        tk.Label(root, text='Phone:', font=label_font, bg='#f0f0f0').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.phone_entry = tk.Entry(root, font=entry_font)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')

        tk.Label(root, text='Email:', font=label_font, bg='#f0f0f0').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.email_entry = tk.Entry(root, font=entry_font)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10, sticky='we')

        # Buttons for saving, viewing, and searching contacts
        save_button = tk.Button(root, text='Save Contact', command=self.save_contact, font=button_font, bg='#8bc34a')
        save_button.grid(row=3, column=0, padx=10, pady=10)

        view_button = tk.Button(root, text='View Contacts', command=self.view_contacts, font=button_font, bg='#03a9f4')
        view_button.grid(row=3, column=1, padx=10, pady=10)

        search_button = tk.Button(root, text='Search Contact', command=self.search_contact, font=button_font, bg='#ff9800')
        search_button.grid(row=3, column=2, padx=10, pady=10, sticky='we')

        # Configure grid column configuration
        root.grid_columnconfigure(1, weight=1)

    def save_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        # Validate entry contents
        if not name or not phone or not email:
            messagebox.showerror("Error", "Please fill out all fields")
            return

        # Write to a file
        with open("contacts.txt", "a") as file:
            file.write(f"{name}, {phone}, {email}\n")
        
        messagebox.showinfo("Success", "Contact saved successfully")
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)

    def view_contacts(self):
        self.show_contacts()

    def search_contact(self):
        search_name = simpledialog.askstring("Search Contact", "Enter name to search:")
        if search_name:
            self.show_contacts(search_name)

    def show_contacts(self, search_name=None):
        top = Toplevel(self.root)
        top.title("Contacts List")
        top.configure(bg='#eeeeee')
        listbox = Listbox(top, width=50, height=15, font=font.Font(size=12), bg='#ffffff')
        listbox.pack(padx=20, pady=20, fill='both', expand=True)

        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    if search_name is None or search_name.lower() in line.split(',')[0].lower().strip():
                        listbox.insert(END, line.strip())
        except FileNotFoundError:
            messagebox.showerror("Error", "No contacts file found")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactSaver(root)
    root.mainloop()
