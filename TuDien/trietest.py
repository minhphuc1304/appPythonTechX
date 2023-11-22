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
            # Trả về một danh sách rỗng nếu tiền tố là chuỗi rỗng
            return []

        node = self.root
        for char in prefix:
            if char not in node.children:
                # Return an empty list if the prefix is not found
                return []

            node = node.children[char]

        return self._get_all_words_from_node(node, prefix)

    def _get_all_words_from_node(self, node, prefix):
        result = []
        if node.is_end_of_word:
            result.append(prefix)

        for char, child_node in node.children.items():
            result.extend(self._get_all_words_from_node(child_node, prefix + char))

        return result
    
    def _get_all_words_from_node(self, node, prefix):
        result = []
        if node.is_end_of_word:
            # Trả về tuple chứa từ, nghĩa và loại từ
            result.append((prefix, dics.get(prefix, {}).get("meaning"), dics.get(prefix, {}).get("word_type")))

        for char, child_node in node.children.items():
            result.extend(self._get_all_words_from_node(child_node, prefix + char))

        return result

def on_key_release(event):
    typed_string = event.widget.get()
    process_typed_string(typed_string)

def process_typed_string(typed_string):
    # Thực hiện xử lý với chuỗi đã gõ ở đây
    prefix = typed_string
    result = trie.search(prefix)

    for word, meaning, word_type in result:
        print(f"Word: {word}, Meaning: {meaning}, Word Type: {word_type}")


# Example Usage:
trie = Trie()
# words = ["cat", "car", "cot", "hot", "hat", "heap"]
dics = {
    "hello": {"meaning": "xin chào", "word_type": "ghi chú"},
    "world": {"meaning": "thế giới", "word_type": "danh từ"},
    "python": {"meaning": "một ngôn ngữ lập trình", "word_type": "danh từ"},
    "apple": {"meaning": "quả táo", "word_type": "danh từ"},
    "banana": {"meaning": "quả chuối", "word_type": "danh từ"},
    "book": {"meaning": "sách", "word_type": "danh từ"},
    "run": {"meaning": "chạy", "word_type": "động từ"},
    "cat": {"meaning": "Mèo", "word_type": "danh từ"},
    "car": {"meaning": "Xe hơi", "word_type": "danh từ"},
}

# Insert words into the trie
for word, details in dics.items():
    trie.insert(word)

root = tk.Tk()
root.title("Từ điển với Trie")

# Tạo một ô văn bản (Entry) để nhập chuỗi
entry = tk.Entry(root)
entry.pack()

# Liên kết sự kiện nhả phím với hàm xử lý on_key_release
entry.bind("<KeyRelease>", on_key_release)

# Chạy vòng lặp sự kiện của Tkinter
root.mainloop()