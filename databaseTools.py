import sqlite3

def economySetUp():
    sql = """create table Economy
    (UserID integer,
    Coins integer)"""

    with sqlite3.connect("user_data.db") as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

economySetUp()