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
    except Exception:
        return False

def Show():
    connection=sqlite3.connect('Student-reistration.db')
    cursor=connection.cursor()
    try:
        cursor.execute("SELECT * FROM students")
        res=cursor.fetchall()
        connection.close()
        return res
    except Exception:
        return False
    
def Delete(id):
    connection=sqlite3.connect('Student-reistration.db')
    cursor=connection.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE student_id=?",(id,))
        connection.commit()
        connection.close()
    except Exception:
        return False

def Search(id='',name='',familly='',age=''):
    connection=sqlite3.connect('Student-reistration.db')
    cursor=connection.cursor()
    try:
        cursor.execute("SELECT * FROM students WHERE student_id=? OR name=? OR familly=? OR age=?",(id,name,familly,age))
        res=cursor.fetchall()
        connection.close()
        return res
    except Exception:
        return False

def Update(name,familly,st_id,age,id):
    connection=sqlite3.connect('Student-reistration.db')
    cursor=connection.cursor()
    try:
        cursor.execute("UPDATE students SET name=? , familly=? , student_id=? , age=? WHERE id=?",(name,familly,st_id,age,id))
        connection.commit()
        connection.close()
    except Exception:
        return False
    

Create_Table()
