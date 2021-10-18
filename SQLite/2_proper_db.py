import sqlite3
import time
import datetime
import random

conn = sqlite3.connect("./SQLite/DBs/first_data_base.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS plotting_stuff(unix REAL,\
              datestamp TEXT, keyword TEXT, value REAL)") # unix is a timestamp

def data_entry():
    c.execute("INSERT INTO plotting_stuff \
        VALUES(64684531, '2016-01-12', 'Python', 21)")
    conn.commit()
    c.close()
    conn.close()
    
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime(
        "%Y-%m-%d %H:%M:%S"))
    keyword = "Python"
    value = random.uniform(0, 9)
    c.execute("INSERT INTO plotting_stuff\
        (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
        (unix, date, keyword, value))
    
    conn.commit()

if __name__ == "__main__":
    create_table()
    
    for i in range(10):
        dynamic_data_entry()
        time.sleep(1)
    
    c.close()
    conn.close()