import sqlite3
conn = sqlite3.connect("my_sqlite.db")
cursor = conn.cursor()

# SQL SELECT statement to delete a specific record
sql = '''DELETE FROM hobbies WHERE id = 2'''
cursor.execute(sql)
# Commit the changes
conn.commit()
conn.close()
