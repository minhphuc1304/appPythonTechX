import tkinter as tk
from PIL import Image, ImageTk

class DictionaryListBoxApp:
    def __init__(self, master, dictionary):
        self.master = master
        self.master.title("Dictionary ListBox App")
        self.dictionary = dictionary

        self.listbox = tk.Listbox(self.master, width=40, height=15)
        self.listbox.pack(padx=10, pady=10)
        self.listbox.bind("<ButtonRelease-1>", self.on_word_selected)

        self.scrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.populate_listbox()

    def populate_listbox(self):
        for word in self.dictionary.keys():
            self.listbox.insert(tk.END, word)

    def on_word_selected(self, event):
        selected_word = self.listbox.get(self.listbox.curselection())
        word_details = self.dictionary.get(selected_word, {})
        self.show_word_details(word_details)


    def show_word_details(self, word_details):
        # Hiển thị chi tiết từ (ví dụ: cửa sổ pop-up, khung thông tin, vv.)
        img_path = word_details.get("img", "default.png")
        img_path = "/Users/lephuc/Desktop/gitpush/TuDien/" + img_path  # Thêm đường dẫn vào trước tên tệp

        try:
            image = Image.open(img_path)
            image = image.resize((120, 140), Image.BICUBIC)  # Sử dụng Image.BICUBIC để thay thế cho Image.ANTIALIAS
            photo = ImageTk.PhotoImage(image)

            img_label = tk.Label(self.master, image=photo)
            img_label.image = photo
            img_label.pack()

        except Exception as e:
            print(f"Error loading image: {e}")

        meaning_label = tk.Label(self.master, text=f"Meaning: {word_details.get('meaning', 'N/A')}")
        meaning_label.pack()

        word_type_label = tk.Label(self.master, text=f"Word Type: {word_details.get('word_type', 'N/A')}")
        word_type_label.pack()

def main():
    dics = {
        "python": {"meaning": "một ngôn ngữ lập trình", "word_type": "danh từ", "img": "python.png"},
        "apple": {"meaning": "quả táo", "word_type": "danh từ", "img": "apple.jpg"},
        "banana": {"meaning": "quả chuối", "word_type": "danh từ", "img": "banana.png"},
        "book": {"meaning": "sách", "word_type": "danh từ", "img": "book.png"},
        "run": {"meaning": "chạy", "word_type": "động từ", "img": "null.png"},
        "bank": {"meaning": "Ngân hàng", "word_type": "danh từ", "img": "bank.png"},
    }

    root = tk.Tk()
    app = DictionaryListBoxApp(root, dics)
    root.mainloop()

if __name__ == "__main__":
    main()
