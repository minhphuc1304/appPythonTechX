import tkinter as tk
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        if not prefix:
            return []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_all_words_from_node(node, prefix)

    def _get_all_words_from_node(self, node, prefix):
        result = []
        if node.is_end_of_word:
            result.append((prefix, dics.get(prefix, {}).get("meaning"), dics.get(prefix, {}).get("word_type")))
        for char, child_node in node.children.items():
            result.extend(self._get_all_words_from_node(child_node, prefix + char))
        return result


dics = {
    "hello": {"meaning": "xin chào", "word_type": "ghi chú"},
    "world": {"meaning": "thế giới", "word_type": "danh từ"},
    "python": {"meaning": "một ngôn ngữ lập trình", "word_type": "danh từ"},
    "apple": {"meaning": "quả táo", "word_type": "danh từ"},
    "banana": {"meaning": "quả chuối", "word_type": "danh từ"},
    "book": {"meaning": "sách", "word_type": "danh từ"},
    "run": {"meaning": "chạy", "word_type": "động từ"},
    "bank": {"meaning": "Ngân hàng", "word_type": "danh từ"},
    "boss": {"meaning": "Sếp lớn", "word_type": "danh từ"},
}

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter_Dictionary.py")
        self.geometry(f"{500}x{400}")

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
        self.label1.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="")
        self.label2 = customtkinter.CTkLabel(master=self.answer_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="e", justify="right")
        self.label2.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="")
        self.label3 = customtkinter.CTkLabel(master=self.answer_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="e", justify="right")
        self.label3.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="")


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
    
    def on_select(self, event):
        # Get the index of the selected item
        selected_index = self.listbox.curselection()

        if selected_index:
            selected_item = self.listbox.get(selected_index)
            meaning = dics.get(selected_item, {}).get("meaning")
            word_type = dics.get(selected_item, {}).get("word_type")
            self.label1.configure(text=f"{selected_item}")
            self.label2.configure(text=f"{meaning}")
            self.label3.configure(text=f"{word_type}")
    
    def search_button_clicked(self):
        typed_string = self.entry.get()  # Lấy chuỗi từ hộp nhập
        result = self.trie.search(typed_string)

        if len(result) == 1:
            # Nếu chỉ có một kết quả, in ra giá trị
            word, meaning, word_type = result[0]
            self.label1.configure(text=f"{word}")
            self.label2.configure(text=f"{meaning}")
            self.label3.configure(text=f"{word_type}")

        else:
            # Nếu có nhiều kết quả hoặc không có kết quả, hiển thị danh sách trong Listbox
            for word, _, _ in result:
                self.listbox.insert(tk.END, word)


if __name__ == "__main__":
    app = App()
    app.mainloop()