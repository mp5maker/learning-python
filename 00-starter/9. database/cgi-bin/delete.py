import sqlite3

connection = sqlite3.connect("../data/coachdata.sqlite")
cursor = connection.cursor()
id = '3'
cursor.execute("DELETE FROM athletes WHERE id = ?", id)
connection.commit()
connection.close()