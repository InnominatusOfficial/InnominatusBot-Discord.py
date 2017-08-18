import sqlite3

def changeCoins(user_id, coins):

    with sqlite3.connect("user_data.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Economy where UserID=?",(user_id,))
        product = cursor.fetchone()


    print(product)

changeCoins(1, 100)