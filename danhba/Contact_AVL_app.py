import tkinter as tk
import customtkinter
from tkinter import simpledialog, messagebox

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class AVLNode:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert_contact(self, name, phone):
        self.root = self._insert_contact(self.root, name, phone)

    def _insert_contact(self, node, name, phone):
        if not node:
            return AVLNode(name, phone)
        
        if name < node.name:
            node.left = self._insert_contact(node.left, name, phone)
        elif name > node.name:
            node.right = self._insert_contact(node.right, name, phone)
        else:
            # Duplicate names are not allowed
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Left Left Case
        if balance > 1 and name < node.left.name:
            return self._rotate_right(node)

        # Right Right Case
        if balance < -1 and name > node.right.name:
            return self._rotate_left(node)

        # Left Right Case
        if balance > 1 and name > node.left.name:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Left Case
        if balance < -1 and name < node.right.name:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def delete_contact(self, name):
        self.root = self._delete_contact(self.root, name)

    def _delete_contact(self, root, name):
        if not root:
            return root

        if name < root.name:
            root.left = self._delete_contact(root.left, name)
        elif name > root.name:
            root.right = self._delete_contact(root.right, name)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._get_min_value_node(root.right)
            root.name = temp.name
            root.phone = temp.phone
            root.right = self._delete_contact(root.right, temp.name)

        if not root:
            return root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        # Left Left Case
        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._rotate_right(root)

        # Right Right Case
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._rotate_left(root)

        # Left Right Case
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right Left Case
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _get_min_value_node(self, node):
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

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("IPHONE")
        self.geometry(f"{350}x{400}")

        self.contact_book = AVLTree()

        # Configure column and row weights
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=0)

        # Entry and searchButton in row 0
        self.search_entry = customtkinter.CTkEntry(self, placeholder_text="")
        self.search_entry.grid(row=0, column=0, columnspan=3, sticky="ew", padx=(20, 10), pady=(5, 5))

        self.searchButton = customtkinter.CTkButton(self, text="Search", command=lambda: self.search_contact(self.search_entry.get()))
        self.searchButton.grid(row=0, column=3, sticky="ew", padx=(10, 20), pady=(5, 5))

        # Listbox in row 1
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=(20, 20), pady=(10, 10))

        # Two buttons in row 3
        self.button1 = customtkinter.CTkButton(self, text="Add Contact", command=self.add_contact)
        self.button1.grid(row=3, column=0, columnspan=2, sticky="ew", padx=(20, 20), pady=(5, 15))

        self.button2 = customtkinter.CTkButton(self, text="Delete Contact", command=self.delete_contact)
        self.button2.grid(row=3, column=2, columnspan=2, sticky="ew", padx=(20, 20), pady=(5, 15))

    def add_contact(self):
        dialog = AddContactDialog(self)
        if dialog.result:
            name, phone = dialog.result
            self.contact_book.insert_contact(name, phone)
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

    def delete_contact(self):
        selected_contact = self.listbox.curselection()
        if selected_contact:
            contact_info = self.listbox.get(selected_contact)
            name = contact_info.split(":")[0].strip()
            self.contact_book.delete_contact(name)
            self.refresh_listbox()
            
    def show_search_results(self, results):
        result_text = "\n".join(results)
        tk.messagebox.showinfo("Search Results", result_text)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        self.contact_book.display_contacts(self.contact_book.root, self.listbox)


if __name__ == "__main__":
    app = App()
    app.mainloop()