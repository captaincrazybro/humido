import time

def humidty_reader_module(config):
    print("Starting humidty reader module...")
    interval = config["humidity_capture_interval_minutes"] * 60 

    while True:
        # TODO: Add humidity reader
        humidty = 30

        print(f'Humidty is {humidty}')
        time.sleep(interval)