import sqlite3

conn = sqlite3.connect("./SQLite/DBs/test1.db")
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
    
create_table()
data_entry()