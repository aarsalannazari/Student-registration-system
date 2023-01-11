import sqlite3

def Create_Table():
    connection=sqlite3.connect('Student-reistration.db')
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) ,
        familly VARCHAR(30) ,
        student_id INTEGER (5) UNIQUE ,
        age INTEGER (3)
    )
    ''')
    connection.commit()
    connection.close()

def Insert(name,familly,st_id,age):
    connection=sqlite3.connect('Student-reistration.db')
    cursor=connection.cursor()
    try:
        cursor.execute("INSERT INTO students VALUES(NULL,?,?,?,?)",(name,familly,st_id,age))
        connection.commit()
        connection.close()
    except Exception as e:
        return False

Create_Table()

# I Continue this program for tomorrow
