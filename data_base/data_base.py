import sqlite3 as sq
import logging


logger = logging.getLogger('data_base')


async def sql_start(_):
    global base, cur
    base = sq.connect('main.db')
    cur = base.cursor()
    if base:
        logger.info(" Data base connected OK!")
        base.execute('CREATE TABLE IF NOT EXISTS users(id INT, name TEXT, duels INT)')
        base.execute('CREATE TABLE IF NOT EXISTS inline_message(id TEXT)') # store inline_message_id that wasn't accepted yet, then delete
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


def insert_inline_message_id(inline_message_id: str):
    cur.execute('INSERT INTO inline_message VALUES (?)', (inline_message_id,))
    base.commit()
    logger.debug(f" Added to inline_message_id ({inline_message_id})")


def is_in_inline_message_id(inline_message_id: str) -> bool:
    """
    return:
        True if in DB

        False if not in DB
    """
    data = cur.execute('SELECT id FROM inline_message WHERE id = (?)', (inline_message_id, )).fetchall()
    if data==[]:
        logger.debug(f" No {inline_message_id} in table 'inline_message'")
        return False
    else:
        cur.execute("DELETE FROM inline_message WHERE id = (?)", (inline_message_id, ))
        base.commit()
        logger.debug(f" Deleted {inline_message_id} from table 'inline_message'")
        return True
