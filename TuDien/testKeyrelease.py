import tkinter as tk
from tkinter import messagebox
import difflib

class DictionaryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Dictionary App")

        # Tạo và hiển thị giao diện
        self.create_widgets()

    def create_widgets(self):
        # Tạo các widget
        self.label = tk.Label(self.master, text="Nhập từ cần tra:")
        self.entry = tk.Entry(self.master)
        self.result_label = tk.Label(self.master, text="Kết quả:")
        self.suggestions_label = tk.Label(self.master, text="Các từ liên quan:")

        # Định vị các widget
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.entry.grid(row=0, column=1, padx=10, pady=10)
        self.result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.suggestions_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Bắt sự kiện khi người dùng nhập vào
        self.entry.bind("<KeyRelease>", self.on_entry_key_release)

    def on_entry_key_release(self, event):
        # Từ điển đơn giản
        dictionary = {
            "hello": "Xin chào",
            "hell": "Xin chào",
            "heheee": "Xin chào",
            "world": "Thế giới",
            "python": "Ngôn ngữ lập trình"
            # Thêm các từ khác nếu cần
        }

        # Lấy từ nhập từ người dùng
        word = self.entry.get().lower()

        # Tra từ trong từ điển
        if word in dictionary:
            definition = dictionary[word]
            self.result_label.config(text=f"Kết quả: {definition}")
        else:
            suggestions = difflib.get_close_matches(word, dictionary.keys())
            if suggestions:
                suggestion_str = ", ".join(suggestions)
                self.suggestions_label.config(text=f"Các từ liên quan: {suggestion_str}")
            else:
                self.suggestions_label.config(text="Không có từ liên quan.")
            self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()
