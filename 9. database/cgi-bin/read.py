import sqlite3

connection = sqlite3.connect("../data/coachdata.sqlite")
cursor = connection.cursor()
cursor.execute("""SELECT * FROM athletes""")
result = cursor.fetchall()
data = []
for i in range(0, (len(result))):
    data.append({"id": result[i][0], "name": result[i][1], "dob": result[i][2]})
connection.commit()
connection.close()
print(data)