import pymysql

db = pymysql.connect("localhost","root","","mybook",charset="utf8")
cursor = db.cursor() 
cursor.execute("SELECT * FROM book")
row = cursor.fetchone()
print(row[0], row[1])
print("-------------------------")      
data = cursor.fetchall()
for row in data:
    print(row[0], row[1])
db.close()

