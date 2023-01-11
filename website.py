import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from humidity_reader import read_humidity, read_temp
from database import Database
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


config_file_name = "config.json"
config_file = open("config.json")
config = json.load(config_file)
config_file.close()

db = Database(config)
env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)

template = env.get_template(config["webserver_template_file"])

class Website(BaseHTTPRequestHandler):
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        
        if params.get("page") == None or not str(params.get("page")[0]).isnumeric():
            page = 1
        else:
            page = int(params["page"][0])

        readings = db.get_readings(page)
        next_page_exists = len(db.get_readings(page + 1)) is not 0

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(template.render(inst_temp=read_temp(), inst_humidity=read_humidity(), readings=readings, page=page, next_page_exists=next_page_exists), "utf-8"))

print("Starting webserver...")
website = HTTPServer((config["webserver_hostname"], config["webserver_port"]), Website)
print(f'Website started at http://{config["webserver_hostname"]}:{config["webserver_port"]}')

try:
    website.serve_forever()
except KeyboardInterrupt:
    pass

website.server_close()
print("Website stopped.")