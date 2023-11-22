import tkinter as tk

def on_key_release(event):
    typed_string = event.widget.get()
    process_typed_string(typed_string)

def process_typed_string(typed_string):
    print(f"Processing typed string: {typed_string}")
    # Thực hiện xử lý với chuỗi đã gõ ở đây

# Giao diện đồ họa
root = tk.Tk()
root.title("Từ điển với Trie")

# Tạo một ô văn bản (Entry) để nhập chuỗi
entry = tk.Entry(root)
entry.pack()

# Liên kết sự kiện nhả phím với hàm xử lý on_key_release
entry.bind("<KeyRelease>", on_key_release)

# Chạy vòng lặp sự kiện của Tkinter
root.mainloop()
