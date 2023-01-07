import json
from database import Database
from http.server import HTTPServer, BaseHTTPRequestHandler

class Website(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("hello world!", "utf-8"))

config_file_name = "config.json"
config_file = open("config.json")
config = json.load(config_file)
config_file.close()

print("Starting webserver...")
website = HTTPServer((config["webserver_hostname"], config["webserver_port"]), Website)
print(f'Website started at http://{config["webserver_hostname"]}:{config["webserver_port"]}')

try:
    website.serve_forever()
except KeyboardInterrupt:
    pass

website.server_close()
print("Website stopped.")