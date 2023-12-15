# Tạo các hàm cho giao diện
import tkinter as tk
import tkinter.messagebox as messagebox

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Hộp Chat")

# Tạo các hàm cho giao diện

# Hàm gửi tin nhắn
def send_message():
    # Lấy tin nhắn từ trường nhập liệu
    message = entry.get()

    # Hiển thị tin nhắn trong hộp văn bản
    chat_box.insert("end", "Bạn: " + message + "\n")

    # Xóa tin nhắn khỏi trường nhập liệu
    entry.delete(0, "end")

# Hàm hiển thị danh sách từ nhạy cảm
def show_list():
    # Hiển thị danh sách từ nhạy cảm trong một cửa sổ bật lên
    messagebox.showinfo("Danh sách từ nhạy cảm", "Danh sách từ nhạy cảm đang trống!")

# Hàm thêm từ nhạy cảm mới
def add_word():
    # Lấy từ nhạy cảm từ trường nhập liệu
    word = entry.get()

    messagebox.showinfo("Thông báo", f"Từ nhạy cảm '{word}' đã được thêm thành công!")


# Tạo hộp văn bản
chat_box = tk.Text(root, wrap="word", relief="groove", borderwidth=5)
chat_box.grid(row=0, column=0, sticky="nsew")

# Tạo trường nhập liệu
entry = tk.Entry(root, relief="ridge", borderwidth=5, width=30)
entry.grid(row=1, column=0, sticky="ew")

# Tạo các nút
send_button = tk.Button(root, text="Gửi", command=send_message, relief="ridge")
send_button.grid(row=2, column=0)

list_button = tk.Button(root, text="Danh sách từ nhạy cảm", command=show_list, relief="ridge")
list_button.grid(row=3, column=0)

add_button = tk.Button(root, text="Thêm từ nhạy cảm", command=add_word, relief="ridge")
add_button.grid(row=4, column=0)

# Bắt đầu vòng lặp chính
root.mainloop()
