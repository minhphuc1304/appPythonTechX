import tkinter as tk
from tkinter import scrolledtext
import enchant

class CustomDictChecker(enchant.Dict):
    def check(self, word):
        # Override the check method to exclude checking for certain words
        excluded_words = ["John", "Doe", "Phúc"]  # Add your own excluded words
        if word.capitalize() in excluded_words:
            return True
        return super().check(word)

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        # Initialize the English dictionary with custom checking
        self.spelling_checker = CustomDictChecker("en_US")

        self.message_entry = None

        self.create_widgets()
        self.message_entry.focus_set()  # Set focus to the message entry

    def create_widgets(self):
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=15, width=80, state=tk.DISABLED)
        self.chat_display.pack(padx=10, pady=10)

        self.entry_placeholder = ""
        self.message_entry = tk.Text(self.root, height=5, width=80)
        self.message_entry.insert(tk.END, self.entry_placeholder)
        self.message_entry.bind("<FocusIn>", self.clear_placeholder)
        self.message_entry.bind("<FocusOut>", self.restore_placeholder)
        self.message_entry.bind("<KeyRelease>", self.check_spelling_on_typing)
        self.message_entry.bind("<Return>", self.send_message_on_enter)
        self.message_entry.pack(pady=10)

        send_button = tk.Button(self.root, text="Send", command=self.send_message)
        send_button.pack()

    def clear_placeholder(self, event):
        current_text = self.message_entry.get("1.0", tk.END)
        if current_text.strip() == self.entry_placeholder:
            self.message_entry.delete("1.0", tk.END)
            self.message_entry.config(fg='black')  # Change text color to black

    def restore_placeholder(self, event):
        current_text = self.message_entry.get("1.0", tk.END)
        if not current_text.strip():
            self.message_entry.insert("1.0", self.entry_placeholder)
            self.message_entry.config(fg='grey')  # Change text color to grey

    def send_message(self, event=None):
        message = self.message_entry.get("1.0", tk.END).strip()
        if message:
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.insert(tk.END, f"You: {message}\n")
            self.chat_display.config(state=tk.DISABLED)
            self.message_entry.delete("1.0", tk.END)
            self.restore_placeholder(None)

    def send_message_on_enter(self, event):
        self.send_message()

    def check_spelling_on_typing(self, event):
        current_text = self.message_entry.get("1.0", tk.END).strip()
        self.message_entry.tag_remove("spelling_error", "1.0", tk.END)

        if current_text:
            words = current_text.split()
            for word in words:
                if not self.spelling_checker.check(word):
                    start_index = "1.0 + {} chars".format(current_text.index(word))
                    end_index = "1.0 + {} chars".format(current_text.index(word) + len(word))
                    self.message_entry.tag_add("spelling_error", start_index, end_index)
                    self.message_entry.tag_config("spelling_error", foreground="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
