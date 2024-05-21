from http.server import BaseHTTPRequestHandler, HTTPServer
import tkinter as tk
from tkinter import ttk
import requests
import os
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

        try:
            response = requests.request(method, url)
            self.display_response(response)
        except requests.exceptions.RequestException as e:
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, f"Error: {str(e)}")

    def display_response(self, response):
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, f"Status Code: {response.status_code}\n")
        self.response_text.insert(tk.END, "Headers:\n")
        self.response_text.insert(tk.END, f"{response.headers}\n\n")
        if response.headers.get('Content-Type', '').startswith('image/'):
            # Display image
            img = tk.PhotoImage(data=response.content)
            label = tk.Label(self, image=img)
            label.image = img
            label.pack()
        else:
            # Display text response
            self.response_text.insert(tk.END, "Response Body:\n")
            self.response_text.insert(tk.END, response.text)

class PyBrowserRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/image":
            self.handle_image()
        else:
            self.handle_default()

    def handle_default(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        self.wfile.write(b"<html><body>")
        self.wfile.write(b"<h1>Welcome to PyBrowser Server!</h1>")
        self.wfile.write(b"</body></html>")

    def handle_image(self):
    image_path = os.path.join("project 1", "dev.jpeg")
    if os.path.exists(image_path):
        self.serve_file(image_path, "image/jpeg")
    else:
        self.send_error(404, "Image Not Found")

def run_server():
    server_address = ('', 8038)
    httpd = HTTPServer(server_address, PyBrowserRequestHandler)
    print("Starting PyBrowser Server on port 8038...")
    httpd.serve_forever()

if __name__ == "__main__":
    app = PyBrowser()
    app.mainloop()
    run_server()
