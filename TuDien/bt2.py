# Trong trie_and_data.py
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

    def get_all_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self.get_all_words(child_node, prefix + char))
        return words

dics = {
    "apace": {"meaning": "Nhanh chóng", "word_type": "adverb", "img": "img/default.png"},
    "adage": {"meaning": "Châm ngôn", "word_type": "noun", "img": "img/default.png"},
    "world": {"meaning": "Thế giới", "word_type": "noun", "img": "img/default.png"},
    "python": {"meaning": "Con trăn", "word_type": "noun", "img": "img/python.jpg"},
    "apple": {"meaning": "Quả táo", "word_type": "noun", "img": "img/apple.jpg"},
    "banana": {"meaning": "Quả chuối", "word_type": "danh từ", "img": "img/banana.jpg"},
    "bath": {"meaning": "Bồn tắm", "word_type": "danh từ", "img": "img/bath.jpg"},
    "bail": {"meaning": "Giấy bảo lãnh", "word_type": "danh từ", "img": "img/default.png"},
    "book": {"meaning": "Cuốn sách", "word_type": "danh từ", "img": "img/book.jpg"},
    "run": {"meaning": "Chạy", "word_type": "động từ", "img": "img/default.png"},
    "bank": {"meaning": "Ngân hàng", "word_type": "danh từ", "img": "img/default.png"},
    "boss": {"meaning": "Sếp lớn", "word_type": "danh từ", "img": "img/default.png"},
    "angel": {"meaning": "Thiên thần", "word_type": "danh từ", "img": "img/default.png"},
    "egg": {"meaning": "Quả trứng", "word_type": "danh từ", "img": "img/egg.jpg"},
    "fan": {"meaning": "Cái quạt", "word_type": "danh từ", "img": "img/default.png"},
}

def main():
    trie = Trie()

    # Thêm dữ liệu từ điển vào trie
    for word in dics.keys():
        trie.insert(word)

    while True:
        # Nhập từ cần tìm kiếm
        search_word = input("Nhập từ cần tìm kiếm (để thoát, nhập 'exit'): ")
        
        if search_word.lower() == 'exit':
            break

        # Tìm kiếm và in kết quả
        results = trie.search(search_word)
        if results:
            for result in results:
                print(f"Từ: {result[0]}, Ý nghĩa: {result[1]}, Loại từ: {result[2]}")
        else:
            print("Không tìm thấy từ.")

if __name__ == "__main__":
    main()