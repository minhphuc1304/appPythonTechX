import os
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
root = customtkinter.CTk()
root.geometry('350x600')

image_path = os.path.join(os.path.dirname(__file__), 'default.jpg')

image =  customtkinter.CTkImage(light_image = Image.open(image_path), size=(75, 75))
image_label = customtkinter.CTkLabel(root, image= image, text='')
image_label.place(x=10, y=20)

root.mainloop()