import tkinter as tk
from tkinter import ttk

# Import TrieFilter và filter_sensitive_words từ đoạn mã TrieFilter
from TrieFilter import TrieFilter, filter_sensitive_words

def gui_tin_nhan():
    tin_nhan = entry.get()
    if tin_nhan:
        # Lọc từ nhạy cảm từ tin nhắn
        filtered_tin_nhan = filter_sensitive_words(tin_nhan, trie_filter)

        # Hiển thị tin nhắn lọc trên chat_box
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

# Tạo TrieFilter và đọc danh sách từ nhạy cảm từ tệp tin
trie_filter = TrieFilter()
trie_filter.add_sensitive_words_from_file("sensitive_words.txt")

root.mainloop()
