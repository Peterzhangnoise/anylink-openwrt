#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('/usr/local/anylink/conf/anylink.db')
c = conn.cursor()
c.execute("delete from ip_map;")
conn.commit()
c.execute("delete from sqlite_sequence where name = 'ip_map';")
conn.commit()
conn.close()
