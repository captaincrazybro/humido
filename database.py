import sqlite3
from datetime import datetime

db_create_statement = """CREATE TABLE READING (
    READ_ID INTEGER PRIMARY KEY,
    READ_SENSOR_NUM INT NOT NULL,
    READ_HUMIDITY DECIMAL(3, 2) NOT NULL,
    READ_TEMP DECIMAL(3, 2) NOT NULL,
    READ_DATE DATETIME NOT NULL)"""

class Database:
    def __init__(self, config):
        self.db_name = config["database_name"]

    def create_readings_table(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute(db_create_statement)
    
        con.close()

    def reset_readings_table(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute("DROP TABLE READING")
        cur.execute(db_create_statement)

        con.close()

    def insert_reading(self, sensor_num, temp, humidity):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        current_date = datetime.now()
        data = (sensor_num, temp, humidity, current_date)

        cur.execute("INSERT INTO READING (READ_SENSOR_NUM, READ_TEMP, READ_HUMIDITY, READ_DATE) VALUES (?, ?, ?, ?)", data)
        con.commit()
        con.close()

    def print_readings_table(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        res = cur.execute("SELECT * FROM READING")
        print(res.fetchall())

        con.close()

    def get_readings(self, page):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        raw_readings = cur.execute("SELECT * FROM READING WHERE julianday('now') - julianday(READ_DATE) BETWEEN ? AND ?", ((page - 1) * 10, page * 10 - 1))
        readings = raw_readings.fetchall()
        con.close()
        return readings

    def insert_dummy_data(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute("INSERT INTO READING (READ_SENSOR_NUM, READ_TEMP, READ_HUMIDITY, READ_DATE) VALUES (?, ?, ?, ?)", (1, 53, 75, "2022-12-31 11:19:00"))
        cur.execute("INSERT INTO READING (READ_SENSOR_NUM, READ_TEMP, READ_HUMIDITY, READ_DATE) VALUES (?, ?, ?, ?)", (1, 54, 75, "2022-12-31 11:20:00"))
        cur.execute("INSERT INTO READING (READ_SENSOR_NUM, READ_TEMP, READ_HUMIDITY, READ_DATE) VALUES (?, ?, ?, ?)", (1, 55, 75, "2022-12-31 11:21:00"))
        con.commit()

        con.close()