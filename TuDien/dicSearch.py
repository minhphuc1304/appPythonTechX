class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # def insert(self, word):
    #     node = self.root
    #     for char in word:
    #         if char not in node.children:
    #             node.children[char] = TrieNode()
    #         node = node.children[char]
    #     node.is_end_of_word = True

    # def search(self, word):
    #     node = self.root
    #     for char in word:
    #         if char not in node.children:
    #             return False
    #         node = node.children[char]
    #     return node.is_end_of_word

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Đối tượng Trie
trie = Trie()

# Đọc từ tệp văn bản và chèn vào Trie
with open("/Users/lephuc/Desktop/gitpush/TuDien/dictionary.txt", "r") as file:
    for line in file:
        word = line.strip()  # Loại bỏ ký tự xuống dòng và khoảng trắng thừa
        trie.insert(word)

# Tìm kiếm các từ trong Trie
while True:
    search_word = input("Nhập từ cần tìm (hoặc nhấn Enter để thoát): ").strip()

    if not search_word:
        break

    if trie.search(search_word):
        print(f"{search_word} tồn tại trong từ điển.")
    else:
        print(f"{search_word} không tồn tại trong từ điển.")
        
