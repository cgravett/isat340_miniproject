#import the built-in sqlite3 module
import sqlite3
#create or connect to an existing database
conn = sqlite3.connect("celebrities.db")
#get a cursor to work with the database
#a database cursor is an object used to pinpoint records in a database
cursor = conn.cursor()
#close the connection ot the database
conn.close()