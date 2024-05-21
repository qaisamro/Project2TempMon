import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk

from io import BytesIO

class PyBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyBrowser")
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

        self.image_label = tk.Label(self)
        self.image_label.pack()

    def send_request(self):
        url = self.url_entry.get()
        method = self.method_var.get()

        try:
            response = requests.request(method, url)
            if response.headers.get("Content-Type", "").startswith("image"):
                img_data = response.content
                img = Image.open(BytesIO(img_data))
                img = img.resize((200, 200))  # Resize the image to fit the window
                photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=photo)
                self.image_label.image = photo
                self.response_text.delete(1.0, tk.END)
            else:
                self.response_text.delete(1.0, tk.END)
                self.response_text.insert(tk.END, response.text)
        except requests.exceptions.RequestException as e:
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, f"Error: {str(e)}")

if __name__ == "__main__":
    app = PyBrowser()
    app.mainloop()
