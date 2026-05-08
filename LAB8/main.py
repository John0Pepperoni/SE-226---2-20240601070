import mysql.connector as sql
import tkinter as tk

def create_database():
    db = sql.connect(
        host='127.0.0.1',
        user='dev_user',
        passwd='root'
    )

    creatorcursor = db.cursor()

    query0 = '''DROP DATABASE IF EXISTS StudentDatabase;
                CREATE DATABASE StudentDatabase;'''

    creatorcursor.execute(query0)

    connection = sql.connect(
        host='127.0.0.1',
        user='dev_user',
        database='StudentDatabase',
        passwd='root'
    )

    cursor = connection.cursor()

    query1 = '''CREATE TABLE Students ( 
                    id   INT AUTO_INCREMENT PRIMARY KEY, 
                    name  CHAR(20), 
                    score INT
                );'''

    cursor.execute(query1)

    query2 = '''INSERT INTO Students(name, SCORE) VALUES ('John', 100);
    INSERT INTO Students(name, SCORE) VALUES ('Jane', 85);
    INSERT INTO Students(name, SCORE) VALUES ('Bob', 76);
    INSERT INTO Students(name, SCORE) VALUES ('Alice', 96);
    INSERT INTO Students(name, SCORE) VALUES ('Eve', 88);
    INSERT INTO Students(name, SCORE) VALUES ('David', 90);
    INSERT INTO Students(name, SCORE) VALUES ('Carol', 53);
    INSERT INTO Students(name, SCORE) VALUES ('Mike', 97);
    INSERT INTO Students(name, SCORE) VALUES ('Jack', 12);
    INSERT INTO Students(name, SCORE) VALUES ('Jill', 35);
    INSERT INTO Students(name, SCORE) VALUES ('Jenny', 28);
    INSERT INTO Students(name, SCORE) VALUES ('Connor', 67);
    INSERT INTO Students(name, SCORE) VALUES ('Johnny', 45);
    INSERT INTO Students(name, SCORE) VALUES ('Jim', 78);
    INSERT INTO Students(name, SCORE) VALUES ('Jake', 23);
    INSERT INTO Students(name, SCORE) VALUES ('Jason', 56);
    INSERT INTO Students(name, SCORE) VALUES ('Coulthard', 34);
    INSERT INTO Students(name, SCORE) VALUES ('Jon', 65);
    INSERT INTO Students(name, SCORE) VALUES ('Jeffery', 43);
    '''

    cursor.execute(query2)
    connection.commit()
    connection.close()
    db.close()


def ui():
    r = tk.Tk()
    r.title("Student Database")
    r.mainloop()

    label = tk.Label(r, text="Student Database")
    label.pack()

    entry = tk.Entry(r)
    entry.pack()

    button = tk.Button(r, text="Submit", command=get_scores(entry.get()))
    button.pack()



def get_scores(score):
    connection = sql.connect(
        host='127.0.0.1',
        user='dev_user',
        database='StudentDatabase',
        passwd='root'
    )

    cursor = connection.cursor()
    query = f'''SELECT * FROM Students WHERE SCORE > {score}'''
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

def main():
    create_database()
    ui()