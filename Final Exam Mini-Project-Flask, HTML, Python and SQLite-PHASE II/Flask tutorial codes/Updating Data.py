import sqlite3
conn = sqlite3.connect("my_sqlite.db")
cursor = conn.cursor()
# SQL select statement
sql = """update hobbies set hobby = 'coding and nano-electronics' where id = 1"""
cursor.execute(sql)
# Commit the changes
conn.commit()
conn.close()
