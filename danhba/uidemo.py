import tkinter as tk
from tkinter import simpledialog, messagebox


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None


class ContactBook:
    def __init__(self):
        self.root = None

    def insert_contact(self, name, phone):
        self.root = self._insert_contact(self.root, name, phone)

    def _insert_contact(self, node, name, phone):
        if node is None:
            return Contact(name, phone)
        if name < node.name:
            node.left = self._insert_contact(node.left, name, phone)
        elif name > node.name:
            node.right = self._insert_contact(node.right, name, phone)
        return node

    def delete_contact(self, name):
        self.root = self._delete_contact(self.root, name)

    def _delete_contact(self, node, name):
        if node is None:
            return node
        if name < node.name:
            node.left = self._delete_contact(node.left, name)
        elif name > node.name:
            node.right = self._delete_contact(node.right, name)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.name = self._min_value_node(node.right).name
            node.right = self._delete_contact(node.right, node.name)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def display_contacts(self, node, listbox):
        if node is not None:
            self.display_contacts(node.left, listbox)
            listbox.insert(tk.END, f"{node.name}: {node.phone}")
            self.display_contacts(node.right, listbox)

    def search_contact(self, node, query, results):
        if node is not None:
            self.search_contact(node.left, query, results)
            if query.lower() in node.name.lower() or query.lower() in node.phone.lower():
                results.append(f"{node.name}: {node.phone}")
            self.search_contact(node.right, query, results)


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


class MyGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.contact_book = ContactBook()

        # Entry and Button in row 0
        button1 = tk.Button(self, text="Add Contact", command=self.add_contact)
        button2 = tk.Button(self, text="Delete Contact", command=self.delete_contact)
        search_entry = tk.Entry(self)
        search_button = tk.Button(self, text="Search", command=lambda: self.search_contact(search_entry.get()))

        button1.grid(row=0, column=0, columnspan=1, sticky="ew")
        button2.grid(row=0, column=1, columnspan=1, sticky="ew")
        search_entry.grid(row=0, column=2, columnspan=1, sticky="ew")
        search_button.grid(row=0, column=3, columnspan=1, sticky="ew")

        # Listbox in row 1
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # Configure column and row weights
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def add_contact(self):
        dialog = AddContactDialog(self)
        if dialog.result:
            name, phone = dialog.result
            self.contact_book.insert_contact(name, phone)
            self.refresh_listbox()

    def delete_contact(self):
        selected_contact = self.listbox.curselection()
        if selected_contact:
            contact_info = self.listbox.get(selected_contact)
            name = contact_info.split(":")[0].strip()
            self.contact_book.delete_contact(name)
            self.refresh_listbox()

    def search_contact(self, query):
        if not query:
            messagebox.showwarning("Warning", "Please enter a search query.")
            return

        results = []
        self.contact_book.search_contact(self.contact_book.root, query, results)

        if not results:
            messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            self.show_search_results(results)

    def show_search_results(self, results):
        result_text = "\n".join(results)
        tk.messagebox.showinfo("Search Results", result_text)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        self.contact_book.display_contacts(self.contact_book.root, self.listbox)


if __name__ == "__main__":
    app = MyGUI()
    app.mainloop()
