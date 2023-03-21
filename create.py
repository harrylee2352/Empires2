import sqlite3
def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it (y/n):".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()
def create_Users_table(): ### inserting a function with table and columns
    sql = """create table Users
    (UserName text,
    Password text,    
    primary key(UserName), 
    foreign key(userName) references UserInfo(UserName)
    on update cascade on delete set null)"""
    create_table(db_name, "Users", sql)
def create_UserInfo_table():
    sql = """create table UserInfo
    (UserName text,
    Yeargroup integer,
    House text,
    primary key(UserName),
    foreign key(UserName) references Users(UserName)
    on update cascade on delete set null)"""
    create_table(db_name, "UserInfo", sql)
def create_Leaderboard_table():
    sql = """create table Leaderboard
    (UserName text,
    Wins integer,
    Losses integer,
    primary key(UserName),
    foreign key(UserName) references Users(UserName)
    foreign key(UserName) references UserInfo(UserName)
    on update cascade on delete set null)"""
    create_table(db_name, "Leaderboard", sql)
if __name__ == "__main__":
    db_name = "users.db" ### assigning a db name
    create_Users_table()
    create_UserInfo_table()
    create_Leaderboard_table() 