import customtkinter

# Đặt chế độ hiển thị (giả sử có một hàm set_appearance_mode trong customtkinter)
customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()

app.title("Từ điển")
app.geometry("500x500")

# Tạo các widget sử dụng thư viện customtkinter
# Thay thế các dòng sau đây bằng các widget và phương thức thực tế của customtkinter

label = customtkinter.Label(app, text="Nhập từ:")  # Sửa lại dòng này
label.pack(pady=10)

entry = customtkinter.Entry(app)
entry.pack(pady=10)

definition_text = customtkinter.Text(app, height=10, width=40)  # Sửa lại dòng này
definition_text.pack(pady=10)

def lookup_word():
    word = entry.get()
    # Thay thế dòng sau đây với logic tra từ trong từ điển thực tế của bạn
    definition = f"Định nghĩa của từ {word} là: ..."
    definition_text.delete("1.0", customtkinter.END)
    definition_text.insert(customtkinter.END, definition)

lookup_button = customtkinter.Button(app, text="Tra từ", command=lookup_word)  # Sửa lại dòng này
lookup_button.pack(pady=10)

app.mainloop()
