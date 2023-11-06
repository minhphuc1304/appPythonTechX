class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class TreeNode:
    def __init__(self, contact):
        self.contact = contact
        self.left = None
        self.right = None

class PhoneBook:
    def __init__(self):
        self.root = None

    def insert(self, contact):
        if not self.root:
            self.root = TreeNode(contact)
        else:
            self._insert(self.root, contact)

    def _insert(self, node, contact):
        if contact.name < node.contact.name:
            if node.left is None:
                node.left = TreeNode(contact)
            else:
                self._insert(node.left, contact)
        elif contact.name > node.contact.name:
            if node.right is None:
                node.right = TreeNode(contact)
            else:
                self._insert(node.right, contact)
        else:
            # If the name already exists, update the contact information
            node.contact = contact

    def search(self, query):
        result = self._search(self.root, query)
        if not result:
            result = self._search(self.root, query, by_phone=True)
        return result

    def _search(self, node, query, by_phone=False):
        if node is None:
            return None
        if by_phone:
            if query == node.contact.phone_number:
                return node.contact
        else:
            if query == node.contact.name:
                return node.contact
        if (by_phone and query < node.contact.phone_number) or (not by_phone and query < node.contact.name):
            return self._search(node.left, query, by_phone)
        else:
            return self._search(node.right, query, by_phone)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    name, phone_number = parts
                    self.insert(Contact(name, phone_number))


# Tạo danh bạ điện thoại và nạp danh bạ từ tệp văn bản
phone_book = PhoneBook()
phone_book.load_from_file("/Users/lephuc/Desktop/work/danhba/phonebook.txt")

while True:
    print("Nhập tên hoặc số điện thoại liên hệ (hoặc nhấn Enter để thoát):")
    query = input()
    if not query:
        break

    result = phone_book.search(query)

    if result:
        print("================================================================")
        print("")
        print(f"Liên hệ cho {query}: {'Tên: ' + result.name if query == result.phone_number else 'Số điện thoại: ' + result.phone_number}")
        print("")
        print("================================================================")
    else:
        print("================================================================")
        print("")
        print(f"Không tìm thấy liên hệ cho {query}")
        print("")
        print("================================================================")
