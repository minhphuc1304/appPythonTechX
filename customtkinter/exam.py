import tkinter as tk

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

def on_key_release(event):
    typed_string = event.widget.get()
    process_typed_string(typed_string)

def process_typed_string(typed_string):
    prefix = typed_string
    result = trie.search(prefix)

    # Xóa tất cả các mục hiện có trong Listbox
    listbox.delete(0, tk.END)

    # Thêm các từ vào Listbox
    for word, _, _ in result:
        listbox.insert(tk.END, word)

def on_select(event):
    # Lấy chỉ số của mục được chọn
    selected_index = listbox.curselection()

    if selected_index:
        # Lấy nội dung của mục được chọn
        selected_item = listbox.get(selected_index)
        # Lấy thông tin chi tiết từ từ điển
        meaning = dics.get(selected_item, {}).get("meaning")
        word_type = dics.get(selected_item, {}).get("word_type")
        # In thông tin chi tiết
        print(f"Word: {selected_item}, Meaning: {meaning}, Word Type: {word_type}")

# Example Usage:
trie = Trie()

dics = {
    "hello": {"meaning": "xin chào", "word_type": "ghi chú"},
    "world": {"meaning": "thế giới", "word_type": "danh từ"},
    "python": {"meaning": "một ngôn ngữ lập trình", "word_type": "danh từ"},
    "apple": {"meaning": "quả táo", "word_type": "danh từ"},
    "banana": {"meaning": "quả chuối", "word_type": "danh từ"},
    "book": {"meaning": "sách", "word_type": "danh từ"},
    "run": {"meaning": "chạy", "word_type": "động từ"},
}

for word in dics.keys():
    trie.insert(word)

root = tk.Tk()
root.title("Từ điển với Trie")

# Tạo một ô văn bản (Entry) để nhập chuỗi
entry = tk.Entry(root)
entry.pack()

# Liên kết sự kiện nhả phím với hàm xử lý on_key_release
entry.bind("<KeyRelease>", on_key_release)

# Tạo một Listbox để hiển thị từ
listbox = tk.Listbox(root)
listbox.pack()

# Liên kết sự kiện chọn mục trong Listbox với hàm xử lý on_select
listbox.bind("<<ListboxSelect>>", on_select)

# Chạy vòng lặp sự kiện của Tkinter
root.mainloop()
