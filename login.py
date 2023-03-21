import sqlite3


def check_valid_details():
    username = input("enter username")
    password = input("enter password")
    with sqlite3.connect('users.db') as db: 
        cursor = db.cursor()
        valid_check = cursor.execute (f"SELECT COUNT(*) FROM users WHERE username = '{username}' AND password = '{password}'")
        count = cursor.fetchone()[0]
        if count > 0:
            print("welcome back",username)
        else:
            choice = input('it is not a valid username, would you like to sign up?[y/n]')
            if choice == 'y':
                import signup
                signup.insertdata
            elif choice == 'n':
                check_valid_details()
check_valid_details()

                
      



