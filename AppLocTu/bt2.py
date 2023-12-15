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
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def contains_sensitive_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end_of_word

    def filter_sensitive_words(self, message):
        words = message.split()
        filtered_words = []
        for word in words:
            if self.contains_sensitive_word(word):
                filtered_words.append("*")
            else:
                filtered_words.append(word)
        return " ".join(filtered_words)

def main():
    trie_filter = TrieFilter()
    trie_filter.add_sensitive_word("hello")
    trie_filter.add_sensitive_word("world")

    while True:
        message = input("Nhập tin nhắn: ")
        filtered_message = trie_filter.filter_sensitive_words(message)
        print(filtered_message)

if __name__ == "__main__":
    main()
