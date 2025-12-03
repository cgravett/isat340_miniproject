import sqlite3
conn = sqlite3.connect("my_sqlite.db")
cursor = conn.cursor()
# SQL INSERT statement
sql = "INSERT INTO hobbies VALUES (?, ?, ?, ?, ?)"
data = (4, "Casey Gravett", "male", 21, "guitar")

cursor.execute(sql, data)

# Commit the changes
conn.commit()
conn.close()