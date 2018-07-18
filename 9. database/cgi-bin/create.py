import sqlite3


connection = sqlite3.connect('../data/coachdata.sqlite')
cursor = connection.cursor()
name = "Shabuktagin Photon Khan"
dob = "1991-08-23"
cursor.execute("INSERT INTO athletes(name, dob) VALUES(?, ?)", (name, dob))
connection.commit()
connection.close()
