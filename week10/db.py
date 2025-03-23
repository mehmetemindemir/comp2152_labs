import sqlite3
import function
db_connection = sqlite3.connect('sqlite.db')
print(db_connection)
cursor = db_connection.cursor()
print(cursor)
# Prepare and execute the query
query1="SELECT * FROM demo"
cursor.execute(query1)
# Fetch from a pre-executed query
print("reading 1 row")
row=cursor.fetchone()
print(row)

print("reading 1 row")
rows=function.query_responder(cursor, "fetchmany", 3)
for row in rows:
    print(row)

print("reading all  rows")
#rows = cursor.fetchall()
#for row in rows:
#    print(row)
function.query_responder(cursor, "fetchall")

query2="insert into demo(Name,Hint) values('Mehmet','Demir')"
cursor.execute(query2)
db_connection.commit()
print("reading all  rows")
id=input("Enter an ID:")
query3="SELECT * FROM demo where ID>?"
cursor.execute(query3,(id,))
function.query_responder(cursor, "fetchall")

db_connection.close()