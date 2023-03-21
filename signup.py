import sqlite3

def insert_data():
    username = input("enter username:")
    password = input("enter password:")
    Yeargroup = input('enter your yeargroup:')
    House = input('enter your house name:')
    values = (username,password)
    values2 = (username,Yeargroup,House)
    with sqlite3.connect("users.db") as db: 
        cursor = db.cursor()
        sql = ("insert into users (UserName, Password) values(?,?)")
        cursor.execute (sql,values)
        db.commit()
    with sqlite3.connect("users.db") as db: 
        cursor = db.cursor()
        sql = ("insert into Userinfo (UserName, Yeargroup, House) values(?,?,?)")
        cursor.execute (sql,values2)
        db.commit()
insert_data()