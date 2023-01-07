import time
from math import sin, pi

from datetime import datetime
from database import Database

def start_humidity_reader(config, db: Database):
    print("Starting humidity reader module...")
    interval = config["humidity_capture_interval_seconds"]

    while True:
        # TODO: Add humidity reader
        temp = read_temp()
        humidity = read_humidity()

        print(f'Temp is {temp}')
        print(f'Humidty is {humidity}')
        db.insert_reading(1, temp, humidity)
        db.print_readings_table()
        time.sleep(interval)

def read_temp():
    date = datetime.now()
    seconds = date.hour * 3600 + date.minute * 60 + date.second
    temp = 2.5 * sin(2 * pi / 24 / 60 / 60 * seconds + pi) + 52.5
    return round(temp, 2)

def read_humidity():
    date = datetime.now()
    seconds = date.hour * 3600 + date.minute * 60 + date.second
    humidity = .075 * sin(2 * pi / 24 / 60 / 60 * seconds) + 75.5
    return round(humidity, 2)