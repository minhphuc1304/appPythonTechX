import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()

app.title("Từ điển")
app.geometry("500x500")

def button1_function():
    print("Hello world!")

button = customtkinter.CTkButton(master=app, text="button", command=button1_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
