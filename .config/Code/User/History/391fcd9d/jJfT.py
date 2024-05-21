import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import base64

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
        headers = {}
        auth = ('admin', 'password')  # Replace with your username and password
        headers['Authorization'] = 'Basic ' + base64.b64encode(f"{auth[0]}:{auth[1]}".encode()).decode()

        try:
            response = requests.request(method, url, headers=headers)
            self.display_response(response)
        except requests.exceptions.RequestException as e:
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, f"Error: {str(e)}")

    def display_response(self, response):
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, f"Status Code: {response.status_code}\n")
        self.response_text.insert(tk.END, "Headers:\n")
        self.response_text.insert(tk.END, f"{response.headers}\n\n")
        self.response_text.insert(tk.END, "Response Body:\n")
        
        if response.headers.get("Content-Type", "").startswith("image"):
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img.show()
        else:
            self.response_text.insert(tk.END, response.text)

if __name__ == "__main__":
     app = PyBrowser()
     app.mainloop()
