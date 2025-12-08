import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

sql = "insert into member_login values (?, ?, ?)"

data = [
    (1, "cgravett", "slider"),

    (2, "ddooley", "dxllvn"),
]

cursor.executemany(sql, data)

conn.commit()
conn.close()
