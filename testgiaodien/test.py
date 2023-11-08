import tkinter as tk
from tkinter import ttk

def gui_tin_nhan():
    tin_nhan = entry.get()
    if tin_nhan:
        chat_box.insert("end", "Bạn: " + tin_nhan + "\n")
        entry.delete(0, "end")

root = tk.Tk()
root.title("Hộp Chat")

frame = ttk.Frame(root, relief="groove", borderwidth=5)  # Sử dụng relief và borderwidth
frame.grid(row=0, column=0, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

chat_box = tk.Text(frame, wrap="word", relief="groove", borderwidth=5)  # Sử dụng relief và borderwidth
scrollbar = ttk.Scrollbar(frame, command=chat_box.yview)

chat_box.config(yscrollcommand=scrollbar.set)
chat_box.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

entry = tk.Entry(root, relief="ridge", borderwidth=5, width=30)  # Sử dụng relief và width
entry.grid(row=1, column=0, sticky="ew")
entry.bind("<Return>", lambda event: gui_tin_nhan())

gui_tin_nhan_button = tk.Button(root, text="Gửi", command=gui_tin_nhan, relief="ridge")  # Sử dụng relief
gui_tin_nhan_button.grid(row=2, column=0)

root.mainloop()
