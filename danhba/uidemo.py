import tkinter as tk

class MyGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Entry and Button in row 0
        entry = tk.Entry(self)
        button = tk.Button(self, text="Click Me")

        entry.grid(row=0, column=0, columnspan=3, sticky="ew")
        button.grid(row=0, column=3, sticky="ew")

        # Listbox in row 1
        listbox = tk.Listbox(self)
        listbox.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # Two buttons in row 3
        button1 = tk.Button(self, text="Button 1")
        button2 = tk.Button(self, text="Button 2")

        button1.grid(row=3, column=0, columnspan=2, sticky="ew")
        button2.grid(row=3, column=2, columnspan=2, sticky="ew")

        # Configure column and row weights
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

if __name__ == "__main__":
    app = MyGUI()
    app.mainloop()
