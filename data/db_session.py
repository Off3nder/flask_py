import sqlite3
from files import DB_PATH

__connector = sqlite3.connect(
    DB_PATH, check_same_thread=False
)
cursor: sqlite3.Cursor = __connector.cursor()

def sql_execute(command, _db_commit = False):
    try:
        result = cursor.execute(command)
        if _db_commit is True:
            db_commit()
        return result
    except sqlite3.OperationalError as error:
        print(f'Error in: {command}')
        raise error

def db_commit():
    __connector.commit()