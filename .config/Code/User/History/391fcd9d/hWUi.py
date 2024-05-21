import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image

class PyBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Browser")
        self.geometry("400x300")

        self.url_label = tk.Label(self, text="URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack()

        self.method_label = tk.Label(self, text="Method:")
        self.method_label.pack()

        self.method_var = tk.StringVar()
        self.method_entry = ttk.Combobox(self, width=17, textvariable=self.method_var)
        self.method_entry['values'] = ('GET', 'POST', 'PUT', 'DELETE', 'HEAD')
        self.method_entry.current(0)
        self.method_entry.pack()

        self.send_button = tk.Button(self, text="Send Request", command=self.send_request)
        self.send_button.pack()

        self.response_text = tk.Text(self, height=10, width=50)
        self.response_text.pack()

    def send_request(self):
        url = self.url_entry.get()
        method = self.method_var.get()

        if url == "dev.jpeg":
            try:
                img = Image.open("dev.jpeg")
                img.show()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open image: {str(e)}")
        else:
            messagebox.showerror("Error", "Invalid URL")

if __name__ == "__main__":
     app = PyBrowser()
     app.mainloop()
