import sqlite3

# Connect to the database
conn = sqlite3.connect("my_sqlite.db")
cursor = conn.cursor()

# Data supplied as a tuple of tuples. ?-are placeholders for data
sql = "INSERT INTO hobbies VALUES (?, ?, ?, ?, ?)"
data = (
    (2, "Sarah", "female", 22, "guitar"),
    (3, "Jean", "female", 21, "bowling")
)

# Insert multiple records at once
cursor.executemany(sql, data)

# Commit the changes
conn.commit()
conn.close()