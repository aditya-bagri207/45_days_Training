import sqlite3
connection = sqlite3.connect("college.db")
cursor = connection.cursor()
cursor.execute("""
              CREATE TABLE student1(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER        
               )
""")

connection.commit()
connection.close()
print("database created succesfull")