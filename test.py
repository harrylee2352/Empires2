import sqlite3


def login_signup():
    choice = int(input('would you like to \n 1. login \n 2. signup'))
    if choice == 1:#login details, function imported from other file
        print('hello')
        import login
        login.check_valid_details() 
    elif choice == 2:
        import signup
        signup.insert_data()
    else:
        print ('invalid choice please try again')

login_signup()
