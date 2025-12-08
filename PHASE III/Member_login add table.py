import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
#create a tbale called "hobbies" with 5 fields - id, name, sec, age, hobby
sql1 = "CREATE table member_login (memberID int PRIMARY KEY, username text, password text)"
cursor.execute(sql1)
#commit the changes to the database
conn.commit()
conn.close()