import json
from database import Database
from humidity_reader import start_humidity_reader

config_file_name = "config.json"
config_file = open("config.json")
config = json.load(config_file)
config_file.close()

db = Database(config)

start_humidity_reader(config, db)