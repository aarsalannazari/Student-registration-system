import sqlite3

def Create_Table():
    connection=sqlite3.connect('Student-reistration.db')
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS student_db
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) ,
        familly VARCHAR(30) ,
        student_id INTEGER (5) ,
        age INTEGER (3)
    )
    ''')
    connection.commit()
    connection.close()
Create_Table()

# I Continue this program for tomorrow
