import sqlite3

class Database:
    def __init__(self, config):
        self.db_name = config["database_name"]

    def create_readings_table(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute("""CREATE TABLE READING (
            READ_ID INT AUTO_INCREMENT,
            READ_SENSOR_NUM INT NOT NULL,
            READ_HUMIDITY DECIMAL(3, 2) NOT NULL,
            READ_TEMP DECIMAL(3, 2) NOT NULL,
            READ_DATE DATETIME NOT NULL,
            PRIMARY KEY (READ_ID))""")
    
        con.close()
