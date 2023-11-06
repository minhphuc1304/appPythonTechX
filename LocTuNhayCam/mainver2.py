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

if __name__ == "__main__":
    trie_filter = TrieFilter()
    
    # Thêm từ nhạy cảm từ tệp tin "sensitive_words.txt"
    trie_filter.add_sensitive_words_from_file("/Users/lephuc/Desktop/work/trie/sensitive_words.txt")

    while True:
        user_input = input("Nhập văn bản (nhập 'q' để thoát): ")

        if user_input == 'q':
            break

        filtered_text = filter_sensitive_words(user_input, trie_filter)
        print("Văn bản đã lọc:", filtered_text)