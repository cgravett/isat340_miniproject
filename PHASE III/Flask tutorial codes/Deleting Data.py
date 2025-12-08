import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

# SQL SELECT statement to delete a specific record
sql = '''DELETE FROM celebs WHERE celebID = 8'''
cursor.execute(sql)
# Commit the changes
conn.commit()
conn.close()
