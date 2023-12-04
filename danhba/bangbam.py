import tkinter as tk
from tkinter import simpledialog, messagebox

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def insert_contact(self, name, phone):
        self.contacts[name] = phone

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def display_contacts(self, listbox):
        listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            listbox.insert(tk.END, f"{name}: {phone}")

    def search_contact(self, query):
        results = []
        for name, phone in self.contacts.items():
            if query.lower() in name.lower() or query.lower() in phone.lower():
                results.append(f"{name}: {phone}")
        return results


class AddContactDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Name:").grid(row=0)
        tk.Label(master, text="Phone:").grid(row=1)

        self.name_entry = tk.Entry(master)
        self.phone_entry = tk.Entry(master)

        self.name_entry.grid(row=0, column=1)
        self.phone_entry.grid(row=1, column=1)

        return self.name_entry

    def apply(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        self.result = (name, phone)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("IPHONE")
        self.geometry(f"{350}x{400}")

        self.contact_book = ContactBook()

        # Configure column and row weights
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=0)

        # Entry and searchButton in row 0
        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=0, column=0, columnspan=2, sticky="ew", padx=(20, 10), pady=(5, 5))

        self.searchButton = tk.Button(self, text="Search", command=self.search_contact)
        self.searchButton.grid(row=0, column=2, sticky="ew", padx=(10, 20), pady=(5, 5))

        # Listbox in row 1
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=(20, 20), pady=(10, 10))

        # Two buttons in row 3
        self.button1 = tk.Button(self, text="Add Contact", command=self.add_contact)
        self.button1.grid(row=3, column=0, columnspan=2, sticky="ew", padx=(20, 20), pady=(5, 15))

        self.button2 = tk.Button(self, text="Delete Contact", command=self.delete_contact)
        self.button2.grid(row=3, column=2, sticky="ew", padx=(20, 20), pady=(5, 15))

    def add_contact(self):
        dialog = AddContactDialog(self)
        if dialog.result:
            name, phone = dialog.result
            self.contact_book.insert_contact(name, phone)
            self.refresh_listbox()

    def search_contact(self):
        query = self.search_entry.get()
        if not query:
            messagebox.showwarning("Warning", "Please enter a search query.")
            return

        results = self.contact_book.search_contact(query)

        if not results:
            messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            self.show_search_results(results)

    def delete_contact(self):
        selected_contact = self.listbox.curselection()
        if selected_contact:
            contact_info = self.listbox.get(selected_contact)
            name = contact_info.split(":")[0].strip()
            self.contact_book.delete_contact(name)
            self.refresh_listbox()

    def show_search_results(self, results):
        result_text = "\n".join(results)
        messagebox.showinfo("Search Results", result_text)

    def refresh_listbox(self):
        self.contact_book.display_contacts(self.listbox)


if __name__ == "__main__":
    app = App()
    app.mainloop()
