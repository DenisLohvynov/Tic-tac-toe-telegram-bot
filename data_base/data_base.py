import sqlite3 as sq
import logging


logger = logging.getLogger()


async def sql_start(_):
    global base, cur
    base = sq.connect('main.db')
    cur = base.cursor()
    if base:
        logger.info(" Data base connected OK!")
        base.execute('CREATE TABLE IF NOT EXISTS users(id INT, name TEXT, duels INT)')
    else:
        logger.critical(" No data base!")


def get_name(id: int) -> str:
    data = cur.execute('SELECT name FROM users WHERE id = (?)', (id, )).fetchone()
    if data==None:
        raise NameError("Not in database")
    else:
        return data[0]


def sign_in(id: int, name: str):
    data = cur.execute('SELECT name FROM users WHERE id = (?)', (id, )).fetchone()
    if data==None:
        cur.execute('INSERT INTO users VALUES (?, ?, ?)', (id, name, 0))
        base.commit()
        logger.debug(f" Added to users ({id}, {name}, 0)")
