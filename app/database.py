import sqlite3 as sq

db = sq.connect('tg.bd')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "cart_id TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS feedback(i_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "feed TEXT)")
    db.commit()