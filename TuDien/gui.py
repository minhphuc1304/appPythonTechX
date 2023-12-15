# Trong gui_design.py
import tkinter as tk
import customtkinter

class CTkFrame(customtkinter.CTkFrame):
    pass

class CTkLabel(customtkinter.CTkLabel):
    pass

class CTkEntry(customtkinter.CTkEntry):
    pass

class CTkButton(customtkinter.CTkButton):
    pass

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter_Dictionary.py")
        self.geometry(f"{560}x{520}")

        # create sidebar frame with widgets
        self.sidebar_frame = CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = CTkLabel(self.sidebar_frame, text="Dictionary", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.listboxWords = tk.Listbox(self.sidebar_frame)
        self.listboxWords.grid(row=4, column=0, padx=20, pady=(10, 10), sticky="nsew")

        # create main entry and button
        self.entry = CTkEntry(self, placeholder_text="")
        self.entry.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")
        # Bind the KeyRelease event to the on_key_release function
        self.entry.bind("<KeyRelease>", self.on_key_release)

        self.main_button_1 = CTkButton(master=self, text="Tra từ", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.search_button_clicked)
        self.main_button_1.grid(row=0, column=3, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create listbox
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=1, column=1, columnspan=3, padx=(20, 20), pady=(0, 5), sticky="nsew")
        # Bind the ListboxSelect event to the on_select function
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        # create answer
        self.answer_frame = CTkFrame(self, width=250)
        self.answer_frame.grid(row=2, column=1, columnspan=3, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.label1 = CTkLabel(master=self.answer_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="e", justify="right")
        self.label1.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nw")
        self.label2 = CTkLabel(master=self.answer_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="e", justify="right")
        self.label2.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.label3 = CTkLabel(master=self.answer_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="e", justify="right",)
        self.label3.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nw")


    def on_key_release(self, event):
        typed_string = event.widget.get()

        if not typed_string:
            self.listbox.delete(0, tk.END)
            self.label1.configure(text="")
            self.label2.configure(text="")
            self.label3.configure(text="")
            return

        self.process_typed_string(typed_string)

    def process_typed_string(self, typed_string):
        pass
        # Placeholder for the logic related to Trie and Dictionary search

    def on_select(self, event):
        pass
        # Placeholder for the logic related to Listbox selection

    def search_button_clicked(self):
        pass
        # Placeholder for the logic related to Trie and Dictionary search

    def populate_listbox(self):
        pass
        # Placeholder for the logic related to populating Listbox

if __name__ == "__main__":
    app = App()
    app.mainloop()