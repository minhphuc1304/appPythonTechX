import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter_Dictionary.py")
        self.geometry(f"{500}x{510}")

        # # configure grid layout (4x4)
        # self.grid_columnconfigure(1, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Dictionary", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(10, 10))
        
        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Tra từ", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=0, column=3, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create listbox
        self.listbox = tkinter.Listbox(self)
        self.listbox.grid(row=1, column=1, columnspan=3, padx=(20, 20), pady=(0, 5), sticky="nsew")
    
        # create answer
        self.ketqua = customtkinter.CTkTabview(self, width=250)
        self.ketqua.grid(row=2, column=1, columnspan=3, padx=(20, 20), pady=(0, 25), sticky="nsew")
        


if __name__ == "__main__":
    app = App()
    app.mainloop()