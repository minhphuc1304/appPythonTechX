import os
import customtkinter
from PIL import Image, ImageTk

class VocabularyApp:
    def __init__(self, master):
        self.master = master
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.master.geometry('350x600')

        # Tạo một từ điển như đã định nghĩa trước đó
        self.dics = {
            "python": {"meaning": "một ngôn ngữ lập trình", "word_type": "danh từ", "img": "python.png"},
            "apple": {"meaning": "quả táo", "word_type": "danh từ", "img": "apple.jpg"},
            # Thêm các từ vựng khác vào đây
        }

        # Tạo các widget và thiết lập giao diện
        self.image_label = customtkinter.CTkLabel(self.master, text='')
        self.image_label.place(x=10, y=20)

        # Nhãn để hiển thị thông tin từ vựng
        self.label1 = customtkinter.CTkLabel(self.master, text='')
        self.label1.place(x=10, y=120)

        # Tạo danh sách các từ vựng
        self.vocabulary_list = customtkinter.CTkListbox(self.master)
        for word in self.dics.keys():
            self.vocabulary_list.insert(customtkinter.END, word)

        # Xử lý sự kiện khi chọn từ vựng từ danh sách
        self.vocabulary_list.bind('<<ListboxSelect>>', self.on_select)

        self.vocabulary_list.place(x=200, y=20)

    def on_select(self, event):
        # Lấy từ vựng được chọn từ danh sách
        selected_item_index = self.vocabulary_list.curselection()
        if selected_item_index:
            selected_item = self.vocabulary_list.get(selected_item_index[0])

            # Lấy thông tin từ từ điển và cập nhật nhãn và hình ảnh
            meaning = self.dics.get(selected_item, {}).get("meaning")
            word_type = self.dics.get(selected_item, {}).get("word_type")
            img_path = os.path.join(os.path.dirname(__file__), self.dics.get(selected_item, {}).get("img", 'default.jpg'))

            # Hiển thị hình ảnh
            img = Image.open(img_path)
            img.thumbnail((75, 75))
            img = ImageTk.PhotoImage(img)
            self.image_label.configure(image=img)
            self.image_label.image = img  # Giữ tham chiếu để tránh lỗi GC

            # Cập nhật nhãn với thông tin từ vựng
            self.label1.configure(text=f"{selected_item}({word_type}): {meaning}")

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = VocabularyApp(root)
    root.mainloop()
