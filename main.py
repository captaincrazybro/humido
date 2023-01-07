import json
from website import start_webserver
from database import Database
from humidity_reader import start_humidty_reader

config_file_name = "config.json"
config_file = open("config.json")
config = json.load(config_file)
config_file.close()

db = Database(config)

start_humidty_reader(config, db)
start_webserver(config, db)