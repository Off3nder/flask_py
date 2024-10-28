from data.db_session import sql_execute

def user_create_table():
    command = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(20),
        password VARCHAR(32)   
    );"""
    return sql_execute(command, _db_commit=True)


def user_create(username, password):
    command = f"""
    INSERT INTO users (username,password) VALUES ("{username}","{password}");"""
    return sql_execute(command, _db_commit = True)

def authenticate(username,password):
    command = f"""
    SELECT * FROM users WHERE ( "username" = "{username}" AND "password" = "{password}" )"""
    user = sql_execute(command)
    return user.fetchone()

def user_get(user_id):
    command = f"""
    SELECT * FROM users WHERE ("id" = "{user_id}")"""
    return sql_execute(command).fetchone()

def user_twin_checker(username):
    command = f"""
    SELECT * FROM users WHERE ("username" = "{username}")"""
    return len(sql_execute(command).fetchall())