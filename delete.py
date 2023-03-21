import sqlite3

remove_user_info = input('enter you username to delete:')
def delete_product(data):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        sql = "delete from users where UserName=?"
        cursor.execute(sql,data)
        db.commit()
if __name__ == "__main__":
    data = (remove_user_info,)#needs a comma, even though single atribute
    delete_product(data)