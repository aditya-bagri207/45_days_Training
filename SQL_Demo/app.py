import sqlite3
from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")

def index():
    conn=get_connection()
    student1=conn.exexute("Select *FROM student1").fetchall()
    conn.close()

    return render_template("index.html",student1=student1)

def get_connection():
    connection =sqlite3.connect("college.db")

    connection.row_factory=sqlite3.Row 

    return connection


connection =get_connection()


cursor=connection.cursor()

cursor.execute(
    "INSERT INTO student(name,age) VALUES(??)",

  
)

connection.commit()
connection.close()

#read

connection = get_connection()
cursor = connection.cursor

cursor.execute("SELECT * FROM STUDENT1")

student = cursor.fetchall()

connection.close()
if __name__=="__main__":
    app.run(debug=True)

    #update
connection  = get_connection()
cursor = connection.cursor()

cursor.execute("""
           UPDATE student1
               SET name=?,
               age = ?
               where id = ?
               """)

student = cursor.fetchall()

connection.close()
if __name__ == "__main__":
    app.run(debug=True)


