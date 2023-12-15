import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Các Hàm trie đã có ở bt2
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        pass

    def search(self, prefix):
        pass


    def _get_all_words_from_node(self, node, prefix):
        pass

    def get_all_words(self, node, prefix):
        pass

dics = {
    "apace": {"meaning": "Nhanh chóng", "word_type": "adverb", "img": "img/default.png"},
    # Đã có ở bài 2
}

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter_Dictionary.py")
        self.geometry(f"{560}x{520}")

        # Initialize Trie and insert words
        self.trie = Trie()
        for word in dics.keys():
            self.trie.insert(word)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Dictionary", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.listboxWords = tkinter.Listbox(self.sidebar_frame)
        self.listboxWords.grid(row=4, column=0, padx=20, pady=(10, 10), sticky="nsew")
        self.listboxWords.bind("<<ListboxSelect>>", self.on_select)
        self.populate_listbox()
        
        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="")
        self.entry.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")
        # Bind the KeyRelease event to the on_key_release function
        self.entry.bind("<KeyRelease>", self.on_key_release)
        
        self.main_button_1 = customtkinter.CTkButton(master=self, text="Tra từ", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.search_button_clicked)
        self.main_button_1.grid(row=0, column=3, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create listbox
        self.listbox = tkinter.Listbox(self)
        self.listbox.grid(row=1, column=1, columnspan=3, padx=(20, 20), pady=(0, 5), sticky="nsew")
        # Bind the ListboxSelect event to the on_select function
        self.listbox.bind("<<ListboxSelect>>", self.on_select)
    
        # create answer
        self.answer_frame = customtkinter.CTkFrame(self, width=250)
        self.answer_frame.grid(row=2, column=1, columnspan=3, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.label1 = customtkinter.CTkLabel(master=self.answer_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="e", justify="right")
        self.label1.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nw")
        self.label2 = customtkinter.CTkLabel(master=self.answer_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="e", justify="right")
        self.label2.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.label3 = customtkinter.CTkLabel(master=self.answer_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="e", justify="right",)
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
        prefix = typed_string
        result = self.trie.search(prefix)

        # Clear all items in the Listbox
        self.listbox.delete(0, tk.END)

        # Add words to the Listbox
        for word, _, _ in result:
            self.listbox.insert(tk.END, word)
    
    def update_labels(self, selected_item):
        meaning = dics.get(selected_item, {}).get("meaning")
        word_type = dics.get(selected_item, {}).get("word_type")

        self.label1.configure(text=f"{selected_item}({word_type}): {meaning}")

        img_path = os.path.join(os.path.dirname(__file__), dics.get(selected_item, {}).get("img", 'default.jpg'))
        img = Image.open(img_path)
        img.thumbnail((210, 220))
        img = ImageTk.PhotoImage(img)
        self.label2.configure(image=img)

    def on_select(self, event):
        # Kiểm tra xem sự kiện đến từ listbox nào
        self.listbox_widget = event.widget

        # Lấy chỉ số của mục được chọn từ listbox
        selected_index = self.listbox_widget.curselection()

        if selected_index:
            # Lấy mục được chọn từ listbox
            selected_item = self.listbox_widget.get(selected_index)

            # Gọi hàm để cập nhật labels
            self.update_labels(selected_item)

    
    def search_button_clicked(self):
        pass

    def populate_listbox(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()