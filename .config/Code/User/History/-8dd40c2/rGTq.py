from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import base64
from PIL import Image

USER = "admin"
PASSWORD = "password"

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if not self.authenticate():
            self.send_authenticate_header()
            return

        if self.path == "/":
            self.handle_root()
        elif self.path == "/data":
            self.handle_data()
        elif self.path == "/image":
            self.handle_image()
        else:
            self.handle_static()

    def send_authenticate_header(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="PyHTTPServer"')
        self.end_headers()
        self.wfile.write(b"Authentication required")

    def authenticate(self):
        auth_header = self.headers.get("Authorization")
        if auth_header:
            auth_type, auth_token = auth_header.split()
            if auth_type.lower() == "basic":
                decoded_token = base64.b64decode(auth_token).decode("utf-8")
                username, password = decoded_token.split(":")
                return username == USER and password == PASSWORD
        return False

    def handle_root(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Welcome to PyHTTPServer!</h1>")

    def handle_data(self):
        data = {"message": "This is dynamic content"}
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def handle_image(self):
        image_path = os.path.join("project 1", "dev.jpeg")
        if os.path.exists(image_path):
            with open(image_path, "rb") as file:
                image_data = file.read()
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()
            self.wfile.write(image_data)
        else:
            self.send_error(404, "Image Not Found")

    def handle_static(self):
        static_file_path = os.path.join("static", os.path.normpath(self.path.lstrip("/")).lstrip("\\/"))
        if os.path.exists(static_file_path) and os.path.isfile(static_file_path):
            with open(static_file_path, "rb") as file:
                content = file.read()
            self.send_response(200)
            self.send_header("Content-type", self.guess_content_type(static_file_path))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_error(404, "File Not Found")

    def guess_content_type(self, file_path):
        _, ext = os.path.splitext(file_path)
        return {
            ".html": "text/html",
            ".css": "text/css",
            ".js": "application/javascript",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg"
        }.get(ext.lower(), "application/octet-stream")

def run_server():
    server_address = ('', 8038)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print("Starting PyHTTPServer on port 8038...")
    httpd.serve_forever()

if __name__ == "__main__":
     run_server()
