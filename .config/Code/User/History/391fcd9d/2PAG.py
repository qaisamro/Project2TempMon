import tkinter as tk
from tkinter import ttk, messagebox
import requests
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
from io import BytesIO

class PyBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Browser")
        self.geometry("400x400")
        self.style = ThemedStyle(self)
        self.style.set_theme("radiance")  # تغيير المظهر إلى Radiance

        style = ttk.Style()
        style.configure("TButton", foreground="black", background="white", font=("Helvetica", 12))
        style.configure("TEntry", foreground="black", background="white", font=("Helvetica", 12))
        style.configure("TLabel", foreground="black", background="white", font=("Helvetica", 12))
        style.configure("TCombobox", foreground="black", background="white", font=("Helvetica", 12))
        style.configure("TText", foreground="black", background="white", font=("Helvetica", 12))

        self.url_label = ttk.Label(self, text="URL:")
        self.url_label.pack()

        self.url_entry = ttk.Entry(self, width=50)
        self.url_entry.pack()

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.pack()

        self.username_entry = ttk.Entry(self, width=50)
        self.username_entry.pack()

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.pack()

        self.password_entry = ttk.Entry(self, width=50, show="*")
        self.password_entry.pack()

        self.method_label = ttk.Label(self, text="Method:")
        self.method_label.pack()

        self.method_var = tk.StringVar()
        self.method_entry = ttk.Combobox(self, width=17, textvariable=self.method_var)
        self.method_entry['values'] = ('GET', 'POST', 'PUT', 'DELETE', 'HEAD')
        self.method_entry.current(0)
        self.method_entry.pack()

        self.send_button = ttk.Button(self, text="Send Request", command=self.send_request)
        self.send_button.pack()

        self.response_text = ttk.Text(self, height=10, width=50)
        self.response_text.pack()

    def send_request(self):
        url = self.url_entry.get()
        method = self.method_var.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            response = requests.request(method, url, auth=(username, password))
            self.display_response(response)
        except requests.exceptions.RequestException as e:
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, f"Error: {str(e)}")

    def display_response(self, response):
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, f"Status Code: {response.status_code}\n")
        self.response_text.insert(tk.END, "Headers:\n")
        self.response_text.insert(tk.END, f"{response.headers}\n\n")

        # Check if the response is an image
        if response.headers.get("Content-Type", "").startswith("image"):
            try:
                img_data = response.content
                img = Image.open(BytesIO(img_data))
                img.show()
            except Exception as e:
                messagebox.showerror("Error", f"Error displaying image: {str(e)}")
        else:
            self.response_text.insert(tk.END, "Response Body:\n")
            self.response_text.insert(tk.END, response.text)

if __name__ == "__main__":
    app = PyBrowser()
    app.mainloop()
