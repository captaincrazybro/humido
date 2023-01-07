import time

def start_humidty_reader(config, db):
    print("Starting humidty reader module...")
    interval = config["humidity_capture_interval_seconds"] * 60 

    while True:
        # TODO: Add humidity reader
        humidty = 30

        print(f'Humidty is {humidty}')
        time.sleep(interval)