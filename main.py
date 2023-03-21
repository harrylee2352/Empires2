import sqlite3


def main_menu():
    print("Welcome to the Main Menu")
    print("1. login/signup")
    print("2. leaderboard")
    print("3. game")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))#
    
    if choice == 1:
        login_signup()
    elif choice == 2:
        leaderboard()
    elif choice == 3:
        game()
    elif choice == 4:
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

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

    
def leaderboard():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute ('select UserName,Wins,Losses from Leaderboard')
        leaderboard = cursor.fetchall()
        print (leaderboard)
   
    
#def game():
    
    

main_menu()
