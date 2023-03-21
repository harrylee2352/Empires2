# from the game function, a variable will be listed as winner with the username of winner, this can automatically be used to change leaderboard table
# need to check if the username is already there
#if false, add username and add win/loss values
#if true, take the win/loss values and .append

import sqlite3

player = ('harrrry')

def append_leaderboard(value):
    with sqlite3.connect('users.db') as db: 
        cursor = db.cursor()
        valid_check = cursor.execute (f"SELECT COUNT(*) FROM Leaderboard WHERE UserName = '{value}'")
        count = cursor.fetchone()[0]
        if count > 0:
            print("User exists in database")
            username = (value)
            values = (username)
            with sqlite3.connect("users.db") as db:
                cursor = db.cursor()
                sql = (f"UPDATE Leaderboard SET wins = wins + 1, losses = losses + 1 WHERE UserName = '{username}' ")
                cursor.execute (sql)
                db.commit()    
        else:

            print("User does not exist in database")
            username = (value)
            wins = (0)
            losses = (0)
            values = (username,wins,losses)
            with sqlite3.connect("users.db") as db: 
                cursor = db.cursor()
                sql = ("insert into Leaderboard (UserName,wins,losses) values(?,?,?)")
                cursor.execute (sql,values)
                db.commit()

append_leaderboard(player)
