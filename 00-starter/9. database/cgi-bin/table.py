import sqlite3

connection = sqlite3.connect('../data/coachdata.sqlite')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE athletes(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, dob DATE NOT NULL)""")
cursor.execute("""CREATE TABLE timing_data(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, athletes_id INT NOT NULL, value TEXT NOT NULL)""")
connection.commit()
connection.close()