import json
from sense_hat_display import sense_hat_display_module
from humidity_reader import humidty_reader_module

config_file_name = "config.json"
config_file = open("config.json")
config = json.load(config_file)


humidty_reader_module(config)
sense_hat_display_module(config)