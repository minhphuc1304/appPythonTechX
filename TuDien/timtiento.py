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
        node = self.root
        result = []

        # Tìm kiếm tiền tố
        for char in prefix:
            if char not in node.children:
                return result
            node = node.children[char]

        # Hàm đệ quy để lấy tất cả các từ có tiền tố là prefix
        self._get_words_with_prefix(node, prefix, result)

        # Nếu tiền tố là một từ, thêm nó vào danh sách kết quả
        if node.is_end_of_word:
            result.append(prefix)

        return result

    def _get_words_with_prefix(self, node, current_word, result):
        if node.is_end_of_word:
            result.append(current_word)
        for char, child_node in node.children.items():
            self._get_words_with_prefix(child_node, current_word + char, result)

# Example usage:
trie = Trie()

# Đọc từ tệp văn bản và chèn vào Trie
with open("/Users/lephuc/Desktop/gitpush/TuDien/dictionary.txt", "r") as file:
    for line in file:
        word = line.strip()  # Loại bỏ ký tự xuống dòng và khoảng trắng thừa
        trie.insert(word)

# Tìm kiếm từ "ap"
search_prefix = "hell"
result = trie.search(search_prefix)

# In kết quả
if result:
    print(f"Các từ có tiền tố '{search_prefix}':")
    for word in result:
        print(word)
else:
    print(f"Không tìm thấy từ có tiền tố '{search_prefix}' trong Trie.")
