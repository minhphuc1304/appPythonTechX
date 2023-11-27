import tkinter as tk
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("IPHONE")
        self.geometry(f"{350}x{400}")

        # Configure column and row weights
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=0)

        # Entry and searchButton in row 0
        self.entry = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry.grid(row=0, column=0, columnspan=3, sticky="ew", padx=(20, 10), pady=(5, 5))

        self.searchButton = customtkinter.CTkButton(self, text="Click Me")
        self.searchButton.grid(row=0, column=3, sticky="ew", padx=(10, 20), pady=(5, 5))

        # Listbox in row 1
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=(20, 20), pady=(10, 10))

        # Two buttons in row 3
        self.button1 = customtkinter.CTkButton(self, text="Button 1")
        self.button1.grid(row=3, column=0, columnspan=2, sticky="ew", padx=(20, 20), pady=(5, 15))

        self.button2 = customtkinter.CTkButton(self, text="Button 2")
        self.button2.grid(row=3, column=2, columnspan=2, sticky="ew", padx=(20, 20), pady=(5, 15))

        self.add_items_to_listbox()

    def add_items_to_listbox(self):
        # Add items to the Listbox
        data = [
            "John - 123456789",
            "Jane - 987654321",
            "Bob - 555555555",
            "Alice - 11112222333"
        ]

        for item in data:
            self.listbox.insert(tk.END, item)



if __name__ == "__main__":
    app = App()
    app.mainloop()