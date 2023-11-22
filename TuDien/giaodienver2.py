import tkinter as tk
from tkinter import ttk

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.meaning = ""
        self.word_type = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, meaning, word_type):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.meaning = meaning
        node.word_type = word_type

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False, "", ""
            node = node.children[char]
        return node.is_end_of_word, node.meaning, node.word_type

    def search_prefix(self, prefix):
        node = self.root
        result = []

        # Tìm kiếm tiền tố
        for char in prefix:
            if char not in node.children:
                return result
            node = node.children[char]

        # Hàm đệ quy để lấy tất cả các từ có tiền tố là prefix
        self._get_words_with_prefix(node, prefix, result)

        return result

    def _get_words_with_prefix(self, node, current_word, result):
        if node.is_end_of_word:
            result.append(current_word)
        for char, child_node in node.children.items():
            self._get_words_with_prefix(child_node, current_word + char, result)

# Xây dựng từ điển trực tiếp trong mã nguồn
tu_dien = {
    "hello": {"meaning": "xin chào", "word_type": "ghi chú"},
    "world": {"meaning": "thế giới", "word_type": "danh từ"},
    "python": {"meaning": "một ngôn ngữ lập trình", "word_type": "danh từ"},
    "apple": {"meaning": "quả táo", "word_type": "danh từ"},
    "banana": {"meaning": "quả chuối", "word_type": "danh từ"},
    "book": {"meaning": "sách", "word_type": "danh từ"},
    "run": {"meaning": "chạy", "word_type": "động từ"},
}

# Tạo đối tượng Trie và chèn từ điển vào Trie
trie = Trie()
for word, info in tu_dien.items():
    trie.insert(word, info["meaning"], info["word_type"])

def tra_tu():
    tu_can_tra = entry_tu.get().lower()

    # Tìm kiếm chính xác từ
    found_exact, meaning_exact, word_type_exact = trie.search(tu_can_tra)

    # Tìm kiếm tiền tố
    result_prefix = trie.search_prefix(tu_can_tra)

    # Hiển thị kết quả
    if found_exact:
        hien_thi_ket_qua(f"Tìm thấy từ: {tu_can_tra}\nNghĩa: {meaning_exact}\nTừ loại: {word_type_exact}")
    elif result_prefix:
        hien_thi_ket_qua(f"Các từ có tiền tố '{tu_can_tra}':\n" + "\n".join(result_prefix))
    else:
        hien_thi_ket_qua(f"Từ '{tu_can_tra}' không có trong từ điển.")

def hien_thi_ket_qua(ket_qua):
    ket_qua_text.config(state=tk.NORMAL)
    ket_qua_text.delete("1.0", tk.END)
    ket_qua_text.insert(tk.END, ket_qua)
    ket_qua_text.config(state=tk.DISABLED)

def them_tu_moi():
    tu_moi = entry_tu_moi.get().lower()
    nghia_moi = entry_nghia_moi.get()
    loai_tu_moi = entry_loai_tu_moi.get()

    if tu_moi and nghia_moi and loai_tu_moi:
        tu_dien[tu_moi] = {"meaning": nghia_moi, "word_type": loai_tu_moi}
        trie.insert(tu_moi, nghia_moi, loai_tu_moi)
        hien_thi_ket_qua(f"Đã thêm từ mới: {tu_moi}\nNghĩa: {nghia_moi}\nTừ loại: {loai_tu_moi}")
    else:
        hien_thi_ket_qua("Vui lòng nhập đủ thông tin cho từ mới.")

def on_key_release(event):
    typed_string = event.widget.get()
    process_typed_string(typed_string)

def process_typed_string(typed_string):
    print(f"Processing typed string: {typed_string}")
    # Thực hiện xử lý với chuỗi đã gõ ở đây

# Giao diện đồ họa
root = tk.Tk()
root.title("Từ điển với Trie")

# Frame tra từ ở dòng 0
frame_tra_tu = tk.Frame(root, bd=2, relief=tk.GROOVE)
frame_tra_tu.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N)

entry_tu = tk.Entry(frame_tra_tu, width=30)
entry_tu.grid(row=0, column=0, padx=5)

button_tra_tu = tk.Button(frame_tra_tu, text="Tra từ", command=tra_tu)
button_tra_tu.grid(row=1, column=0, padx=5)

# Frame hiển thị kết quả ở dòng 1, cột 0 và chiếm 2 cột
frame_ket_qua = tk.Frame(root, bd=2, relief=tk.GROOVE)
frame_ket_qua.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

ket_qua_text = tk.Text(frame_ket_qua, height=5, width=40, wrap=tk.WORD, state=tk.DISABLED)
ket_qua_text.grid(row=0, column=0)

# Frame thêm từ mới ở dòng 2
frame_them_tu_moi = tk.Frame(root, bd=2, relief=tk.GROOVE)

frame_them_tu_moi.grid(row=2, column=0, padx=10, pady=10, sticky=tk.N)

entry_tu_moi = tk.Entry(frame_them_tu_moi, width=20)
entry_tu_moi.grid(row=0, column=0, padx=5)

entry_nghia_moi = tk.Entry(frame_them_tu_moi, width=20)
entry_nghia_moi.grid(row=1, column=0, padx=5)

entry_loai_tu_moi = tk.Entry(frame_them_tu_moi, width=20)
entry_loai_tu_moi.grid(row=2, column=0, padx=5)

button_them_tu_moi = tk.Button(frame_them_tu_moi, text="Thêm từ mới", command=them_tu_moi)
button_them_tu_moi.grid(row=3, column=0, padx=5)

root.mainloop()
