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

def filter_sensitive_words(input_file, output_file, sensitive_words_file):
    trie_filter = TrieFilter()

    # Đọc danh sách từ nhạy cảm từ tệp sensitive_words_file
    with open(sensitive_words_file, 'r') as f:
        for line in f:
            word = line.strip()
            trie_filter.add_sensitive_word(word)

    # Đọc và kiểm tra từng dòng trong tệp input_file
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            text = line.strip()
            sensitive_words = trie_filter.contains_sensitive_word(text)

            # Nếu không có từ nhạy cảm, ghi dòng đó vào tệp output_file
            if not sensitive_words:
                output_f.write(text + '\n')

    
def export_filtered_words(input_file, output_file, sensitive_words_file):
    trie_filter = TrieFilter()

    # Đọc danh sách từ nhạy cảm từ tệp sensitive_words_file
    with open(sensitive_words_file, 'r') as f:
        for line in f:
            word = line.strip()
            trie_filter.add_sensitive_word(word)

    filtered_words = set()

    # Đọc và kiểm tra từng dòng trong tệp input_file
    with open(input_file, 'r') as input_f:
        for line in input_f:
            text = line.strip()
            sensitive_words = trie_filter.contains_sensitive_word(text)
            filtered_words.update(sensitive_words)

    # Ghi các từ nhạy cảm đã lọc vào tệp output_file
    with open(output_file, 'w') as output_f:
        for word in filtered_words:
            output_f.write(word + '\n')

# Hàm để lọc từ nhạy cảm và xuất các từ đã lọc
def filter_and_export_sensitive_words(input_file, output_file, sensitive_words_file):
    trie_filter = TrieFilter()

    # Đọc danh sách từ nhạy cảm từ tệp sensitive_words_file
    with open(sensitive_words_file, 'r') as f:
        for line in f:
            word = line.strip()
            trie_filter.add_sensitive_word(word)

    # Đọc và kiểm tra từng dòng trong tệp input_file
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            text = line.strip()
            sensitive_words = trie_filter.contains_sensitive_word(text)

            # Nếu không có từ nhạy cảm, ghi dòng đó vào tệp output_file
            if not sensitive_words:
                output_f.write(text + '\n')

    # Gọi hàm xuất các từ đã lọc
    export_filtered_words(input_file, "/Users/lephuc/Desktop/work/trie/filtered_words.txt", sensitive_words_file)

if __name__ == "__main__":
    input_file = "/Users/lephuc/Desktop/work/trie/input2.txt"  # Tên tệp đầu vào của bạn
    output_file = "/Users/lephuc/Desktop/work/trie/output.txt"  # Tên tệp đầu ra của bạn
    sensitive_words_file = "/Users/lephuc/Desktop/work/trie/sensitive_words.txt"  # Tên tệp từ nhạy cảm của bạn

    filter_and_export_sensitive_words(input_file, output_file, sensitive_words_file)
