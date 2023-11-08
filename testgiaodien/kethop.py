import tkinter as tk
from tkinter import ttk

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    # (Mã code TrieNode tại đây)

class TrieFilter:
    def __init__(self):
        self.root = TrieNode()

    def add_sensitive_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def add_sensitive_words_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()  # Loại bỏ khoảng trắng và ký tự xuống dòng từ từ nhạy cảm
                self.add_sensitive_word(word)

    def contains_sensitive_word(self, text):
        node = self.root
        found_words = set()
        for i, char in enumerate(text):
            if char in node.children:
                node = node.children[char]
                if node.is_end_of_word:
                    found_words.add(text[:i + 1])
            else:
                node = self.root
        return found_words
    

def filter_sensitive_words(text, trie_filter):
    words = text.split()  # Tách văn bản thành danh sách các từ
    filtered_text = []  # Danh sách để lưu trữ văn bản đã lọc

    for word in words:
        # Kiểm tra xem từ word có chứa từ nhạy cảm không
        found_words = trie_filter.contains_sensitive_word(word)
        if found_words:
            for found_word in found_words:
                # Thay thế từ nhạy cảm bằng dấu "*"
                word = word.replace(found_word, '*' * len(found_word))
        filtered_text.append(word)

    return ' '.join(filtered_text)  # Trả về văn bản sau khi đã lọc

def gui_tin_nhan():
    tin_nhan = entry.get()
    if tin_nhan:
        filtered_tin_nhan = filter_sensitive_words(tin_nhan, trie_filter)
        chat_box.insert("end", "Bạn: " + filtered_tin_nhan + "\n")
        entry.delete(0, "end")

root = tk.Tk()
root.title("Hộp Chat")

frame = ttk.Frame(root, relief="groove", borderwidth=5)
frame.grid(row=0, column=0, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

chat_box = tk.Text(frame, wrap="word", relief="groove", borderwidth=5)
scrollbar = ttk.Scrollbar(frame, command=chat_box.yview)

chat_box.config(yscrollcommand=scrollbar.set)
chat_box.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

entry = tk.Entry(root, relief="ridge", borderwidth=5, width=30)
entry.grid(row=1, column=0, sticky="ew")
entry.bind("<Return>", lambda event: gui_tin_nhan())

gui_tin_nhan_button = tk.Button(root, text="Gửi", command=gui_tin_nhan, relief="ridge")
gui_tin_nhan_button.grid(row=2, column=0)

trie_filter = TrieFilter()
trie_filter.add_sensitive_words_from_file("/Users/lephuc/Desktop/gitpush/testgiaodien/sensitive_words.txt")  # Đảm bảo đường dẫn đúng đến tệp tin sensitive_words.txt

root.mainloop()
