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

    def get_all_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self.get_all_words(child_node, prefix + char))
        return words

dics = {
    "apace": {"meaning": "Nhanh chóng", "word_type": "adverb"},
    "adage": {"meaning": "Châm ngôn", "word_type": "noun"},
    "world": {"meaning": "Thế giới", "word_type": "noun"},
    "python": {"meaning": "Con trăn", "word_type": "noun"},
    "apple": {"meaning": "Quả táo", "word_type": "noun"},
    "banana": {"meaning": "Quả chuối", "word_type": "danh từ"},
    "bath": {"meaning": "Bồn tắm", "word_type": "danh từ"},
    "bail": {"meaning": "Giấy bảo lãnh", "word_type": "danh từ"},
    "book": {"meaning": "Cuốn sách", "word_type": "danh từ"},
    "run": {"meaning": "Chạy", "word_type": "động từ"},
    "bank": {"meaning": "Ngân hàng", "word_type": "danh từ"},
    "boss": {"meaning": "Sếp lớn", "word_type": "danh từ"},
    "angel": {"meaning": "Thiên thần", "word_type": "danh từ"},
    "egg": {"meaning": "Quả trứng", "word_type": "danh từ"},
    "fan": {"meaning": "Cái quạt", "word_type": "danh từ"},
}

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter_Dictionary.py")
        self.geometry(f"{560}x{420}")

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

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Tra từ", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.search_button_clicked)
        self.main_button_1.grid(row=0, column=3, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Bind the KeyRelease event to the on_key_release function
        self.entry.bind("<KeyRelease>", self.on_key_release)

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
        self.label2.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nw")
        self.label3 = customtkinter.CTkLabel(master=self.answer_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="e", justify="right")
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
        # self.label2.configure(text=f"Nghĩa: {meaning}")
        # self.label3.configure(text=f"Loại từ: {word_type}")

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
        typed_string = self.entry.get()  # Lấy chuỗi từ hộp nhập
        result = self.trie.search(typed_string)
        self.listbox.delete(0, tk.END)

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

    def populate_listbox(self):
        all_words = self.trie.get_all_words(self.trie.root, "")
        for word in all_words:
            self.listboxWords.insert(tk.END, word)


if __name__ == "__main__":
    app = App()
    app.mainloop()