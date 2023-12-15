import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

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
    
    def get_sensitive_words(self):
        # Hàm này trả về danh sách các từ nhạy cảm trong Trie
        danh_sach_tu = []
        self._get_sensitive_words_recursive(self.root, "", danh_sach_tu)
        return danh_sach_tu

    def _get_sensitive_words_recursive(self, node, current_word, danh_sach_tu):
        # Hàm đệ quy để lấy danh sách từ nhạy cảm
        if node.is_end_of_word:
            danh_sach_tu.append(current_word)
        for char, child_node in node.children.items():
            self._get_sensitive_words_recursive(child_node, current_word + char, danh_sach_tu)

def main():
    trie_filter = TrieFilter()
    trie_filter.add_sensitive_word("hello")
    trie_filter.add_sensitive_word("world")
    
    # Don't reassign trie_filter here, use the existing instance
    trie_filter.add_sensitive_words_from_file("/Users/lephuc/Desktop/gitpush/AppLocTu/sensitive_words.txt")

    message = input("Nhập tin nhắn: ")
    found_words = trie_filter.contains_sensitive_word(message)

    if found_words:
        print("Có từ nhạy cảm trong tin nhắn:")
        for word in found_words:
            print(word)
    else:
        print("Không có từ nhạy cảm trong tin nhắn.")

if __name__ == "__main__":
    main()

