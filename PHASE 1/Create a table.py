import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
#create a tbale called "hobbies" with 5 fields - id, name, sec, age, hobby
sql1 = "CREATE table celebs (celebID int PRIMARY KEY, firstname text, lastname text, age int, email text, photo text, bio text)"
cursor.execute(sql1)
sql2 = "CREATE table members (memberID int PRIMARY KEY, firstname text, lastname text, age int, email text, bio text)"
cursor.execute(sql2)
#commit the changes to the database
conn.commit()
conn.close()