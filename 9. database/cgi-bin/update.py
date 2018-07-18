import sqlite3

connection = sqlite3.connect("../data/coachdata.sqlite")
cursor = connection.cursor()
name = 'Shabuktagin Photon Khan'
dob = '19991-08-23'
id = 1
cursor.execute("UPDATE athletes SET name = ?, dob = ? WHERE id = ?", (name, dob, id))
connection.commit()
connection.close()