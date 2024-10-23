import sqlite3 as sq

db = sq.connect('tg.bd')
cur = db.cursor()

async def db_start():

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, feed TEXT")
    db.commit()


async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id))
    if not user:
        cur.execute("INSERT INTO profile VALUES(?,?,?,?,?)", (user_id,'','','',''))
        db.commit()

async def edit_profile(state,user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile WHERE user_id=='{}' SET feed == '{}',".format(user_id,data['feed']))
        db.commit()