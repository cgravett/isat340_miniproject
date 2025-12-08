import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
#data supplied as tuple. ? - are placeholders for data
sql = "insert into members values (?, ?, ?, ?, ?, ?)"
data = (1, "Dillon", "Dooley", 20, "Dxllvn@gmail.com", "My name is Dillon Dooley and I love coding.")
cursor.execute(sql, data)
#commit the changes to the database
conn.commit()
conn.close()