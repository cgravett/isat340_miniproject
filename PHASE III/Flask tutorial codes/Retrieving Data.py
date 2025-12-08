import sqlite3
# Connect to the database
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
# SQL SELECT statement
sql = "SELECT * FROM members"
cursor.execute(sql)
# Get the rows
rows = cursor.fetchall()
# Iterate over the results and print them
for row in rows:
    print(row)
# Close the connection
conn.close()
